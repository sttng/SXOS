###########################################################
# TX SX OS MIPS VM disassembler - by hexkyz and naehrwert #
###########################################################

import os
import re
import struct

host_calls_0 = {
    0x8E943DA2 : "host_crc32 (ptr r4r5, len r6)",
    0xD4AC6D16 : "host_expmod (dst r4, mod r5, exp r6, exp_size r7)",
    0x87205A64 : "host_read_u64 (r2r3 = *r4r5)",
    0x5BECE776 : "host_aes_set_key (ptr r4)",
    0xC58ACD13 : "host_call_function (ptr r4, arg r5)",
    0xBA4FC26A : "host_memcmp (ptr1 r4r5, ptr2 r6r7, len stk4)",
    0xFD859C9C : "host_data_cache_civac (ptr r4, len r5)",
    0x6445C898 : "host_write_u64 (*r4r5 = r6r7)",
    0x308EBEA4 : "host_get_ipc_result",
    0xA4345EDA : "host_memmove (ptr1 r4, ptr2 r5, len r6)",
    0xFB198D4C : "host_aes_enc_cbc",
    0x93F23757 : "host_rsa_oaep",
    0xB68EA896 : "host_aes_dec_cbc",
    0x46915487 : "host_aes_ctr",
    0x5045611F : "host_sha2 (ptr r4, len r5, dst ptr r6r7)",
    0x2E3DB2AB : "host_vm_memcpy (dst r4, src r5, size r6)",
    0x8CC2D88C : "host_sha2_hmac",
    0x9D104BEC : "host_get_license_buf",
    0x42D35BC8 : "host_get_field_98",
    0x4F56CFC3 : "host_vm_get_ptr",
    0x24083A54 : "host_parse_ipc_cmd",
    0x37646C3F : "host_vm_memcmp",
    0x418B8052 : "host_memcpy",
    0xC2A24132 : "host_memcpy",
    0x80A67D6D : "host_vm_memset",
    0x680419E7 : "host_read_u32",
    0x9D063E97 : "host_read_u8",
    0x9BE8BFCA : "host_fat_open_file",
    0x66E9BFF7 : "host_ipc_handle",
    0x5CC2894D : "host_svcSendSyncRequest",
    0x63F3D563 : "host_connect_to_service",
    0x2F365F20 : "host_search_pattern",
    0x70757343 : "host_write_u32",
    0xE02CE3F9 : "host_memset",
}

host_calls_1 = {
    0x9B40C841 : "host_crc32 (ptr r4r5, len r6)",
    0xC8B077C8 : "host_expmod (dst r4, mod r5, exp r6, exp_size r7)",
    0x921495FE : "host_read_u64 (r2r3 = *r4r5)",
    0x5A6641E2 : "host_aes_set_key (ptr r4)",
    0xC58ACD13 : "host_call_function (ptr r4, arg r5)",
    0xB0BCD374 : "host_memcmp (ptr1 r4r5, ptr2 r6r7, len stk4)",
    0xFD859C9C : "host_data_cache_civac (ptr r4, len r5)",
    0x6F946C26 : "host_write_u64 (*r4r5 = r6r7)",
    0x1ACB4B1B : "host_get_ipc_result",
    0xA4345EDA : "host_memmove (ptr1 r4, ptr2 r5, len r6)",
    0xF243B10F : "host_aes_enc_cbc",
    0x9D39D484 : "host_rsa_oaep",
    0xB08249FB : "host_aes_dec_cbc",
    0x44AAA3FC : "host_aes_ctr",
    0x4BE3D010 : "host_sha2 (ptr r4, len r5, dst ptr r6r7)",
    0x0B7944DC : "host_vm_memcpy (dst r4, src r5, size r6)",
    0x93217280 : "host_sha2_hmac",
    0xAA840564 : "host_get_license_buf",
    0x3766570A : "host_get_field_98",
    0x45872313 : "host_vm_get_ptr",
    0x001A6147 : "host_parse_ipc_cmd",
    0x28DA2760 : "host_vm_memcmp",
    0x370C4363 : "host_memcpy",
    0xB66C364C : "host_memcpy",
    0x8CFF0E3B : "host_vm_memset",
    0x74ADB312 : "host_read_u32",
    0xA9A17504 : "host_read_u8",
    0xA049A7D6 : "host_fat_open_file",
    0x70B8F5BF : "host_ipc_handle",
    0x686E04E0 : "host_svcSendSyncRequest",
    0x6C803A13 : "host_connect_to_service",
    0x1205F934 : "host_search_pattern",
    0x85DFF35C : "host_write_u32",
    0xCC8A94A1 : "host_memset",
}

