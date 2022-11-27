0000		nop
0004		nop
0008		nop
000C		lis $v0, 0x0
0010		addi $v0, $v0, 0x28
0014		brx $ra, $v0
0018		nop
001C		nop
0020		nop
0024		nop
0028		addi $sp, $sp, -0x18
002C		bneq $zero, $a2, loc_40
0030		st.32 [$sp + 0x14], $ra
0034		jal sub_128
0038		nop
003C		j loc_74

loc_40:
0040		ld.32 $ra, [$sp + 0x14]
0044		addi $v0, $zero, 0x1
0048		bneq $v0, $a2, loc_5C
004C		addi $v0, $zero, 0x2
0050		jal sub_62C
0054		nop
0058		j loc_74

loc_5C:
005C		ld.32 $ra, [$sp + 0x14]
0060		bneq $v0, $a2, loc_70
0064		ld.32 $ra, [$sp + 0x14]
0068		jal sub_14B0
006C		nop

loc_70:
0070		ld.32 $ra, [$sp + 0x14]

loc_74:
0074		add $v0, $zero, $zero
0078		jr $ra
007C		addi $sp, $sp, 0x18

;------- subroutine -------
sub_80:
0080		lis $v0, 0x0
0084		addi $sp, $sp, -0x140
0088		ld.32 $v1, [$v0 + 0x2844]
008C		st.32 [$sp + 0x134], $s0
0090		addi $s0, $zero, 0x1
0094		st.32 [$sp + 0x13C], $ra
0098		beq $s0, $v1, loc_110
009C		st.32 [$sp + 0x138], $s1
00A0		addi $a0, $sp, 0x118
00A4		jal sub_1270
00A8		add $s1, $v0, $zero
00AC		bneq $zero, $v0, loc_100
00B0		nop
00B4		jal sub_17B0
00B8		addi $a0, $sp, 0x18
00BC		st.32 [$sp + 0x128], $v0
00C0		jal sub_1788
00C4		st.32 [$sp + 0x12C], $v1
00C8		addi $a2, $zero, 0x100
00CC		ld.32 $a0, [$sp + 0x128]
00D0		ld.32 $a1, [$sp + 0x12C]
00D4		st.32 [$sp + 0x10], $a2
00D8		add $a3, $v1, $zero
00DC		jal sub_1828
00E0		add $a2, $v0, $zero
00E4		addi $a0, $sp, 0x18
00E8		jal sub_13C4
00EC		addi $a1, $sp, 0x118
00F0		beq $zero, $v0, loc_100
00F4		lis $v0, 0x0
00F8		st.32 [$v0 + 0x305C], $s0
00FC		lis $v0, 0x0

loc_100:
0100		st.32 [$v0 + 0x3058], $zero
0104		jal sub_128
0108		nop
010C		addi $v0, $zero, 0x1

loc_110:
0110		st.32 [$s1 + 0x2844], $v0
0114		ld.32 $ra, [$sp + 0x13C]
0118		ld.32 $s1, [$sp + 0x138]
011C		ld.32 $s0, [$sp + 0x134]
0120		jr $ra
0124		addi $sp, $sp, 0x140

;------- subroutine -------
sub_128:
0128		addi $sp, $sp, -0x18
012C		st.32 [$sp + 0x14], $ra
0130		jal sub_1788
0134		nop
0138		add $a1, $v1, $zero
013C		add $a0, $v0, $zero
0140		jal sub_16D4
0144		addi $a2, $zero, 0x100
0148		lis $v1, 0x0
014C		ld.32 $a2, [$v1 + 0x2840]
0150		addi $a0, $zero, 0x1
0154		bneq $a0, $a2, loc_174
0158		lis $a1, 0x0
015C		ld.32 $v1, [$a1 + 0x3054]
0160		beq $v0, $v1, loc_17C
0164		lis $v0, 0x0
0168		st.32 [$v0 + 0x305C], $a2
016C		lis $v0, 0x0
0170		j loc_180

loc_174:
0174		st.32 [$v0 + 0x3058], $zero
0178		st.32 [$a1 + 0x3054], $v0

loc_17C:
017C		st.32 [$v1 + 0x2840], $a0

loc_180:
0180		ld.32 $ra, [$sp + 0x14]
0184		jr $ra
0188		addi $sp, $sp, 0x18

;------- subroutine -------
sub_18C:
018C		addi $sp, $sp, -0x48
0190		st.32 [$sp + 0x10], $a0
0194		ld.32 $a0, [$sp + 0x58]
0198		st.32 [$sp + 0x44], $ra
019C		st.32 [$sp + 0x14], $a1
01A0		st.32 [$sp + 0x18], $a2
01A4		jal sub_17B0
01A8		st.32 [$sp + 0x1C], $a3
01AC		st.32 [$sp + 0x20], $v0
01B0		ld.32 $a0, [$sp + 0x60]
01B4		ld.32 $v0, [$sp + 0x5C]
01B8		st.32 [$sp + 0x24], $v1
01BC		jal sub_17B0
01C0		st.32 [$sp + 0x28], $v0
01C4		st.32 [$sp + 0x30], $v0
01C8		ld.32 $v0, [$sp + 0x64]
01CC		addi $a0, $sp, 0x10
01D0		st.32 [$sp + 0x34], $v1
01D4		jal sub_16C0
01D8		st.32 [$sp + 0x38], $v0
01DC		ld.32 $ra, [$sp + 0x44]
01E0		jr $ra
01E4		addi $sp, $sp, 0x48

;------- subroutine -------
sub_1E8:
01E8		lis $a0, 0x0
01EC		j loc_18C8
01F0		addi $a0, $a0, 0x3060

;------- subroutine -------
sub_1F4:
01F4		addi $sp, $sp, -0x40
01F8		st.32 [$sp + 0x3C], $ra
01FC		st.32 [$sp + 0x38], $fp
0200		st.32 [$sp + 0x30], $s6
0204		st.32 [$sp + 0x2C], $s5
0208		st.32 [$sp + 0x24], $s3
020C		st.32 [$sp + 0x20], $s2
0210		st.32 [$sp + 0x1C], $s1
0214		st.32 [$sp + 0x18], $s0
0218		add $fp, $sp, $zero
021C		st.32 [$sp + 0x34], $s7
0220		st.32 [$sp + 0x28], $s4
0224		addi $sp, $sp, -0x3B0
0228		addi $s3, $sp, 0x27
022C		shr $s3, $s3, 0x4
0230		shl $s3, $s3, 0x4
0234		addi $s0, $s3, 0x1F0
0238		add $s6, $a0, $zero
023C		add $a0, $s0, $zero
0240		jal sub_1368
0244		add $s5, $a1, $zero
0248		jal sub_179C
024C		nop
0250		add $s1, $v1, $zero
0254		or $v1, $v0, $v1
0258		add $s2, $v0, $zero
025C		beq $zero, $v1, loc_348
0260		addi $v0, $zero, 0x666
0264		add $a1, $s1, $zero
0268		add $a0, $s2, $zero
026C		add $a2, $zero, $zero
0270		addi $a3, $zero, 0x10
0274		jal sub_1864
0278		addi $s4, $zero, 0x10
027C		add $a0, $s0, $zero
0280		add $a2, $s2, $zero
0284		add $a3, $s1, $zero
0288		st.32 [$sp + 0x10], $s4
028C		jal sub_1310
0290		st.32 [$sp + 0x14], $zero
0294		add $a0, $s0, $zero
0298		jal sub_17D8
029C		addi $a1, $zero, 0x18
02A0		lis $a2, 0x4943
02A4		add $s0, $v0, $zero
02A8		add $a0, $v0, $zero
02AC		add $a1, $v1, $zero
02B0		ori $a2, $a2, 0x4653; = 0x49434653
02B4		add $a3, $zero, $zero
02B8		jal sub_1918
02BC		add $s7, $v1, $zero
02C0		addi $a0, $s0, 0x8
02C4		slt $a1, $a0, $s0
02C8		add $a1, $a1, $s7
02CC		addi $a2, $zero, 0x64
02D0		jal sub_1918
02D4		add $a3, $zero, $zero
02D8		addi $a0, $s0, 0x10
02DC		slt $a1, $a0, $s0
02E0		add $a1, $a1, $s7
02E4		addi $a2, $zero, 0x10
02E8		jal sub_1918
02EC		add $a3, $zero, $zero
02F0		jal sub_18DC
02F4		add $a0, $s6, $zero
02F8		bne $zero, $v0, loc_34C
02FC		add $sp, $fp, $zero
0300		jal sub_17C4
0304		add $a0, $s3, $zero
0308		ld.32 $v0, [$s3 + 0x1D8]
030C		ld.32 $a1, [$s3 + 0x1DC]
0310		addi $a0, $v0, 0x8
0314		slt $v0, $a0, $v0
0318		jal sub_188C
031C		add $a1, $v0, $a1
0320		bneq $zero, $v0, loc_344
0324		add $s0, $v0, $zero
0328		jal sub_17B0
032C		add $a0, $s5, $zero
0330		add $a0, $v0, $zero
0334		st.32 [$sp + 0x10], $s4
0338		add $a1, $v1, $zero
033C		add $a2, $s2, $zero
0340		jal sub_1828

loc_344:
0344		add $a3, $s1, $zero

loc_348:
0348		add $v0, $s0, $zero

loc_34C:
034C		add $sp, $fp, $zero
0350		ld.32 $ra, [$sp + 0x3C]
0354		ld.32 $fp, [$sp + 0x38]
0358		ld.32 $s7, [$sp + 0x34]
035C		ld.32 $s6, [$sp + 0x30]
0360		ld.32 $s5, [$sp + 0x2C]
0364		ld.32 $s4, [$sp + 0x28]
0368		ld.32 $s3, [$sp + 0x24]
036C		ld.32 $s2, [$sp + 0x20]
0370		ld.32 $s1, [$sp + 0x1C]
0374		ld.32 $s0, [$sp + 0x18]
0378		jr $ra
037C		addi $sp, $sp, 0x40

