###############################################
# TX SX OS unpacker - by hexkyz and naehrwert #
###############################################

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import struct

"""
typedef struct boot_dat_hdr
{
    unsigned char magic[0x8];
    unsigned char version[0x8];
    unsigned char stage2_sha256[0x20];
    unsigned int stage2_dst;
    unsigned int stage2_size;
    unsigned int stage2_enc;
    unsigned char pad[0x10];
    unsigned int app_offset;
    unsigned int boot_dat_hdr_sig_offset;
    unsigned int se_keyslot_mask;
    unsigned int unk;
    unsigned int boot_dat_hdr2_offset;
    unsigned char pad2[0x80];
    unsigned char boot_dat_hdr_sha256[0x20];
} boot_dat_hdr_t;
"""
"""
typedef struct boot_dat_hdr2
{
    unsigned int stage3_size;
    unsigned int stage3_dst;
    unsigned char rnd[0x8];
    unsigned char stage3_ctr[0x10];
    unsigned char stage3_sha256[0x20];
    unsigned char rnd2[0xA0];
    unsigned char boot_dat_hdr2_sha256[0x20];
    unsigned char stage3_sig[0x100];
} boot_dat_hdr2_t;
"""

def aes_ctr_dec(buf, key, iv):
    ctr = Counter.new(128, initial_value=long(iv.encode('hex'), 16))
    return AES.new(key, AES.MODE_CTR, counter=ctr).encrypt(buf)

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

version = get_ver_int(struct.unpack("II", b[0x08:0x10]))
s2_base, s2_size = struct.unpack("II", b[0x30:0x38])
s2_key = "47E6BFB05965ABCD00E2EE4DDF540261".decode("hex")
s2_ctr = "8E4C7889CBAE4A3D64797DDA84BDB086".decode("hex")

if version == 100:
    arm64_key = "35D8FFC4AA1BAB9514825EB0658FB493".decode("hex")
    arm64_ctr = "C38EA26FF3CCE98FD8D5ED431D9D5B94".decode("hex")
    arm64_off = 0x53BAB0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
    
    fb_key = "E2AC05206A701C9AA514D2B2B7C9F395".decode("hex")
    fb_ctr = "46FAB59AF0E469EF116614DEC366D15F".decode("hex")
    fb_off = 0x17BAB0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload80_key = "030D865B7E458B10AD5706F6E227F4EB".decode("hex")
    payload80_ctr = "AFFC93692EBD2E3D252339F01E03416B".decode("hex")
    payload80_off = 0x5F40
    payload80_size = 0x175B70
    payload80_base = 0x80000000
    
    payload90_key = "7F5ADF4D874E452E03D49127A42F1E76".decode("hex")
    payload90_ctr = "94251152C910E701397BE2DB4F1C6CA8".decode("hex")
    payload90_off = 0xC0B8D0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "7D3903433AFF4454E7C4494CF78B2C27".decode("hex")
    payload98_ctr = "47A6B1EE20DDB7CDBB4A486C42638D54".decode("hex")
    payload98_off = 0xD013F0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "470248AF0FD18221C7920635705980F6".decode("hex")
    payloadA0_ctr = "4CC30D28126D38749F755A506B21EE15".decode("hex")
    payloadA0_off = 0xDBD680
    payloadA0_size = 0x1154D0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C9B5A5746CF37F46417DD6842B48361B".decode("hex")
    bootloader_ctr = "40FBE01C573B0C286BC7956455475788".decode("hex")
    bootloader_off = 0x571E20
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "677EC85A86F798AFD6B8BC046B65F0F5".decode("hex")
    assets_ctr = "31C8DBE98486D59CD69DA7C470A69A0B".decode("hex")
    assets_off = 0x592DE0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "31756DA6C12CA907C050861D60A5E0A5".decode("hex")
    fw_ctr = "DA0F8243F83358F15F431FF6F674C099".decode("hex")
    fw_off = 0
    fw_size = 0x1154D0
elif version == 110:
    arm64_key = "51A39F0B46BAE4691AD39A698146E865".decode("hex")
    arm64_ctr = "7A307ED7F1ECC792F0E821ECD6999853".decode("hex")
    arm64_off = 0x53BAE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
    
    fb_key = "27BABEE3DCFEF100C744A2388B57E957".decode("hex")
    fb_ctr = "0B88AC25AFAF9B92D81372331AD66E24".decode("hex")
    fb_off = 0x17BAE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload80_key = "8D6FEABE0F3936145A474D3F05D33679".decode("hex")
    payload80_ctr = "2846EFA9DACB065C51C71C154F0E9EA2".decode("hex")
    payload80_off = 0x5F50
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "7013D0DDA6F8C9149163EA51A67018B1".decode("hex")
    payload90_ctr = "E3D4923757E97D29CFAD58896D53EE85".decode("hex")
    payload90_off = 0xC0B900
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "28E56A613F36B70FE295E22A44DA918E".decode("hex")
    payload98_ctr = "82566B8311E419CD238F9454994A6904".decode("hex")
    payload98_off = 0xD01420
    payload98_size = 0xBC290
    payload98_base = 0x98000000

    payloadA0_key = "7A0E46F3E362CCBC9988171F9EA89F47".decode("hex")
    payloadA0_ctr = "8074330C69CA88D593EFF15670E78989".decode("hex")
    payloadA0_off = 0xDBD6B0
    payloadA0_size = 0x115870
    payloadA0_base = 0xA0000000
    
    bootloader_key = "9C333852BBABC82FE5AD8C8D7EC05BF7".decode("hex")
    bootloader_ctr = "7214E2B09A5C7B9DC54FDB8C46CFFD59".decode("hex")
    bootloader_off = 0x571E50
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "B9501029CBB75F277EE8315F26DD4BCE".decode("hex")
    assets_ctr = "6C99263F2A07EFBA2A5A9609F02746BB".decode("hex")
    assets_off = 0x592E10
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "78176C951176AE5B0B6784F45B8553FC".decode("hex")
    fw_ctr = "56B409BC21DB9A7FEC8ED64C5A7E09D0".decode("hex")
    fw_off = 0
    fw_size = 0x115870
elif version == 120:
    arm64_key = "22429923901AF74ED6944992C824ACFE".decode("hex")
    arm64_ctr = "590BE04550CC6139921D1C95241F34AC".decode("hex")
    arm64_off = 0x53BAD0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "E483A884AB59D5D0014404C2EB698517".decode("hex")
    fb_ctr = "55A60F59F29DD518B4CAA59D0E3D1629".decode("hex")
    fb_off = 0x17BAD0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "AF8F5811D075F5317924E5C1DD70A531".decode("hex")
    payload80_ctr = "78219A2BB518BF9E302AFF75CE5862E1".decode("hex")
    payload80_off = 0x5F50
    payload80_size = 0x175B80
    payload80_base = 0x80000000
    
    payload90_key = "3DE87D8E1A24E06B2D50F6100AA09B4C".decode("hex")
    payload90_ctr = "94162463FF6B54FE9B6683F72CE79760".decode("hex")
    payload90_off = 0xC0B8F0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "5EBBF535CA7C7EE6C97A770CB1AA7E37".decode("hex")
    payload98_ctr = "BF9BA9CB3E2328ACD4676CE106081B3D".decode("hex")
    payload98_off = 0xD01410
    payload98_size = 0xBC290
    payload98_base = 0x98000000

    payloadA0_key = "9EBBBD4F4A5CC82B705431DFF5AA260A".decode("hex")
    payloadA0_ctr = "8A7923E459F12ED38CD533EFF69727D9".decode("hex")
    payloadA0_off = 0xDBD6A0
    payloadA0_size = 0x120530
    payloadA0_base = 0xA0000000
    
    bootloader_key = "F1A4E1EE2F279BB55A0C16D0373961BC".decode("hex")
    bootloader_ctr = "BC40537AB5F23088B9F1DD51FB0BB1D7".decode("hex")
    bootloader_off = 0x571E40
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "8D0CC65A2DE679BDB3D73C3F11734E0E".decode("hex")
    assets_ctr = "6CA93EAEEC84E218918F68DBFF8C95E9".decode("hex")
    assets_off = 0x592E00
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "84BB031A9E20D2BEAA10CE85BD4157BF".decode("hex")
    fw_ctr = "DC986E7B0FF4DD433F21D655B082BF43".decode("hex")
    fw_off = 0
    fw_size = 0x120530
elif version == 130:
    arm64_key = "0DA0D677361625E81FD6DF236B9450D5".decode("hex")
    arm64_ctr = "B368ECA0F8C078908F6B979613D0E52A".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "1E76718F0BAF7D8BB72ECCE4F657DAF8".decode("hex")
    fb_ctr = "4B0D81D9F44B8458F1EA93324C40BCD1".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "5B52BF7DED400C967FB0B2E013B55E68".decode("hex")
    payload80_ctr = "A1E038CE082F2C26052BE75F111CE3D1".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "36FC59BEBA2AABC77D124668E025350E".decode("hex")
    payload90_ctr = "E773714BD860B532A356F2C6A07B843E".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "9334A1F1943C16B2506BB1D9EBF33F93".decode("hex")
    payload98_ctr = "7BE8A72FBA0943AE57E93E6F6D6FB46A".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F1AC8CB71383F07FAF34C12879025BEE".decode("hex")
    payloadA0_ctr = "86B9D01C6FFAAF157CE31AE1162A7C48".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x1312E0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C439958095F3AC5CA361E46481A778B4".decode("hex")
    bootloader_ctr = "07E32283C45EC5215DEFDBB199AD2F5B".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "5E5C65FA5C93C43BD8BA5B7B93A59687".decode("hex")
    assets_ctr = "45E156D62914D27529AA7A8B7EAC8A31".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "264AAE11C24A65AB99E021788BFE6E66".decode("hex")
    fw_ctr = "71C68F4C9CBB2203AC267B917BAC76B0".decode("hex")
    fw_off = 0
    fw_size = 0x1312E0
elif version == 140:
    arm64_key = "C1BAE9D0BDBC2CFFE702BB071E5F08DD".decode("hex")
    arm64_ctr = "030B4E269E13F89A13D25F45474FB3C7".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "01009C5028E64261ABA99BDD588D062A".decode("hex")
    fb_ctr = "ED2FD755767BC51052B2414F938AA960".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "9BF5F63498B8CB415D33F78CAA18CBE8".decode("hex")
    payload80_ctr = "0886AA9881287E4D0529F011D6ED8DE2".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "404C0187E5B990DCED5180D1F8A6041B".decode("hex")
    payload90_ctr = "ADAD0B390E3192F7A8BB969C1F0F0485".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "E84E13FFD5C88C1B5C517E9DDB3EDAF9".decode("hex")
    payload98_ctr = "DBFCDD08231C6232029021EFDBDDC960".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "2C4E4F4389D142C5C8F19E221852241E".decode("hex")
    payloadA0_ctr = "CA9CCD03146F35CA1BEF06C8D3B37E2B".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x59FF0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "FADE622772177CC77B145F98A4D929BF".decode("hex")
    bootloader_ctr = "28EC8A0780FCDDD588467DD5143D8615".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "6F7FCB8B647E3B8F571B1897C9C87436".decode("hex")
    assets_ctr = "B43F32C904EDF459BC4811A6E074D86F".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "B8C11D378EE722BA3402B669C7278879".decode("hex")
    fw_ctr = "8FF8C494DED46749215202407DB70357".decode("hex")
    fw_off = 0
    fw_size = 0x59FF0
elif version == 150:
    arm64_key = "407CC1C82F9C2E527C4A1B2EB37B323D".decode("hex")
    arm64_ctr = "92C67922E69AFFB196D9B69E7B2127C8".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "99A5466D889C26E1E7D0B22DF4684264".decode("hex")
    fb_ctr = "8649C0C70C461E4AB4A0299547655EF6".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "F98AF4F9797B7817BD9815D7B238D077".decode("hex")
    payload80_ctr = "A4D4D0F8A7946F2AD2E479CCDD3F5A9F".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "AE6DA6A206B70A5D89CC1D0884634643".decode("hex")
    payload90_ctr = "C461A8629F78081F6C3F0F5FC51607C3".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "0AB48861EA47036DC3E45B06A200B88E".decode("hex")
    payload98_ctr = "2FFDE0F331F6BA7DBCE7B2B228EDD0F0".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "A6BCA4B3EA6BBDF020F3F61268598608".decode("hex")
    payloadA0_ctr = "1897D379814B637E838C472B47C65C2D".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x689A0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "735B1BB11204B95DEF28338008AD9EEB".decode("hex")
    bootloader_ctr = "759421CBAB3C0164998705EAC843686E".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "1FE697859710A3E4A0A5F583EABB5360".decode("hex")
    assets_ctr = "B22FC3208D038C5025AB3716F466EFF3".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "534F6705DB4C19822A90D72A0E52871E".decode("hex")
    fw_ctr = "D29A20D59C1615CD84D09D95A4A5824D".decode("hex")
    fw_off = 0
    fw_size = 0x689A0