xor_block = re.sub(r"\W", "", """
F0 A4 46 B0 C6 B1 9A E0 81 83 F8 0A 0A CE B3 4A 
56 57 BF 88 81 1E 7D 7A 0C D1 AE B4 C1 58 A3 B3 
64 BE 39 BC F1 72 2E 7E 66 12 6B D2 8C 69 04 3A 
CB 84 52 FB F1 AC 98 F0 94 92 6F E9 BD 83 E6 7E 
51 12 55 A5 4B B2 73 39 55 BB 96 A5 B8 0B FD 49 
42 33 5F 61 8D 16 2D B9 57 26 21 A0 23 C3 D0 B6 
59 51 6A 5E BD A8 3C 77 1B DB CE D2 C5 ED 36 C1 
2D B9 68 3F 44 BC FB 70 88 7D 74 F2 9E 70 4E FF 
F3 19 72 9E 32 06 91 BF D9 42 47 EE 1C 3B B8 D9 
BB CF 0C C7 29 EC F2 A3 E2 46 6B EC 68 41 4C DA 
2C 9D 05 02 F0 6D F8 24 41 7E 5E B6 78 37 18 95 
1D EB FB 27 8F 34 A1 B1 7D 3B C8 87 51 E7 D0 BB 
68 09 D2 8F 42 38 D1 01 81 93 CB 0E 7D 1B ED B8 
0A 0E 58 CF D9 FC 3E C6 0D 6A F5 41 DC 7D C7 11 
BD D5 B3 88 02 8D 74 87 A2 FD 2C 52 20 B5 8B D5 
D2 41 BF 36 5E 5F C4 85 90 37 9E 7F 67 CA 87 10
""").decode("hex")

rnam = [
    "$zero", 
    "$at", 
    "$v0", "$v1", 
    "$a0", "$a1", "$a2", "$a3", 
    "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", 
    "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", 
    "$t8", "$t9", 
    "$k0", "$k1", 
    "$gp", 
    "$sp", 
    "$fp", 
    "$ra", 
]

def vm_get_instr(p, i):
    xi = (i & 0xFF)
    x = struct.unpack("I", xor_block[xi : xi + 4])[0]
    y = struct.unpack("I", p[i : i + 4])[0]
    return x ^ y

def str_simm16(imm):
    return "{0}0x{1:X}".format("-" if imm < 0 else "", -imm if imm < 0 else imm)

def decode_simm16(imm):
    return -(0xFFFF - imm + 1) if imm & 0x8000 else imm

