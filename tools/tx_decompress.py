# The following is adapted from https://github.com/reswitched/loaders/blob/master/nxo64.py
#
# ===========================================================================================
#
# Copyright 2017 Reswitched Team
#
# Permission to use, copy, modify, and/or distribute this software for any purpose with or
# without fee is hereby granted, provided that the above copyright notice and this permission
# notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
# CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
# OR PERFORMANCE OF THIS SOFTWARE.

import os
import struct
import lz4.block

uncompress = lz4.block.decompress

# Skip the non-standard size field
kip_skip = 0
 
def kip1_blz_decompress(compressed):
    compressed_size, init_index, uncompressed_addl_size = struct.unpack('<III', compressed[-0xC:])
    decompressed = compressed[:] + '\x00' * uncompressed_addl_size
    decompressed_size = len(decompressed)
    if len(compressed) != compressed_size:
        assert len(compressed) > compressed_size
        compressed = compressed[len(compressed) - compressed_size:]
    if not (compressed_size + uncompressed_addl_size):
        return ''
    compressed = map(ord, compressed)
    decompressed = map(ord, decompressed)
    index = compressed_size - init_index
    outindex = decompressed_size
    while outindex > 0:
        index -= 1
        control = compressed[index]
        for i in xrange(8):
            if control & 0x80:
                if index < 2:
                    print(ValueError('INFO: Compression out of bounds!'))
                index -= 2
                segmentoffset = compressed[index] | (compressed[index+1] << 8)
                segmentsize = ((segmentoffset >> 12) & 0xF) + 3
                segmentoffset &= 0x0FFF
                segmentoffset += 2
                if outindex < segmentsize:
                    print(ValueError('INFO: Compression out of bounds!'))
                for j in xrange(segmentsize):
                    if outindex + segmentoffset >= decompressed_size:
                        print(ValueError('INFO: Compression out of bounds!'))
                    data = decompressed[outindex+segmentoffset]
                    outindex -= 1
                    decompressed[outindex] = data
            else:
                if outindex < 1:
                    print(ValueError('INFO: Compression out of bounds!'))
                outindex -= 1
                index -= 1
                decompressed[outindex] = compressed[index]
            control <<= 1
            control &= 0xFF
            if not outindex:
                break
    return ''.join(map(chr, decompressed))
    
class BinFile(object):
    def __init__(self, li):
        self._f = li
 
    def read(self, arg):
        if isinstance(arg, str):
            fmt = '<' + arg
            size = struct.calcsize(fmt)
            raw = self._f.read(size)
            out = struct.unpack(fmt, raw)
            if len(out) == 1:
                return out[0]
            return out
        elif arg is None:
            return self._f.read()
        else:
            out = self._f.read(arg)
            return out
 
    def read_from(self, arg, offset):
        old = self.tell()
        try:
            self.seek(offset)
            out = self.read(arg)
        finally:
            self.seek(old)
        return out
 
    def seek(self, off):
        self._f.seek(off)
 
    def close(self):
        self._f.close()
 
    def tell(self):
        return self._f.tell()
        
def decompress_kip(fileobj):
    f = BinFile(fileobj)

    if f.read_from('4s', 0 + kip_skip) != 'KIP1':
        raise NxoException('Invalid KIP magic')
 
    tloc, tsize, tfilesize = f.read_from('III', 0x20 + kip_skip)
    rloc, rsize, rfilesize = f.read_from('III', 0x30 + kip_skip)
    dloc, dsize, dfilesize = f.read_from('III', 0x40 + kip_skip)
     
    toff = 0x100
    roff = toff + tfilesize
    doff = roff + rfilesize

    bsssize = f.read_from('I', 0x18 + kip_skip)
 
    text = kip1_blz_decompress(str(f.read_from(tfilesize, toff + kip_skip)))
    ro   = kip1_blz_decompress(str(f.read_from(rfilesize, roff + kip_skip)))
    data = kip1_blz_decompress(str(f.read_from(dfilesize, doff + kip_skip)))

    full = text
    if rloc >= len(full):
        full += '\0' * (rloc - len(full))
    else:
        full = full[:rloc]
    full += ro
    if dloc >= len(full):
        full += '\0' * (dloc - len(full))
    else:
        full = full[:dloc]
    full += data
 
    return full
    