;------- subroutine -------
sub_380:
0380		addi $sp, $sp, -0x30
0384		addi $v0, $zero, 0x66
0388		st.32 [$sp + 0x28], $fp
038C		add $fp, $sp, $zero
0390		st.32 [$sp + 0x24], $s3
0394		st.32 [$sp + 0x1C], $s1
0398		st.32 [$sp + 0x2C], $ra
039C		st.32 [$sp + 0x20], $s2
03A0		st.32 [$sp + 0x18], $s0
03A4		st.8 [$fp + 0x10], $v0
03A8		addi $sp, $sp, -0x3B0
03AC		addi $v0, $zero, 0x73
03B0		addi $v1, $zero, 0x70
03B4		addi $s1, $sp, 0x1F
03B8		st.8 [$fp + 0x11], $v0
03BC		st.8 [$fp + 0x14], $v0
03C0		lis $s3, 0x0
03C4		addi $v0, $zero, 0x72
03C8		shr $s1, $s1, 0x4
03CC		st.8 [$fp + 0x12], $v1
03D0		st.8 [$fp + 0x15], $v0
03D4		addi $v1, $zero, 0x2D
03D8		addi $v0, $zero, 0x76
03DC		addi $a0, $s3, 0x3060
03E0		addi $a1, $fp, 0x10
03E4		shl $s1, $s1, 0x4
03E8		st.8 [$fp + 0x13], $v1
03EC		st.8 [$fp + 0x16], $v0
03F0		jal sub_18F0
03F4		st.8 [$fp + 0x17], $zero
03F8		bne $zero, $v0, loc_4A0
03FC		add $sp, $fp, $zero
0400		addi $s0, $s1, 0x1F0
0404		jal sub_1368
0408		add $a0, $s0, $zero
040C		jal sub_1374
0410		add $a0, $s0, $zero
0414		add $a0, $s0, $zero
0418		jal sub_17D8
041C		addi $a1, $zero, 0x18
0420		lis $a2, 0x4943
0424		add $s0, $v0, $zero
0428		add $a0, $v0, $zero
042C		add $a1, $v1, $zero
0430		ori $a2, $a2, 0x4653; = 0x49434653
0434		add $a3, $zero, $zero
0438		jal sub_1918
043C		add $s2, $v1, $zero
0440		addi $a0, $s0, 0x8
0444		slt $a1, $a0, $s0
0448		add $a1, $a1, $s2
044C		addi $a2, $zero, 0x1
0450		jal sub_1918
0454		add $a3, $zero, $zero
0458		addi $a0, $s0, 0x10
045C		slt $a1, $a0, $s0
0460		add $a1, $a1, $s2
0464		add $a2, $zero, $zero
0468		jal sub_1918
046C		add $a3, $zero, $zero
0470		jal sub_18DC
0474		addi $a0, $s3, 0x3060
0478		bne $zero, $v0, loc_4A0
047C		add $sp, $fp, $zero
0480		jal sub_17C4
0484		add $a0, $s1, $zero
0488		ld.32 $v0, [$s1 + 0x1D8]
048C		ld.32 $a1, [$s1 + 0x1DC]
0490		addi $a0, $v0, 0x8
0494		slt $v0, $a0, $v0
0498		jal sub_188C
049C		add $a1, $v0, $a1

loc_4A0:
04A0		add $sp, $fp, $zero
04A4		ld.32 $ra, [$sp + 0x2C]
04A8		ld.32 $fp, [$sp + 0x28]
04AC		ld.32 $s3, [$sp + 0x24]
04B0		ld.32 $s2, [$sp + 0x20]
04B4		ld.32 $s1, [$sp + 0x1C]
04B8		ld.32 $s0, [$sp + 0x18]
04BC		jr $ra
04C0		addi $sp, $sp, 0x30

;------- subroutine -------
sub_4C4:
04C4		addi $sp, $sp, -0x30
04C8		st.32 [$sp + 0x2C], $ra
04CC		st.32 [$sp + 0x28], $fp
04D0		st.32 [$sp + 0x24], $s3
04D4		add $fp, $sp, $zero
04D8		st.32 [$sp + 0x20], $s2
04DC		st.32 [$sp + 0x1C], $s1
04E0		st.32 [$sp + 0x18], $s0
04E4		addi $sp, $sp, -0x3B0
04E8		addi $s0, $sp, 0x1F
04EC		shr $s0, $s0, 0x4
04F0		shl $s0, $s0, 0x4
04F4		addi $s1, $s0, 0x1F0
04F8		add $s3, $a0, $zero
04FC		jal sub_1368
0500		add $a0, $s1, $zero
0504		add $a0, $s1, $zero
0508		jal sub_17D8
050C		addi $a1, $zero, 0x10
0510		lis $a2, 0x4943
0514		add $s1, $v0, $zero
0518		add $a0, $v0, $zero
051C		add $a1, $v1, $zero
0520		ori $a2, $a2, 0x4653; = 0x49434653
0524		add $a3, $zero, $zero
0528		jal sub_1918
052C		add $s2, $v1, $zero
0530		addi $a0, $s1, 0x8
0534		slt $a1, $a0, $s1
0538		add $a1, $a1, $s2
053C		addi $a2, $zero, 0x190
0540		jal sub_1918
0544		add $a3, $zero, $zero
0548		lis $a0, 0x0
054C		jal sub_18DC
0550		addi $a0, $a0, 0x3060
0554		bne $zero, $v0, loc_598
0558		add $sp, $fp, $zero
055C		jal sub_17C4
0560		add $a0, $s0, $zero
0564		ld.32 $v1, [$s0 + 0x1D8]
0568		ld.32 $a1, [$s0 + 0x1DC]
056C		addi $a0, $v1, 0x8
0570		slt $v1, $a0, $v1
0574		jal sub_188C
0578		add $a1, $v1, $a1
057C		bne $zero, $v0, loc_598
0580		add $sp, $fp, $zero
0584		ld.32 $a1, [$s0 + 0x18]
0588		add $a0, $s3, $zero
058C		jal sub_1934
0590		st.32 [$fp + 0x10], $v0
0594		ld.32 $v0, [$fp + 0x10]

loc_598:
0598		add $sp, $fp, $zero
059C		ld.32 $ra, [$sp + 0x2C]
05A0		ld.32 $fp, [$sp + 0x28]
05A4		ld.32 $s3, [$sp + 0x24]
05A8		ld.32 $s2, [$sp + 0x20]
05AC		ld.32 $s1, [$sp + 0x1C]
05B0		ld.32 $s0, [$sp + 0x18]
05B4		jr $ra
05B8		addi $sp, $sp, 0x30

;------- subroutine -------
sub_5BC:
05BC		addi $v0, $a0, 0x124
05C0		slt $v1, $v0, $a0
05C4		addi $sp, $sp, -0x18
05C8		add $a1, $v1, $a1
05CC		add $a0, $v0, $zero
05D0		st.32 [$sp + 0x10], $s0
05D4		st.32 [$sp + 0x14], $ra
05D8		jal sub_1878
05DC		add $s0, $a2, $zero
05E0		lis $v1, 0x1
05E4		ori $v1, $v1, 0x8600; = 0x18600
05E8		bne $v1, $v0, loc_604
05EC		addi $v0, $zero, 0x12C
05F0		addi $v0, $zero, 0x130
05F4		st.32 [$s0 + 0x0], $v0
05F8		addi $v0, $zero, 0x12C
05FC		st.32 [$s0 + 0x4], $v0
0600		j loc_618

loc_604:
0604		addi $v0, $zero, 0x140
0608		st.32 [$s0 + 0x0], $v0
060C		addi $v0, $zero, 0x128
0610		st.32 [$s0 + 0x4], $v0
0614		addi $v0, $zero, 0x13C

loc_618:
0618		ld.32 $ra, [$sp + 0x14]
061C		st.32 [$s0 + 0x8], $v0
0620		ld.32 $s0, [$sp + 0x10]
0624		jr $ra
0628		addi $sp, $sp, 0x18

;------- subroutine -------
sub_62C:
062C		addi $sp, $sp, -0x68
0630		st.32 [$sp + 0x54], $s5
0634		add $s5, $a0, $zero
0638		st.32 [$sp + 0x64], $ra
063C		st.32 [$sp + 0x60], $fp
0640		st.32 [$sp + 0x5C], $s7
0644		st.32 [$sp + 0x58], $s6
0648		st.32 [$sp + 0x50], $s4
064C		add $s6, $a1, $zero
0650		st.32 [$sp + 0x4C], $s3
0654		st.32 [$sp + 0x48], $s2
0658		st.32 [$sp + 0x40], $s0
065C		jal sub_188C
0660		st.32 [$sp + 0x44], $s1
0664		addi $a0, $s5, 0x8
0668		slt $a1, $a0, $s5
066C		add $a1, $a1, $s6
0670		st.32 [$sp + 0x30], $v0
0674		jal sub_188C
0678		st.32 [$sp + 0x34], $v1
067C		addi $a0, $s5, 0x10
0680		slt $a1, $a0, $s5
0684		add $a1, $a1, $s6
0688		add $s4, $v0, $zero
068C		jal sub_188C
0690		add $fp, $v1, $zero
0694		addi $a0, $s5, 0x18
0698		slt $a1, $a0, $s5
069C		add $a1, $a1, $s6
06A0		add $s2, $v0, $zero
06A4		jal sub_188C
06A8		add $s3, $v1, $zero
06AC		or $s0, $v0, $v1
06B0		add $s6, $v0, $zero
06B4		add $s5, $v1, $zero
06B8		beq $zero, $s0, loc_6F4
06BC		or $s7, $s2, $s3
06C0		add $a0, $v0, $zero
06C4		add $a1, $v1, $zero
06C8		jal sub_1904
06CC		add $a2, $zero, $zero
06D0		beq $zero, $s7, loc_6F8
06D4		lis $v1, 0x0
06D8		addi $a0, $s2, 0x10
06DC		slt $a1, $a0, $s2
06E0		jal sub_1878
06E4		add $a1, $a1, $s3
06E8		add $a2, $v0, $zero
06EC		add $a0, $s6, $zero
06F0		jal sub_1904