elif version == 160:
    arm64_key = "81A2CEBC2923A84082A2738B62AE4237".decode("hex")
    arm64_ctr = "B5EB1DEC39C6D6D75EFBAD01215CF01B".decode("hex")
    arm64_off = 0x53BB00
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "345F7D4471FB2B21CA5CCFE4C6432959".decode("hex")
    fb_ctr = "B488803EA9C1EBCEFEFF6A3F9D813BB2".decode("hex")
    fb_off = 0x17BB00
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "06BA3CE40A34917CD5791F5AA07C5678".decode("hex")
    payload80_ctr = "938AF18A64DB9899921B896BF8F9F190".decode("hex")
    payload80_off = 0x5F70
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "EB2CCE4A12A5E67D18BA7E7694BB668E".decode("hex")
    payload90_ctr = "541D5A701ACE180CF8FF4BEDA9420084".decode("hex")
    payload90_off = 0xC0B920
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "D21A5BCC99ACD2D06C785596A38E783A".decode("hex")
    payload98_ctr = "7C20F115244654025B14833A9AD949EE".decode("hex")
    payload98_off = 0xD01440
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "9E1B0673697520D8431F121D93B97DEF".decode("hex")
    payloadA0_ctr = "205800A34B37097DFD7B7C4780C2F982".decode("hex")
    payloadA0_off = 0xDBD6D0
    payloadA0_size = 0x68AE0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "6D3210FFF1CF4514C0CEFD0D1FB1B975".decode("hex")
    bootloader_ctr = "E5DE043AC5D59CE37AF79F73B04309CB".decode("hex")
    bootloader_off = 0x571E70
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "EFB643AC023866040B25509F002C3239".decode("hex")
    assets_ctr = "B7651B5E1A5C17EF5067B447F5F7DDB9".decode("hex")
    assets_off = 0x592E30
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "376D7644BD386A377DDBFAEC8F25773B".decode("hex")
    fw_ctr = "2DF4E0DB583089B9873A53E8F420CA59".decode("hex")
    fw_off = 0
    fw_size = 0x68AE0
elif version == 170:
    arm64_key = "469481EDF8300C6F02A860479AEDEE70".decode("hex")
    arm64_ctr = "E68E3300AB7837501D20D53218363937".decode("hex")
    arm64_off = 0x53BB70
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "D61B4F92411613F1EF352446C898A1BA".decode("hex")
    fb_ctr = "CC4BB77C97C741E54C2BDB02B797A1D4".decode("hex")
    fb_off = 0x17BB70
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "F6319F3E4C4D6DDC11154B50DBD80AF2".decode("hex")
    payload80_ctr = "429DF9227D66937F1F80F3F0E57B24E8".decode("hex")
    payload80_off = 0x5FE0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "C6E8A08D888CF9CFCFABAA6593F5E209".decode("hex")
    payload90_ctr = "4161154C99F06E1E1464B7864C2CDDD9".decode("hex")
    payload90_off = 0xC0B990
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "C4A04B22B56E93445953C0B868C2C2F8".decode("hex")
    payload98_ctr = "250450BAB0DA9EACD3BA333CEAD4BA7B".decode("hex")
    payload98_off = 0xD014B0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F951256F5AB23C7EF1C2837D8581FA77".decode("hex")
    payloadA0_ctr = "0FAC52D6D8D7C212B2499810C9815232".decode("hex")
    payloadA0_off = 0xDBD740
    payloadA0_size = 0x68E30
    payloadA0_base = 0xA0000000
    
    bootloader_key = "E678C11F28849BC6DC525061A7C2C0D9".decode("hex")
    bootloader_ctr = "79029F017F0CA753E524145F362AC3E5".decode("hex")
    bootloader_off = 0x571EE0
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "767744996BAC7107FC2B3B4882033476".decode("hex")
    assets_ctr = "A298473FBFD787EDBA8DE2B50E0A25CA".decode("hex")
    assets_off = 0x592EA0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "3FBE84AD7FD4DACEA0A1A3401B548F3B".decode("hex")
    fw_ctr = "9378E449EF34C8FC5B204853F12CD01F".decode("hex")
    fw_off = 0
    fw_size = 0x68E30
elif version == 180:
    arm64_key = "080B73616C9E082B934F31F6C5B112FD".decode("hex")
    arm64_ctr = "8F13149E9F88FE285D375E856CEA4C80".decode("hex")
    arm64_off = 0x53BB70
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "5358EB25799A7DB78539DF6170F7E48F".decode("hex")
    fb_ctr = "3B3616F6375038D975E71E488A34CE7F".decode("hex")
    fb_off = 0x17BB70
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "3CA900F5767B81D0F9294E1C6EA6E972".decode("hex")
    payload80_ctr = "508E7E6941A9021F4BC1D85BF081F6C8".decode("hex")
    payload80_off = 0x5FE0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "C436E39A1BCD198F4200516242217010".decode("hex")
    payload90_ctr = "1840E301126AA9CA8F549CCDF3889294".decode("hex")
    payload90_off = 0xC0B990
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "CD16B01836D1A7587DA50F546CA68AC9".decode("hex")
    payload98_ctr = "BA4E9B943DCCDE3E1A91038773E7A1BA".decode("hex")
    payload98_off = 0xD014B0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "13F112C8668B8715C3BEDF24012CCE43".decode("hex")
    payloadA0_ctr = "58A06A2FAB8FC3C2D849A7E0D3687C25".decode("hex")
    payloadA0_off = 0xDBD740
    payloadA0_size = 0x68EA0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "D361215F332E1D2487D656DE89DC60BB".decode("hex")
    bootloader_ctr = "7ACB8F5587023560AD3C565D4072B748".decode("hex")
    bootloader_off = 0x571EE0
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "5F6FDE101B5490272E94FC8B02E16598".decode("hex")
    assets_ctr = "A6EB0224D08BB2EAE9AF6A9C34BFE0A5".decode("hex")
    assets_off = 0x592EA0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "24ABD9DBBFA9B286464069CB43406126".decode("hex")
    fw_ctr = "753D3C5922B09B82FDF093B1EC0679F0".decode("hex")
    fw_off = 0
    fw_size = 0x68EA0
elif version == 190:
    arm64_key = "8FF020361DC5EE595B24432190A56A37".decode("hex")
    arm64_ctr = "9601BB4E5D8B96505BD8600636A6B6F6".decode("hex")
    arm64_off = 0x53F7B0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "D00D6F8135CAC6D48A5F5E538953F194".decode("hex")
    fb_ctr = "AF73E22FE3B4120E8AD00411F9B507EE".decode("hex")
    fb_off = 0x17F7B0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "88D11A7F1DA0744E24D5080CC6E60144".decode("hex")
    payload80_ctr = "A530383538AB4E14BB593CC63056FC31".decode("hex")
    payload80_off = 0x9C20
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "B9ADE0F7BD1EAE99F5D069766B191CF7".decode("hex")
    payload90_ctr = "0C71509233E4EAD601FA430CD92FB679".decode("hex")
    payload90_off = 0xC0F5D0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "C553D270DE004031B1A500C40856E051".decode("hex")
    payload98_ctr = "DE2551AC87A3CC5245A2D327395D8232".decode("hex")
    payload98_off = 0xD050F0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "363413B94F08FADBA77B201E5874A17D".decode("hex")
    payloadA0_ctr = "E59D8ED75CF96EAB5ADB14BD1210ADA4".decode("hex")
    payloadA0_off = 0xDC1380
    payloadA0_size = 0x674B0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "63742C20A5766B1A5D0550D6056958AB".decode("hex")
    bootloader_ctr = "ECE382D94917BA828804828DBC57E96F".decode("hex")
    bootloader_off = 0x575B20
    bootloader_size = 0x20FC0
    bootloader_base = 0x88000000
    
    assets_key = "E343335CBDFE5DFA8FD5271E42FE7C11".decode("hex")
    assets_ctr = "8982C3250EF72A55EF7E3597F2F2A28F".decode("hex")
    assets_off = 0x596AE0
    assets_size = 0x4C0400
    assets_base = 0x88020FC0
    
    fw_key = "B2E2F4A27F6CA2238DA3090C665CB444".decode("hex")
    fw_ctr = "0E1EC09B58C73BC225CF0F5757311B20".decode("hex")
    fw_off = 0
    fw_size = 0x674B0
elif version == 200:
    arm64_key = "5421346FCE84BB6AEC3AEF846DF1F827".decode("hex")
    arm64_ctr = "48ADCB7E1696EDEB0A3D5BEE6A131DCB".decode("hex")
    arm64_off = 0x53FFE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "5F58D9832339AC0B1B7893573575E77E".decode("hex")
    fb_ctr = "05BE5152A45F3E47BA9941E6FED1D166".decode("hex")
    fb_off = 0x17FFE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "1A4B9803CB5CF96B7F17167A558A77F8".decode("hex")
    payload80_ctr = "EDDDC820771DBAA60A16CC2CCB1AE5D8".decode("hex")
    payload80_off = 0xA450
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "8545442BF5CB8848C752969379495834".decode("hex")
    payload90_ctr = "A39FE90850DF95CFEAD2330174AB8AA4".decode("hex")
    payload90_off = 0xC39E40
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "4BA67934D070999376E8A22E7A3E3DED".decode("hex")
    payload98_ctr = "3FDA98AC6C106E6C4AF0DB6E9F6B6976".decode("hex")
    payload98_off = 0xD2F960
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "B57345C1307C406F39161A03A0800C76".decode("hex")
    payloadA0_ctr = "535A4EF3B062A457736CAFFDB23A477A".decode("hex")
    payloadA0_off = 0xDEBBF0
    payloadA0_size = 0x68FF0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "25BB22426788BA349A6084F86F639966".decode("hex")
    bootloader_ctr = "A0F3C3D386912249AAC13D4080A34BAD".decode("hex")
    bootloader_off = 0x576350
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "56CEFAA60C9228C084AE2F8F9BF05A9B".decode("hex")
    assets_ctr = "29B3EEF7629A3B266A304D2C2686CCEE".decode("hex")
    assets_off = 0x5A9350
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "A644D3896171F04BFAFA145670CFA754".decode("hex")
    fw_ctr = "1D5ED868682B78C22B975533EC54B940".decode("hex")
    fw_off = 0
    fw_size = 0x68FF0
elif version == 201:
    arm64_key = "88F63BD5167EC20830152F043E689EB8".decode("hex")
    arm64_ctr = "B0DA5DC62EB6F5B5AE2CBD4E76B3E243".decode("hex")
    arm64_off = 0x53FFE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "1FBC61D0C68485EE7E0CCEFDA071455F".decode("hex")
    fb_ctr = "AC5525DB506255FA65F5FB4861347725".decode("hex")
    fb_off = 0x17FFE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "C9B2B700D354E3C2B4A7B1E0B3391B28".decode("hex")
    payload80_ctr = "AE809C9199F025B3A511ABC778B9BFDD".decode("hex")
    payload80_off = 0xA450
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "B98E565F67B2CE98362AA4BF4F63B285".decode("hex")
    payload90_ctr = "A1C674C08191F55DA125433207B74DB2".decode("hex")
    payload90_off = 0xC39E40
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "A3A8F9B91107049835FFE38CFAC02F03".decode("hex")
    payload98_ctr = "682EEF46CA0979B1A9DA6EE3CD977D0D".decode("hex")
    payload98_off = 0xD2F960
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F14481FA77A09437046AF1C453210562".decode("hex")
    payloadA0_ctr = "8583C354ED368877E1624FABB80D5631".decode("hex")
    payloadA0_off = 0xDEBBF0
    payloadA0_size = 0x6A2F0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "AEA54EBE9D700CC9334165ED88F52348".decode("hex")
    bootloader_ctr = "8350C5A81015E6BE4D8C1A8F6F9E833E".decode("hex")
    bootloader_off = 0x576350
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "174BD6B29158444A775CCA63D2A5238E".decode("hex")
    assets_ctr = "4A6AA511A75A277162284451E36B4D82".decode("hex")
    assets_off = 0x5A9350
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "474325E4147C63092E96EA693E7D1433".decode("hex")
    fw_ctr = "0414D05A071E83B3C64C3E61C8557255".decode("hex")
    fw_off = 0
    fw_size = 0x6A2F0