def decompress_nso(fileobj):
    f = BinFile(fileobj)

    if f.read_from('4s', 0) != 'NSO0':
        raise NxoException('Invalid NSO magic')

    toff, tloc, tsize = f.read_from('III', 0x10)
    roff, rloc, rsize = f.read_from('III', 0x20)
    doff, dloc, dsize = f.read_from('III', 0x30)

    tfilesize, rfilesize, dfilesize = f.read_from('III', 0x60)
    bsssize = f.read_from('I', 0x3C)

    text = uncompress(f.read_from(tfilesize, toff), uncompressed_size=tsize)
    ro   = uncompress(f.read_from(rfilesize, roff), uncompressed_size=rsize)
    data = uncompress(f.read_from(dfilesize, doff), uncompressed_size=dsize)

    full = text
    if rloc >= len(full):
        full += '\0' * (rloc - len(full))
    else:
        full = full[:rloc]
    full += ro
    if dloc >= len(full):
        full += '\0' * (dloc - len(full))
    else:
        full = full[:dloc]
    full += data
 
    return full

# ===========================================================================================

def get_ver_int(boot_ver):
    if boot_ver[1] == 0x302E3156:                                       # TX BOOT V1.0
        return 100
    elif boot_ver[1] == 0x312E3156:                                     # TX BOOT V1.1
        return 110
    elif boot_ver[1] == 0x322E3156:                                     # TX BOOT V1.2
        return 120
    elif boot_ver[1] == 0x332E3156:                                     # TX BOOT V1.3
        return 130
    elif boot_ver[1] == 0x342E3156:                                     # TX BOOT V1.4
        return 140
    elif boot_ver[1] == 0x352E3156:                                     # TX BOOT V1.5
        return 150
    elif boot_ver[1] == 0x362E3156:                                     # TX BOOT V1.6
        return 160
    elif boot_ver[1] == 0x372E3156:                                     # TX BOOT V1.7
        return 170
    elif boot_ver[1] == 0x382E3156:                                     # TX BOOT V1.8
        return 180
    elif boot_ver[1] == 0x392E3156:                                     # TX BOOT V1.9
        return 190
    elif boot_ver[1] == 0x302E3256:                                     # TX BOOT V2.0
        return 200
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x302E3256):       # TX BOOT V2.0.1
        return 201
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x312E3256):            # TX BOOT V2.1
        return 210
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x322E3256):            # TX BOOT V2.2
        return 220
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x322E3256):       # TX BOOT V2.2.1
        return 221
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x332E3256):            # TX BOOT V2.3
        return 230
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x342E3256):            # TX BOOT V2.4
        return 240
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x342E3256):       # TX BOOT V2.4.1
        return 241
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x352E3256):            # TX BOOT V2.5
        return 250
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x352E3256):       # TX BOOT V2.5.1
        return 251
    elif (boot_ver[1] == 0x322E) and (boot_ver[0] == 0x352E3256):       # TX BOOT V2.5.2
        return 252
    elif (boot_ver[1] == 0x332E) and (boot_ver[0] == 0x352E3256):       # TX BOOT V2.5.3
        return 253
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x362E3256):            # TX BOOT V2.6
        return 260
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x362E3256):       # TX BOOT V2.6.1
        return 261
    elif (boot_ver[1] == 0x322E) and (boot_ver[0] == 0x362E3256):       # TX BOOT V2.6.2
        return 262
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x372E3256):            # TX BOOT V2.7
        return 270
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x372E3256):       # TX BOOT V2.7.1
        return 271
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x382E3256):            # TX BOOT V2.8
        return 280
    elif (boot_ver[1] == 0) and (boot_ver[0] == 0x392E3256):            # TX BOOT V2.9
        return 290
    elif (boot_ver[1] == 0x312E) and (boot_ver[0] == 0x392E3256):       # TX BOOT V2.9.1
        return 291
    elif (boot_ver[1] == 0x322E) and (boot_ver[0] == 0x392E3256):       # TX BOOT V2.9.2
        return 292
    elif (boot_ver[1] == 0x332E) and (boot_ver[0] == 0x392E3256):       # TX BOOT V2.9.3
        return 293
    elif (boot_ver[1] == 0x342E) and (boot_ver[0] == 0x392E3256):       # TX BOOT V2.9.4
        return 294
    elif (boot_ver[1] == 0x352E) and (boot_ver[0] == 0x392E3256):       # TX BOOT V2.9.5
        return 295
    elif (boot_ver[1] == 0x30) and (boot_ver[0] == 0x2E302E33):         # TX BOOT 3.0.0
        return 300
    elif (boot_ver[1] == 0x31) and (boot_ver[0] == 0x2E302E33):         # TX BOOT 3.0.1
        return 301
    elif (boot_ver[1] == 0x322E) and (boot_ver[0] == 0x302E3356):       # TX BOOT V3.0.2
        return 302
    elif (boot_ver[1] == 0x332E) and (boot_ver[0] == 0x302E3356):       # TX BOOT V3.0.3
        return 303
    elif (boot_ver[1] == 0x342E) and (boot_ver[0] == 0x302E3356):       # TX BOOT V3.0.4
        return 304
    elif (boot_ver[1] == 0x352E) and (boot_ver[0] == 0x302E3356):       # TX BOOT V3.0.5
        return 305
    elif (boot_ver[1] == 0x302E) and (boot_ver[0] == 0x312E3356):       # TX BOOT V3.1.0
        return 310
    else:
        return 0