loc_6F4:
06F4		add $a1, $s5, $zero

loc_6F8:
06F8		lis $v1, 0x0
06FC		addi $v0, $v1, 0x306C
0700		ld.32 $a0, [$v0 + 0x194]
0704		add $s1, $v1, $zero
0708		addi $v1, $zero, 0x1
070C		beq $v1, $a0, loc_71C
0710		add $a0, $v0, $zero
0714		jal sub_1230
0718		st.32 [$sp + 0x38], $v0

loc_71C:
071C		ld.32 $v0, [$sp + 0x38]
0720		lis $v1, 0x0
0724		ld.32 $v1, [$v1 + 0x305C]
0728		beq $zero, $v1, loc_74C
072C		add $a0, $s4, $zero
0730		lis $a0, 0x0
0734		ld.32 $v1, [$a0 + 0x3058]
0738		addi $v1, $v1, 0x1
073C		st.32 [$a0 + 0x3058], $v1
0740		sltiu $v1, $v1, 0x4E21
0744		beq $zero, $v1, loc_748

loc_748:
0748		st.32 [$v0 + 0x194], $zero

loc_74C:
074C		add $a0, $s4, $zero
0750		jal sub_1878
0754		add $a1, $fp, $zero
0758		addi $a0, $s4, 0x4
075C		slt $a1, $a0, $s4
0760		add $a1, $a1, $fp
0764		jal sub_1878
0768		st.32 [$sp + 0x10], $v0
076C		st.32 [$sp + 0x14], $v0
0770		beq $zero, $s7, loc_7D0
0774		st.32 [$sp + 0x20], $zero
0778		add $a0, $s2, $zero
077C		jal sub_188C
0780		add $a1, $s3, $zero
0784		addi $a0, $s2, 0x8
0788		slt $a1, $a0, $s2
078C		add $a1, $a1, $s3
0790		st.32 [$sp + 0x18], $v0
0794		jal sub_188C
0798		st.32 [$sp + 0x1C], $v1
079C		addi $a0, $s2, 0x10
07A0		slt $a1, $a0, $s2
07A4		add $a1, $a1, $s3
07A8		jal sub_1878
07AC		st.32 [$sp + 0x38], $v0
07B0		ld.32 $v1, [$sp + 0x38]
07B4		addi $a0, $s2, 0x14
07B8		mul $v0, $v0, $v1
07BC		slt $a1, $a0, $s2
07C0		add $a1, $a1, $s3
07C4		jal sub_1878
07C8		st.32 [$sp + 0x20], $v0
07CC		sltiu $v0, $v0, 0x1

loc_7D0:
07D0		st.32 [$sp + 0x24], $v0
07D4		addi $a0, $s1, 0x306C
07D8		addi $a2, $sp, 0x28
07DC		jal sub_908
07E0		addi $a1, $sp, 0x10
07E4		addi $a0, $s4, 0x8
07E8		slt $a1, $a0, $s4
07EC		ld.32 $s1, [$sp + 0x28]
07F0		jal sub_1878
07F4		add $a1, $a1, $fp
07F8		ld.32 $a0, [$sp + 0x30]
07FC		ld.32 $a1, [$sp + 0x34]
0800		add $a2, $s1, $zero
0804		jal sub_874
0808		add $a3, $v0, $zero
080C		beq $zero, $s7, loc_83C
0810		ld.32 $ra, [$sp + 0x64]
0814		beq $zero, $s0, loc_840
0818		ld.32 $fp, [$sp + 0x60]
081C		addi $a0, $s2, 0x10
0820		slt $a1, $a0, $s2
0824		jal sub_1878
0828		add $a1, $a1, $s3
082C		add $a2, $v0, $zero
0830		add $a0, $s6, $zero
0834		jal sub_1904
0838		add $a1, $s5, $zero

loc_83C:
083C		ld.32 $ra, [$sp + 0x64]

loc_840:
0840		ld.32 $fp, [$sp + 0x60]
0844		ld.32 $s7, [$sp + 0x5C]
0848		ld.32 $s6, [$sp + 0x58]
084C		ld.32 $s5, [$sp + 0x54]
0850		ld.32 $s4, [$sp + 0x50]
0854		ld.32 $s3, [$sp + 0x4C]
0858		ld.32 $s2, [$sp + 0x48]
085C		ld.32 $s1, [$sp + 0x44]
0860		ld.32 $s0, [$sp + 0x40]
0864		addi $v0, $zero, 0x1
0868		add $v1, $zero, $zero
086C		jr $ra
0870		addi $sp, $sp, 0x68

;------- subroutine -------
sub_874:
0874		addi $sp, $sp, -0x38
0878		st.32 [$sp + 0x30], $s3
087C		add $s3, $a2, $zero
0880		addi $a2, $sp, 0x10
0884		st.32 [$sp + 0x34], $ra
0888		st.32 [$sp + 0x2C], $s2
088C		st.32 [$sp + 0x28], $s1
0890		add $s2, $a3, $zero
0894		add $s1, $a1, $zero
0898		st.32 [$sp + 0x24], $s0
089C		jal sub_5BC
08A0		add $s0, $a0, $zero
08A4		ld.32 $a0, [$sp + 0x10]
08A8		add $a2, $s3, $zero
08AC		add $a0, $s0, $a0
08B0		slt $a1, $a0, $s0
08B4		jal sub_1904
08B8		add $a1, $a1, $s1
08BC		ld.32 $a0, [$sp + 0x14]
08C0		add $a2, $s2, $zero
08C4		add $a0, $s0, $a0
08C8		slt $a1, $a0, $s0
08CC		jal sub_1904
08D0		add $a1, $a1, $s1
08D4		ld.32 $a0, [$sp + 0x18]
08D8		add $a2, $s2, $zero
08DC		add $a0, $s0, $a0
08E0		slt $a1, $a0, $s0
08E4		jal sub_1904
08E8		add $a1, $a1, $s1
08EC		ld.32 $ra, [$sp + 0x34]
08F0		ld.32 $s3, [$sp + 0x30]
08F4		ld.32 $s2, [$sp + 0x2C]
08F8		ld.32 $s1, [$sp + 0x28]
08FC		ld.32 $s0, [$sp + 0x24]
0900		jr $ra
0904		addi $sp, $sp, 0x38

;------- subroutine -------
sub_908:
0908		ld.32 $v0, [$a0 + 0x8]
090C		addi $sp, $sp, -0x60
0910		ld.32 $v1, [$a1 + 0x0]
0914		st.32 [$sp + 0x50], $s3
0918		st.32 [$sp + 0x4C], $s2
091C		st.32 [$sp + 0x5C], $ra
0920		st.32 [$sp + 0x58], $s5
0924		st.32 [$sp + 0x54], $s4
0928		st.32 [$sp + 0x48], $s1
092C		st.32 [$sp + 0x44], $s0
0930		st.32 [$a2 + 0x0], $v0
0934		addi $v0, $zero, 0xD
0938		add $s3, $a0, $zero
093C		bneq $v0, $v1, loc_968
0940		add $s2, $a1, $zero
0944		ld.32 $v0, [$a0 + 0x1DC]
0948		addi $v0, $v0, 0x1
094C		st.32 [$a0 + 0x1DC], $v0
0950		sltiu $v0, $v0, 0x4
0954		bne $zero, $v0, loc_970
0958		ld.32 $v0, [$s2 + 0x0]
095C		addi $v0, $zero, 0x804
0960		st.32 [$a0 + 0x8], $v0
0964		j loc_970

loc_968:
0968		st.8 [$a0 + 0x181], $zero
096C		st.32 [$a0 + 0x1DC], $zero

loc_970:
0970		ld.32 $v0, [$s2 + 0x0]
0974		addi $v1, $zero, 0x3C
0978		bneq $v1, $v0, loc_A88
097C		addi $v1, $zero, 0x3D
0980		ld.8 $v0, [$s3 + 0x181]
0984		beq $zero, $v0, loc_9A4
0988		ld.32 $a0, [$s2 + 0x8]
098C		addi $v0, $zero, 0x40
0990		ld.32 $a2, [$s2 + 0x8]
0994		ld.32 $a3, [$s2 + 0xC]
0998		st.32 [$sp + 0x10], $v0
099C		jal sub_1724
09A0		addi $a0, $s3, 0x44