elif version == 210:
    arm64_key = "726D57B05F0B2BC6F6A31E7ADF21618E".decode("hex")
    arm64_ctr = "6FBF960EDBC5EA149FCC7675439B2368".decode("hex")
    arm64_off = 0x53FFE0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "518F2FFC9B4AEC2BF5A488B439366408".decode("hex")
    fb_ctr = "46689C134D45E2FD7639220FB8FAB472".decode("hex")
    fb_off = 0x17FFE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "0ADF1975F209A3B093B60A3FF32EE146".decode("hex")
    payload80_ctr = "CDCAA8CEAA893BC6B2B4C8F44CF11970".decode("hex")
    payload80_off = 0xA450
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "ECE308D1D6E3CFF988EC332C69A727ED".decode("hex")
    payload90_ctr = "4F1B32C985BB6B5BB93262FE3305C0AA".decode("hex")
    payload90_off = 0xC39E40
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "8BA66D50922849A87EC13E7A78DB0109".decode("hex")
    payload98_ctr = "C091B06C606A6E2AA4F06FB093691EB5".decode("hex")
    payload98_off = 0xD2F960
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "469F945F581F038A45618B20C7DF6F76".decode("hex")
    payloadA0_ctr = "A8959DB43802B08C891D0B55F2FB6794".decode("hex")
    payloadA0_off = 0xDEBBF0
    payloadA0_size = 0x6B240
    payloadA0_base = 0xA0000000
    
    bootloader_key = "0409FC24536E362DD080CBFD1498DFC6".decode("hex")
    bootloader_ctr = "7ABAE1B8335974D6B4E586D3B4D33196".decode("hex")
    bootloader_off = 0x576350
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "D63BE485CB58716196055AFF004BF143".decode("hex")
    assets_ctr = "B673F5BD2C1B3C9174060552B598D7D6".decode("hex")
    assets_off = 0x5A9350
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "4FB6882B92DA97D5DA233E660CBBF1E2".decode("hex")
    fw_ctr = "C21F0EF96CD2F18360089D8C65C63D88".decode("hex")
    fw_off = 0
    fw_size = 0x6B240
elif version == 220:
    arm64_key = "912F24E1F53D56CA9805D14BDBF8A0D1".decode("hex")
    arm64_ctr = "D6DA10E22727B429527D511DAF0243F5".decode("hex")
    arm64_off = 0x5400B0
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "9FECE0235086D7DF3ED4EFC7FCFA63F7".decode("hex")
    fb_ctr = "76CA419A93A544988C96BA8828B46E92".decode("hex")
    fb_off = 0x1800B0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "B98F301D97A66F3EF3ADE65E8E78014A".decode("hex")
    payload80_ctr = "3448F56D78DBD16CD8D1D9E28D3349E8".decode("hex")
    payload80_off = 0xA520
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "EE676C14CF4FC1B56B5E3CBCE6C6AA56".decode("hex")
    payload90_ctr = "6A4F46C609D042A506109DC67CF67321".decode("hex")
    payload90_off = 0xC39F10
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "817D7934FD5D10AEB4D3AC5B86D1D929".decode("hex")
    payload98_ctr = "602D2EE3EB8221FA5B4DDAE88A333567".decode("hex")
    payload98_off = 0xD2FA30
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "764A681CAC520674DAA3F07B743E412E".decode("hex")
    payloadA0_ctr = "A4FC4B6A126A3A7429351AE514D51847".decode("hex")
    payloadA0_off = 0xDEBCC0
    payloadA0_size = 0x71880
    payloadA0_base = 0xA0000000
    
    bootloader_key = "FA0C4982AE476B3E1EA48BF49C07A680".decode("hex")
    bootloader_ctr = "138914FCE54056BA18C472FF35EAF2B4".decode("hex")
    bootloader_off = 0x576420
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "F1769A875BF70CF0C1D59326A4A45DB6".decode("hex")
    assets_ctr = "39B1C4AD9AC8C8949DF95E883B0B8261".decode("hex")
    assets_off = 0x5A9420
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "496F4B42816945B371662126BB192D49".decode("hex")
    fw_ctr = "B674C639CF3D522752320983DAB987C5".decode("hex")
    fw_off = 0
    fw_size = 0x71880
elif version == 221:
    arm64_key = "DF7F3184C466FAA56EDFCC43E74905A0".decode("hex")
    arm64_ctr = "4B6DB003373192CABA447B5E3305D779".decode("hex")
    arm64_off = 0x540530
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "72CB3A30DED6AC9C8DDDDCE778AF18C3".decode("hex")
    fb_ctr = "0DCF05FCD3165ED2B76E9E5048EA5FE0".decode("hex")
    fb_off = 0x180530
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "0CE4F9BE6BCE9D4FC85CF56110D03F15".decode("hex")
    payload80_ctr = "F60A799057A5ABE69D56E40089DDEDF7".decode("hex")
    payload80_off = 0xA9A0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "BCDDF8E03BB29E4AF53EA437B5A327A9".decode("hex")
    payload90_ctr = "1BEAA065F8A4AA120A3BB9786FCFF815".decode("hex")
    payload90_off = 0xC3A390
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "A18C98DD5BEEBC30C62F950C6C2D0133".decode("hex")
    payload98_ctr = "D07406E4BE4557967E7FACF0F006EF2E".decode("hex")
    payload98_off = 0xD2FEB0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "38C852F0B636FD231E7E3FC3CAD1C2E3".decode("hex")
    payloadA0_ctr = "3A50EB632ACEF74542C16623F31AB046".decode("hex")
    payloadA0_off = 0xDEC140
    payloadA0_size = 0x76F00
    payloadA0_base = 0xA0000000
    
    bootloader_key = "80EDE7A42FCE5EC197D1EAC37085981C".decode("hex")
    bootloader_ctr = "46FF431605844B997FA939B2053E668B".decode("hex")
    bootloader_off = 0x5768A0
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "AE2AEDAAF6D2BE55B4449A8593827D1E".decode("hex")
    assets_ctr = "79CDE541DAEF4E0CBFB4BC89A79DB992".decode("hex")
    assets_off = 0x5A98A0
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "908B117B241C5257DFB09FC20BE8943E".decode("hex")
    fw_ctr = "6A0BE18089129A58181155C5B7A9BBC4".decode("hex")
    fw_off = 0
    fw_size = 0x76F00
elif version == 230:
    arm64_key = "CF7286C1F8C3300F9E9F218065CE6FE0".decode("hex")
    arm64_ctr = "9B285AD4E527E3ADDDCBFDA21536E2D0".decode("hex")
    arm64_off = 0x540650
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "3842A6270DF9488EF47D7FD28106502E".decode("hex")
    fb_ctr = "AF95C4B76752D5360CEE8DA3613E5ACD".decode("hex")
    fb_off = 0x180650
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "0C482DA896C0F1A20785D773E541D5C4".decode("hex")
    payload80_ctr = "C6A03A8ACE0C553F43D36EF71679232F".decode("hex")
    payload80_off = 0xAAD0
    payload80_size = 0x175B80
    payload80_base = 0x80000000
    
    payload90_key = "5057CD5B625D54EAC873D701E4242D2C".decode("hex")
    payload90_ctr = "DE702CDA2C10DFB4A5C301779D6C8E01".decode("hex")
    payload90_off = 0xC3A4B0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "E91CFD27867700954A69B6F25D3BB58A".decode("hex")
    payload98_ctr = "D614424E4876404863588BF93A5EDEFF".decode("hex")
    payload98_off = 0xD2FFD0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "C17826EC6E847F83C3AB34F5B686AADF".decode("hex")
    payloadA0_ctr = "0359E40094782F4F4E8BCD90D2440A70".decode("hex")
    payloadA0_off = 0xDEC260
    payloadA0_size = 0x7F360
    payloadA0_base = 0xA0000000
    
    bootloader_key = "708F97BE5663BE4D248A2F1F2FFCB02E".decode("hex")
    bootloader_ctr = "CFA497C913CADA90C23EA3135E931EE1".decode("hex")
    bootloader_off = 0x5769C0
    bootloader_size = 0x33000
    bootloader_base = 0x88000000
    
    assets_key = "595D289B1D5A19A59E2AE1EB213738D9".decode("hex")
    assets_ctr = "A456EE87BFF343CCC55A75E369CDE106".decode("hex")
    assets_off = 0x5A99C0
    assets_size = 0x4D8400
    assets_base = 0x88033000
    
    fw_key = "9CC31623621336122680BE55CE1205F8".decode("hex")
    fw_ctr = "83169D2F38590669158A9928EC0DD3CA".decode("hex")
    fw_off = 0
    fw_size = 0x7F360
elif version == 240:
    arm64_key = "E2E56C54A36A9F0E91249B01E522ED1E".decode("hex")
    arm64_ctr = "B54A8A7BBD65DEA725E5FB6CBC19BC77".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36370
    arm64_base = 0x80FFFE00
     
    fb_key = "4F5E892DDA5946254E33C2F7D76B7904".decode("hex")
    fb_ctr = "2965E52C440D0A90861D18A9F09518D2".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "3CDC53A1FA0725B0A0FBEA7A47A711D2".decode("hex")
    payload80_ctr = "5BB2774E4BB8D05C6A6A707BE87792B6".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "F84650B75C01E9826116A08C0457C386".decode("hex")
    payload90_ctr = "D9BD23C8BAF707819922B2C10551BEF5".decode("hex")
    payload90_off = 0xC393A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "97788D3B3D092BB7FB1A3E788C3DD3EF".decode("hex")
    payload98_ctr = "63BDB1B13C354417B12D9DF312751570".decode("hex")
    payload98_off = 0xD2EEC0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "6423AA4095B57572D684568DB3712853".decode("hex")
    payloadA0_ctr = "E80E301C71518C31ACDFCCCE7A98DA2E".decode("hex")
    payloadA0_off = 0xDEB150
    payloadA0_size = 0x7DC60
    payloadA0_base = 0xA0000000
    
    bootloader_key = "776333894C7C7EF9819ADD4A00FC8E9D".decode("hex")
    bootloader_ctr = "16EC2B9012FA6849D3FE8BA51AB860C0".decode("hex")
    bootloader_off = 0x5778B0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "D6E524558716AB4495367CF6DBF4C4FB".decode("hex")
    assets_ctr = "F12B4BA9CBE043D470CE81FFD365FFF3".decode("hex")
    assets_off = 0x5A88B0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "BF7B24E0478167AD5E2F76C57DD41C59".decode("hex")
    fw_ctr = "514A33384321976B6F04BD02E587C1E8".decode("hex")
    fw_off = 0
    fw_size = 0x7DC60
elif version == 241:
    arm64_key = "AD52C9AC41A930629A1C007832EA656C".decode("hex")
    arm64_ctr = "3DB839FD3C3AC1718D2AEFCD474FC510".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "393046399B2CE12109B7E250EB7E66B8".decode("hex")
    fb_ctr = "1CABBB1A1E2C18ECA2C623EAEFF10DC3".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "80261C64FB62543607DE3179FDB8BD8F".decode("hex")
    payload80_ctr = "0997749F304867A249FE5154CAE19114".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "A0BA31F12B44E3C51231731F8E7DCE3D".decode("hex")
    payload90_ctr = "EA3467C4C2DDCF9E2B237CEEFA8B2F73".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "CD24A287EF803E1A03862F5702F2213F".decode("hex")
    payload98_ctr = "EBAE7A97BD9EE2F85E592E5B6324DD43".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "AF7F69790C0BCE3BEC55402416683C85".decode("hex")
    payloadA0_ctr = "8803D2D2FA3630748AF548A45C982AF3".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x7DC50
    payloadA0_base = 0xA0000000
    
    bootloader_key = "2A882183AC20AE70CF8C18CCBD393945".decode("hex")
    bootloader_ctr = "CE5792D332C7D854567E698E3FB438F1".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "CFCFC912920E9BD17CD38829A5FB5B38".decode("hex")
    assets_ctr = "A052D42CB1BAB825F256315B980C5DEE".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "328E1D6E8C5E435F6D1C342090475C72".decode("hex")
    fw_ctr = "422571782D7CFB7E26CC0516801AD181".decode("hex")
    fw_off = 0
    fw_size = 0x7DC50