def vm_dis(p, vm_version):
    jal_targ = []
    b_targ = []
    lis_val = [-1] * 32
    lines = [[""] for i in xrange(0, len(p), 4)]
    for i in xrange(0, len(p), 4):
        lines[i/4].append("{0:04X}\t\t".format(i))
        inst = vm_get_instr(p, i)
        op = inst >> 26
        if ((vm_version == 0) and (op == 53)) \
            or ((vm_version == 1) and (op == 20)):
            reg = (inst >> 21) & 0x1F
            off = inst & 0xFFFF
            lines[i/4].append("bgz {0}, loc_{1:X}".format(rnam[reg], i + 4 * off))
            b_targ.append(i + 4 * off)
        elif ((vm_version == 0) and (op == 15)) \
            or ((vm_version == 1) and (op == 34)):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("ld.32 {0}, [{1} + {2}]".format(rnam[dst_reg], rnam[src_reg], str_simm16(off)))
        elif ((vm_version == 0) and (op == 56)) \
            or ((vm_version == 1) and (op == 26)):
            reg1 = (inst >> 16) & 0x1F
            reg2 = (inst >> 21) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("beq {0}, {1}, loc_{2:X}".format(rnam[reg1], rnam[reg2], i + 4 * off))
            b_targ.append(i + 4 * off)
        elif ((vm_version == 0) and (op == 28)) \
            or ((vm_version == 1) and (op == 57)):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            imm = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("addi {0}, {1}, {2}".format(rnam[dst_reg], rnam[src_reg], str_simm16(imm)))
        elif ((vm_version == 0) and (op == 1 or op == 49)) \
            or ((vm_version == 1) and ((op == 6) or (op == 14))):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("ld.8 {0}, [{1} + {2}]".format(rnam[dst_reg], rnam[src_reg], str_simm16(off)))
        elif ((vm_version == 0) and (op == 20)) \
            or ((vm_version == 1) and (op == 0)):
            imm = 4 * (inst & 0x3FFFFFF)
            lines[i/4].append("j loc_{0:X}".format(imm))
            b_targ.append(imm)
        elif ((vm_version == 0) and (op == 23)) \
            or ((vm_version == 1) and (op == 4)):
            dst_reg = (inst >> 16) & 0x1F
            imm = (inst << 16) & 0xFFFF0000
            lines[i/4].append("lis {0}, 0x{1:X}".format(rnam[dst_reg], imm >> 16))
            lis_val[dst_reg] = imm
        elif ((vm_version == 0) and (op == 21)) \
            or ((vm_version == 1) and (op == 37)):
            reg1 = (inst >> 16) & 0x1F
            reg2 = (inst >> 21) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("beq {0}, {1}, loc_{2:X}".format(rnam[reg1], rnam[reg2], i + 4 * off))
            b_targ.append(i + 4 * off)
        elif ((vm_version == 0) and (op == 10)) \
            or ((vm_version == 1) and (op == 31)):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            lines[i/4].append("unk {0}, {1}, {2:X}, {3:X}, {4:X}".format(rnam[dst_reg], rnam[src_reg], inst & 0x7FF, ((inst >> 6) & 0x1F), (inst & 0xFFFF) >> 11))
        elif ((vm_version == 0) and (op == 24)) \
            or ((vm_version == 1) and (op == 56)):
            dst_reg = (inst >> 11) & 0x1F
            src1_reg = (inst >> 21) & 0x1F
            src2_reg = (inst >> 16) & 0x1F
            lines[i/4].append("mul {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
        elif ((vm_version == 0) and (op == 51)) \
            or ((vm_version == 1) and (op == 47)):
            dst_reg = (inst >> 21) & 0x1F
            src_reg = (inst >> 16) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("st.8 [{0} + {1}], {2}".format(rnam[dst_reg], str_simm16(off), rnam[src_reg]))
        elif ((vm_version == 0) and ((op == 26) or (op == 35))) \
            or ((vm_version == 1) and ((op == 24) or (op == 35))):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            imm = inst & 0xFFFF
            lines[i/4].append("sltiu {0}, {1}, 0x{2:X}".format(rnam[dst_reg], rnam[src_reg], imm))
        elif ((vm_version == 0) and (op == 17)) \
            or ((vm_version == 1) and (op == 60)):
            imm = 4 * (inst & 0x3FFFFFF)
            lines[i/4].append("jal sub_{0:X}".format(imm))
            jal_targ.append(imm)
        elif ((vm_version == 0) and (op == 37)) \
            or ((vm_version == 1) and (op == 1)):
            reg1 = (inst >> 16) & 0x1F
            reg2 = (inst >> 21) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("bne {0}, {1}, loc_{2:X}".format(rnam[reg1], rnam[reg2], i + 4 * off))
            b_targ.append(i + 4 * off)
        elif ((vm_version == 0) and (op == 4)) \
            or ((vm_version == 1) and (op == 63)):
            reg1 = (inst >> 16) & 0x1F
            reg2 = (inst >> 21) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("bneq {0}, {1}, loc_{2:X}".format(rnam[reg1], rnam[reg2], i + 4 * off))
            b_targ.append(i + 4 * off)
        elif ((vm_version == 0) and (op == 39)) \
            or ((vm_version == 1) and (op == 30)):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            imm = inst & 0xFFFF
            lines[i/4].append("ori {0}, {1}, 0x{2:X}".format(rnam[dst_reg], rnam[src_reg], imm))
            if dst_reg == src_reg and lis_val[dst_reg] != -1:
                val = lis_val[dst_reg] | imm
                lis_val[dst_reg] = -1
                lines[i/4].append("; = 0x{0:X}".format(val))
                if dst_reg == 2:
                    if ((vm_version == 0) and (val in host_calls_0)):
                        lines[i/4].append(" - {0}".format(host_calls_0[val]))
                    elif ((vm_version == 1) and (val in host_calls_1)):
                        lines[i/4].append(" - {0}".format(host_calls_1[val]))
                    else:
                        lines[i/4].append(" - UNK")
        elif ((vm_version == 0) and (op == 32)) \
            or ((vm_version == 1) and (op == 51)):
            dst_reg = (inst >> 21) & 0x1F
            src_reg = (inst >> 16) & 0x1F
            off = decode_simm16(inst & 0xFFFF)
            lines[i/4].append("st.32 [{0} + {1}], {2}".format(rnam[dst_reg], str_simm16(off), rnam[src_reg]))
        elif ((vm_version == 0) and (op == 29)) \
            or ((vm_version == 1) and (op == 61)):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            imm = inst & 0xFFFF
            lines[i/4].append("xori {0}, {1}, 0x{2:X}".format(rnam[dst_reg], rnam[src_reg], imm))
        elif ((vm_version == 1) and (op == 21)):
            dst_reg = (inst >> 16) & 0x1F
            src_reg = (inst >> 21) & 0x1F
            imm = inst & 0xFFFF
            lines[i/4].append("andi {0}, {1}, 0x{2:X}".format(rnam[dst_reg], rnam[src_reg], imm))
        elif ((vm_version == 0) and (op == 18)) \
            or ((vm_version == 1) and (op == 3)):
            sop = inst & 0x3F
            if ((vm_version == 0) and (sop == 12)) \
                or ((vm_version == 1) and (sop == 15)):
                dst_reg = (inst >> 11) & 0x1F
                src_reg = (inst >> 16) & 0x1F
                imm = (inst >> 6) & 0x1F
                lines[i/4].append("shr {0}, {1}, 0x{2:X}".format(rnam[dst_reg], rnam[src_reg], imm))
            elif ((vm_version == 0) and (sop == 48)) \
                or ((vm_version == 1) and (sop == 20)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("ashr {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 52)) \
                or ((vm_version == 1) and (sop == 6)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("shr {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 53)) \
                or ((vm_version == 1) and (sop == 23)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("sub {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 7)) \
                or ((vm_version == 1) and (sop == 0)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("xor {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 63)) \
                or ((vm_version == 1) and (sop == 3)):
                reg = (inst >> 21) & 0x1F
                lines[i/4].append("jr {0}".format(rnam[reg]))
            elif ((vm_version == 0) and (sop == 62)) \
                or ((vm_version == 1) and (sop == 37)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("and {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 6)) \
                or ((vm_version == 1) and (sop == 55)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("add {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 30)) \
                or ((vm_version == 1) and (sop == 12)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("nor {0}, ~{1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 14)) \
                or ((vm_version == 1) and (sop == 52)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("cmov.nz {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 27)) \
                or ((vm_version == 1) and (sop == 24)):
                dst_reg = (inst >> 11) & 0x1F
                src_reg = (inst >> 16) & 0x1F
                imm = (inst >> 6) & 0x1F
                if (dst_reg == 0) and (src_reg == 0) and (imm == 0):
                    lines[i/4].append("nop")
                else:
                    lines[i/4].append("shl {0}, {1}, 0x{2:X}".format(rnam[dst_reg], rnam[src_reg], imm))
            elif ((vm_version == 0) and (sop == 49)) \
                or ((vm_version == 1) and (sop == 40)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("shl {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 3)) \
                or ((vm_version == 1) and (sop == 14)):
                dst_reg = (inst >> 11) & 0x1F
                src_reg = (inst >> 21) & 0x1F
                lines[i/4].append("brx {0}, {1}".format(rnam[dst_reg], rnam[src_reg]))
            elif ((vm_version == 0) and (sop == 33)) \
                or ((vm_version == 1) and (sop == 18)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("or {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 43)) \
                or ((vm_version == 1) and (sop == 11)):
                dst_reg = (inst >> 11) & 0x1F
                src1_reg = (inst >> 21) & 0x1F
                src2_reg = (inst >> 16) & 0x1F
                lines[i/4].append("slt {0}, {1}, {2}".format(rnam[dst_reg], rnam[src1_reg], rnam[src2_reg]))
            elif ((vm_version == 0) and (sop == 1)) \
                or ((vm_version == 1) and (sop == 36)):
                lines[i/4].append("host_call")
            else:
                lines[i/4].append("extended op 0x{0:X}".format(sop))
        else:
            lines[i/4].append("unknown op 0x{0:X}".format(op))
    for i in xrange(0, len(p), 4):
        if i in jal_targ:
            lines[i/4] = ["\n;------- subroutine -------\nsub_{0:X}:\n".format(i)] + lines[i/4]
        elif i in b_targ:
            lines[i/4] = ["\nloc_{0:X}:\n".format(i)] + lines[i/4]
    return lines

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

# Open main file
f = open("boot.dat", "rb")
b = f.read()
f.close()

# Extract the version
version = get_ver_int(struct.unpack("II", b[0x08:0x10]))

# Only support the most relevant versions
if version == 140:
    vm_off = 0x4E470
    vm_size = 0x194C
    vm_version = 0
elif version == 290:
    vm_off = 0xA45C8
    vm_size = 0x1ED4
    vm_version = 1
else:
    exit()

# Enter the Loader KIP's directory
if os.path.exists("./sxos/firmware/Loader/"):
    os.chdir("./sxos/firmware/Loader/")
else:
    exit()

# Open and read the extracted Loader binary
f = open("Loader.bin", "rb")
v = f.read()
f.close()

# Locate and disassemble the MIPS VM
f = open("Loader_VM.asm", "w")
lines = vm_dis(v[vm_off:vm_off+vm_size], vm_version)
for l in lines:
    f.write("%s\n" % "".join(l));
f.close()