loc_9A4:
09A4		ld.32 $a0, [$s2 + 0x8]
09A8		jal sub_18A0
09AC		ld.32 $a1, [$s2 + 0xC]
09B0		addi $v1, $zero, 0x1
09B4		beq $v1, $v0, loc_A80
09B8		addi $v1, $zero, 0x2
09BC		beq $v1, $v0, loc_A80
09C0		addi $v1, $zero, 0x3
09C4		beq $v1, $v0, loc_A80
09C8		addi $v1, $zero, 0x4
09CC		beq $v1, $v0, loc_A80
09D0		addi $v1, $zero, 0x5
09D4		beq $v1, $v0, loc_A80
09D8		addi $v1, $zero, 0x6
09DC		beq $v1, $v0, loc_A80
09E0		addi $v1, $zero, 0x7
09E4		beq $v1, $v0, loc_A80
09E8		addi $v1, $zero, 0x8
09EC		beq $v1, $v0, loc_A80
09F0		addi $v1, $zero, 0x9
09F4		beq $v1, $v0, loc_A80
09F8		addi $v1, $zero, 0xA
09FC		bneq $v1, $v0, loc_A30
0A00		addi $v1, $zero, 0x12
0A04		addi $v0, $zero, 0xA
0A08		st.32 [$s3 + 0x10], $v0
0A0C		addi $v0, $zero, 0x1
0A10		addi $a0, $s3, 0x44
0A14		st.8 [$s3 + 0x181], $v0
0A18		addi $a1, $s3, 0x34
0A1C		jal sub_1814
0A20		addi $a2, $zero, 0x10
0A24		jal sub_1710
0A28		addi $a0, $s3, 0x24
0A2C		j loc_120C

loc_A30:
0A30		ld.32 $ra, [$sp + 0x5C]
0A34		beq $v1, $v0, loc_A80
0A38		addi $v1, $zero, 0x11
0A3C		beq $v1, $v0, loc_A80
0A40		addi $v1, $zero, 0x10
0A44		bne $v1, $v0, loc_A64
0A48		addi $v1, $zero, 0xE
0A4C		addi $a0, $s3, 0x19C
0A50		jal sub_17B0
0A54		st.32 [$s3 + 0x10], $v0
0A58		ld.32 $a2, [$s2 + 0x8]
0A5C		ld.32 $a3, [$s2 + 0xC]
0A60		j loc_C34

loc_A64:
0A64		addi $a0, $zero, 0x40
0A68		beq $v1, $v0, loc_A80
0A6C		addi $v1, $zero, 0xB
0A70		beq $v1, $v0, loc_A80
0A74		addi $v1, $zero, 0xC
0A78		beq $v1, $v0, loc_A80
0A7C		xori $v1, $v0, 0xF

loc_A80:
0A80		cmov.nz $v0, $zero, $v1
0A84		j loc_1208

loc_A88:
0A88		st.32 [$s3 + 0x10], $v0
0A8C		beq $v1, $v0, loc_1204
0A90		addi $v1, $zero, 0xD
0A94		beq $v1, $v0, loc_1204
0A98		addi $v1, $zero, 0x19
0A9C		bne $v1, $v0, loc_C64
0AA0		addi $v1, $zero, 0x12
0AA4		ld.32 $s0, [$s3 + 0x10]
0AA8		addi $v0, $zero, 0x1
0AAC		bneq $v0, $s0, loc_B40
0AB0		addi $v0, $zero, 0x3
0AB4		ld.32 $v0, [$s2 + 0x10]
0AB8		sltiu $v0, $v0, 0x200
0ABC		bneq $zero, $v0, loc_B38
0AC0		addi $v0, $zero, 0x800
0AC4		ld.32 $v0, [$s2 + 0x8]
0AC8		ld.32 $a1, [$s2 + 0xC]
0ACC		addi $a0, $v0, 0x110
0AD0		slt $v0, $a0, $v0
0AD4		jal sub_18A0
0AD8		add $a1, $v0, $a1
0ADC		bneq $s0, $v0, loc_B04
0AE0		st.8 [$s3 + 0x180], $v0
0AE4		lis $v0, 0x0
0AE8		addi $v0, $v0, 0x1A24
0AEC		st.32 [$s3 + 0x174], $v0
0AF0		lis $v0, 0x0
0AF4		addi $v0, $v0, 0x19E4
0AF8		st.32 [$s3 + 0x178], $v0
0AFC		lis $v0, 0x0
0B00		j loc_B34

loc_B04:
0B04		addi $v0, $v0, 0x1A04
0B08		addi $v1, $zero, 0x3
0B0C		bneq $v1, $v0, loc_B38
0B10		addi $v0, $zero, 0x800
0B14		lis $v0, 0x0
0B18		addi $v0, $v0, 0x1A84
0B1C		st.32 [$s3 + 0x174], $v0
0B20		lis $v0, 0x0
0B24		addi $v0, $v0, 0x1A44
0B28		st.32 [$s3 + 0x178], $v0
0B2C		lis $v0, 0x0
0B30		addi $v0, $v0, 0x1A64

loc_B34:
0B34		st.32 [$s3 + 0x17C], $v0

loc_B38:
0B38		addi $v0, $zero, 0x800
0B3C		j loc_1208

loc_B40:
0B40		st.32 [$s3 + 0x8], $v0
0B44		bneq $v0, $s0, loc_B88
0B48		addi $v0, $zero, 0x5
0B4C		ld.32 $v0, [$s2 + 0x10]
0B50		sltiu $v0, $v0, 0xF0
0B54		bne $zero, $v0, loc_1208
0B58		ld.32 $ra, [$sp + 0x5C]
0B5C		jal sub_17B0
0B60		addi $a0, $s3, 0x74
0B64		ld.32 $a0, [$s2 + 0x8]
0B68		ld.32 $a3, [$s2 + 0xC]
0B6C		addi $a2, $a0, 0x130
0B70		slt $t0, $a2, $a0
0B74		addi $a0, $zero, 0x100
0B78		st.32 [$sp + 0x10], $a0
0B7C		add $a1, $v1, $zero
0B80		add $a0, $v0, $zero
0B84		j loc_CC8

loc_B88:
0B88		add $a3, $t0, $a3
0B8C		bneq $v0, $s0, loc_BDC
0B90		addi $v0, $s0, -0x6
0B94		addi $v0, $s3, 0x182
0B98		ld.32 $a0, [$s3 + 0x17C]
0B9C		lis $a1, 0x0
0BA0		lis $a2, 0x0
0BA4		st.32 [$sp + 0x10], $v0
0BA8		addi $a3, $sp, 0x20
0BAC		addi $a1, $a1, 0x26A8
0BB0		jal sub_1760
0BB4		addi $a2, $a2, 0x2714
0BB8		addi $a0, $s3, 0x24
0BBC		addi $a1, $sp, 0x20
0BC0		jal sub_1814
0BC4		addi $a2, $zero, 0x10
0BC8		addi $a0, $s3, 0x34
0BCC		addi $a1, $sp, 0x30
0BD0		jal sub_1814
0BD4		addi $a2, $zero, 0x10
0BD8		j loc_120C

loc_BDC:
0BDC		ld.32 $ra, [$sp + 0x5C]
0BE0		sltiu $v0, $v0, 0x2
0BE4		bneq $zero, $v0, loc_1204
0BE8		addi $v0, $zero, 0x8
0BEC		bneq $v0, $s0, loc_C40
0BF0		addi $v0, $zero, 0xB
0BF4		ld.32 $v0, [$s2 + 0x10]
0BF8		sltiu $v0, $v0, 0x200
0BFC		bne $zero, $v0, loc_1208
0C00		ld.32 $ra, [$sp + 0x5C]
0C04		ld.32 $a2, [$s2 + 0x8]
0C08		ld.32 $a3, [$s2 + 0xC]
0C0C		addi $v0, $zero, 0x200
0C10		st.32 [$sp + 0x10], $v0
0C14		addi $a0, $s3, 0x24
0C18		jal sub_16E8
0C1C		addi $a1, $s3, 0x34
0C20		jal sub_17B0
0C24		addi $a0, $s3, 0x54
0C28		ld.32 $a2, [$s2 + 0x8]
0C2C		ld.32 $a3, [$s2 + 0xC]
0C30		addi $a0, $zero, 0x20

loc_C34:
0C34		st.32 [$sp + 0x10], $a0
0C38		add $a1, $v1, $zero
0C3C		j loc_CC8

loc_C40:
0C40		add $a0, $v0, $zero
0C44		bneq $v0, $s0, loc_1208
0C48		ld.32 $ra, [$sp + 0x5C]
0C4C		ld.32 $v0, [$s2 + 0x10]
0C50		sltiu $v1, $v0, 0x200
0C54		bneq $zero, $v1, loc_120C
0C58		ld.32 $s5, [$sp + 0x58]
0C5C		ld.32 $a2, [$s2 + 0x8]
0C60		j loc_11FC

loc_C64:
0C64		ld.32 $a3, [$s2 + 0xC]
0C68		bneq $v1, $v0, loc_1208
0C6C		ld.32 $ra, [$sp + 0x5C]
0C70		ld.32 $s4, [$s3 + 0x10]
0C74		addi $v1, $zero, 0x2
0C78		bne $v1, $s4, loc_CD4
0C7C		addi $v1, $zero, 0x4
0C80		ld.32 $s1, [$s2 + 0x8]
0C84		ld.32 $s0, [$s2 + 0xC]
0C88		or $v0, $s1, $s0
0C8C		beq $zero, $v0, loc_EB4
0C90		addi $v0, $zero, 0x10
0C94		ld.32 $v0, [$s2 + 0x10]
0C98		sltiu $v0, $v0, 0x400
0C9C		bneq $zero, $v0, loc_EB4
0CA0		addi $v0, $zero, 0x10
0CA4		lis $a0, 0x0
0CA8		jal sub_17B0
0CAC		addi $a0, $a0, 0x22A8
0CB0		addi $a0, $zero, 0x400
0CB4		st.32 [$sp + 0x10], $a0
0CB8		add $a1, $s0, $zero
0CBC		add $a0, $s1, $zero
0CC0		add $a2, $v0, $zero
0CC4		add $a3, $v1, $zero

loc_CC8:
0CC8		jal sub_1828
0CCC		nop
0CD0		j loc_120C