elif version == 250:
    arm64_key = "DBD3059B920D1CC75C555401CDEC045E".decode("hex")
    arm64_ctr = "69C7E7E3E2ACD315E74C6040386108A6".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "F087C3E9E75674DA01D0CFAF44279B6D".decode("hex")
    fb_ctr = "5544128B01DA21DC065536A7D29A795C".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "FA50BBB9499D3F790D733633BDF4D9DB".decode("hex")
    payload80_ctr = "A4C2D2ED364D57412C2384CDA65C3434".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "4B7FB43C99888DBAC0942D1B14A6AB36".decode("hex")
    payload90_ctr = "4FA7F1C5C2E056C371F36C38DA586B26".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "7CF57477016CAFE525DD570EFC0A4386".decode("hex")
    payload98_ctr = "F12CC7DD80DAC7C6F87F85A49855FA3A".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "B3356B83B3189050458D7F17D0275E3E".decode("hex")
    payloadA0_ctr = "94F7D32D84B2E34C809B9C9FD67A0777".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x86280
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C196E7A1B6DB410B95C2EC30233B6ED3".decode("hex")
    bootloader_ctr = "1AFDBF2A89F090D0FFE5756CAB835631".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "8B21B2E6418DC8483277F87A94C3392F".decode("hex")
    assets_ctr = "2835032A4624915A757DD73F95166D3D".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "6E34454ACAB9824A8A2FD1DA8516CB50".decode("hex")
    fw_ctr = "51556B291B98251E7CF1AB867357B6E4".decode("hex")
    fw_off = 0
    fw_size = 0x86280
elif version == 251:
    arm64_key = "B6F78BEB41AB6982B0916C09749E3538".decode("hex")
    arm64_ctr = "3ECA0C1E11AC66E9D9BE36E8C69F1675".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "3AD0173DC807EEF2A10106A02423F36F".decode("hex")
    fb_ctr = "55EE810C8B37616E88FD60E8A88C4484".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "E58C28B94260E1C68DC83A15199AB43E".decode("hex")
    payload80_ctr = "34A5A9BE720951098473FF91FAE4AB0D".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "1312378C696D73F5B9C0CAF435BF9E01".decode("hex")
    payload90_ctr = "30B0F050605DEE6544E882BDCAB00270".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "68EDAB3E2990E61AFBEF3131CE81AFBB".decode("hex")
    payload98_ctr = "36537950E3EC3CCE0310B29E44DFF398".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "97BD4243B2A51595CEBF10FFACD12709".decode("hex")
    payloadA0_ctr = "4CAEC0B13D430C9DCF08C1443F29888F".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x86470
    payloadA0_base = 0xA0000000
    
    bootloader_key = "450BE513C651C282A81FD7900B9D7625".decode("hex")
    bootloader_ctr = "3B73FFA158508B95F85755B03A95E2BA".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "FE4878237692DFD1F337DC6886CCB140".decode("hex")
    assets_ctr = "F0AAA0969B69FDBCD9DD7E2CF8C4DA5E".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "B68AE8028313C1EF761FA1BE41E56A66".decode("hex")
    fw_ctr = "51B3A71C9C574F251835C88C322BEAEC".decode("hex")
    fw_off = 0
    fw_size = 0x86470
elif version == 252:
    arm64_key = "0883194678432CD79ED54ED7C5D1CBEC".decode("hex")
    arm64_ctr = "72D199289598A3DCD84C06ECDFA85DDE".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "14C3A3A33B4B1F4659F364DC29422DFD".decode("hex")
    fb_ctr = "2ADA0FD01AB8CEC1669BB97E616E1CBD".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "172A09354DA46832FDCC89E8511898DF".decode("hex")
    payload80_ctr = "40AE331DEF273A6E76FB803AD7460167".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "5FCCC552C3A858E3650D60784C51E978".decode("hex")
    payload90_ctr = "649C698868CEB4FEFACB250E7E0E18FE".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "96FDA317909656484D6EE412959B189E".decode("hex")
    payload98_ctr = "B3ADA7BEB8695216B9CEF145DB18A053".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "E8C815198227E14A646E7465A682EB63".decode("hex")
    payloadA0_ctr = "176A50BE0A2481646C8CDFF0707099F9".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x86490
    payloadA0_base = 0xA0000000
    
    bootloader_key = "D3B64C8E57033058582643AB5065FFDF".decode("hex")
    bootloader_ctr = "E3A6EA967CF832D1DF2B731620EDBBDA".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "9E270E5E9A0EBDAB95589446793D7E78".decode("hex")
    assets_ctr = "A05CFA29C04FD14B267CB52795BE6262".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "AF18B196DE0E240655F8D8A59FAD585D".decode("hex")
    fw_ctr = "5F0251C985697D2216576991F4C7F5DD".decode("hex")
    fw_off = 0
    fw_size = 0x86490
elif version == 253:
    arm64_key = "5C1D2D863D75E399E79BE6A7F8298FD4".decode("hex")
    arm64_ctr = "2ECEECE30C6C98EB47F2519381178CF2".decode("hex")
    arm64_off = 0x541540
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "700C5C4A5A8A4930577E6712B7B0BF42".decode("hex")
    fb_ctr = "E6B5B163DE91E6A04F5E7E7DCD44DD84".decode("hex")
    fb_off = 0x181540
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "992DCFF93D1346957F57116D5FF0E902".decode("hex")
    payload80_ctr = "A446E7629E99B02C6F2770D99B877E62".decode("hex")
    payload80_off = 0xB9B0
    payload80_size = 0x175B90
    payload80_base = 0x80000000
    
    payload90_key = "06E663F93362E4A7D6CBBFCF4E790E54".decode("hex")
    payload90_ctr = "8DC308384AB3152E593106481EB40E61".decode("hex")
    payload90_off = 0xC395A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "6D5366A10514D10BC1E0A46DC0CEBA69".decode("hex")
    payload98_ctr = "B5C9BDEFF1ABCB7175C1939E63420910".decode("hex")
    payload98_off = 0xD2F0C0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "1B850B5690AFC211CC994D83FEEE94DE".decode("hex")
    payloadA0_ctr = "530D7DF487C635901B8E689D03EFD902".decode("hex")
    payloadA0_off = 0xDEB350
    payloadA0_size = 0x864A0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "BA6DF53AB718F544755733C804B279D7".decode("hex")
    bootloader_ctr = "68DFA341E6F561D2D3A1598A83CDADB3".decode("hex")
    bootloader_off = 0x577AB0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "6208AB46E0227D8EACB9B08F8383BE8C".decode("hex")
    assets_ctr = "A8040F28D07989AFC6CFD19FCC5DFCB0".decode("hex")
    assets_off = 0x5A8AB0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "9165377EB58BABC3AAD9977F50299213".decode("hex")
    fw_ctr = "A6E10A060055BBB699A2FA9652C17D00".decode("hex")
    fw_off = 0
    fw_size = 0x864A0
elif version == 260:
    arm64_key = "8602ED08DCABF1A6EAC619FB13AFA956".decode("hex")
    arm64_ctr = "BFE5AF933926CF398937C41D108149D4".decode("hex")
    arm64_off = 0x5783F0
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "A99AA061834C4F648025848C7071F217".decode("hex")
    fb_ctr = "9C8D93727825A258EE6C61350FFD3BCB".decode("hex")
    fb_off = 0x1B83F0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "1968B5AD31ACE9BF160D45A308C7EB88".decode("hex")
    payload80_ctr = "D2D492B9E32501E291453CF99DFD5DF0".decode("hex")
    payload80_off = 0x127E0
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "4005657B030C31AAA6DA29C5488C4DDD".decode("hex")
    payload90_ctr = "2821BD60180A43146CC18B65456F10A6".decode("hex")
    payload90_off = 0xC70450
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "4BE17E971CE5B3F6F3071A78AF2373EC".decode("hex")
    payload98_ctr = "9ED3E8312484F3159C00AFF2E83255DE".decode("hex")
    payload98_off = 0xD65F70
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "8CC8262F88745BAB871DA653B87118C6".decode("hex")
    payloadA0_ctr = "6B31A8E63F3C84C10F72627ECD4C8FBE".decode("hex")
    payloadA0_off = 0xE22200
    payloadA0_size = 0xF6530
    payloadA0_base = 0xA0000000
    
    bootloader_key = "278330AF57BB10EAD06F7C8022ADE770".decode("hex")
    bootloader_ctr = "B81759B053DF95AD15546FFECFD01227".decode("hex")
    bootloader_off = 0x5AE960
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "BB98BE3411898A275AED852296C19013".decode("hex")
    assets_ctr = "828BEF4898945390DA6A7123C99623B6".decode("hex")
    assets_off = 0x5DF960
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "A796385D2538768CD04DEB1446721A85".decode("hex")
    fw_ctr = "21FA30085D92E13A1AF42FC5F7CA177B".decode("hex")
    fw_off = 0
    fw_size = 0xF6530
elif version == 261:
    arm64_key = "3A2C6326CA64CFF697C80EC72C45789F".decode("hex")
    arm64_ctr = "E3B43062ED8E821C13586B8A33CB6816".decode("hex")
    arm64_off = 0x5783F0
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "05FAA5928AB58C992430764C8F07EB62".decode("hex")
    fb_ctr = "E5C9E675BE4A76BB2D000EB27F959BB5".decode("hex")
    fb_off = 0x1B83F0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "A4BF1516A18F9886CBF2908D0C36B193".decode("hex")
    payload80_ctr = "AB3A5480CCACBBBC3ED8DDE6BC591549".decode("hex")
    payload80_off = 0x127E0
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "400D5B45B2BE801D4068B72334B9171E".decode("hex")
    payload90_ctr = "DF8EB8E101C09D46A6775ED4692D3AB7".decode("hex")
    payload90_off = 0xC70450
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "0BDCA7628024A661EE34F5BC617A6AFA".decode("hex")
    payload98_ctr = "8CA1406966CA5818290F936730A8ED40".decode("hex")
    payload98_off = 0xD65F70
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "E826CD81F45DD36B40D7797367112430".decode("hex")
    payloadA0_ctr = "DF0103D103ED12513D85592939D12414".decode("hex")
    payloadA0_off = 0xE22200
    payloadA0_size = 0xF6500
    payloadA0_base = 0xA0000000
    
    bootloader_key = "2C0722619C824A37FF8BB4E8D07EA7E8".decode("hex")
    bootloader_ctr = "7E21DEE65622697E2CEE413E09EE163F".decode("hex")
    bootloader_off = 0x5AE960
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "CDD7F774BDAF447BB6E8434866906A01".decode("hex")
    assets_ctr = "40701C44498AE67A09F4B014FB08981E".decode("hex")
    assets_off = 0x5DF960
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "9B97497C339741C2A12EC892B3887333".decode("hex")
    fw_ctr = "EBEDCAFA1CAEB5949D200843883D82B3".decode("hex")
    fw_off = 0
    fw_size = 0xF6500
elif version == 262:
    arm64_key = "D224A1EF9A3F4EBD5A9E32831D9E8117".decode("hex")
    arm64_ctr = "F500D3B105516DF1BF0636BD868E1114".decode("hex")
    arm64_off = 0x5783F0
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "7B0D9E403591E77048B7A08CED882B19".decode("hex")
    fb_ctr = "27CF9F9D0E1113E881A510E352E9E87F".decode("hex")
    fb_off = 0x1B83F0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "531F93CC62807B70691D4A33D2B1934B".decode("hex")
    payload80_ctr = "0B60C21AA33D0B38E99A746C1EC4C397".decode("hex")
    payload80_off = 0x127E0
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "70A047745010733626B3333EBCA47D22".decode("hex")
    payload90_ctr = "482B6E21D13C4C450BE83F0A165CEA30".decode("hex")
    payload90_off = 0xC70450
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "8439F2269B1EBDFCA6247A663126DFBA".decode("hex")
    payload98_ctr = "3DFEFA0ADF70BCB137B2791027B394A6".decode("hex")
    payload98_off = 0xD65F70
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "13B3322459DC080772FA381878F606BD".decode("hex")
    payloadA0_ctr = "D2E8456CF71BF47F38A76979C54A59AC".decode("hex")
    payloadA0_off = 0xE22200
    payloadA0_size = 0xF6580
    payloadA0_base = 0xA0000000
    
    bootloader_key = "A680F5000121C66CB1526312B2DDF037".decode("hex")
    bootloader_ctr = "D214275C9BBEC7B1F5F0D5CE72C96561".decode("hex")
    bootloader_off = 0x5AE960
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "EB697CA723AFF3CF4F1FAE659C35025D".decode("hex")
    assets_ctr = "6F1F9686500DF2D8E5B056552E1645A0".decode("hex")
    assets_off = 0x5DF960
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "0CEFA3047B692C0FDCF206FB7A25A5E0".decode("hex")
    fw_ctr = "D27B776C2DEDBD374465E4CEB9930F74".decode("hex")
    fw_off = 0
    fw_size = 0xF6580