f = open("boot.dat", "rb")
b = f.read()
f.close()

# Get the version from boot.dat
version = get_ver_int(struct.unpack("II", b[0x08:0x10]))

if version == 100:
    kip_skip = 0x8
    tx_nso_off = 0x30DD8
    tx_nso_size = 0xF0F3C
    hbl_nso_off = 0x1222A0
    hbl_nso_size = 0x8F90
elif version == 110:
    kip_skip = 0x8
    tx_nso_off = 0x30DD8
    tx_nso_size = 0xF1068
    hbl_nso_off = 0x1223CC
    hbl_nso_size = 0x90DC
elif version == 120:
    kip_skip = 0x8
    tx_nso_off = 0x31DE0
    tx_nso_size = 0xF1198
    hbl_nso_off = 0x123504
    hbl_nso_size = 0x90DC
elif version == 130:
    kip_skip = 0x10
    tx_nso_off = 0x31CF0
    tx_nso_size = 0xED474
    hbl_nso_off = 0x11F6F0
    hbl_nso_size = 0x8E18
elif version == 140:
    kip_skip = 0x10
    hbl_nso_off = 0x32CB0
    hbl_nso_size = 0x9024
    tx_nso_off = 0x3C0A0
    tx_nso_size = 0xA010
elif version == 150:
    kip_skip = 0x10
    hbl_nso_off = 0x44CD8
    hbl_nso_size = 0x9024
    tx_nso_off = 0x4E0C8
    tx_nso_size = 0xA010
elif version == 160:
    kip_skip = 0x10
    hbl_nso_off = 0x44CD8
    hbl_nso_size = 0x9034
    tx_nso_off = 0x4E0D8
    tx_nso_size = 0xA018
elif version == 170 or version == 180:
    kip_skip = 0x10
    hbl_nso_off = 0x44CD8
    hbl_nso_size = 0x90D0
    tx_nso_off = 0x4E174
    tx_nso_size = 0xA0CC
elif version == 190 or version == 200:
    kip_skip = 0x10
    hbl_nso_off = 0x40CD8
    hbl_nso_size = 0x90F4
    tx_nso_off = 0x4A198
    tx_nso_size = 0xA0C8
elif version == 201:
    kip_skip = 0x10
    hbl_nso_off = 0x41CD8
    hbl_nso_size = 0x90F4
    tx_nso_off = 0x4B198
    tx_nso_size = 0xA0C8
elif version == 210:
    kip_skip = 0x10
    hbl_nso_off = 0x43D50
    hbl_nso_size = 0x90F4
    tx_nso_off = 0x4D210
    tx_nso_size = 0xA0C8
elif version == 220:
    kip_skip = 0x10
    hbl_nso_off = 0x4CD68
    hbl_nso_size = 0x90F4
    tx_nso_off = 0x56228
    tx_nso_size = 0xA0C8
elif version == 221:
    kip_skip = 0x10
    hbl_nso_off = 0x51D78
    hbl_nso_size = 0x91A4
    tx_nso_off = 0x5B2E8
    tx_nso_size = 0xAF3C
elif version == 230:
    kip_skip = 0x10
    hbl_nso_off = 0x5BDD0
    hbl_nso_size = 0x9504
    tx_nso_off = 0x656A0
    tx_nso_size = 0xBDEC
elif version == 240 or version == 241:
    kip_skip = 0x10
    hbl_nso_off = 0x55DD0
    hbl_nso_size = 0xA608
    tx_nso_off = 0x607A4
    tx_nso_size = 0xBE24
elif version == 250 or version == 251 or version == 252 or version == 253:
    kip_skip = 0x10
    hbl_nso_off = 0x56E00
    hbl_nso_size = 0xA608
    tx_nso_off = 0x617D4
    tx_nso_size = 0xBE24