loc_CD4:
0CD4		ld.32 $ra, [$sp + 0x5C]
0CD8		bneq $v1, $s4, loc_D74
0CDC		addi $v1, $zero, 0x6
0CE0		ld.32 $v0, [$s2 + 0x10]
0CE4		sltiu $v0, $v0, 0x200
0CE8		bneq $zero, $v0, loc_EB4
0CEC		addi $v0, $zero, 0x10
0CF0		lis $v0, 0x0
0CF4		ld.32 $a1, [$s2 + 0xC]
0CF8		addi $v0, $v0, 0x26A8
0CFC		ld.32 $a0, [$s2 + 0x8]
0D00		st.32 [$s3 + 0x20], $v0
0D04		addi $a2, $zero, 0xFF
0D08		jal sub_1864
0D0C		addi $a3, $zero, 0x200
0D10		ld.32 $a0, [$s3 + 0x20]
0D14		ld.32 $s0, [$s2 + 0x8]
0D18		jal sub_17B0
0D1C		ld.32 $s1, [$s2 + 0xC]
0D20		addi $a0, $zero, 0x20
0D24		st.32 [$sp + 0x10], $a0
0D28		add $a1, $s1, $zero
0D2C		add $a0, $s0, $zero
0D30		add $a2, $v0, $zero
0D34		jal sub_1828
0D38		add $a3, $v1, $zero
0D3C		lis $v0, 0x0
0D40		addi $v0, $v0, 0x1AA4
0D44		st.32 [$sp + 0x10], $v0
0D48		addi $v0, $zero, 0x3
0D4C		st.32 [$sp + 0x14], $v0
0D50		ld.32 $v0, [$s3 + 0x174]
0D54		ld.32 $a0, [$s2 + 0x8]
0D58		ld.32 $a1, [$s2 + 0xC]
0D5C		st.32 [$sp + 0x18], $v0
0D60		st.32 [$sp + 0x1C], $zero
0D64		addi $a2, $zero, 0x20
0D68		jal sub_174C
0D6C		addi $a3, $s3, 0x74
0D70		j loc_120C

loc_D74:
0D74		ld.32 $ra, [$sp + 0x5C]
0D78		bneq $v1, $s4, loc_DE4
0D7C		addi $v1, $zero, 0x9
0D80		ld.32 $v0, [$s2 + 0x10]
0D84		sltiu $v0, $v0, 0x200
0D88		bneq $zero, $v0, loc_10B4
0D8C		addi $v0, $zero, 0xC
0D90		lis $a0, 0x0
0D94		ld.32 $s0, [$s2 + 0x8]
0D98		ld.32 $s1, [$s2 + 0xC]
0D9C		jal sub_17B0
0DA0		addi $a0, $a0, 0x26F4
0DA4		addi $a0, $zero, 0x20
0DA8		st.32 [$sp + 0x10], $a0
0DAC		add $a1, $s1, $zero
0DB0		add $a0, $s0, $zero
0DB4		add $a2, $v0, $zero
0DB8		jal sub_1828
0DBC		add $a3, $v1, $zero
0DC0		ld.32 $v0, [$s2 + 0x8]
0DC4		ld.32 $a1, [$s2 + 0xC]
0DC8		addi $a0, $v0, 0x20
0DCC		slt $v0, $a0, $v0
0DD0		add $a1, $v0, $a1
0DD4		addi $a2, $zero, 0xFF
0DD8		jal sub_1864
0DDC		addi $a3, $zero, 0x1E0
0DE0		j loc_120C

loc_DE4:
0DE4		ld.32 $ra, [$sp + 0x5C]
0DE8		bneq $v1, $s4, loc_E48
0DEC		nop
0DF0		ld.32 $v0, [$s2 + 0x10]
0DF4		sltiu $v0, $v0, 0x200
0DF8		bneq $zero, $v0, loc_10FC
0DFC		addi $v0, $zero, 0xF
0E00		ld.32 $a0, [$s2 + 0x8]
0E04		ld.32 $a1, [$s2 + 0xC]
0E08		addi $a2, $zero, 0xFF
0E0C		jal sub_1864
0E10		addi $a3, $zero, 0x200
0E14		ld.32 $a2, [$s2 + 0x8]
0E18		ld.32 $a3, [$s2 + 0xC]
0E1C		addi $a0, $s3, 0x54
0E20		jal sub_1774
0E24		addi $a1, $zero, 0x20
0E28		addi $v0, $zero, 0x20
0E2C		ld.32 $a2, [$s2 + 0x8]
0E30		ld.32 $a3, [$s2 + 0xC]
0E34		st.32 [$sp + 0x10], $v0
0E38		addi $a0, $s3, 0x24
0E3C		jal sub_16FC
0E40		addi $a1, $s3, 0x34
0E44		j loc_120C

loc_E48:
0E48		ld.32 $ra, [$sp + 0x5C]
0E4C		bneq $v0, $s4, loc_EB4
0E50		addi $v0, $zero, 0x10
0E54		ld.32 $v0, [$s2 + 0x10]
0E58		sltiu $v0, $v0, 0x200
0E5C		bneq $zero, $v0, loc_1208
0E60		ld.32 $ra, [$sp + 0x5C]
0E64		ld.32 $a1, [$s2 + 0xC]
0E68		ld.32 $a0, [$s2 + 0x8]
0E6C		addi $a2, $zero, 0xFF
0E70		jal sub_1864
0E74		addi $a3, $zero, 0x200
0E78		lis $a0, 0x0
0E7C		ld.32 $s0, [$s2 + 0x8]
0E80		ld.32 $s1, [$s2 + 0xC]
0E84		jal sub_17B0
0E88		addi $a0, $a0, 0x194C
0E8C		addi $a0, $zero, 0x20
0E90		add $a2, $v0, $zero
0E94		st.32 [$sp + 0x10], $a0
0E98		add $a3, $v1, $zero
0E9C		add $a0, $s0, $zero
0EA0		jal sub_1828
0EA4		add $a1, $s1, $zero
0EA8		ld.32 $a2, [$s2 + 0x8]
0EAC		ld.32 $a3, [$s2 + 0xC]
0EB0		j loc_11FC

loc_EB4:
0EB4		addi $v0, $zero, 0x200
0EB8		bneq $v0, $s4, loc_FBC
0EBC		addi $v0, $zero, 0xE
0EC0		ld.32 $v0, [$s2 + 0x10]
0EC4		sltiu $v0, $v0, 0x200
0EC8		bneq $zero, $v0, loc_1208
0ECC		ld.32 $ra, [$sp + 0x5C]
0ED0		ld.8 $v0, [$s3 + 0x1A4]
0ED4		addi $v1, $zero, 0x28
0ED8		bneq $v1, $v0, loc_F04
0EDC		addi $v1, $zero, 0xA5
0EE0		ld.32 $a0, [$s2 + 0x8]
0EE4		ld.32 $a1, [$s2 + 0xC]
0EE8		addi $a2, $zero, 0xFF
0EEC		jal sub_1864
0EF0		addi $a3, $zero, 0x200
0EF4		lis $a0, 0x0
0EF8		ld.32 $s0, [$s2 + 0x8]
0EFC		ld.32 $s1, [$s2 + 0xC]
0F00		j loc_F34

loc_F04:
0F04		addi $a0, $a0, 0x1994
0F08		bneq $v1, $v0, loc_F5C
0F0C		addi $v1, $zero, 0x5B
0F10		ld.32 $a0, [$s2 + 0x8]
0F14		ld.32 $a1, [$s2 + 0xC]
0F18		addi $a2, $zero, 0xFF
0F1C		jal sub_1864
0F20		addi $a3, $zero, 0x200
0F24		lis $a0, 0x0
0F28		ld.32 $s0, [$s2 + 0x8]
0F2C		ld.32 $s1, [$s2 + 0xC]
0F30		addi $a0, $a0, 0x199C

loc_F34:
0F34		jal sub_17B0
0F38		nop
0F3C		addi $a0, $zero, 0x4

loc_F40:
0F40		st.32 [$sp + 0x10], $a0
0F44		add $a1, $s1, $zero
0F48		add $a0, $s0, $zero
0F4C		add $a2, $v0, $zero
0F50		jal sub_1828
0F54		add $a3, $v1, $zero
0F58		j loc_11F4

loc_F5C:
0F5C		ld.32 $a2, [$s2 + 0x8]
0F60		beq $v1, $v0, loc_F6C
0F64		addi $v1, $zero, 0x21
0F68		bne $v1, $v0, loc_11F0

loc_F6C:
0F6C		ld.32 $a2, [$s2 + 0x8]
0F70		ld.8 $v1, [$s3 + 0x1A5]
0F74		ld.8 $v0, [$s3 + 0x1A6]
0F78		shl $v1, $v1, 0x18
0F7C		shl $v0, $v0, 0x10
0F80		or $v0, $v1, $v0
0F84		ld.8 $v1, [$s3 + 0x1A8]
0F88		or $v0, $v0, $v1
0F8C		ld.8 $v1, [$s3 + 0x1A7]
0F90		shl $v1, $v1, 0x8
0F94		or $v0, $v0, $v1
0F98		jal sub_80
0F9C		st.32 [$s3 + 0x198], $v0
0FA0		ld.32 $a3, [$s2 + 0x10]
0FA4		ld.32 $a0, [$s2 + 0x8]
0FA8		ld.32 $a1, [$s2 + 0xC]
0FAC		ld.32 $a2, [$s3 + 0x198]
0FB0		jal sub_18B4
0FB4		shr $a3, $a3, 0x9
0FB8		j loc_11F4