elif version == 270:
    arm64_key = "B744819653918B2432458290A531C005".decode("hex")
    arm64_ctr = "63203138AD414B7E801F315E6CC756D7".decode("hex")
    arm64_off = 0x5783F0
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "C4C56E64E38EB91A0DC210CAC3E3FE4E".decode("hex")
    fb_ctr = "0F0C57167FE85D122276D257F8B397D3".decode("hex")
    fb_off = 0x1B83F0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "D0B7D2E334CFC034AB9519DAE43B995F".decode("hex")
    payload80_ctr = "01E6561E5106247CBE0E410FB7EA01B7".decode("hex")
    payload80_off = 0x127E0
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "C1CDE0D8F6F83AB40C187E5B14BFC8B9".decode("hex")
    payload90_ctr = "12C2430E52092D2C4063EA1B2E9CAC99".decode("hex")
    payload90_off = 0xC70450
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "31E434B81E0CFD008BB9B003473A256A".decode("hex")
    payload98_ctr = "92BE750E67CAD0A4123F0441A2AA0364".decode("hex")
    payload98_off = 0xD65F70
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "4325283B2FE90A02B2FCF3962BBD4FB1".decode("hex")
    payloadA0_ctr = "97091C1C7ED23DC6F7A4DB3F61DD38D5".decode("hex")
    payloadA0_off = 0xE22200
    payloadA0_size = 0xF70B0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "98627ABD58519C89C039CA3C125C4B71".decode("hex")
    bootloader_ctr = "637560A6B09EA02357CF541F17C61D47".decode("hex")
    bootloader_off = 0x5AE960
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "4C476B3459CDB962178F70D3F57F0CD2".decode("hex")
    assets_ctr = "5875B8C96E0A264FC7DEEB41929C173D".decode("hex")
    assets_off = 0x5DF960
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "05877D34CBCED60AAF26168840A2D718".decode("hex")
    fw_ctr = "E312C836EE8434E5F5B47FD0C7F05B37".decode("hex")
    fw_off = 0
    fw_size = 0xF70B0
elif version == 271:
    arm64_key = "AA9CF1D37A2F703DDD8F07B1005E79F4".decode("hex")
    arm64_ctr = "806117036F05DD130BC7FBCA493DB157".decode("hex")
    arm64_off = 0x5783F0
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "48B27109D22741B4DBC250BA82964F51".decode("hex")
    fb_ctr = "0FD6F9CE43C4390C5CC462FC7D1BE07D".decode("hex")
    fb_off = 0x1B83F0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "89FE60AC754F4DB10F60DDA364B3B228".decode("hex")
    payload80_ctr = "F7E6CC94713029B248C03DCECF89A776".decode("hex")
    payload80_off = 0x127E0
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "529CEE940293709D7B3D2176ABFC82A5".decode("hex")
    payload90_ctr = "AFB726F5BDEFA2E9D6933431AFF9DBBC".decode("hex")
    payload90_off = 0xC70450
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "A38E6497D3888ADF031CF4BCDF6BE476".decode("hex")
    payload98_ctr = "E339CA2430261B1BE6CC41147942FABF".decode("hex")
    payload98_off = 0xD65F70
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "9A5520D7E453899FB5B768B28CF4CDA4".decode("hex")
    payloadA0_ctr = "FAC57B6B4A7551B16B7A6BDD5FFA16AC".decode("hex")
    payloadA0_off = 0xE22200
    payloadA0_size = 0xF7160
    payloadA0_base = 0xA0000000
    
    bootloader_key = "8A1E3C0B9CDF38BD63AC8990BF599E7A".decode("hex")
    bootloader_ctr = "6FE79DFFCAB11BE868DB3F322C6A377A".decode("hex")
    bootloader_off = 0x5AE960
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "C5375A4DE2BC9AC2E2E694E994FAA829".decode("hex")
    assets_ctr = "6893E6E5120108767502A0B3A74C0BEA".decode("hex")
    assets_off = 0x5DF960
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "9C7053DAEE0EBC01732C80849CABA068".decode("hex")
    fw_ctr = "1CE90390C8AA4AAA3A722374A8180E5E".decode("hex")
    fw_off = 0
    fw_size = 0xF7160
elif version == 280:
    arm64_key = "3861203386C585A8E9AD935F20D0C599".decode("hex")
    arm64_ctr = "2D403828E7D9F828173BAFF8FFBD7052".decode("hex")
    arm64_off = 0x5783E0
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "1FB0B69E81A71F13C3489449547D40B2".decode("hex")
    fb_ctr = "F08545349F182BE461FDDCE669FB5E63".decode("hex")
    fb_off = 0x1B83E0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "EA826144114C1F9B242A8E724331876C".decode("hex")
    payload80_ctr = "488354CED6496988542B5F56E5612BD0".decode("hex")
    payload80_off = 0x127E0
    payload80_size = 0x1A5C00
    payload80_base = 0x80000000
    
    payload90_key = "0A8DD622D3C535E35FA04B632D9453A4".decode("hex")
    payload90_ctr = "150BD50B1EE667E89330C51B7500C41E".decode("hex")
    payload90_off = 0xC70440
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "995D5845FD8BD172D27810DB575D0E44".decode("hex")
    payload98_ctr = "C7E60C4FBFA40FA91775B4DF9434902B".decode("hex")
    payload98_off = 0xD65F60
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "AC22255E11FC4F610ACC29DFE65BBC2B".decode("hex")
    payloadA0_ctr = "B4F2D5A638BA568FB5F3BA98BFC4654B".decode("hex")
    payloadA0_off = 0xE221F0
    payloadA0_size = 0xF7280
    payloadA0_base = 0xA0000000
    
    bootloader_key = "D0B50F4A7588BA92A8247F1A99324A12".decode("hex")
    bootloader_ctr = "3BC4F9DFE181D8D48F3658A1396A3F2F".decode("hex")
    bootloader_off = 0x5AE950
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "5A403E8D8CEF853F59CF8CF09EB8EB02".decode("hex")
    assets_ctr = "55967DA1816FB4099408A109705CFBFC".decode("hex")
    assets_off = 0x5DF950
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "E5D3A89D04155B564235E2C99E2BF77A".decode("hex")
    fw_ctr = "42D3DBF4C812EF6BA50C7C445C58D678".decode("hex")
    fw_off = 0
    fw_size = 0xF7280
elif version == 290:
    arm64_key = "78E90599CE05DF3D782211839B86094A".decode("hex")
    arm64_ctr = "66A8D5DE77F0B4B75DA69D5D2D7CC8B5".decode("hex")
    arm64_off = 0x578440
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "3AA3D22A165B08EEBE48669F875F8ACC".decode("hex")
    fb_ctr = "25998A24513D03CDEDB519627CA171B5".decode("hex")
    fb_off = 0x1B8440
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "CC30896E3196BD0419A429120A009AD9".decode("hex")
    payload80_ctr = "B252C28EF51CF0F2805F8C9F48ADAC58".decode("hex")
    payload80_off = 0x12840
    payload80_size = 0x1A5C00
    payload80_base = 0x80000000
    
    payload90_key = "41A291F3BD9AA942ECE1D6E1B27E486F".decode("hex")
    payload90_ctr = "9A7B1F30F7EE04C70FE6BB23B7D438E5".decode("hex")
    payload90_off = 0xC704A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "8E08320951FCA723258EF13BAD82FCB0".decode("hex")
    payload98_ctr = "40472A4C8886B641725FD9F193044ABD".decode("hex")
    payload98_off = 0xD65FC0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "E44ACD0A71F86D49359E102964123419".decode("hex")
    payloadA0_ctr = "0AA06CF0044086052D6CADED6823E4DB".decode("hex")
    payloadA0_off = 0xE22250
    payloadA0_size = 0x13DFB0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "14F8D4A31FD3CFD95432B1ACC7C9D668".decode("hex")
    bootloader_ctr = "259B741886925B283B73A6198B9FBA7F".decode("hex")
    bootloader_off = 0x5AE9B0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "9700DFE632D161B7B09AD9AE53BED3CC".decode("hex")
    assets_ctr = "DFE2AC853D27B1F7CBFCEAA83BB12D1C".decode("hex")
    assets_off = 0x5DF9B0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "611BE8DC8A2BDBE2232760938E94250F".decode("hex")
    fw_ctr = "560CF5302AB7C8248712F9C8BF0EFC3F".decode("hex")
    fw_off = 0
    fw_size = 0x13DFB0
elif version == 291:
    arm64_key = "2D875D860AD8227E48D67964EFD14534".decode("hex")
    arm64_ctr = "EDDD84CB53D79F8E8D613659FD0621B9".decode("hex")
    arm64_off = 0x578440
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "C26802E169AF4C6993E263F6FB83DCB5".decode("hex")
    fb_ctr = "BD45FE5EF70DB92199A83EA7F80E53EA".decode("hex")
    fb_off = 0x1B8440
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "D42C2429964CE5C240D6F0B83A7D8768".decode("hex")
    payload80_ctr = "56443F6B6E34C4A9C378A0A49A798BC5".decode("hex")
    payload80_off = 0x12840
    payload80_size = 0x1A5C00
    payload80_base = 0x80000000
    
    payload90_key = "4E3FC25C3EB4489F9B53CEAD312FF845".decode("hex")
    payload90_ctr = "4763745737B20BF9CF17D50A36DD68D6".decode("hex")
    payload90_off = 0xC704A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "BDAC8478DE65EB257CC6C07C20A167FA".decode("hex")
    payload98_ctr = "BAC94D13D30D01366BEE9D2D67747804".decode("hex")
    payload98_off = 0xD65FC0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "7EE10E8DA2518B9F6DE9E86278089AE2".decode("hex")
    payloadA0_ctr = "E40EA57D863BA78027883A457B518426".decode("hex")
    payloadA0_off = 0xE22250
    payloadA0_size = 0x13E490
    payloadA0_base = 0xA0000000
    
    bootloader_key = "277DAE3928708113BACD90D158D52E5E".decode("hex")
    bootloader_ctr = "4DB319653838F8F1621657A4DF04BD3C".decode("hex")
    bootloader_off = 0x5AE9B0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "5C7FF7E1C0D209D51A0ED30493A5588B".decode("hex")
    assets_ctr = "7DFAE44F6E0F353D72FE944D8FF077AB".decode("hex")
    assets_off = 0x5DF9B0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "78CEA2D8ECEB0A0FEA2D4FCFBC289354".decode("hex")
    fw_ctr = "46110F0129EA7F4360E58EC091CD5143".decode("hex")
    fw_off = 0
    fw_size = 0x13E490
elif version == 292:
    arm64_key = "AF770458F73BFEDF7313397AA28B90DB".decode("hex")
    arm64_ctr = "5784BCEAB41FEF756D10929A7C3994BE".decode("hex")
    arm64_off = 0x578440
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "74464783EB8DBB37D848CC366D310463".decode("hex")
    fb_ctr = "B7427C2ABA046FDF4CFEC1895B814FF9".decode("hex")
    fb_off = 0x1B8440
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "62047367D930D44A4A706CEF97AD786A".decode("hex")
    payload80_ctr = "DE72BD820E361C5B445207C25D8A4BFA".decode("hex")
    payload80_off = 0x12840
    payload80_size = 0x1A5C00
    payload80_base = 0x80000000
    
    payload90_key = "982F6A38864BF97E3579B735E70440D2".decode("hex")
    payload90_ctr = "DB8929D706DD5CE6E28D36752B3B64A9".decode("hex")
    payload90_off = 0xC704A0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "8D5CED1D42F031424594923699526C2D".decode("hex")
    payload98_ctr = "39303EB5D2DC12E871EBC28193BEBD65".decode("hex")
    payload98_off = 0xD65FC0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "029FB62968116F09A8721820D25D1B30".decode("hex")
    payloadA0_ctr = "A9AA3A9EBDCB3FAD38B2A8EF6611B597".decode("hex")
    payloadA0_off = 0xE22250
    payloadA0_size = 0x123D30
    payloadA0_base = 0xA0000000
    
    bootloader_key = "508BA415B5B275901E4BD1B37DD00323".decode("hex")
    bootloader_ctr = "62A002045A839F2538A4CF20A8143189".decode("hex")
    bootloader_off = 0x5AE9B0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "11B7A88ABE4A2D3BF4F0D90D5351A6D3".decode("hex")
    assets_ctr = "0F88BFA85DD56ED50680DF75A80D9F8D".decode("hex")
    assets_off = 0x5DF9B0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "90FE8D082A29A62BA263CB7CB87615ED".decode("hex")
    fw_ctr = "6F77FD84161D117B182B37BEB4C39FF2".decode("hex")
    fw_off = 0
    fw_size = 0x123D30