elif version == 260:
    kip_skip = 0x10
    hbl_nso_off = 0x69D98
    hbl_nso_size = 0xC048
    tx_nso_off = 0x761AC
    tx_nso_size = 0xDE28
elif version == 261:
    kip_skip = 0x10
    hbl_nso_off = 0x69DA8
    hbl_nso_size = 0xC048
    tx_nso_off = 0x761BC
    tx_nso_size = 0xDE28
elif version == 262:
    kip_skip = 0x10
    hbl_nso_off = 0x69DB8
    hbl_nso_size = 0xC048
    tx_nso_off = 0x761CC
    tx_nso_size = 0xDE28
elif version == 270 or version == 271 or version == 280:
    kip_skip = 0x10
    hbl_nso_off = 0x69E00
    hbl_nso_size = 0xC048
    tx_nso_off = 0x76214
    tx_nso_size = 0xDE28
elif version == 290 or version == 291:
    kip_skip = 0x10
    hbl_nso_off = 0x724C0
    hbl_nso_size = 0xF298
    tx_nso_off = 0x81B24
    tx_nso_size = 0xFFE4
elif version == 292 or version == 293 or version == 294 or version == 295:
    kip_skip = 0x10
    hbl_nso_off = 0
    hbl_nso_size = 0
    tx_nso_off = 0
    tx_nso_size = 0
elif version >= 300:
    kip_skip = 0
    hbl_nso_off = 0
    hbl_nso_size = 0
    tx_nso_off = 0
    tx_nso_size = 0
else:
    exit()

# Check which firmware files are present
kip_list = os.listdir("./sxos/firmware/")

# No files found
if not kip_list:
    exit()

os.chdir("./sxos/firmware/")
    
for i in xrange(len(kip_list)):
    if os.path.isfile(kip_list[i]):
        kip_file = open(kip_list[i], "rb")    
        kip_file.seek(kip_skip)
        kip_magic = struct.unpack("I", kip_file.read(4))[0]
        
        # Make sure the file is a KIP1
        if kip_magic == 0x3150494B:
            kip_name = kip_file.read(12).rstrip('\x00')
            
            # Create folder for this KIP1
            if not os.path.exists("./{:s}/".format(kip_name)):
                os.mkdir("./{:s}/".format(kip_name))
            os.chdir("./{:s}/".format(kip_name))  
            
            # Decompress
            dec_kip_file = open("{:s}.bin".format(kip_name), "wb")
            dec_kip_file.write(decompress_kip(kip_file))
            dec_kip_file.close()
            
            # Handle Loader's NSOs
            if (kip_name == "Loader") and \
                    ((hbl_nso_off > 0) and (hbl_nso_off > 0)) and \
                    ((tx_nso_off > 0) and (tx_nso_size > 0)):
                # Create folder for the NSOs
                if not os.path.exists("./NSO/"):
                    os.mkdir("./NSO/")
                
                # Extract the NSOs
                dec_kip_file = open("{:s}.bin".format(kip_name), "rb")
                dec_kip_file.seek(tx_nso_off)
                tx_nso_data = dec_kip_file.read(tx_nso_size)
                dec_kip_file.seek(hbl_nso_off)
                hbl_nso_data = dec_kip_file.read(hbl_nso_size)
                dec_kip_file.close()
                
                # Save the compressed NSOs
                tx_nso_file = open("./NSO/tx.bin", "wb")
                hbl_nso_file = open("./NSO/hbl.bin", "wb")
                tx_nso_file.write(tx_nso_data)
                hbl_nso_file.write(hbl_nso_data)
                hbl_nso_file.close()
                tx_nso_file.close()
                
                os.chdir("./NSO/")
                
                # Create folders
                if not os.path.exists("./tx/".format(kip_name)):
                    os.mkdir("./tx/".format(kip_name)) 
                if not os.path.exists("./hbl/".format(kip_name)):
                    os.mkdir("./hbl/".format(kip_name)) 
                
                # Decompress
                tx_nso_file = open("tx.bin", "rb")
                hbl_nso_file = open("hbl.bin", "rb")
                dec_tx_nso_file = open("./tx/main", "wb")
                dec_hbl_nso_file = open("./hbl/main", "wb")
                dec_tx_nso_file.write(decompress_nso(tx_nso_file))
                dec_hbl_nso_file.write(decompress_nso(hbl_nso_file))
                dec_hbl_nso_file.close()
                dec_tx_nso_file.close()
                hbl_nso_file.close()
                tx_nso_file.close()
                
                os.chdir("..")
            os.chdir("..") 
            
        kip_file.close()