loc_FBC:
0FBC		ld.32 $a2, [$s2 + 0x8]
0FC0		bneq $v0, $s4, loc_10B4
0FC4		addi $v0, $zero, 0xC
0FC8		ld.32 $v0, [$s2 + 0x10]
0FCC		sltiu $v0, $v0, 0x200
0FD0		bneq $zero, $v0, loc_1208
0FD4		ld.32 $ra, [$sp + 0x5C]
0FD8		jal sub_1618
0FDC		nop
0FE0		ld.32 $a0, [$s2 + 0x8]
0FE4		ld.32 $a1, [$s2 + 0xC]
0FE8		add $a2, $zero, $zero
0FEC		jal sub_18B4
0FF0		addi $a3, $zero, 0x1
0FF4		ld.32 $v0, [$s2 + 0x8]
0FF8		ld.32 $v1, [$s2 + 0xC]
0FFC		addi $a0, $v0, 0x8
1000		addi $a2, $v0, 0x100
1004		slt $a1, $a0, $v0
1008		addi $a3, $zero, 0x90
100C		slt $v0, $a2, $v0
1010		add $a1, $a1, $v1
1014		st.32 [$sp + 0x10], $a3
1018		jal sub_183C
101C		add $a3, $v0, $v1
1020		lis $a0, 0x0
1024		ld.32 $s0, [$s2 + 0x8]
1028		ld.32 $s1, [$s2 + 0xC]
102C		jal sub_17B0
1030		addi $a0, $a0, 0x19A4
1034		addi $a0, $zero, 0x8
1038		add $a3, $v1, $zero
103C		add $a1, $s1, $zero
1040		add $a2, $v0, $zero
1044		st.32 [$sp + 0x10], $a0
1048		jal sub_1828
104C		add $a0, $s0, $zero
1050		ld.32 $v0, [$s2 + 0x8]
1054		ld.32 $a1, [$s2 + 0xC]
1058		addi $a0, $v0, 0x98
105C		slt $v0, $a0, $v0
1060		add $a1, $v0, $a1
1064		add $a2, $zero, $zero
1068		jal sub_1864
106C		addi $a3, $zero, 0x70
1070		ld.32 $v0, [$s2 + 0x8]
1074		ld.32 $a1, [$s2 + 0xC]
1078		addi $a0, $v0, 0x108
107C		slt $v0, $a0, $v0
1080		add $a1, $v0, $a1
1084		addi $a2, $zero, 0xFF
1088		jal sub_1864
108C		addi $a3, $zero, 0xF8
1090		ld.32 $v0, [$s2 + 0x8]
1094		ld.32 $v1, [$s2 + 0xC]
1098		addi $s0, $v0, 0x68
109C		lis $a0, 0x0
10A0		slt $v0, $s0, $v0
10A4		addi $a0, $a0, 0x1970
10A8		jal sub_17B0
10AC		add $s1, $v0, $v1
10B0		j loc_F40

loc_10B4:
10B4		addi $a0, $zero, 0x20
10B8		bneq $v0, $s4, loc_10FC
10BC		addi $v0, $zero, 0xF
10C0		ld.32 $v0, [$s2 + 0x10]
10C4		sltiu $v0, $v0, 0x200
10C8		bneq $zero, $v0, loc_1208
10CC		ld.32 $ra, [$sp + 0x5C]
10D0		ld.32 $a0, [$s2 + 0x8]
10D4		ld.32 $a1, [$s2 + 0xC]
10D8		addi $a2, $zero, 0xFF
10DC		jal sub_1864
10E0		addi $a3, $zero, 0x200
10E4		lis $a0, 0x0
10E8		addi $a0, $a0, 0x19B0
10EC		ld.32 $s0, [$s2 + 0x8]
10F0		jal sub_17B0
10F4		ld.32 $s1, [$s2 + 0xC]
10F8		j loc_F40

loc_10FC:
10FC		addi $a0, $zero, 0x30
1100		bneq $v0, $s4, loc_1208
1104		ld.32 $ra, [$sp + 0x5C]
1108		ld.32 $v0, [$s2 + 0x10]
110C		sltiu $v0, $v0, 0x800
1110		bneq $zero, $v0, loc_120C
1114		ld.32 $s5, [$sp + 0x58]
1118		lis $s5, 0x0
111C		ld.32 $s0, [$s2 + 0x8]
1120		ld.32 $s1, [$s2 + 0xC]
1124		jal sub_17B0
1128		addi $a0, $s5, 0x1AA8
112C		addi $a0, $zero, 0x800
1130		add $a2, $v0, $zero
1134		add $a3, $v1, $zero
1138		st.32 [$sp + 0x10], $a0
113C		add $a1, $s1, $zero
1140		jal sub_1828
1144		add $a0, $s0, $zero
1148		ld.32 $v0, [$s2 + 0x8]
114C		ld.32 $a1, [$s2 + 0xC]
1150		addi $a0, $v0, 0x200
1154		slt $v0, $a0, $v0
1158		add $a1, $v0, $a1
115C		addi $a2, $zero, 0x38
1160		jal sub_18B4
1164		addi $a3, $zero, 0x1
1168		ld.32 $v0, [$s2 + 0x8]
116C		ld.32 $a3, [$s2 + 0xC]
1170		addi $a0, $v0, 0x200
1174		addi $a2, $v0, 0x201
1178		slt $a1, $a0, $v0
117C		slt $v0, $a2, $v0
1180		add $a1, $a1, $a3
1184		st.32 [$sp + 0x10], $s4
1188		jal sub_1800
118C		add $a3, $v0, $a3
1190		bneq $zero, $v0, loc_11D0
1194		ld.32 $v0, [$s2 + 0x8]
1198		ld.32 $v1, [$s2 + 0xC]
119C		addi $s0, $v0, 0x200
11A0		slt $v0, $s0, $v0
11A4		addi $a0, $s5, 0x1AA8
11A8		jal sub_17B0
11AC		add $s1, $v0, $v1
11B0		addi $a2, $v0, 0x200
11B4		addi $a0, $zero, 0x200
11B8		slt $a3, $a2, $v0
11BC		st.32 [$sp + 0x10], $a0
11C0		add $a1, $s1, $zero
11C4		add $a0, $s0, $zero
11C8		jal sub_1828
11CC		add $a3, $a3, $v1

loc_11D0:
11D0		ld.32 $v0, [$s2 + 0x8]
11D4		ld.32 $a1, [$s2 + 0xC]
11D8		addi $a0, $v0, 0x600
11DC		slt $v0, $a0, $v0
11E0		add $a1, $v0, $a1
11E4		add $a2, $zero, $zero
11E8		jal sub_1864
11EC		addi $a3, $zero, 0x200

loc_11F0:
11F0		ld.32 $a2, [$s2 + 0x8]

loc_11F4:
11F4		ld.32 $a3, [$s2 + 0xC]
11F8		ld.32 $v0, [$s2 + 0x10]

loc_11FC:
11FC		st.32 [$sp + 0x10], $v0
1200		jal sub_1724

loc_1204:
1204		addi $a0, $s3, 0x44

loc_1208:
1208		ld.32 $ra, [$sp + 0x5C]

loc_120C:
120C		ld.32 $s5, [$sp + 0x58]
1210		ld.32 $s4, [$sp + 0x54]
1214		ld.32 $s3, [$sp + 0x50]
1218		ld.32 $s2, [$sp + 0x4C]
121C		ld.32 $s1, [$sp + 0x48]
1220		ld.32 $s0, [$sp + 0x44]
1224		add $v0, $zero, $zero
1228		jr $ra
122C		addi $sp, $sp, 0x60

;------- subroutine -------
sub_1230:
1230		addi $v0, $zero, 0x804
1234		st.32 [$a0 + 0x8], $v0
1238		addi $v0, $zero, 0x1
123C		st.32 [$a0 + 0x194], $v0
1240		lis $v0, 0x0
1244		addi $v0, $v0, 0x1A84
1248		st.32 [$a0 + 0x174], $v0
124C		lis $v0, 0x0
1250		addi $v0, $v0, 0x1A44
1254		st.32 [$a0 + 0x178], $v0
1258		lis $v0, 0x0
125C		addi $v0, $v0, 0x1A64
1260		st.8 [$a0 + 0x181], $zero
1264		st.32 [$a0 + 0x1DC], $zero
1268		jr $ra
126C		st.32 [$a0 + 0x17C], $v0

;------- subroutine -------
sub_1270:
1270		addi $sp, $sp, -0x30
1274		st.32 [$sp + 0x28], $s1
1278		st.32 [$sp + 0x24], $s0
127C		st.32 [$sp + 0x2C], $ra
1280		jal sub_380
1284		add $s1, $a0, $zero
1288		bneq $zero, $v0, loc_12B8
128C		addi $s0, $zero, -0x1
1290		jal sub_4C4
1294		addi $a0, $sp, 0x10
1298		bneq $zero, $v0, loc_12A8
129C		addi $a0, $sp, 0x10
12A0		jal sub_1F4
12A4		add $a1, $s1, $zero

loc_12A8:
12A8		add $s0, $v0, $zero
12AC		jal sub_192C
12B0		addi $a0, $sp, 0x10
12B4		jal sub_1E8

loc_12B8:
12B8		nop
12BC		ld.32 $ra, [$sp + 0x2C]
12C0		add $v0, $s0, $zero
12C4		ld.32 $s1, [$sp + 0x28]
12C8		ld.32 $s0, [$sp + 0x24]
12CC		jr $ra
12D0		addi $sp, $sp, 0x30

;------- subroutine -------
sub_12D4:
12D4		addi $sp, $sp, -0x20
12D8		st.32 [$sp + 0x1C], $ra
12DC		jal sub_1788
12E0		nop
12E4		addi $a2, $v0, 0x1
12E8		add $a1, $v1, $zero
12EC		slt $a3, $a2, $v0
12F0		addi $v1, $zero, 0xFF
12F4		st.32 [$sp + 0x10], $v1
12F8		add $a0, $v0, $zero
12FC		jal sub_1800
1300		add $a3, $a3, $a1
1304		ld.32 $ra, [$sp + 0x1C]
1308		jr $ra
130C		addi $sp, $sp, 0x20