elif version == 293:
    arm64_key = "973A084B40D019278FCB8230B8EE2222".decode("hex")
    arm64_ctr = "A079288B750080C9E88CA0F6E5517459".decode("hex")
    arm64_off = 0x578450
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "6959AF4EDCE863CBB59707C856DBA9B3".decode("hex")
    fb_ctr = "B50459C2DCD0764D636D95CCA6021077".decode("hex")
    fb_off = 0x1B8450
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "CE25F150ED9FCB0072366DC3EE0C13B8".decode("hex")
    payload80_ctr = "50C7F53D2301515F581928BABA274677".decode("hex")
    payload80_off = 0x12840
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "33A72B2F50CED6FB91C8B8C2EA196E01".decode("hex")
    payload90_ctr = "784FCE5DB2E3168B11318C3C3F2FDC7B".decode("hex")
    payload90_off = 0xC704B0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "857293803549F85D88637302300160AC".decode("hex")
    payload98_ctr = "320EA5E8704F7DA55AFFE97C59D65436".decode("hex")
    payload98_off = 0xD65FD0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "1D7A1A4001C420668642C30FEF46EE87".decode("hex")
    payloadA0_ctr = "CC6B3B267FE64097E2F945F3AF2B06D3".decode("hex")
    payloadA0_off = 0xE22260
    payloadA0_size = 0x1252C0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "23CD127D91B56932E42C8F363D654FB4".decode("hex")
    bootloader_ctr = "36C53BB329453055044D8D81DFC26C2F".decode("hex")
    bootloader_off = 0x5AE9C0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "858176AA281CFBDAAE4225EC6AD5F3BD".decode("hex")
    assets_ctr = "D9D273ABE168900DD1938D3D3329F626".decode("hex")
    assets_off = 0x5DF9C0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "8B993F3EEF42804B749AB4EE8CA5F725".decode("hex")
    fw_ctr = "CCB7AD2CAF44B518C4F7B7B53445DE8A".decode("hex")
    fw_off = 0
    fw_size = 0x1252C0
elif version == 294:
    arm64_key = "50123829997FEF8CA851D9A330C62A3D".decode("hex")
    arm64_ctr = "C3A099CC0449E176352714A8C1FF1672".decode("hex")
    arm64_off = 0x578610
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "7D357EE24BB11DCC81400950410FE42E".decode("hex")
    fb_ctr = "7A5F3CC51B4ABB46C863D9A19B9D2B12".decode("hex")
    fb_off = 0x1B8610
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "242364B25159E5EEC88D0CE91AE1EC54".decode("hex")
    payload80_ctr = "02FE41B6762E0BB350C366175DE19952".decode("hex")
    payload80_off = 0x12A00
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "40BF6CF8BA659F3600A5EB3E857E43A0".decode("hex")
    payload90_ctr = "69BE5466D77DE83D23D0B45B783B5F8F".decode("hex")
    payload90_off = 0xC70670
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "529511C09C135F7AB962AD13DB40AEDC".decode("hex")
    payload98_ctr = "AB61BB156757BB39EE3F42632C5CB520".decode("hex")
    payload98_off = 0xD66190
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "F05562DDC8EEC77C1821386C607BB7CC".decode("hex")
    payloadA0_ctr = "485FE6E12B5374A5EBDF641D85D72A66".decode("hex")
    payloadA0_off = 0xE22420
    payloadA0_size = 0x125320
    payloadA0_base = 0xA0000000
    
    bootloader_key = "E61DBE1F4C79C10D211EF7AA46FAC277".decode("hex")
    bootloader_ctr = "B7CED1144DD8E54BDD6EE6194142277C".decode("hex")
    bootloader_off = 0x5AEB80
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "65A510BD9363DD2510563661305EEEE3".decode("hex")
    assets_ctr = "B69F929BE7F638D46D0FBE34D2CF28E9".decode("hex")
    assets_off = 0x5DFB80
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "849526813F8B3156D3882121320B6AF1".decode("hex")
    fw_ctr = "8B89CFD8B3D65C6B9672BDC0DD621827".decode("hex")
    fw_off = 0
    fw_size = 0x125320
elif version == 295:
    arm64_key = "129181A1C460F54E2AD09A79018746B1".decode("hex")
    arm64_ctr = "FD87356FBB7D55C5D0A497F7848AF5D4".decode("hex")
    arm64_off = 0x578450
    arm64_size = 0x36570
    arm64_base = 0x80FFFE00
     
    fb_key = "100103AE43390C767D02B2832D317A96".decode("hex")
    fb_ctr = "4375C41CAEDF56D075ACC60AD1D80108".decode("hex")
    fb_off = 0x1B8450
    fb_size = 0x3C0000
    fb_base = 0xF0000000
     
    payload80_key = "8D65A659D22976FFB3AD8DF04DF6231F".decode("hex")
    payload80_ctr = "4DC3342EAF3BA1FBB287EB378014EC90".decode("hex")
    payload80_off = 0x12840
    payload80_size = 0x1A5C10
    payload80_base = 0x80000000
    
    payload90_key = "E2EE2B6B042E1E10A84E70D14CB3B8FE".decode("hex")
    payload90_ctr = "0BE014E13941760D5319713B62B6BDF9".decode("hex")
    payload90_off = 0xC704B0
    payload90_size = 0xF5B20
    payload90_base = 0x90000000
    
    payload98_key = "201F5299D1F1E557D3E104CF63130711".decode("hex")
    payload98_ctr = "D2BA7C240F26C1C6CF50138FD943EFD0".decode("hex")
    payload98_off = 0xD65FD0
    payload98_size = 0xBC290
    payload98_base = 0x98000000
    
    payloadA0_key = "51E48E8AEC88251092D84B66908A672C".decode("hex")
    payloadA0_ctr = "BDDFD08BCEE497E733FB6526838184E9".decode("hex")
    payloadA0_off = 0xE22260
    payloadA0_size = 0x124D30
    payloadA0_base = 0xA0000000
    
    bootloader_key = "2C027DC11634CD89D735E8359A9A1344".decode("hex")
    bootloader_ctr = "70DF35B2721BB12566018242454D540A".decode("hex")
    bootloader_off = 0x5AE9C0
    bootloader_size = 0x31000
    bootloader_base = 0x88000000
    
    assets_key = "D3ECCF951931AE43C87503DCBE7CC40F".decode("hex")
    assets_ctr = "F89D9748195096BB721CE9C3EA3129CF".decode("hex")
    assets_off = 0x5DF9C0
    assets_size = 0x4D8400
    assets_base = 0x88031000
    
    fw_key = "CA25F72C2BA94823AC88557248A833E8".decode("hex")
    fw_ctr = "52166D383F2D34F043477FF5E9318958".decode("hex")
    fw_off = 0
    fw_size = 0x124D30
elif version == 300:
    fb_key = "9412DFFD80DE93E2C95A180EB1D43361".decode("hex")
    fb_ctr = "B32FA6691A490719ADB9789C27132DCE".decode("hex")
    fb_off = 0x1F81E0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "D46024238BB1E5E601205295E7EA9D01".decode("hex")
    payload81_ctr = "F12F0ED9E6293660E331E0C8520BF220".decode("hex")
    payload81_off = 0x215E0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "122BD985ED85A5620B978F36FC7FAAB1".decode("hex")
    payload90_ctr = "F25F18355A21014F401F1529707F9731".decode("hex")
    payload90_off = 0xC95CD0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "26219A44838331CD27D3CD6265F04075".decode("hex")
    payload98_ctr = "2AA42DFDCF0C72D5E00F302BEA916B2D".decode("hex")
    payload98_off = 0xDBA810
    payload98_size = 0x17B410
    payload98_base = 0x98000000
    
    payloadA0_key = "0F8088E33E62BAF5D87A7C058177F252".decode("hex")
    payloadA0_ctr = "684202C5677D4A5066786487FFA9662A".decode("hex")
    payloadA0_off = 0xF35C20
    payloadA0_size = 0x27D530
    payloadA0_base = 0xA0000000
    
    bootloader_key = "40597B717536438A0DF8C2000AAE7C72".decode("hex")
    bootloader_ctr = "2680291171280EE7D785514DD3EAE7E1".decode("hex")
    bootloader_off = 0x5B81E0
    bootloader_size = 0x49000
    bootloader_base = 0x88000000
    
    assets_key = "98816BA5008B29C42DE878E590964B98".decode("hex")
    assets_ctr = "1BF18D57BD82808B557F455F0D6B7FA0".decode("hex")
    assets_off = 0x6011E0
    assets_size = 0x4DC400
    assets_base = 0x88049000
    
    fw_key = "5C40CBFCD94BCFD1A579BCC7D06A2811".decode("hex")
    fw_ctr = "006DEFDA019CB1905EC4388160894B9D".decode("hex")
    fw_off = 0
    fw_size = 0x27D530
elif version == 301:
    fb_key = "62DED15EC60FBE757866A964F12A0E85".decode("hex")
    fb_ctr = "86FFAAF67EA3D94CCF3990BB8E6DDEBA".decode("hex")
    fb_off = 0x1F69E0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "CBDD911C67680975D3A7786DF7D0CB4C".decode("hex")
    payload81_ctr = "690BC0BFA8113EBCBC60588269D4CCB7".decode("hex")
    payload81_off = 0x1FDE0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "FFCF22B11A8D1E6FC7D9C415D0CAE1CE".decode("hex")
    payload90_ctr = "C80779C06B574A729B5EA00C7B5A9594".decode("hex")
    payload90_off = 0xC944D0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "902228E8DF3CE4E4479BB06051141944".decode("hex")
    payload98_ctr = "0BB53BA3D0AE8D578F3F31302C6103F6".decode("hex")
    payload98_off = 0xDB9010
    payload98_size = 0x183410
    payload98_base = 0x98000000
    
    payloadA0_key = "14B5A96E7CCE762381D340A8FD6CE3B6".decode("hex")
    payloadA0_ctr = "D718B9152267A8EFD95223FDF1671796".decode("hex")
    payloadA0_off = 0xF3C420
    payloadA0_size = 0x27DD00
    payloadA0_base = 0xA0000000
    
    bootloader_key = "FA72233A5B08181890797165D2CE6939".decode("hex")
    bootloader_ctr = "B4E88BE9751F62A8FE2690BF2169E264".decode("hex")
    bootloader_off = 0x5B69E0
    bootloader_size = 0x49000
    bootloader_base = 0x88000000
    
    assets_key = "ACFCBFB5AC9327FE0394EC7C58F6BB36".decode("hex")
    assets_ctr = "BE550C778EF67A66A2BE525C7C4912BF".decode("hex")
    assets_off = 0x5FF9E0
    assets_size = 0x4DC400
    assets_base = 0x88049000
    
    fw_key = "025E60D726747BB3E9850EA594276354".decode("hex")
    fw_ctr = "ACA76B5BB26B5D3020A46E6A9A0E3D8D".decode("hex")
    fw_off = 0
    fw_size = 0x27DD00