;------- subroutine -------
sub_1310:
1310		ld.32 $v0, [$a0 + 0x8]
1314		ld.32 $a1, [$a0 + 0x0]
1318		ld.32 $t0, [$a0 + 0xC]
131C		add $a1, $a1, $v0
1320		shl $v1, $a1, 0x3
1324		add $v1, $a0, $v1
1328		st.32 [$v1 + 0x18], $a2
132C		ld.32 $a2, [$sp + 0x10]
1330		addi $a1, $a1, 0x26
1334		st.32 [$v1 + 0x1C], $a3
1338		st.32 [$v1 + 0x58], $a2
133C		st.32 [$v1 + 0x5C], $zero
1340		shl $a1, $a1, 0x2
1344		ld.32 $v1, [$sp + 0x14]
1348		add $a1, $a0, $a1
134C		st.32 [$a1 + 0x0], $v1
1350		addi $v1, $v0, 0x1
1354		slt $v0, $v1, $v0
1358		add $t0, $v0, $t0
135C		st.32 [$a0 + 0x8], $v1
1360		jr $ra
1364		st.32 [$a0 + 0xC], $t0

;------- subroutine -------
sub_1368:
1368		add $a1, $zero, $zero
136C		j loc_1850
1370		addi $a2, $zero, 0x1B0

;------- subroutine -------
sub_1374:
1374		addi $v0, $zero, 0x1
1378		jr $ra
137C		st.8 [$a0 + 0x150], $v0

;------- subroutine -------
sub_1380:
1380		j loc_1738
1384		nop

;------- subroutine -------
sub_1388:
1388		addi $sp, $sp, -0x20
138C		st.32 [$sp + 0x18], $s0
1390		add $s0, $a0, $zero
1394		add $a0, $a2, $zero
1398		st.32 [$sp + 0x1C], $ra
139C		jal sub_17B0
13A0		st.32 [$sp + 0x10], $a1
13A4		ld.32 $a1, [$sp + 0x10]
13A8		ld.32 $ra, [$sp + 0x1C]
13AC		add $a0, $s0, $zero
13B0		ld.32 $s0, [$sp + 0x18]
13B4		add $a2, $v0, $zero
13B8		add $a3, $v1, $zero
13BC		j loc_1774
13C0		addi $sp, $sp, 0x20

;------- subroutine -------
sub_13C4:
13C4		addi $sp, $sp, -0x138
13C8		add $v0, $a0, $zero
13CC		addi $a0, $sp, 0x10
13D0		st.32 [$sp + 0x130], $s0
13D4		addi $a2, $zero, 0x100
13D8		add $s0, $a1, $zero
13DC		st.32 [$sp + 0x134], $ra
13E0		jal sub_1488
13E4		add $a1, $v0, $zero
13E8		lis $a1, 0x0
13EC		lis $a2, 0x0
13F0		addi $a0, $sp, 0x10
13F4		addi $a1, $a1, 0x2738
13F8		addi $a2, $a2, 0x2734
13FC		jal sub_1380
1400		addi $a3, $zero, 0x3
1404		add $a0, $s0, $zero
1408		addi $a1, $zero, 0x10
140C		jal sub_1388
1410		addi $a2, $sp, 0x110
1414		ld.8 $v0, [$sp + 0x10]
1418		bneq $zero, $v0, loc_1468
141C		ld.8 $v1, [$sp + 0x11]
1420		addi $v0, $zero, 0x1
1424		bneq $v0, $v1, loc_1468
1428		ld.8 $v0, [$sp + 0xEF]
142C		bneq $zero, $v0, loc_1468
1430		addi $v0, $sp, 0x12
1434		addi $v1, $sp, 0xEF
1438		addi $a0, $zero, 0xFF

loc_143C:
143C		ld.8 $a1, [$v0 + 0x0]
1440		bneq $a0, $a1, loc_1468
1444		addi $v0, $v0, 0x1
1448		bne $v1, $v0, loc_143C
144C		ld.8 $a1, [$v0 + 0x0]
1450		addi $a0, $sp, 0xF0
1454		addi $a1, $sp, 0x110
1458		jal sub_1480
145C		addi $a2, $zero, 0x20
1460		slt $v0, $zero, $v0
1464		j loc_1470

loc_1468:
1468		sub $v0, $zero, $v0
146C		addi $v0, $zero, -0x1

loc_1470:
1470		ld.32 $ra, [$sp + 0x134]
1474		ld.32 $s0, [$sp + 0x130]
1478		jr $ra
147C		addi $sp, $sp, 0x138

;------- subroutine -------
sub_1480:
1480		j loc_17EC
1484		nop

;------- subroutine -------
sub_1488:
1488		addi $sp, $sp, -0x18
148C		st.32 [$sp + 0x14], $ra
1490		st.32 [$sp + 0x10], $s0
1494		jal sub_1814
1498		add $s0, $a0, $zero
149C		ld.32 $ra, [$sp + 0x14]
14A0		add $v0, $s0, $zero
14A4		ld.32 $s0, [$sp + 0x10]
14A8		jr $ra
14AC		addi $sp, $sp, 0x18

;------- subroutine -------
sub_14B0:
14B0		addi $sp, $sp, -0x40
14B4		st.32 [$sp + 0x28], $s2
14B8		add $s2, $a0, $zero
14BC		st.32 [$sp + 0x3C], $ra
14C0		st.32 [$sp + 0x38], $s6
14C4		st.32 [$sp + 0x34], $s5
14C8		st.32 [$sp + 0x30], $s4
14CC		st.32 [$sp + 0x2C], $s3
14D0		st.32 [$sp + 0x24], $s1
14D4		add $s3, $a1, $zero
14D8		jal sub_188C
14DC		st.32 [$sp + 0x20], $s0
14E0		addi $a0, $s2, 0x8
14E4		slt $a1, $a0, $s2
14E8		add $a1, $a1, $s3
14EC		add $s6, $v0, $zero
14F0		jal sub_188C
14F4		add $s5, $v1, $zero
14F8		addi $a0, $s2, 0x14
14FC		slt $a1, $a0, $s2
1500		add $a1, $a1, $s3
1504		add $s1, $v1, $zero
1508		jal sub_1878
150C		add $s0, $v0, $zero
1510		addi $a0, $s2, 0x10
1514		slt $a1, $a0, $s2
1518		add $a1, $a1, $s3
151C		jal sub_1878
1520		add $s4, $v0, $zero
1524		add $s2, $v0, $zero
1528		addi $v0, $zero, 0x33
152C		bneq $v0, $s6, loc_15F0
1530		ld.32 $ra, [$sp + 0x3C]
1534		lis $v0, 0x100
1538		bne $v0, $s5, loc_15F4
153C		ld.32 $s6, [$sp + 0x38]
1540		addi $v0, $zero, 0x1
1544		bne $v0, $s4, loc_15F4
1548		ld.32 $s6, [$sp + 0x38]
154C		jal sub_12D4
1550		nop
1554		beq $zero, $v0, loc_15F0
1558		ld.32 $ra, [$sp + 0x3C]
155C		lis $v0, 0x0
1560		addi $v0, $v0, 0x26CC
1564		st.32 [$sp + 0x10], $v0
1568		addi $v0, $zero, 0xA
156C		st.32 [$sp + 0x14], $v0
1570		lis $v0, 0x0
1574		addi $v0, $v0, 0x26C8
1578		add $a0, $s0, $zero
157C		add $a1, $s1, $zero
1580		st.32 [$sp + 0x18], $v0
1584		st.32 [$sp + 0x1C], $s4
1588		add $a2, $s2, $zero
158C		jal sub_18C
1590		add $a3, $zero, $zero
1594		add $s0, $v0, $zero
1598		or $v0, $v0, $v1
159C		beq $zero, $v0, loc_15EC
15A0		add $s1, $v1, $zero
15A4		add $a0, $s0, $zero
15A8		add $a1, $v1, $zero
15AC		jal sub_1904
15B0		lis $a2, 0xD280
15B4		addi $a0, $s0, 0x4
15B8		slt $a1, $a0, $s0
15BC		ld.32 $ra, [$sp + 0x3C]
15C0		ld.32 $s6, [$sp + 0x38]
15C4		ld.32 $s5, [$sp + 0x34]
15C8		ld.32 $s4, [$sp + 0x30]
15CC		ld.32 $s3, [$sp + 0x2C]
15D0		ld.32 $s2, [$sp + 0x28]
15D4		ld.32 $s0, [$sp + 0x20]
15D8		add $a1, $a1, $s1
15DC		lis $a2, 0xD65F
15E0		ld.32 $s1, [$sp + 0x24]
15E4		addi $a2, $a2, 0x3C0
15E8		j loc_1904

loc_15EC:
15EC		addi $sp, $sp, 0x40

loc_15F0:
15F0		ld.32 $ra, [$sp + 0x3C]

loc_15F4:
15F4		ld.32 $s6, [$sp + 0x38]
15F8		ld.32 $s5, [$sp + 0x34]
15FC		ld.32 $s4, [$sp + 0x30]
1600		ld.32 $s3, [$sp + 0x2C]
1604		ld.32 $s2, [$sp + 0x28]
1608		ld.32 $s1, [$sp + 0x24]
160C		ld.32 $s0, [$sp + 0x20]
1610		jr $ra
1614		addi $sp, $sp, 0x40

;------- subroutine -------
sub_1618:
1618		addi $sp, $sp, -0x28
161C		st.32 [$sp + 0x18], $s1
1620		lis $s1, 0x0
1624		st.32 [$sp + 0x14], $s0
1628		addi $a0, $s1, 0x0
162C		lis $v0, 0x0
1630		lis $s0, 0x0
1634		st.32 [$sp + 0x24], $ra
1638		st.32 [$sp + 0x20], $s3
163C		st.32 [$sp + 0x1C], $s2
1640		st.32 [$v0 + 0x2844], $zero
1644		jal sub_17B0
1648		ld.32 $s2, [$s0 + 0x2848]
164C		lis $a2, 0x0
1650		addi $s1, $s1, 0x0
1654		addi $a2, $a2, 0x283C
1658		sub $a2, $a2, $s1
165C		add $a0, $v0, $zero
1660		add $a1, $v1, $zero
1664		jal sub_16D4
1668		addi $s0, $s0, 0x2848
166C		ld.32 $a2, [$s0 + 0x8]
1670		add $s3, $v0, $zero
1674		lis $a0, 0xD000
1678		addi $a1, $zero, -0x1
167C		jal sub_16D4
1680		ld.32 $s1, [$s0 + 0x4]
1684		bne $s3, $s2, loc_1690
1688		lis $v0, 0x0
168C		beq $v0, $s1, loc_16A0

loc_1690:
1690		lis $v0, 0x0
1694		addi $v1, $zero, 0x1
1698		st.32 [$v0 + 0x305C], $v1
169C		lis $v0, 0x0

loc_16A0:
16A0		st.32 [$v0 + 0x3058], $zero
16A4		ld.32 $ra, [$sp + 0x24]
16A8		ld.32 $s3, [$sp + 0x20]
16AC		ld.32 $s2, [$sp + 0x1C]
16B0		ld.32 $s1, [$sp + 0x18]
16B4		ld.32 $s0, [$sp + 0x14]
16B8		jr $ra
16BC		addi $sp, $sp, 0x28

;------- subroutine -------
sub_16C0:
16C0		lis $v0, 0x2F36
16C4		ori $v0, $v0, 0x5F20; = 0x2F365F20 - host_search_pattern
16C8		host_call
16CC		jr $ra
16D0		nop

;------- subroutine -------
sub_16D4:
16D4		lis $v0, 0x8E94
16D8		ori $v0, $v0, 0x3DA2; = 0x8E943DA2 - host_crc32 (ptr r4r5, len r6)
16DC		host_call
16E0		jr $ra
16E4		nop

;------- subroutine -------
sub_16E8:
16E8		lis $v0, 0xB68E
16EC		ori $v0, $v0, 0xA896; = 0xB68EA896 - host_aes_dec_cbc
16F0		host_call
16F4		jr $ra
16F8		nop

;------- subroutine -------
sub_16FC:
16FC		lis $v0, 0xFB19
1700		ori $v0, $v0, 0x8D4C; = 0xFB198D4C - host_aes_enc_cbc
1704		host_call
1708		jr $ra
170C		nop

;------- subroutine -------
sub_1710:
1710		lis $v0, 0x5BEC
1714		ori $v0, $v0, 0xE776; = 0x5BECE776 - host_aes_set_key (ptr r4)
1718		host_call
171C		jr $ra
1720		nop

;------- subroutine -------
sub_1724:
1724		lis $v0, 0x4691
1728		ori $v0, $v0, 0x5487; = 0x46915487 - host_aes_ctr
172C		host_call
1730		jr $ra
1734		nop

loc_1738:
1738		lis $v0, 0xD4AC
173C		ori $v0, $v0, 0x6D16; = 0xD4AC6D16 - host_expmod (dst r4, mod r5, exp r6, exp_size r7)
1740		host_call
1744		jr $ra
1748		nop

;------- subroutine -------
sub_174C:
174C		lis $v0, 0x93F2
1750		ori $v0, $v0, 0x3757; = 0x93F23757 - host_rsa_oaep
1754		host_call
1758		jr $ra
175C		nop

;------- subroutine -------
sub_1760:
1760		lis $v0, 0x8CC2
1764		ori $v0, $v0, 0xD88C; = 0x8CC2D88C - host_sha2_hmac
1768		host_call
176C		jr $ra
1770		nop

;------- subroutine -------
sub_1774:
1774		lis $v0, 0x5045
1778		ori $v0, $v0, 0x611F; = 0x5045611F - host_sha2 (ptr r4, len r5, dst ptr r6r7)
177C		host_call
1780		jr $ra
1784		nop

;------- subroutine -------
sub_1788:
1788		lis $v0, 0x9D10
178C		ori $v0, $v0, 0x4BEC; = 0x9D104BEC - host_get_license_buf
1790		host_call
1794		jr $ra
1798		nop

;------- subroutine -------
sub_179C:
179C		lis $v0, 0x42D3
17A0		ori $v0, $v0, 0x5BC8; = 0x42D35BC8 - host_get_field_98
17A4		host_call
17A8		jr $ra
17AC		nop

;------- subroutine -------
sub_17B0:
17B0		lis $v0, 0x4F56
17B4		ori $v0, $v0, 0xCFC3; = 0x4F56CFC3 - host_vm_get_ptr
17B8		host_call
17BC		jr $ra
17C0		nop

;------- subroutine -------
sub_17C4:
17C4		lis $v0, 0x308E
17C8		ori $v0, $v0, 0xBEA4; = 0x308EBEA4 - host_get_ipc_result
17CC		host_call
17D0		jr $ra
17D4		nop

;------- subroutine -------
sub_17D8:
17D8		lis $v0, 0x2408
17DC		ori $v0, $v0, 0x3A54; = 0x24083A54 - host_parse_ipc_cmd
17E0		host_call
17E4		jr $ra
17E8		nop

loc_17EC:
17EC		lis $v0, 0x3764
17F0		ori $v0, $v0, 0x6C3F; = 0x37646C3F - host_vm_memcmp
17F4		host_call
17F8		jr $ra
17FC		nop

;------- subroutine -------
sub_1800:
1800		lis $v0, 0xBA4F
1804		ori $v0, $v0, 0xC26A; = 0xBA4FC26A - host_memcmp (ptr1 r4r5, ptr2 r6r7, len stk4)
1808		host_call
180C		jr $ra
1810		nop

;------- subroutine -------
sub_1814:
1814		lis $v0, 0x2E3D
1818		ori $v0, $v0, 0xB2AB; = 0x2E3DB2AB - host_vm_memcpy (dst r4, src r5, size r6)
181C		host_call
1820		jr $ra
1824		nop

;------- subroutine -------
sub_1828:
1828		lis $v0, 0x418B
182C		ori $v0, $v0, 0x8052; = 0x418B8052 - host_memcpy
1830		host_call
1834		jr $ra
1838		nop

;------- subroutine -------
sub_183C:
183C		lis $v0, 0xC2A2
1840		ori $v0, $v0, 0x4132; = 0xC2A24132 - host_memcpy
1844		host_call
1848		jr $ra
184C		nop

loc_1850:
1850		lis $v0, 0x80A6
1854		ori $v0, $v0, 0x7D6D; = 0x80A67D6D - host_vm_memset
1858		host_call
185C		jr $ra
1860		nop

;------- subroutine -------
sub_1864:
1864		lis $v0, 0xE02C
1868		ori $v0, $v0, 0xE3F9; = 0xE02CE3F9 - host_memset
186C		host_call
1870		jr $ra
1874		nop

;------- subroutine -------
sub_1878:
1878		lis $v0, 0x6804
187C		ori $v0, $v0, 0x19E7; = 0x680419E7 - host_read_u32
1880		host_call
1884		jr $ra
1888		nop

;------- subroutine -------
sub_188C:
188C		lis $v0, 0x8720
1890		ori $v0, $v0, 0x5A64; = 0x87205A64 - host_read_u64 (r2r3 = *r4r5)
1894		host_call
1898		jr $ra
189C		nop

;------- subroutine -------
sub_18A0:
18A0		lis $v0, 0x9D06
18A4		ori $v0, $v0, 0x3E97; = 0x9D063E97 - host_read_u8
18A8		host_call
18AC		jr $ra
18B0		nop

;------- subroutine -------
sub_18B4:
18B4		lis $v0, 0x9BE8
18B8		ori $v0, $v0, 0xBFCA; = 0x9BE8BFCA - host_fat_open_file
18BC		host_call
18C0		jr $ra
18C4		nop

loc_18C8:
18C8		lis $v0, 0x66E9
18CC		ori $v0, $v0, 0xBFF7; = 0x66E9BFF7 - host_ipc_handle
18D0		host_call
18D4		jr $ra
18D8		nop

;------- subroutine -------
sub_18DC:
18DC		lis $v0, 0x5CC2
18E0		ori $v0, $v0, 0x894D; = 0x5CC2894D - host_svcSendSyncRequest
18E4		host_call
18E8		jr $ra
18EC		nop

;------- subroutine -------
sub_18F0:
18F0		lis $v0, 0x63F3
18F4		ori $v0, $v0, 0xD563; = 0x63F3D563 - host_connect_to_service
18F8		host_call
18FC		jr $ra
1900		nop

;------- subroutine -------
sub_1904:
1904		lis $v0, 0x7075
1908		ori $v0, $v0, 0x7343; = 0x70757343 - host_write_u32
190C		host_call
1910		jr $ra
1914		nop

;------- subroutine -------
sub_1918:
1918		lis $v0, 0x6445
191C		ori $v0, $v0, 0xC898; = 0x6445C898 - host_write_u64 (*r4r5 = r6r7)
1920		host_call
1924		jr $ra
1928		nop

;------- subroutine -------
sub_192C:
192C		j loc_18C8
1930		nop

;------- subroutine -------
sub_1934:
1934		addi $v0, $zero, 0x1
1938		st.32 [$a0 + 0x8], $v0
193C		addi $v0, $zero, -0x1
1940		st.32 [$a0 + 0x0], $a1
1944		jr $ra
1948		st.32 [$a0 + 0x4], $v0