elif version == 302:
    fb_key = "3BF98F9EC315930E52947E4097AD312B".decode("hex")
    fb_ctr = "A1479326BC31BAA666B612E50FB3737C".decode("hex")
    fb_off = 0x1F69E0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "1E2616C2A27D8A8791C903188EAF52DC".decode("hex")
    payload81_ctr = "9B6C19A132975E1129A67B231D2B7920".decode("hex")
    payload81_off = 0x1FDE0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "12A5E97CEBBFFD9ABBB110570301D4FA".decode("hex")
    payload90_ctr = "C30B92FE39CBDA426DC708B05EEF87F1".decode("hex")
    payload90_off = 0xC944D0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "54D3465D50AD90E55A24D0B2B27E77CB".decode("hex")
    payload98_ctr = "03B66171CFF9C53717272F3699EEC6D4".decode("hex")
    payload98_off = 0xDB9010
    payload98_size = 0x183410
    payload98_base = 0x98000000
    
    payloadA0_key = "E9B5FF19C9AE8C12E7FA656C532ECF7E".decode("hex")
    payloadA0_ctr = "291A81ED99CD6F33F54C5A5A8A58F8DC".decode("hex")
    payloadA0_off = 0xF3C420
    payloadA0_size = 0x27DD40
    payloadA0_base = 0xA0000000
    
    bootloader_key = "D327E54206CA2865569647EE3381E598".decode("hex")
    bootloader_ctr = "E1F4764FB90AA279E0671C7182AC7E8E".decode("hex")
    bootloader_off = 0x5B69E0
    bootloader_size = 0x49000
    bootloader_base = 0x88000000
    
    assets_key = "E3F40E1A3B3A697A143ABF4BD05BA0B4".decode("hex")
    assets_ctr = "513915AE2D56670F2707AF219D9BB5ED".decode("hex")
    assets_off = 0x5FF9E0
    assets_size = 0x4DC400
    assets_base = 0x88049000
    
    fw_key = "0F43ECCFCF7B0D61B21719DEB91C420D".decode("hex")
    fw_ctr = "D89E55311984F6999503BA48C9898A65".decode("hex")
    fw_off = 0
    fw_size = 0x27DD40
elif version == 303:
    fb_key = "5E683603CE7F775946EE189AD422F04F".decode("hex")
    fb_ctr = "230C25940DCA7640B0F3B9DB68C1EC51".decode("hex")
    fb_off = 0x1F69E0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "A1739894D75C2570ED3241E41F10F327".decode("hex")
    payload81_ctr = "BC6C793A05E0988181061AB6FB066EB2".decode("hex")
    payload81_off = 0x1FDE0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "5DE41DF5A42AA6753A43DEA3BCAB2C17".decode("hex")
    payload90_ctr = "0FD6A28784962A43DF53B8A8CB149C6F".decode("hex")
    payload90_off = 0xC954D0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "C95946D44A2F61F3F9A669EF32FB841E".decode("hex")
    payload98_ctr = "DAF594C65FC5276530270722B8E34178".decode("hex")
    payload98_off = 0xDBA010
    payload98_size = 0x183410
    payload98_base = 0x98000000
    
    payloadA0_key = "533505DA5634323D0C8EDB806291B509".decode("hex")
    payloadA0_ctr = "67E2CBBC78C6361E420D4496804F5070".decode("hex")
    payloadA0_off = 0xF3D420
    payloadA0_size = 0x27DDB0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "C6BB2F35588A6AD2D27F4388FEC851A1".decode("hex")
    bootloader_ctr = "F990A7DE3BE5CA749C3C266F388E787C".decode("hex")
    bootloader_off = 0x5B69E0
    bootloader_size = 0x4A000
    bootloader_base = 0x88000000
    
    assets_key = "2BF117758BDB2560A97F011282B9717F".decode("hex")
    assets_ctr = "2E6E6B75B7A2C44FD91EC78C1FC9A2C7".decode("hex")
    assets_off = 0x6009E0
    assets_size = 0x4DC400
    assets_base = 0x8804A000
    
    fw_key = "7A3B453156C2110F3DB709F84C171102".decode("hex")
    fw_ctr = "D6CD088F0B4C45B1F1F31666B54C47EA".decode("hex")
    fw_off = 0
    fw_size = 0x27DDB0
elif version == 304:
    fb_key = "F1269E08C443FD63498B030A142E665D".decode("hex")
    fb_ctr = "83A63A2DD880DDCD9A7D4E728F8DEB74".decode("hex")
    fb_off = 0x1F69E0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "3E1A6918BDA3F35488BCB5F9A186D658".decode("hex")
    payload81_ctr = "926C8716D2729A84B46BC69FAC771AEE".decode("hex")
    payload81_off = 0x1FDE0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "1EF0E3BEE2AF107AE68959980B7FC34C".decode("hex")
    payload90_ctr = "9FEB3517EE2F3DE704C7B673B92F0EA2".decode("hex")
    payload90_off = 0xC954D0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "91F907C1999BB373C76E417EBC3476D5".decode("hex")
    payload98_ctr = "9CD9FEF4DF3349A1379EB3273C586A2F".decode("hex")
    payload98_off = 0xDBA010
    payload98_size = 0x183410
    payload98_base = 0x98000000
    
    payloadA0_key = "59C2C117D6985D5B44CF905096F96EBA".decode("hex")
    payloadA0_ctr = "2361D93EDA70248541FF6F9DFFDCFBBC".decode("hex")
    payloadA0_off = 0xF3D420
    payloadA0_size = 0x27DDB0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "E083C2043F0C685E35D57BF918D070F7".decode("hex")
    bootloader_ctr = "0E94061E7FEB9383AB259D0B18EE42CD".decode("hex")
    bootloader_off = 0x5B69E0
    bootloader_size = 0x4A000
    bootloader_base = 0x88000000
    
    assets_key = "F9A52DB6ECC2659910859DDA2ACEB88B".decode("hex")
    assets_ctr = "B8CF72205CDB385BF098C561A8E5E878".decode("hex")
    assets_off = 0x6009E0
    assets_size = 0x4DC400
    assets_base = 0x8804A000
    
    fw_key = "F57A6D0DE29F3755D90CAAED3E414A86".decode("hex")
    fw_ctr = "C65B04F61CECB3A0D74A2D414C766441".decode("hex")
    fw_off = 0
    fw_size = 0x27DDB0
elif version == 305:
    fb_key = "414A2F120393080D1BECB2EF1D890C88".decode("hex")
    fb_ctr = "A8102DF5643EFE39F1B16E7B144C63CE".decode("hex")
    fb_off = 0x1F6DE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "A112FF3E4322AEA3F3B43E7A75AEBE44".decode("hex")
    payload81_ctr = "CD1618A9972116DF0B1885715FCCB961".decode("hex")
    payload81_off = 0x201E0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "91DC1B72FBAE5DC0A2A95F58A9139019".decode("hex")
    payload90_ctr = "43383B3C165DE016087959C62B3CDB2F".decode("hex")
    payload90_off = 0xC958D0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "56716367669F63E11144E1523B670B5A".decode("hex")
    payload98_ctr = "837750BB23487DD3C62542B74280970B".decode("hex")
    payload98_off = 0xDBA410
    payload98_size = 0x183410
    payload98_base = 0x98000000
    
    payloadA0_key = "15664B1FF796FE869B985E87748228D2".decode("hex")
    payloadA0_ctr = "11B6AB394B10CE191568FEDE93FD82FA".decode("hex")
    payloadA0_off = 0xF3D820
    payloadA0_size = 0x27E2D0
    payloadA0_base = 0xA0000000
    
    bootloader_key = "124D57EA621B56B86746E41B74C3A0A3".decode("hex")
    bootloader_ctr = "C405A2CD9466C2571B2347D6DDDDD71A".decode("hex")
    bootloader_off = 0x5B6DE0
    bootloader_size = 0x4A000
    bootloader_base = 0x88000000
    
    assets_key = "E311FD951CEC5A95C19955B555BBBF36".decode("hex")
    assets_ctr = "95190D025A80C227B1E8AD9E8CE3E528".decode("hex")
    assets_off = 0x600DE0
    assets_size = 0x4DC400
    assets_base = 0x8804A000
    
    fw_key = "9FB3C11A775D9EDE46CDB748B3C7FBB8".decode("hex")
    fw_ctr = "34B0270240CC7AF8350A2DB1A99CF58F".decode("hex")
    fw_off = 0
    fw_size = 0x27E2D0
elif version == 310:
    fb_key = "4599F62BF51E62B6AC05AAA7E7B03DE3".decode("hex")
    fb_ctr = "39B0F6E0846C53DCE0457F285797AE99".decode("hex")
    fb_off = 0x1F6DE0
    fb_size = 0x3C0000
    fb_base = 0xF0000000
    
    payload81_key = "12280A64B7A487E99864CD2E22393C87".decode("hex")
    payload81_ctr = "C28124EAA147BEE8EF865E2AE8496834".decode("hex")
    payload81_off = 0x201E0
    payload81_size = 0x1D6C00
    payload81_base = 0x81000000
    
    payload90_key = "95F4D1F3C1EC6E5A54AC70F49AE315F5".decode("hex")
    payload90_ctr = "DCD96167060A7A9E1F2BC8C1C2A611B4".decode("hex")
    payload90_off = 0xC958D0
    payload90_size = 0x124B40
    payload90_base = 0x90000000
    
    payload98_key = "DEE47F27900D540AFE04C4063638CE0F".decode("hex")
    payload98_ctr = "467E7F219FDCAFA5E6187262755D4DFC".decode("hex")
    payload98_off = 0xDBA410
    payload98_size = 0x183410
    payload98_base = 0x98000000
    
    payloadA0_key = "043AB07482B9A8B55EA9041C74CD92EB".decode("hex")
    payloadA0_ctr = "AAF5295AEC233F953B408EE27F892CF8".decode("hex")
    payloadA0_off = 0xF3D820
    payloadA0_size = 0x2AE220
    payloadA0_base = 0xA0000000
    
    bootloader_key = "FB61357AB9DEE1C9D4C49F6488349EF0".decode("hex")
    bootloader_ctr = "5BCF60493E61BCB930FD44C7FAC0EE09".decode("hex")
    bootloader_off = 0x5B6DE0
    bootloader_size = 0x4A000
    bootloader_base = 0x88000000
    
    assets_key = "EF48639FC925C8D0364B2DA7614EB038".decode("hex")
    assets_ctr = "7298408E70FBE048DCC6E594B0C272B6".decode("hex")
    assets_off = 0x600DE0
    assets_size = 0x4DC400
    assets_base = 0x8804A000
    
    fw_key = "81F555CC58EF03CB41BD81C90A8E8F79".decode("hex")
    fw_ctr = "A4C122884E6C8979E3E3E0F07D116E52".decode("hex")
    fw_off = 0
    fw_size = 0x2AE220
else:
    exit()

# Create main folder
if not os.path.exists("./sxos/"):
    os.mkdir("./sxos/")
os.chdir("./sxos/")

# Create folder for the initial boot files
if not os.path.exists("./init/"):
    os.mkdir("./init/")
os.chdir("./init/")

# Decrypt Stage2 IRAM payload
f = open("stage2_{0:08X}.bin".format(s2_base), "wb")
f.write(aes_ctr_dec(b[0x100:0x100+s2_size], s2_key, s2_ctr))
f.close()

# New Stage3 DRAM payload
if version >= 300:
    boot_dat_hdr2_off = struct.unpack("I", b[0x5C:0x60])[0]
    boot_dat_hdr2_size = 0x200
    s3_key = "D548D48DBA299604CED1AE5B47D8429C".decode("hex")
    s3_ctr = b[boot_dat_hdr2_off+0x10:boot_dat_hdr2_off+0x20]
    s3_off = (boot_dat_hdr2_off + boot_dat_hdr2_size)
    s3_size, s3_base = struct.unpack("II", b[boot_dat_hdr2_off:boot_dat_hdr2_off+0x08])

    # Decrypt Stage3 DRAM payload
    f = open("stage3_{0:08X}.bin".format(s3_base), "wb")
    f.write(aes_ctr_dec(b[s3_off:s3_off+s3_size], s3_key, s3_ctr))
    f.close()

# Old ARM64 memory training blob
if version < 300:
    # Decrypt ARM64 memory training blob
    f = open("arm64_{0:08X}.bin".format(arm64_base), "wb")
    f.write(aes_ctr_dec(b[arm64_off:arm64_off+arm64_size], arm64_key, arm64_ctr))
    f.close()

# Decrypt initial framebuffer binary
f = open("fb_{0:08X}.bin".format(fb_base), "wb")
f.write(aes_ctr_dec(b[fb_off:fb_off+fb_size], fb_key, fb_ctr))
f.close()

# Create folder for the obfuscation payloads
if not os.path.exists("../payloads/"):
    os.mkdir("../payloads/")
os.chdir("../payloads/")

if version >= 300:
    # Decrypt first layer's obfuscation payload
    f = open("payload_{0:08X}.bin".format(payload81_base), "wb")
    f.write(aes_ctr_dec(b[payload81_off:payload81_off+payload81_size], payload81_key, payload81_ctr))
    f.close()
else: 
    # Decrypt first layer's obfuscation payload
    f = open("payload_{0:08X}.bin".format(payload80_base), "wb")
    f.write(aes_ctr_dec(b[payload80_off:payload80_off+payload80_size], payload80_key, payload80_ctr))
    f.close()

# Decrypt second layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payload90_base), "wb")
f.write(aes_ctr_dec(b[payload90_off:payload90_off+payload90_size], payload90_key, payload90_ctr))
f.close()

# Decrypt third layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payload98_base), "wb")
f.write(aes_ctr_dec(b[payload98_off:payload98_off+payload98_size], payload98_key, payload98_ctr))
f.close()

# Decrypt fourth layer's obfuscation payload
f = open("payload_{0:08X}.bin".format(payloadA0_base), "wb")
f.write(aes_ctr_dec(b[payloadA0_off:payloadA0_off+payloadA0_size], payloadA0_key, payloadA0_ctr))
f.close()

# Create folder for the bootloader
if not os.path.exists("../bootloader/"):
    os.mkdir("../bootloader/")
os.chdir("../bootloader/")

# Decrypt SX OS bootloader's code and assets
f = open("bootloader_{0:08X}.bin".format(bootloader_base), "wb")
f.write(aes_ctr_dec(b[bootloader_off:bootloader_off+bootloader_size], bootloader_key, bootloader_ctr))
f.write(aes_ctr_dec(b[assets_off:assets_off+assets_size], assets_key, assets_ctr))
f.close()

os.chdir("../payloads/")

# Open final firmware binary (encrypted)
f = open("payload_A0000000.bin", "rb")
d = f.read()
f.close()

# Decrypt final firmware binary
f = open("payload_A0000000_dec.bin", "wb")
f.write(aes_ctr_dec(d[fw_off:fw_off+fw_size], fw_key, fw_ctr))
f.close()

# Open final firmware binary (decrypted)
f = open("payload_A0000000_dec.bin", "rb")
d = f.read()
f.close()

# Create folder for the patcher binaries
if not os.path.exists("../patcher/"):
    os.mkdir("../patcher/")
os.chdir("../patcher/")

if version < 120:                                           # Old layout
    patcher_size = struct.unpack("I", d[0x10:0x14])[0]
    patcher_off = struct.unpack("I", d[0x14:0x18])[0]
    patcher_base = struct.unpack("I", d[0x18:0x1C])[0]
    patcher_crc = struct.unpack("I", d[0x1C:0x20])[0]
    patcher_hash = struct.unpack("8I", d[0x50:0x70])
        
    # Parse and store the PK11 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x20:0x24])[0]
    patcher_off = struct.unpack("I", d[0x24:0x28])[0]
    patcher_base = struct.unpack("I", d[0x28:0x2C])[0]
    patcher_crc = struct.unpack("I", d[0x2C:0x30])[0]
    patcher_hash = struct.unpack("8I", d[0x70:0x90])

    # Parse and store the KIP1/INI1 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x30:0x34])[0]
    patcher_off = struct.unpack("I", d[0x34:0x38])[0]
    patcher_base = struct.unpack("I", d[0x38:0x3C])[0]
    patcher_crc = struct.unpack("I", d[0x3C:0x40])[0]
    patcher_hash = struct.unpack("8I", d[0x90:0xB0])
        
    # Parse and store the kernel patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    # Create folder for the actual firmware binaries
    if not os.path.exists("../firmware/"):
        os.mkdir("../firmware/")
    os.chdir("../firmware/")
        
    kip_size = struct.unpack("I", d[0x40:0x44])[0]
    kip_off = struct.unpack("I", d[0x44:0x48])[0]
    kip_base = struct.unpack("I", d[0x48:0x4C])[0]
    kip_crc = struct.unpack("I", d[0x4C:0x50])[0]
    kip_hash = struct.unpack("8I", d[0xB0:0xD0])

    # Parse and store the Loader KIP1
    f = open("kip_{0:08X}.bin".format(kip_base), "wb")
    f.write(d[kip_off:kip_off+kip_size])
    f.close()
else:                                                       # New layout
    patcher_size = struct.unpack("I", d[0x00:0x04])[0]
    patcher_off = struct.unpack("I", d[0x04:0x08])[0]
    patcher_base = struct.unpack("I", d[0x08:0x0C])[0]
    patcher_crc = struct.unpack("I", d[0x0C:0x10])[0]
    patcher_hash = struct.unpack("8I", d[0x10:0x30])
        
    # Parse and store the PK11 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x30:0x34])[0]
    patcher_off = struct.unpack("I", d[0x34:0x38])[0]
    patcher_base = struct.unpack("I", d[0x38:0x3C])[0]
    patcher_crc = struct.unpack("I", d[0x3C:0x40])[0]
    patcher_hash = struct.unpack("8I", d[0x40:0x60])

    # Parse and store the KIP1/INI1 patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    patcher_size = struct.unpack("I", d[0x60:0x64])[0]
    patcher_off = struct.unpack("I", d[0x64:0x68])[0]
    patcher_base = struct.unpack("I", d[0x68:0x6C])[0]
    patcher_crc = struct.unpack("I", d[0x6C:0x70])[0]
    patcher_hash = struct.unpack("8I", d[0x70:0x90])
        
    # Parse and store the kernel patcher
    f = open("patcher_{0:08X}.bin".format(patcher_base), "wb")
    f.write(d[patcher_off:patcher_off+patcher_size])
    f.close()

    # Create folder for the actual firmware binaries
    if not os.path.exists("../firmware/"):
        os.mkdir("../firmware/")
    os.chdir("../firmware/")
    
    if version >= 300:
        kip_region_size = struct.unpack("I", d[0x90:0x94])[0]
        kip_region_off = struct.unpack("I", d[0x94:0x98])[0]
        kip_region_base = struct.unpack("I", d[0x98:0x9C])[0]
        kip_region_crc = struct.unpack("I", d[0x9C:0xA0])[0]
        kip_region_hash = struct.unpack("8I", d[0xA0:0xC0])
        
        # Parse the KIP region header
        kip_header_size = 0x100
        kip_header = d[kip_region_off:kip_region_off+kip_header_size]
        kip_entry_count = struct.unpack("I", kip_header[0x00:0x04])[0]
        kip_entry_size = 0x08
        
        # Store the KIP region header
        f = open("kip_header.bin", "wb")
        f.write(kip_header)
        f.close()
            
        # Parse and store the KIPs
        for i in xrange(kip_entry_count):
            kip_off = struct.unpack("I", kip_header[0x04 + i * kip_entry_size:0x08 + i * kip_entry_size])[0]
            kip_size = struct.unpack("I", kip_header[0x08 + i * kip_entry_size:0x0C + i * kip_entry_size])[0]
            
            # Loader, sm, ProcessMana and mitm
            f = open("kip_{0:08X}.bin".format(kip_region_base+kip_off), "wb")
            f.write(d[kip_region_off+kip_off:kip_region_off+kip_off+kip_size])
            f.close()
    else:
        kip_size = struct.unpack("I", d[0x90:0x94])[0]
        kip_off = struct.unpack("I", d[0x94:0x98])[0]
        kip_base = struct.unpack("I", d[0x98:0x9C])[0]
        kip_crc = struct.unpack("I", d[0x9C:0xA0])[0]
        kip_hash = struct.unpack("8I", d[0xA0:0xC0])

        # Parse and store the Loader KIP1
        f = open("kip_{0:08X}.bin".format(kip_base), "wb")
        f.write(d[kip_off:kip_off+kip_size])
        f.close()
    
        kip_size = struct.unpack("I", d[0xC0:0xC4])[0]
        kip_off = struct.unpack("I", d[0xC4:0xC8])[0]
        kip_base = struct.unpack("I", d[0xC8:0xCC])[0]
        kip_crc = struct.unpack("I", d[0xCC:0xD0])[0]
        kip_hash = struct.unpack("8I", d[0xD0:0xF0])

        # Parse and store the sm KIP1
        f = open("kip_{0:08X}.bin".format(kip_base), "wb")
        f.write(d[kip_off:kip_off+kip_size])
        f.close()
        
        # New KIP file in V1.3+
        if version >= 130:
            kip_size = struct.unpack("I", d[0xF0:0xF4])[0]
            kip_off = struct.unpack("I", d[0xF4:0xF8])[0]
            kip_base = struct.unpack("I", d[0xF8:0xFC])[0]
            kip_crc = struct.unpack("I", d[0xFC:0x100])[0]
            kip_hash = struct.unpack("8I", d[0x100:0x120])

            # Parse and store the fs.mitm KIP1
            f = open("kip_{0:08X}.bin".format(kip_base), "wb")
            f.write(d[kip_off:kip_off+kip_size])
            f.close()
    
        # New KIP file in V2.9+
        if version >= 290:
            kip_size = struct.unpack("I", d[0x120:0x124])[0]
            kip_off = struct.unpack("I", d[0x124:0x128])[0]
            kip_base = struct.unpack("I", d[0x128:0x12C])[0]
            kip_crc = struct.unpack("I", d[0x12C:0x130])[0]
            kip_hash = struct.unpack("8I", d[0x130:0x150])

            # Parse and store the ProcessMana KIP1
            f = open("kip_{0:08X}.bin".format(kip_base), "wb")
            f.write(d[kip_off:kip_off+kip_size])
            f.close()
        
# New application files in V1.4+
if version >= 140:
    app_region_off = struct.unpack("I", b[0x4C:0x50])[0]
    app_region_size = (len(b) - app_region_off)
    app_region = aes_ctr_dec(b[app_region_off:app_region_off+app_region_size], fw_key, fw_ctr)
    app_header_off = 0
    app_header_size = 0x310
    app_header = app_region[app_header_off:app_header_size]
    app_entry_count = struct.unpack("I", app_header[0x00:0x04])[0]
    app_entry_size = 0x30
    
    # Create folder for the application binaries
    if not os.path.exists("../apps/"):
        os.mkdir("../apps/")
    os.chdir("../apps/")
    
    # Store the application region header
    f = open("app_header.bin", "wb")
    f.write(app_header)
    f.close()
    
    # Parse and store the applications
    for i in xrange(app_entry_count):
        app_magic = struct.unpack("2I", app_header[0x10 + i * app_entry_size:0x18 + i * app_entry_size])
        app_hash = struct.unpack("8I", app_header[0x18 + i * app_entry_size:0x38 + i * app_entry_size])
        app_off = struct.unpack("I", app_header[0x38 + i * app_entry_size:0x3C + i * app_entry_size])[0]
        app_size = struct.unpack("I", app_header[0x3C + i * app_entry_size:0x40 + i * app_entry_size])[0]
        
        # ROMMENU
        if ((app_magic[0] == 0x4D454E55) and (app_magic[1] == 0x00524F4D)):
            f = open("ROMMENU.bin", "wb")
            f.write(app_region[app_off:app_off+app_size])
            f.close()
            
        # HBMENU
        if ((app_magic[0] == 0x4D454E55) and (app_magic[1] == 0x00004842)):
            f = open("HBMENU.bin", "wb")
            f.write(app_region[app_off:app_off+app_size])
            f.close()
        
        # New application files in V2.9.2+
        if version >= 292:
            # MLBIN
            if ((app_magic[0] == 0x4C42494E) and (app_magic[1] == 0x0000004D)):
                f = open("MLBIN.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # MLMETA
            if ((app_magic[0] == 0x4D455441) and (app_magic[1] == 0x00004D4C)):
                f = open("MLMETA.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # HBLBIN
            if ((app_magic[0] == 0x4C42494E) and (app_magic[1] == 0x00004842)):
                f = open("HBLBIN.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # HBLMETA
            if ((app_magic[0] == 0x4D455441) and (app_magic[1] == 0x0048424C)):
                f = open("HBLMETA.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
                
            # FTLBIN
            if ((app_magic[0] == 0x4C42494E) and (app_magic[1] == 0x00004654)):
                f = open("FTLBIN.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # FTLMETA
            if ((app_magic[0] == 0x4D455441) and (app_magic[1] == 0x0046544C)):
                f = open("FTLMETA.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # CREPBIN
            if ((app_magic[0] == 0x5042494E) and (app_magic[1] == 0x00435245)):
                f = open("CREPBIN.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # CREPMETA
            if ((app_magic[0] == 0x4D455441) and (app_magic[1] == 0x43524550)):
                f = open("CREPMETA.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # ECLBIN
            if ((app_magic[0] == 0x4C42494E) and (app_magic[1] == 0x00004543)):
                f = open("ECLBIN.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
            
            # ECLMETA
            if ((app_magic[0] == 0x4D455441) and (app_magic[1] == 0x0045434C)):
                f = open("ECLMETA.bin", "wb")
                f.write(app_region[app_off:app_off+app_size])
                f.close()
