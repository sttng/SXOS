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
0050		jal sub_688
0054		nop
0058		j loc_74

loc_5C:
005C		ld.32 $ra, [$sp + 0x14]
0060		bneq $v0, $a2, loc_70
0064		ld.32 $ra, [$sp + 0x14]
0068		jal sub_168C
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
0088		ld.32 $v1, [$v0 + 0x2F24]
008C		st.32 [$sp + 0x134], $s0
0090		addi $s0, $zero, 0x1
0094		st.32 [$sp + 0x13C], $ra
0098		beq $s0, $v1, loc_110
009C		st.32 [$sp + 0x138], $s1
00A0		addi $a0, $sp, 0x118
00A4		jal sub_144C
00A8		add $s1, $v0, $zero
00AC		bneq $zero, $v0, loc_100
00B0		nop
00B4		jal sub_1D38
00B8		addi $a0, $sp, 0x18
00BC		st.32 [$sp + 0x128], $v0
00C0		jal sub_1D10
00C4		st.32 [$sp + 0x12C], $v1
00C8		addi $a2, $zero, 0x100
00CC		ld.32 $a0, [$sp + 0x128]
00D0		ld.32 $a1, [$sp + 0x12C]
00D4		st.32 [$sp + 0x10], $a2
00D8		add $a3, $v1, $zero
00DC		jal sub_1DB0
00E0		add $a2, $v0, $zero
00E4		addi $a0, $sp, 0x18
00E8		jal sub_15A0
00EC		addi $a1, $sp, 0x118
00F0		beq $zero, $v0, loc_100
00F4		lis $v0, 0x0
00F8		st.32 [$v0 + 0x373C], $s0
00FC		lis $v0, 0x0

loc_100:
0100		st.32 [$v0 + 0x3738], $zero
0104		jal sub_128
0108		nop
010C		addi $v0, $zero, 0x1

loc_110:
0110		st.32 [$s1 + 0x2F24], $v0
0114		ld.32 $ra, [$sp + 0x13C]
0118		ld.32 $s1, [$sp + 0x138]
011C		ld.32 $s0, [$sp + 0x134]
0120		jr $ra
0124		addi $sp, $sp, 0x140

;------- subroutine -------
sub_128:
0128		addi $sp, $sp, -0x18
012C		st.32 [$sp + 0x14], $ra
0130		jal sub_1D10
0134		nop
0138		add $a1, $v1, $zero
013C		add $a0, $v0, $zero
0140		jal sub_1C48
0144		addi $a2, $zero, 0x100
0148		lis $v1, 0x0
014C		ld.32 $a2, [$v1 + 0x2F20]
0150		addi $a0, $zero, 0x1
0154		bneq $a0, $a2, loc_174
0158		lis $a1, 0x0
015C		ld.32 $v1, [$a1 + 0x3734]
0160		beq $v0, $v1, loc_17C
0164		lis $v0, 0x0
0168		st.32 [$v0 + 0x373C], $a2
016C		lis $v0, 0x0
0170		j loc_180

loc_174:
0174		st.32 [$v0 + 0x3738], $zero
0178		st.32 [$a1 + 0x3734], $v0

loc_17C:
017C		st.32 [$v1 + 0x2F20], $a0

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
01A4		jal sub_1D38
01A8		st.32 [$sp + 0x1C], $a3
01AC		st.32 [$sp + 0x20], $v0
01B0		ld.32 $a0, [$sp + 0x60]
01B4		ld.32 $v0, [$sp + 0x5C]
01B8		st.32 [$sp + 0x24], $v1
01BC		jal sub_1D38
01C0		st.32 [$sp + 0x28], $v0
01C4		st.32 [$sp + 0x30], $v0
01C8		ld.32 $v0, [$sp + 0x64]
01CC		addi $a0, $sp, 0x10
01D0		st.32 [$sp + 0x34], $v1
01D4		jal sub_1C20
01D8		st.32 [$sp + 0x38], $v0
01DC		ld.32 $ra, [$sp + 0x44]
01E0		jr $ra
01E4		addi $sp, $sp, 0x48

;------- subroutine -------
sub_1E8:
01E8		addi $sp, $sp, -0x48
01EC		st.32 [$sp + 0x10], $a0
01F0		ld.32 $a0, [$sp + 0x58]
01F4		st.32 [$sp + 0x44], $ra
01F8		st.32 [$sp + 0x14], $a1
01FC		st.32 [$sp + 0x18], $a2
0200		jal sub_1D38
0204		st.32 [$sp + 0x1C], $a3
0208		st.32 [$sp + 0x20], $v0
020C		ld.32 $a0, [$sp + 0x60]
0210		ld.32 $v0, [$sp + 0x5C]
0214		st.32 [$sp + 0x24], $v1
0218		jal sub_1D38
021C		st.32 [$sp + 0x28], $v0
0220		st.32 [$sp + 0x30], $v0
0224		ld.32 $v0, [$sp + 0x64]
0228		addi $a0, $sp, 0x10
022C		st.32 [$sp + 0x34], $v1
0230		jal sub_1C34
0234		st.32 [$sp + 0x38], $v0
0238		ld.32 $ra, [$sp + 0x44]
023C		jr $ra
0240		addi $sp, $sp, 0x48

;------- subroutine -------
sub_244:
0244		lis $a0, 0x0
0248		j loc_1E50
024C		addi $a0, $a0, 0x3740

;------- subroutine -------
sub_250:
0250		addi $sp, $sp, -0x40
0254		st.32 [$sp + 0x3C], $ra
0258		st.32 [$sp + 0x38], $fp
025C		st.32 [$sp + 0x30], $s6
0260		st.32 [$sp + 0x2C], $s5
0264		st.32 [$sp + 0x24], $s3
0268		st.32 [$sp + 0x20], $s2
026C		st.32 [$sp + 0x1C], $s1
0270		st.32 [$sp + 0x18], $s0
0274		add $fp, $sp, $zero
0278		st.32 [$sp + 0x34], $s7
027C		st.32 [$sp + 0x28], $s4
0280		addi $sp, $sp, -0x3E0
0284		addi $s3, $sp, 0x27
0288		shr $s3, $s3, 0x4
028C		shl $s3, $s3, 0x4
0290		addi $s0, $s3, 0x220
0294		add $s6, $a0, $zero
0298		add $a0, $s0, $zero
029C		jal sub_1544
02A0		add $s5, $a1, $zero
02A4		jal sub_1D24
02A8		nop
02AC		add $s1, $v1, $zero
02B0		or $v1, $v0, $v1
02B4		add $s2, $v0, $zero
02B8		beq $zero, $v1, loc_3A4
02BC		addi $v0, $zero, 0x666
02C0		add $a1, $s1, $zero
02C4		add $a0, $s2, $zero
02C8		add $a2, $zero, $zero
02CC		addi $a3, $zero, 0x10
02D0		jal sub_1DEC
02D4		addi $s4, $zero, 0x10
02D8		add $a0, $s0, $zero
02DC		add $a2, $s2, $zero
02E0		add $a3, $s1, $zero
02E4		st.32 [$sp + 0x10], $s4
02E8		jal sub_14EC
02EC		st.32 [$sp + 0x14], $zero
02F0		add $a0, $s0, $zero
02F4		jal sub_1D60
02F8		addi $a1, $zero, 0x18
02FC		lis $a2, 0x4943
0300		add $s0, $v0, $zero
0304		add $a0, $v0, $zero
0308		add $a1, $v1, $zero
030C		ori $a2, $a2, 0x4653; = 0x49434653
0310		add $a3, $zero, $zero
0314		jal sub_1EA0
0318		add $s7, $v1, $zero
031C		addi $a0, $s0, 0x8
0320		slt $a1, $a0, $s0
0324		add $a1, $a1, $s7
0328		addi $a2, $zero, 0x64
032C		jal sub_1EA0
0330		add $a3, $zero, $zero
0334		addi $a0, $s0, 0x10
0338		slt $a1, $a0, $s0
033C		add $a1, $a1, $s7
0340		addi $a2, $zero, 0x10
0344		jal sub_1EA0
0348		add $a3, $zero, $zero
034C		jal sub_1E64
0350		add $a0, $s6, $zero
0354		bne $zero, $v0, loc_3A8
0358		add $sp, $fp, $zero
035C		jal sub_1D4C
0360		add $a0, $s3, $zero
0364		ld.32 $v0, [$s3 + 0x208]
0368		ld.32 $a1, [$s3 + 0x20C]
036C		addi $a0, $v0, 0x8
0370		slt $v0, $a0, $v0
0374		jal sub_1E14
0378		add $a1, $v0, $a1
037C		bneq $zero, $v0, loc_3A0
0380		add $s0, $v0, $zero
0384		jal sub_1D38
0388		add $a0, $s5, $zero
038C		add $a0, $v0, $zero
0390		st.32 [$sp + 0x10], $s4
0394		add $a1, $v1, $zero
0398		add $a2, $s2, $zero
039C		jal sub_1DB0

loc_3A0:
03A0		add $a3, $s1, $zero

loc_3A4:
03A4		add $v0, $s0, $zero

loc_3A8:
03A8		add $sp, $fp, $zero
03AC		ld.32 $ra, [$sp + 0x3C]
03B0		ld.32 $fp, [$sp + 0x38]
03B4		ld.32 $s7, [$sp + 0x34]
03B8		ld.32 $s6, [$sp + 0x30]
03BC		ld.32 $s5, [$sp + 0x2C]
03C0		ld.32 $s4, [$sp + 0x28]
03C4		ld.32 $s3, [$sp + 0x24]
03C8		ld.32 $s2, [$sp + 0x20]
03CC		ld.32 $s1, [$sp + 0x1C]
03D0		ld.32 $s0, [$sp + 0x18]
03D4		jr $ra
03D8		addi $sp, $sp, 0x40

;------- subroutine -------
sub_3DC:
03DC		addi $sp, $sp, -0x30
03E0		addi $v0, $zero, 0x66
03E4		st.32 [$sp + 0x28], $fp
03E8		add $fp, $sp, $zero
03EC		st.32 [$sp + 0x24], $s3
03F0		st.32 [$sp + 0x1C], $s1
03F4		st.32 [$sp + 0x2C], $ra
03F8		st.32 [$sp + 0x20], $s2
03FC		st.32 [$sp + 0x18], $s0
0400		st.8 [$fp + 0x10], $v0
0404		addi $sp, $sp, -0x3E0
0408		addi $v0, $zero, 0x73
040C		addi $v1, $zero, 0x70
0410		addi $s1, $sp, 0x1F
0414		st.8 [$fp + 0x11], $v0
0418		st.8 [$fp + 0x14], $v0
041C		lis $s3, 0x0
0420		addi $v0, $zero, 0x72
0424		shr $s1, $s1, 0x4
0428		st.8 [$fp + 0x12], $v1
042C		st.8 [$fp + 0x15], $v0
0430		addi $v1, $zero, 0x2D
0434		addi $v0, $zero, 0x76
0438		addi $a0, $s3, 0x3740
043C		addi $a1, $fp, 0x10
0440		shl $s1, $s1, 0x4
0444		st.8 [$fp + 0x13], $v1
0448		st.8 [$fp + 0x16], $v0
044C		jal sub_1E78
0450		st.8 [$fp + 0x17], $zero
0454		bne $zero, $v0, loc_4FC
0458		add $sp, $fp, $zero
045C		addi $s0, $s1, 0x220
0460		jal sub_1544
0464		add $a0, $s0, $zero
0468		jal sub_1550
046C		add $a0, $s0, $zero
0470		add $a0, $s0, $zero
0474		jal sub_1D60
0478		addi $a1, $zero, 0x18
047C		lis $a2, 0x4943
0480		add $s0, $v0, $zero
0484		add $a0, $v0, $zero
0488		add $a1, $v1, $zero
048C		ori $a2, $a2, 0x4653; = 0x49434653
0490		add $a3, $zero, $zero
0494		jal sub_1EA0
0498		add $s2, $v1, $zero
049C		addi $a0, $s0, 0x8
04A0		slt $a1, $a0, $s0
04A4		add $a1, $a1, $s2
04A8		addi $a2, $zero, 0x1
04AC		jal sub_1EA0
04B0		add $a3, $zero, $zero
04B4		addi $a0, $s0, 0x10
04B8		slt $a1, $a0, $s0
04BC		add $a1, $a1, $s2
04C0		add $a2, $zero, $zero
04C4		jal sub_1EA0
04C8		add $a3, $zero, $zero
04CC		jal sub_1E64
04D0		addi $a0, $s3, 0x3740
04D4		bne $zero, $v0, loc_4FC
04D8		add $sp, $fp, $zero
04DC		jal sub_1D4C
04E0		add $a0, $s1, $zero
04E4		ld.32 $v0, [$s1 + 0x208]
04E8		ld.32 $a1, [$s1 + 0x20C]
04EC		addi $a0, $v0, 0x8
04F0		slt $v0, $a0, $v0
04F4		jal sub_1E14
04F8		add $a1, $v0, $a1

loc_4FC:
04FC		add $sp, $fp, $zero
0500		ld.32 $ra, [$sp + 0x2C]
0504		ld.32 $fp, [$sp + 0x28]
0508		ld.32 $s3, [$sp + 0x24]
050C		ld.32 $s2, [$sp + 0x20]
0510		ld.32 $s1, [$sp + 0x1C]
0514		ld.32 $s0, [$sp + 0x18]
0518		jr $ra
051C		addi $sp, $sp, 0x30

;------- subroutine -------
sub_520:
0520		addi $sp, $sp, -0x30
0524		st.32 [$sp + 0x2C], $ra
0528		st.32 [$sp + 0x28], $fp
052C		st.32 [$sp + 0x24], $s3
0530		add $fp, $sp, $zero
0534		st.32 [$sp + 0x20], $s2
0538		st.32 [$sp + 0x1C], $s1
053C		st.32 [$sp + 0x18], $s0
0540		addi $sp, $sp, -0x3E0
0544		addi $s0, $sp, 0x1F
0548		shr $s0, $s0, 0x4
054C		shl $s0, $s0, 0x4
0550		addi $s1, $s0, 0x220
0554		add $s3, $a0, $zero
0558		jal sub_1544
055C		add $a0, $s1, $zero
0560		add $a0, $s1, $zero
0564		jal sub_1D60
0568		addi $a1, $zero, 0x10
056C		lis $a2, 0x4943
0570		add $s1, $v0, $zero
0574		add $a0, $v0, $zero
0578		add $a1, $v1, $zero
057C		ori $a2, $a2, 0x4653; = 0x49434653
0580		add $a3, $zero, $zero
0584		jal sub_1EA0
0588		add $s2, $v1, $zero
058C		addi $a0, $s1, 0x8
0590		slt $a1, $a0, $s1
0594		add $a1, $a1, $s2
0598		addi $a2, $zero, 0x190
059C		jal sub_1EA0
05A0		add $a3, $zero, $zero
05A4		lis $a0, 0x0
05A8		jal sub_1E64
05AC		addi $a0, $a0, 0x3740
05B0		bne $zero, $v0, loc_5F4
05B4		add $sp, $fp, $zero
05B8		jal sub_1D4C
05BC		add $a0, $s0, $zero
05C0		ld.32 $v1, [$s0 + 0x208]
05C4		ld.32 $a1, [$s0 + 0x20C]
05C8		addi $a0, $v1, 0x8
05CC		slt $v1, $a0, $v1
05D0		jal sub_1E14
05D4		add $a1, $v1, $a1
05D8		bne $zero, $v0, loc_5F4
05DC		add $sp, $fp, $zero
05E0		ld.32 $a1, [$s0 + 0x18]
05E4		add $a0, $s3, $zero
05E8		jal sub_1EBC
05EC		st.32 [$fp + 0x10], $v0
05F0		ld.32 $v0, [$fp + 0x10]

loc_5F4:
05F4		add $sp, $fp, $zero
05F8		ld.32 $ra, [$sp + 0x2C]
05FC		ld.32 $fp, [$sp + 0x28]
0600		ld.32 $s3, [$sp + 0x24]
0604		ld.32 $s2, [$sp + 0x20]
0608		ld.32 $s1, [$sp + 0x1C]
060C		ld.32 $s0, [$sp + 0x18]
0610		jr $ra
0614		addi $sp, $sp, 0x30

;------- subroutine -------
sub_618:
0618		addi $v0, $a0, 0x124
061C		slt $v1, $v0, $a0
0620		addi $sp, $sp, -0x18
0624		add $a1, $v1, $a1
0628		add $a0, $v0, $zero
062C		st.32 [$sp + 0x10], $s0
0630		st.32 [$sp + 0x14], $ra
0634		jal sub_1E00
0638		add $s0, $a2, $zero
063C		lis $v1, 0x1
0640		ori $v1, $v1, 0x8600; = 0x18600
0644		bne $v1, $v0, loc_660
0648		addi $v0, $zero, 0x12C
064C		addi $v0, $zero, 0x130
0650		st.32 [$s0 + 0x0], $v0
0654		addi $v0, $zero, 0x12C
0658		st.32 [$s0 + 0x4], $v0
065C		j loc_674

loc_660:
0660		addi $v0, $zero, 0x140
0664		st.32 [$s0 + 0x0], $v0
0668		addi $v0, $zero, 0x128
066C		st.32 [$s0 + 0x4], $v0
0670		addi $v0, $zero, 0x13C

loc_674:
0674		ld.32 $ra, [$sp + 0x14]
0678		st.32 [$s0 + 0x8], $v0
067C		ld.32 $s0, [$sp + 0x10]
0680		jr $ra
0684		addi $sp, $sp, 0x18

;------- subroutine -------
sub_688:
0688		addi $sp, $sp, -0x68
068C		st.32 [$sp + 0x54], $s5
0690		add $s5, $a0, $zero
0694		st.32 [$sp + 0x64], $ra
0698		st.32 [$sp + 0x60], $fp
069C		st.32 [$sp + 0x5C], $s7
06A0		st.32 [$sp + 0x58], $s6
06A4		st.32 [$sp + 0x50], $s4
06A8		add $s6, $a1, $zero
06AC		st.32 [$sp + 0x4C], $s3
06B0		st.32 [$sp + 0x48], $s2
06B4		st.32 [$sp + 0x40], $s0
06B8		jal sub_1E14
06BC		st.32 [$sp + 0x44], $s1
06C0		addi $a0, $s5, 0x8
06C4		slt $a1, $a0, $s5
06C8		add $a1, $a1, $s6
06CC		st.32 [$sp + 0x30], $v0
06D0		jal sub_1E14
06D4		st.32 [$sp + 0x34], $v1
06D8		addi $a0, $s5, 0x10
06DC		slt $a1, $a0, $s5
06E0		add $a1, $a1, $s6
06E4		add $s4, $v0, $zero
06E8		jal sub_1E14
06EC		add $fp, $v1, $zero
06F0		addi $a0, $s5, 0x18
06F4		slt $a1, $a0, $s5
06F8		add $a1, $a1, $s6
06FC		add $s2, $v0, $zero
0700		jal sub_1E14
0704		add $s3, $v1, $zero
0708		or $s0, $v0, $v1
070C		add $s6, $v0, $zero
0710		add $s5, $v1, $zero
0714		beq $zero, $s0, loc_750
0718		or $s7, $s2, $s3
071C		add $a0, $v0, $zero
0720		add $a1, $v1, $zero
0724		jal sub_1E8C
0728		add $a2, $zero, $zero
072C		beq $zero, $s7, loc_754
0730		lis $v1, 0x0
0734		addi $a0, $s2, 0x10
0738		slt $a1, $a0, $s2
073C		jal sub_1E00
0740		add $a1, $a1, $s3
0744		add $a2, $v0, $zero
0748		add $a0, $s6, $zero
074C		jal sub_1E8C

loc_750:
0750		add $a1, $s5, $zero

loc_754:
0754		lis $v1, 0x0
0758		addi $v0, $v1, 0x374C
075C		ld.32 $a0, [$v0 + 0x194]
0760		add $s1, $v1, $zero
0764		addi $v1, $zero, 0x1
0768		beq $v1, $a0, loc_778
076C		add $a0, $v0, $zero
0770		jal sub_140C
0774		st.32 [$sp + 0x38], $v0

loc_778:
0778		ld.32 $v0, [$sp + 0x38]
077C		lis $v1, 0x0
0780		ld.32 $v1, [$v1 + 0x373C]
0784		beq $zero, $v1, loc_7A8
0788		add $a0, $s4, $zero
078C		lis $a0, 0x0
0790		ld.32 $v1, [$a0 + 0x3738]
0794		addi $v1, $v1, 0x1
0798		st.32 [$a0 + 0x3738], $v1
079C		sltiu $v1, $v1, 0x4E21
07A0		beq $zero, $v1, loc_7A4

loc_7A4:
07A4		st.32 [$v0 + 0x194], $zero

loc_7A8:
07A8		add $a0, $s4, $zero
07AC		jal sub_1E00
07B0		add $a1, $fp, $zero
07B4		addi $a0, $s4, 0x4
07B8		slt $a1, $a0, $s4
07BC		add $a1, $a1, $fp
07C0		jal sub_1E00
07C4		st.32 [$sp + 0x10], $v0
07C8		st.32 [$sp + 0x14], $v0
07CC		beq $zero, $s7, loc_82C
07D0		st.32 [$sp + 0x20], $zero
07D4		add $a0, $s2, $zero
07D8		jal sub_1E14
07DC		add $a1, $s3, $zero
07E0		addi $a0, $s2, 0x8
07E4		slt $a1, $a0, $s2
07E8		add $a1, $a1, $s3
07EC		st.32 [$sp + 0x18], $v0
07F0		jal sub_1E14
07F4		st.32 [$sp + 0x1C], $v1
07F8		addi $a0, $s2, 0x10
07FC		slt $a1, $a0, $s2
0800		add $a1, $a1, $s3
0804		jal sub_1E00
0808		st.32 [$sp + 0x38], $v0
080C		ld.32 $v1, [$sp + 0x38]
0810		addi $a0, $s2, 0x14
0814		mul $v0, $v0, $v1
0818		slt $a1, $a0, $s2
081C		add $a1, $a1, $s3
0820		jal sub_1E00
0824		st.32 [$sp + 0x20], $v0
0828		sltiu $v0, $v0, 0x1

loc_82C:
082C		st.32 [$sp + 0x24], $v0
0830		addi $a0, $s1, 0x374C
0834		addi $a2, $sp, 0x28
0838		jal sub_111C
083C		addi $a1, $sp, 0x10
0840		addi $a0, $s4, 0x8
0844		slt $a1, $a0, $s4
0848		ld.32 $s1, [$sp + 0x28]
084C		jal sub_1E00
0850		add $a1, $a1, $fp
0854		ld.32 $a0, [$sp + 0x30]
0858		ld.32 $a1, [$sp + 0x34]
085C		add $a2, $s1, $zero
0860		jal sub_8D0
0864		add $a3, $v0, $zero
0868		beq $zero, $s7, loc_898
086C		ld.32 $ra, [$sp + 0x64]
0870		beq $zero, $s0, loc_89C
0874		ld.32 $fp, [$sp + 0x60]
0878		addi $a0, $s2, 0x10
087C		slt $a1, $a0, $s2
0880		jal sub_1E00
0884		add $a1, $a1, $s3
0888		add $a2, $v0, $zero
088C		add $a0, $s6, $zero
0890		jal sub_1E8C
0894		add $a1, $s5, $zero

loc_898:
0898		ld.32 $ra, [$sp + 0x64]

loc_89C:
089C		ld.32 $fp, [$sp + 0x60]
08A0		ld.32 $s7, [$sp + 0x5C]
08A4		ld.32 $s6, [$sp + 0x58]
08A8		ld.32 $s5, [$sp + 0x54]
08AC		ld.32 $s4, [$sp + 0x50]
08B0		ld.32 $s3, [$sp + 0x4C]
08B4		ld.32 $s2, [$sp + 0x48]
08B8		ld.32 $s1, [$sp + 0x44]
08BC		ld.32 $s0, [$sp + 0x40]
08C0		addi $v0, $zero, 0x1
08C4		add $v1, $zero, $zero
08C8		jr $ra
08CC		addi $sp, $sp, 0x68

;------- subroutine -------
sub_8D0:
08D0		addi $sp, $sp, -0x38
08D4		st.32 [$sp + 0x30], $s3
08D8		add $s3, $a2, $zero
08DC		addi $a2, $sp, 0x10
08E0		st.32 [$sp + 0x34], $ra
08E4		st.32 [$sp + 0x2C], $s2
08E8		st.32 [$sp + 0x28], $s1
08EC		add $s2, $a3, $zero
08F0		add $s1, $a1, $zero
08F4		st.32 [$sp + 0x24], $s0
08F8		jal sub_618
08FC		add $s0, $a0, $zero
0900		ld.32 $a0, [$sp + 0x10]
0904		add $a2, $s3, $zero
0908		add $a0, $s0, $a0
090C		slt $a1, $a0, $s0
0910		jal sub_1E8C
0914		add $a1, $a1, $s1
0918		ld.32 $a0, [$sp + 0x14]
091C		add $a2, $s2, $zero
0920		add $a0, $s0, $a0
0924		slt $a1, $a0, $s0
0928		jal sub_1E8C
092C		add $a1, $a1, $s1
0930		ld.32 $a0, [$sp + 0x18]
0934		add $a2, $s2, $zero
0938		add $a0, $s0, $a0
093C		slt $a1, $a0, $s0
0940		jal sub_1E8C
0944		add $a1, $a1, $s1
0948		ld.32 $ra, [$sp + 0x34]
094C		ld.32 $s3, [$sp + 0x30]
0950		ld.32 $s2, [$sp + 0x2C]
0954		ld.32 $s1, [$sp + 0x28]
0958		ld.32 $s0, [$sp + 0x24]
095C		jr $ra
0960		addi $sp, $sp, 0x38

;------- subroutine -------
sub_964:
0964		addi $sp, $sp, -0x28
0968		st.32 [$sp + 0x20], $s1
096C		st.32 [$sp + 0x1C], $s0
0970		st.32 [$sp + 0x24], $ra
0974		ld.8 $v0, [$a0 + 0x181]
0978		add $s0, $a0, $zero
097C		beq $zero, $v0, loc_998
0980		add $s1, $a1, $zero
0984		ld.32 $a2, [$a1 + 0x8]
0988		ld.32 $a3, [$a1 + 0xC]
098C		addi $v0, $zero, 0x40
0990		st.32 [$sp + 0x10], $v0
0994		jal sub_1C98

loc_998:
0998		addi $a0, $a0, 0x44
099C		ld.32 $a0, [$s1 + 0x8]
09A0		jal sub_1E28
09A4		ld.32 $a1, [$s1 + 0xC]
09A8		addi $v1, $v0, -0x1
09AC		andi $v1, $v1, 0xFF
09B0		sltiu $a0, $v1, 0x12
09B4		beq $zero, $a0, loc_A40
09B8		addi $a0, $zero, 0x1
09BC		lis $a1, 0x3
09C0		shl $v1, $v1, $a0
09C4		addi $a1, $a1, 0x7DFF
09C8		and $a1, $v1, $a1
09CC		bne $zero, $a1, loc_A48
09D0		st.32 [$s0 + 0x10], $v0
09D4		andi $v0, $v1, 0x8000
09D8		bneq $zero, $v0, loc_A0C
09DC		andi $v1, $v1, 0x200
09E0		beq $zero, $v1, loc_A40
09E4		addi $v0, $zero, 0xA
09E8		st.8 [$s0 + 0x181], $a0
09EC		st.32 [$s0 + 0x10], $v0
09F0		addi $a0, $s0, 0x44
09F4		addi $a1, $s0, 0x34
09F8		jal sub_1D9C
09FC		addi $a2, $zero, 0x10
0A00		jal sub_1C84
0A04		addi $a0, $s0, 0x24
0A08		j loc_A50

loc_A0C:
0A0C		ld.32 $ra, [$sp + 0x24]
0A10		addi $v0, $zero, 0x10
0A14		addi $a0, $s0, 0x19C
0A18		jal sub_1D38
0A1C		st.32 [$s0 + 0x10], $v0
0A20		addi $a0, $zero, 0x40
0A24		ld.32 $a2, [$s1 + 0x8]
0A28		ld.32 $a3, [$s1 + 0xC]
0A2C		st.32 [$sp + 0x10], $a0
0A30		add $a1, $v1, $zero
0A34		jal sub_1DB0
0A38		add $a0, $v0, $zero
0A3C		j loc_A50

loc_A40:
0A40		ld.32 $ra, [$sp + 0x24]

loc_A44:
0A44		j loc_A44

loc_A48:
0A48		nop
0A4C		ld.32 $ra, [$sp + 0x24]

loc_A50:
0A50		ld.32 $s1, [$sp + 0x20]
0A54		ld.32 $s0, [$sp + 0x1C]
0A58		add $v0, $zero, $zero
0A5C		jr $ra
0A60		addi $sp, $sp, 0x28

;------- subroutine -------
sub_A64:
0A64		ld.32 $v0, [$a0 + 0x10]
0A68		addi $sp, $sp, -0x48
0A6C		addi $v0, $v0, -0x2
0A70		sltiu $v1, $v0, 0x11
0A74		st.32 [$sp + 0x38], $s2
0A78		st.32 [$sp + 0x44], $ra
0A7C		st.32 [$sp + 0x40], $s4
0A80		st.32 [$sp + 0x3C], $s3
0A84		st.32 [$sp + 0x34], $s1
0A88		st.32 [$sp + 0x30], $s0
0A8C		beq $zero, $v1, loc_AC0
0A90		add $s2, $a0, $zero
0A94		lis $v1, 0x0
0A98		shl $v0, $v0, 0x2
0A9C		addi $v1, $v1, 0x1F60
0AA0		add $v0, $v1, $v0
0AA4		ld.32 $v0, [$v0 + 0x0]
0AA8		jr $v0
0AAC		add $s3, $a1, $zero
0AB0		ld.32 $s1, [$a1 + 0x8]
0AB4		ld.32 $s0, [$a1 + 0xC]
0AB8		or $v0, $s1, $s0
0ABC		bne $zero, $v0, loc_AC8

loc_AC0:
0AC0		ld.32 $v0, [$a1 + 0x10]
0AC4		j loc_10F4

loc_AC8:
0AC8		nop
0ACC		sltiu $v0, $v0, 0x400
0AD0		bneq $zero, $v0, loc_AC0
0AD4		lis $a0, 0x0
0AD8		jal sub_1D38
0ADC		addi $a0, $a0, 0x28AC
0AE0		addi $a0, $zero, 0x400
0AE4		st.32 [$sp + 0x10], $a0
0AE8		add $a1, $s0, $zero
0AEC		add $a0, $s1, $zero
0AF0		add $a2, $v0, $zero
0AF4		jal sub_1DB0
0AF8		add $a3, $v1, $zero
0AFC		j loc_10FC
0B00		ld.32 $ra, [$sp + 0x44]
0B04		ld.32 $v0, [$a1 + 0x10]
0B08		sltiu $v0, $v0, 0x200
0B0C		bneq $zero, $v0, loc_AC0
0B10		lis $v0, 0x0
0B14		addi $v0, $v0, 0x2CAC
0B18		st.32 [$a0 + 0x20], $v0
0B1C		ld.32 $a0, [$a1 + 0x8]
0B20		ld.32 $a1, [$a1 + 0xC]
0B24		addi $a2, $zero, 0xFF
0B28		jal sub_1DEC
0B2C		addi $a3, $zero, 0x200
0B30		ld.32 $a0, [$s2 + 0x20]
0B34		ld.32 $s0, [$s3 + 0x8]
0B38		jal sub_1D38
0B3C		ld.32 $s1, [$s3 + 0xC]
0B40		addi $a0, $zero, 0x20
0B44		st.32 [$sp + 0x10], $a0
0B48		add $a1, $s1, $zero
0B4C		add $a0, $s0, $zero
0B50		add $a2, $v0, $zero
0B54		jal sub_1DB0
0B58		add $a3, $v1, $zero
0B5C		lis $v0, 0x0
0B60		addi $v0, $v0, 0x20A8
0B64		ld.32 $a0, [$s3 + 0x8]
0B68		ld.32 $a1, [$s3 + 0xC]
0B6C		st.32 [$sp + 0x10], $v0
0B70		addi $v0, $zero, 0x3
0B74		st.32 [$sp + 0x14], $v0
0B78		ld.32 $v0, [$s2 + 0x174]
0B7C		st.32 [$sp + 0x1C], $zero
0B80		st.32 [$sp + 0x18], $v0
0B84		addi $a2, $zero, 0x20
0B88		jal sub_1CC0
0B8C		addi $a3, $s2, 0x74
0B90		j loc_10FC
0B94		ld.32 $ra, [$sp + 0x44]
0B98		ld.32 $v0, [$a1 + 0x10]
0B9C		sltiu $v0, $v0, 0x200
0BA0		bneq $zero, $v0, loc_AC0
0BA4		lis $a0, 0x0
0BA8		ld.32 $s0, [$a1 + 0x8]
0BAC		ld.32 $s1, [$a1 + 0xC]
0BB0		jal sub_1D38
0BB4		addi $a0, $a0, 0x2DD4
0BB8		addi $a0, $zero, 0x20
0BBC		st.32 [$sp + 0x10], $a0
0BC0		add $a1, $s1, $zero
0BC4		add $a0, $s0, $zero
0BC8		add $a2, $v0, $zero
0BCC		jal sub_1DB0
0BD0		add $a3, $v1, $zero
0BD4		ld.32 $v0, [$s3 + 0x8]
0BD8		ld.32 $a1, [$s3 + 0xC]
0BDC		addi $a0, $v0, 0x20
0BE0		slt $v0, $a0, $v0
0BE4		add $a1, $v0, $a1
0BE8		addi $a2, $zero, 0xFF
0BEC		jal sub_1DEC
0BF0		addi $a3, $zero, 0x1E0
0BF4		j loc_10FC
0BF8		ld.32 $ra, [$sp + 0x44]
0BFC		ld.32 $v0, [$a1 + 0x10]
0C00		sltiu $v0, $v0, 0x200
0C04		bneq $zero, $v0, loc_AC0
0C08		addi $a2, $zero, 0xFF
0C0C		ld.32 $a0, [$a1 + 0x8]
0C10		ld.32 $a1, [$a1 + 0xC]
0C14		jal sub_1DEC
0C18		addi $a3, $zero, 0x200
0C1C		ld.32 $a2, [$s3 + 0x8]
0C20		ld.32 $a3, [$s3 + 0xC]
0C24		addi $a0, $s2, 0x54
0C28		jal sub_1CE8
0C2C		addi $a1, $zero, 0x20
0C30		ld.32 $a2, [$s3 + 0x8]
0C34		ld.32 $a3, [$s3 + 0xC]
0C38		addi $v0, $zero, 0x20
0C3C		st.32 [$sp + 0x10], $v0
0C40		addi $a0, $s2, 0x24
0C44		jal sub_1C70
0C48		addi $a1, $s2, 0x34
0C4C		j loc_10FC
0C50		ld.32 $ra, [$sp + 0x44]
0C54		ld.32 $v0, [$a1 + 0x10]
0C58		sltiu $v0, $v0, 0x200
0C5C		bneq $zero, $v0, loc_AC0
0C60		addi $a2, $zero, 0xFF
0C64		ld.32 $a0, [$a1 + 0x8]
0C68		ld.32 $a1, [$a1 + 0xC]
0C6C		jal sub_1DEC
0C70		addi $a3, $zero, 0x200
0C74		lis $a0, 0x0
0C78		ld.32 $s0, [$s3 + 0x8]
0C7C		ld.32 $s1, [$s3 + 0xC]
0C80		jal sub_1D38
0C84		addi $a0, $a0, 0x1ED4
0C88		addi $a0, $zero, 0x20
0C8C		add $a2, $v0, $zero
0C90		st.32 [$sp + 0x10], $a0
0C94		add $a3, $v1, $zero
0C98		add $a0, $s0, $zero
0C9C		jal sub_1DB0
0CA0		add $a1, $s1, $zero
0CA4		ld.32 $a2, [$s3 + 0x8]
0CA8		ld.32 $a3, [$s3 + 0xC]
0CAC		j loc_10E0
0CB0		addi $v0, $zero, 0x200
0CB4		ld.32 $v0, [$a1 + 0x10]
0CB8		sltiu $v0, $v0, 0x200
0CBC		bneq $zero, $v0, loc_AC0
0CC0		addi $v1, $zero, 0x28
0CC4		ld.8 $v0, [$a0 + 0x1A4]
0CC8		beq $v1, $v0, loc_D00
0CCC		sltiu $v1, $v0, 0x29
0CD0		beq $zero, $v1, loc_CE8
0CD4		addi $v1, $zero, 0x5B
0CD8		addi $v1, $zero, 0x21
0CDC		beq $v1, $v0, loc_D78
0CE0		ld.8 $v1, [$s2 + 0x1A5]
0CE4		j loc_DC8

loc_CE8:
0CE8		nop
0CEC		beq $v1, $v0, loc_D74
0CF0		addi $v1, $zero, 0xA5
0CF4		beq $v1, $v0, loc_D28
0CF8		ld.32 $a0, [$a1 + 0x8]
0CFC		j loc_DC8

loc_D00:
0D00		nop
0D04		ld.32 $a0, [$a1 + 0x8]
0D08		ld.32 $a1, [$a1 + 0xC]
0D0C		addi $a2, $zero, 0xFF
0D10		jal sub_1DEC
0D14		addi $a3, $zero, 0x200
0D18		lis $a0, 0x0
0D1C		ld.32 $s0, [$s3 + 0x8]
0D20		ld.32 $s1, [$s3 + 0xC]
0D24		j loc_D4C

loc_D28:
0D28		addi $a0, $a0, 0x1F1C
0D2C		ld.32 $a1, [$a1 + 0xC]
0D30		addi $a2, $zero, 0xFF
0D34		jal sub_1DEC
0D38		addi $a3, $zero, 0x200
0D3C		lis $a0, 0x0
0D40		ld.32 $s0, [$s3 + 0x8]
0D44		ld.32 $s1, [$s3 + 0xC]
0D48		addi $a0, $a0, 0x1F24

loc_D4C:
0D4C		jal sub_1D38
0D50		nop
0D54		addi $a0, $zero, 0x4

loc_D58:
0D58		st.32 [$sp + 0x10], $a0
0D5C		add $a1, $s1, $zero
0D60		add $a0, $s0, $zero
0D64		add $a2, $v0, $zero
0D68		jal sub_1DB0
0D6C		add $a3, $v1, $zero
0D70		j loc_10D8

loc_D74:
0D74		ld.32 $a2, [$s3 + 0x8]

loc_D78:
0D78		ld.8 $v1, [$s2 + 0x1A5]
0D7C		ld.8 $v0, [$s2 + 0x1A6]
0D80		shl $v1, $v1, 0x18
0D84		shl $v0, $v0, 0x10
0D88		or $v0, $v1, $v0
0D8C		ld.8 $v1, [$s2 + 0x1A8]
0D90		or $v0, $v0, $v1
0D94		ld.8 $v1, [$s2 + 0x1A7]
0D98		shl $v1, $v1, 0x8
0D9C		or $v0, $v0, $v1
0DA0		jal sub_80
0DA4		st.32 [$s2 + 0x198], $v0
0DA8		ld.32 $a3, [$s3 + 0x10]
0DAC		ld.32 $a0, [$s3 + 0x8]
0DB0		ld.32 $a1, [$s3 + 0xC]
0DB4		ld.32 $a2, [$s2 + 0x198]
0DB8		jal sub_1E3C
0DBC		shr $a3, $a3, 0x9
0DC0		j loc_10D8
0DC4		ld.32 $a2, [$s3 + 0x8]

loc_DC8:
0DC8		j loc_DC8
0DCC		nop
0DD0		ld.32 $v0, [$a1 + 0x10]
0DD4		sltiu $v0, $v0, 0x200
0DD8		bneq $zero, $v0, loc_AC0
0DDC		nop
0DE0		jal sub_1B78
0DE4		add $s0, $zero, $zero
0DE8		ld.32 $a0, [$s3 + 0x8]
0DEC		ld.32 $a1, [$s3 + 0xC]
0DF0		add $a2, $zero, $zero
0DF4		jal sub_1E3C
0DF8		addi $a3, $zero, 0x1
0DFC		add $s1, $zero, $zero

loc_E00:
0E00		addi $s4, $zero, 0x10

loc_E04:
0E04		ld.32 $v1, [$s3 + 0x8]
0E08		ld.32 $a0, [$s3 + 0xC]
0E0C		addi $v0, $v1, 0x12F
0E10		slt $a1, $v0, $v1
0E14		add $a1, $a1, $a0
0E18		sub $a0, $v0, $s0
0E1C		slt $v0, $v0, $a0
0E20		sub $a1, $a1, $s1
0E24		jal sub_1E28
0E28		sub $a1, $a1, $v0
0E2C		addi $a0, $sp, 0x20
0E30		add $v1, $a0, $s0
0E34		st.8 [$v1 + 0x0], $v0
0E38		addi $v0, $s0, 0x1
0E3C		slt $v1, $v0, $s0
0E40		add $s1, $v1, $s1
0E44		bneq $s4, $v0, loc_E00
0E48		add $s0, $v0, $zero
0E4C		bne $zero, $s1, loc_E04
0E50		ld.32 $v1, [$s3 + 0x8]
0E54		ld.32 $v0, [$s3 + 0x8]
0E58		ld.32 $a3, [$s3 + 0xC]
0E5C		addi $a2, $v0, 0x190
0E60		addi $a0, $zero, 0x70
0E64		slt $v0, $a2, $v0
0E68		st.32 [$sp + 0x10], $a0
0E6C		lis $a0, 0x0
0E70		add $a3, $v0, $a3
0E74		addi $a0, $a0, 0x1FD0
0E78		jal sub_1C5C
0E7C		addi $a1, $sp, 0x20
0E80		ld.32 $v0, [$s3 + 0x8]
0E84		ld.32 $v1, [$s3 + 0xC]
0E88		addi $a0, $v0, 0x8
0E8C		addi $a2, $v0, 0x100
0E90		slt $a1, $a0, $v0
0E94		addi $a3, $zero, 0x100
0E98		slt $v0, $a2, $v0
0E9C		add $a1, $a1, $v1
0EA0		st.32 [$sp + 0x10], $a3
0EA4		jal sub_1DC4
0EA8		add $a3, $v0, $v1
0EAC		lis $a0, 0x0
0EB0		ld.32 $s0, [$s3 + 0x8]
0EB4		ld.32 $s1, [$s3 + 0xC]
0EB8		jal sub_1D38
0EBC		addi $a0, $a0, 0x1FE0
0EC0		addi $s4, $zero, 0x4
0EC4		add $a1, $s1, $zero
0EC8		add $a2, $v0, $zero
0ECC		add $a3, $v1, $zero
0ED0		add $a0, $s0, $zero
0ED4		jal sub_1DB0
0ED8		st.32 [$sp + 0x10], $s4
0EDC		ld.32 $v0, [$s3 + 0x8]
0EE0		ld.32 $v1, [$s3 + 0xC]
0EE4		addi $s0, $v0, 0x4
0EE8		lis $a0, 0x0
0EEC		slt $v0, $s0, $v0
0EF0		addi $a0, $a0, 0x1FE4
0EF4		jal sub_1D38
0EF8		add $s1, $v0, $v1
0EFC		add $a2, $v0, $zero
0F00		add $a1, $s1, $zero
0F04		add $a3, $v1, $zero
0F08		add $a0, $s0, $zero
0F0C		jal sub_1DB0
0F10		st.32 [$sp + 0x10], $s4
0F14		ld.32 $v0, [$s3 + 0x8]
0F18		ld.32 $v1, [$s3 + 0xC]
0F1C		addi $s0, $v0, 0x68
0F20		lis $a0, 0x0
0F24		slt $v0, $s0, $v0
0F28		addi $a0, $a0, 0x1EF8
0F2C		jal sub_1D38
0F30		add $s1, $v0, $v1
0F34		addi $a0, $zero, 0x20
0F38		add $a2, $v0, $zero
0F3C		st.32 [$sp + 0x10], $a0
0F40		add $a1, $s1, $zero
0F44		add $a0, $s0, $zero
0F48		jal sub_1DB0
0F4C		add $a3, $v1, $zero
0F50		ld.32 $v0, [$s3 + 0x8]
0F54		ld.32 $a1, [$s3 + 0xC]
0F58		addi $a0, $v0, 0x108
0F5C		slt $v0, $a0, $v0
0F60		add $a1, $v0, $a1
0F64		addi $a2, $zero, 0xFF
0F68		j loc_10CC
0F6C		addi $a3, $zero, 0xF8
0F70		ld.32 $v0, [$a1 + 0x10]
0F74		sltiu $v0, $v0, 0x200
0F78		bneq $zero, $v0, loc_AC0
0F7C		addi $a2, $zero, 0xFF
0F80		ld.32 $a0, [$a1 + 0x8]
0F84		ld.32 $a1, [$a1 + 0xC]
0F88		jal sub_1DEC
0F8C		addi $a3, $zero, 0x200
0F90		lis $a0, 0x0
0F94		addi $a0, $a0, 0x1F2C
0F98		ld.32 $s0, [$s3 + 0x8]
0F9C		jal sub_1D38
0FA0		ld.32 $s1, [$s3 + 0xC]
0FA4		j loc_D58
0FA8		addi $a0, $zero, 0x30
0FAC		ld.32 $v0, [$a1 + 0x10]
0FB0		sltiu $v0, $v0, 0x800
0FB4		bneq $zero, $v0, loc_AC0
0FB8		lis $s4, 0x0
0FBC		ld.32 $s0, [$a1 + 0x8]
0FC0		ld.32 $s1, [$a1 + 0xC]
0FC4		jal sub_1D38
0FC8		addi $a0, $s4, 0x20AC
0FCC		addi $a0, $zero, 0x800
0FD0		add $a1, $s1, $zero
0FD4		add $a2, $v0, $zero
0FD8		add $a3, $v1, $zero
0FDC		st.32 [$sp + 0x10], $a0
0FE0		jal sub_1DB0
0FE4		add $a0, $s0, $zero
0FE8		ld.32 $v0, [$s3 + 0x8]
0FEC		ld.32 $v1, [$s3 + 0xC]
0FF0		addi $s0, $v0, 0x8
0FF4		lis $a0, 0x0
0FF8		slt $v0, $s0, $v0
0FFC		addi $a0, $a0, 0x1FE4
1000		jal sub_1D38
1004		add $s1, $v0, $v1
1008		addi $a0, $zero, 0x4
100C		add $a3, $v1, $zero
1010		add $a2, $v0, $zero
1014		st.32 [$sp + 0x10], $a0
1018		add $a1, $s1, $zero
101C		jal sub_1DB0
1020		add $a0, $s0, $zero
1024		ld.32 $v0, [$s3 + 0x8]
1028		ld.32 $a1, [$s3 + 0xC]
102C		addi $a0, $v0, 0x200
1030		slt $v0, $a0, $v0
1034		add $a1, $v0, $a1
1038		addi $a2, $zero, 0x38
103C		jal sub_1E3C
1040		addi $a3, $zero, 0x1
1044		ld.32 $v0, [$s3 + 0x8]
1048		ld.32 $v1, [$s3 + 0xC]
104C		addi $a0, $v0, 0x200
1050		addi $a2, $v0, 0x201
1054		slt $a1, $a0, $v0
1058		addi $a3, $zero, 0xF
105C		slt $v0, $a2, $v0
1060		st.32 [$sp + 0x10], $a3
1064		add $a1, $a1, $v1
1068		jal sub_1D88
106C		add $a3, $v0, $v1
1070		bneq $zero, $v0, loc_10B0
1074		ld.32 $v0, [$s3 + 0x8]
1078		ld.32 $v1, [$s3 + 0xC]
107C		addi $s0, $v0, 0x200
1080		slt $v0, $s0, $v0
1084		addi $a0, $s4, 0x20AC
1088		jal sub_1D38
108C		add $s1, $v0, $v1
1090		addi $a2, $v0, 0x200
1094		addi $a0, $zero, 0x200
1098		slt $a3, $a2, $v0
109C		st.32 [$sp + 0x10], $a0
10A0		add $a1, $s1, $zero
10A4		add $a0, $s0, $zero
10A8		jal sub_1DB0
10AC		add $a3, $a3, $v1

loc_10B0:
10B0		ld.32 $v0, [$s3 + 0x8]
10B4		ld.32 $a1, [$s3 + 0xC]
10B8		addi $a0, $v0, 0x600
10BC		slt $v0, $a0, $v0
10C0		add $a1, $v0, $a1
10C4		add $a2, $zero, $zero
10C8		addi $a3, $zero, 0x200

loc_10CC:
10CC		jal sub_1DEC
10D0		nop
10D4		ld.32 $a2, [$s3 + 0x8]

loc_10D8:
10D8		ld.32 $a3, [$s3 + 0xC]
10DC		ld.32 $v0, [$s3 + 0x10]

loc_10E0:
10E0		st.32 [$sp + 0x10], $v0
10E4		jal sub_1C98
10E8		addi $a0, $s2, 0x44
10EC		j loc_10FC
10F0		ld.32 $ra, [$sp + 0x44]

loc_10F4:
10F4		j loc_10F4
10F8		nop

loc_10FC:
10FC		ld.32 $s4, [$sp + 0x40]
1100		ld.32 $s3, [$sp + 0x3C]
1104		ld.32 $s2, [$sp + 0x38]
1108		ld.32 $s1, [$sp + 0x34]
110C		ld.32 $s0, [$sp + 0x30]
1110		add $v0, $zero, $zero
1114		jr $ra
1118		addi $sp, $sp, 0x48

;------- subroutine -------
sub_111C:
111C		ld.32 $v1, [$a0 + 0x8]
1120		addi $sp, $sp, -0x18
1124		st.32 [$a2 + 0x0], $v1
1128		ld.32 $v1, [$a1 + 0x0]
112C		addi $a3, $zero, 0xD
1130		beq $a3, $v1, loc_1178
1134		st.32 [$sp + 0x14], $ra
1138		addi $v0, $zero, 0x3C
113C		beq $v0, $v1, loc_11C0
1140		st.32 [$a0 + 0x1DC], $zero
1144		sltiu $v0, $v1, 0x3D
1148		beq $zero, $v0, loc_1164
114C		addi $v0, $zero, 0x12
1150		beq $v0, $v1, loc_11A0
1154		addi $v0, $zero, 0x19
1158		beq $v0, $v1, loc_11B0
115C		nop
1160		j loc_11D4

loc_1164:
1164		nop
1168		sltiu $v1, $v1, 0x40
116C		bneq $zero, $v1, loc_11DC
1170		ld.32 $ra, [$sp + 0x14]
1174		j loc_11D4

loc_1178:
1178		nop
117C		ld.32 $v1, [$a0 + 0x1DC]
1180		addi $v1, $v1, 0x1
1184		st.32 [$a0 + 0x1DC], $v1
1188		sltiu $v1, $v1, 0x4
118C		bneq $zero, $v1, loc_11DC
1190		ld.32 $ra, [$sp + 0x14]
1194		addi $v1, $zero, 0x804
1198		st.32 [$a0 + 0x8], $v1
119C		j loc_11DC

loc_11A0:
11A0		st.8 [$a0 + 0x181], $zero
11A4		jal sub_A64
11A8		nop
11AC		j loc_11E0

loc_11B0:
11B0		ld.32 $ra, [$sp + 0x14]
11B4		jal sub_11EC
11B8		nop
11BC		j loc_11E0

loc_11C0:
11C0		ld.32 $ra, [$sp + 0x14]
11C4		jal sub_964
11C8		nop
11CC		j loc_11E0
11D0		ld.32 $ra, [$sp + 0x14]

loc_11D4:
11D4		j loc_11D4
11D8		nop

loc_11DC:
11DC		ld.32 $ra, [$sp + 0x14]

loc_11E0:
11E0		add $v0, $zero, $zero
11E4		jr $ra
11E8		addi $sp, $sp, 0x18

;------- subroutine -------
sub_11EC:
11EC		ld.32 $v0, [$a0 + 0x10]
11F0		addi $sp, $sp, -0x48
11F4		addi $v0, $v0, -0x1
11F8		sltiu $v1, $v0, 0xB
11FC		st.32 [$sp + 0x3C], $s0
1200		st.32 [$sp + 0x44], $ra
1204		st.32 [$sp + 0x40], $s1
1208		beq $zero, $v1, loc_1360
120C		add $s0, $a0, $zero
1210		lis $v1, 0x0
1214		shl $v0, $v0, 0x2
1218		addi $v1, $v1, 0x1FA4
121C		add $v0, $v1, $v0
1220		ld.32 $v0, [$v0 + 0x0]
1224		jr $v0
1228		add $s1, $a1, $zero
122C		ld.32 $v0, [$a1 + 0x10]
1230		sltiu $v0, $v0, 0x200
1234		bneq $zero, $v0, loc_12B4
1238		addi $v0, $zero, 0x800
123C		ld.32 $v0, [$a1 + 0x8]
1240		ld.32 $a1, [$a1 + 0xC]
1244		addi $a0, $v0, 0x110
1248		slt $v0, $a0, $v0
124C		jal sub_1E28
1250		add $a1, $v0, $a1
1254		addi $v1, $zero, 0x1
1258		bneq $v1, $v0, loc_1280
125C		st.8 [$s0 + 0x180], $v0
1260		lis $v0, 0x0
1264		addi $v0, $v0, 0x2028
1268		st.32 [$s0 + 0x174], $v0
126C		lis $v0, 0x0
1270		addi $v0, $v0, 0x1FE8
1274		st.32 [$s0 + 0x178], $v0
1278		lis $v0, 0x0
127C		j loc_12B0

loc_1280:
1280		addi $v0, $v0, 0x2008
1284		addi $v1, $zero, 0x3
1288		bneq $v1, $v0, loc_12B4
128C		addi $v0, $zero, 0x800
1290		lis $v0, 0x0
1294		addi $v0, $v0, 0x2088
1298		st.32 [$s0 + 0x174], $v0
129C		lis $v0, 0x0
12A0		addi $v0, $v0, 0x2048
12A4		st.32 [$s0 + 0x178], $v0
12A8		lis $v0, 0x0
12AC		addi $v0, $v0, 0x2068

loc_12B0:
12B0		st.32 [$s0 + 0x17C], $v0

loc_12B4:
12B4		addi $v0, $zero, 0x800
12B8		j loc_13F4
12BC		st.32 [$s0 + 0x8], $v0
12C0		ld.32 $v0, [$a1 + 0x10]
12C4		sltiu $v0, $v0, 0xF0
12C8		bneq $zero, $v0, loc_12FC
12CC		nop
12D0		jal sub_1D38
12D4		addi $a0, $a0, 0x74
12D8		ld.32 $a0, [$s1 + 0x8]
12DC		ld.32 $a3, [$s1 + 0xC]
12E0		addi $a2, $a0, 0x130
12E4		slt $t0, $a2, $a0
12E8		addi $a0, $zero, 0x100
12EC		st.32 [$sp + 0x10], $a0
12F0		add $a1, $v1, $zero
12F4		add $a0, $v0, $zero
12F8		j loc_13B4

loc_12FC:
12FC		add $a3, $t0, $a3

loc_1300:
1300		j loc_1300
1304		nop
1308		addi $v0, $s0, 0x182
130C		ld.32 $a0, [$a0 + 0x17C]
1310		lis $a1, 0x0
1314		lis $a2, 0x0
1318		st.32 [$sp + 0x10], $v0
131C		addi $a3, $sp, 0x18
1320		addi $a1, $a1, 0x2CAC
1324		jal sub_1CD4
1328		addi $a2, $a2, 0x2DF4
132C		addi $a0, $s0, 0x24
1330		addi $a1, $sp, 0x18
1334		jal sub_1D9C
1338		addi $a2, $zero, 0x10
133C		addi $a0, $s0, 0x34
1340		addi $a1, $sp, 0x28
1344		jal sub_1D9C
1348		addi $a2, $zero, 0x10
134C		j loc_13F8
1350		ld.32 $ra, [$sp + 0x44]
1354		ld.32 $v0, [$a1 + 0x10]
1358		sltiu $v0, $v0, 0x200
135C		beq $zero, $v0, loc_13F4

loc_1360:
1360		ld.32 $ra, [$sp + 0x44]
1364		j loc_13EC
1368		nop
136C		ld.32 $v0, [$a1 + 0x10]
1370		sltiu $v0, $v0, 0x200
1374		bneq $zero, $v0, loc_1360
1378		addi $v0, $zero, 0x200
137C		ld.32 $a2, [$a1 + 0x8]
1380		ld.32 $a3, [$a1 + 0xC]
1384		addi $a1, $s0, 0x34
1388		st.32 [$sp + 0x10], $v0
138C		jal sub_1C5C
1390		addi $a0, $a0, 0x24
1394		jal sub_1D38
1398		addi $a0, $s0, 0x54
139C		addi $a0, $zero, 0x20
13A0		ld.32 $a2, [$s1 + 0x8]
13A4		ld.32 $a3, [$s1 + 0xC]
13A8		add $a1, $v1, $zero
13AC		st.32 [$sp + 0x10], $a0
13B0		add $a0, $v0, $zero

loc_13B4:
13B4		jal sub_1DB0
13B8		nop
13BC		j loc_13F8
13C0		ld.32 $ra, [$sp + 0x44]
13C4		ld.32 $v0, [$a1 + 0x10]
13C8		sltiu $v1, $v0, 0x200
13CC		bneq $zero, $v1, loc_1360
13D0		addi $a0, $a0, 0x44
13D4		ld.32 $a2, [$a1 + 0x8]
13D8		ld.32 $a3, [$a1 + 0xC]
13DC		jal sub_1C98
13E0		st.32 [$sp + 0x10], $v0
13E4		j loc_13F8
13E8		ld.32 $ra, [$sp + 0x44]

loc_13EC:
13EC		j loc_13EC
13F0		nop

loc_13F4:
13F4		ld.32 $ra, [$sp + 0x44]

loc_13F8:
13F8		ld.32 $s1, [$sp + 0x40]
13FC		ld.32 $s0, [$sp + 0x3C]
1400		add $v0, $zero, $zero
1404		jr $ra
1408		addi $sp, $sp, 0x48

;------- subroutine -------
sub_140C:
140C		addi $v0, $zero, 0x804
1410		st.32 [$a0 + 0x8], $v0
1414		addi $v0, $zero, 0x1
1418		st.32 [$a0 + 0x194], $v0
141C		lis $v0, 0x0
1420		addi $v0, $v0, 0x2088
1424		st.32 [$a0 + 0x174], $v0
1428		lis $v0, 0x0
142C		addi $v0, $v0, 0x2048
1430		st.32 [$a0 + 0x178], $v0
1434		lis $v0, 0x0
1438		addi $v0, $v0, 0x2068
143C		st.8 [$a0 + 0x181], $zero
1440		st.32 [$a0 + 0x1DC], $zero
1444		jr $ra
1448		st.32 [$a0 + 0x17C], $v0

;------- subroutine -------
sub_144C:
144C		addi $sp, $sp, -0x30
1450		st.32 [$sp + 0x28], $s1
1454		st.32 [$sp + 0x24], $s0
1458		st.32 [$sp + 0x2C], $ra
145C		jal sub_3DC
1460		add $s1, $a0, $zero
1464		bneq $zero, $v0, loc_1494
1468		addi $s0, $zero, -0x1
146C		jal sub_520
1470		addi $a0, $sp, 0x10
1474		bneq $zero, $v0, loc_1484
1478		addi $a0, $sp, 0x10
147C		jal sub_250
1480		add $a1, $s1, $zero

loc_1484:
1484		add $s0, $v0, $zero
1488		jal sub_1EB4
148C		addi $a0, $sp, 0x10
1490		jal sub_244

loc_1494:
1494		nop
1498		ld.32 $ra, [$sp + 0x2C]
149C		add $v0, $s0, $zero
14A0		ld.32 $s1, [$sp + 0x28]
14A4		ld.32 $s0, [$sp + 0x24]
14A8		jr $ra
14AC		addi $sp, $sp, 0x30

;------- subroutine -------
sub_14B0:
14B0		addi $sp, $sp, -0x20
14B4		st.32 [$sp + 0x1C], $ra
14B8		jal sub_1D10
14BC		nop
14C0		addi $a2, $v0, 0x1
14C4		add $a1, $v1, $zero
14C8		slt $a3, $a2, $v0
14CC		addi $v1, $zero, 0xFF
14D0		st.32 [$sp + 0x10], $v1
14D4		add $a0, $v0, $zero
14D8		jal sub_1D88
14DC		add $a3, $a3, $a1
14E0		ld.32 $ra, [$sp + 0x1C]
14E4		jr $ra
14E8		addi $sp, $sp, 0x20

;------- subroutine -------
sub_14EC:
14EC		ld.32 $v0, [$a0 + 0x8]
14F0		ld.32 $a1, [$a0 + 0x0]
14F4		ld.32 $t0, [$a0 + 0xC]
14F8		add $a1, $a1, $v0
14FC		shl $v1, $a1, 0x3
1500		add $v1, $a0, $v1
1504		st.32 [$v1 + 0x18], $a2
1508		ld.32 $a2, [$sp + 0x10]
150C		addi $a1, $a1, 0x26
1510		st.32 [$v1 + 0x1C], $a3
1514		st.32 [$v1 + 0x58], $a2
1518		st.32 [$v1 + 0x5C], $zero
151C		shl $a1, $a1, 0x2
1520		ld.32 $v1, [$sp + 0x14]
1524		add $a1, $a0, $a1
1528		st.32 [$a1 + 0x0], $v1
152C		addi $v1, $v0, 0x1
1530		slt $v0, $v1, $v0
1534		add $t0, $v0, $t0
1538		st.32 [$a0 + 0x8], $v1
153C		jr $ra
1540		st.32 [$a0 + 0xC], $t0

;------- subroutine -------
sub_1544:
1544		add $a1, $zero, $zero
1548		j loc_1DD8
154C		addi $a2, $zero, 0x1B0

;------- subroutine -------
sub_1550:
1550		addi $v0, $zero, 0x1
1554		jr $ra
1558		st.8 [$a0 + 0x150], $v0

;------- subroutine -------
sub_155C:
155C		j loc_1CAC
1560		nop

;------- subroutine -------
sub_1564:
1564		addi $sp, $sp, -0x20
1568		st.32 [$sp + 0x18], $s0
156C		add $s0, $a0, $zero
1570		add $a0, $a2, $zero
1574		st.32 [$sp + 0x1C], $ra
1578		jal sub_1D38
157C		st.32 [$sp + 0x10], $a1
1580		ld.32 $a1, [$sp + 0x10]
1584		ld.32 $ra, [$sp + 0x1C]
1588		add $a0, $s0, $zero
158C		ld.32 $s0, [$sp + 0x18]
1590		add $a2, $v0, $zero
1594		add $a3, $v1, $zero
1598		j loc_1CE8
159C		addi $sp, $sp, 0x20

;------- subroutine -------
sub_15A0:
15A0		addi $sp, $sp, -0x138
15A4		add $v0, $a0, $zero
15A8		addi $a0, $sp, 0x10
15AC		st.32 [$sp + 0x130], $s0
15B0		addi $a2, $zero, 0x100
15B4		add $s0, $a1, $zero
15B8		st.32 [$sp + 0x134], $ra
15BC		jal sub_1664
15C0		add $a1, $v0, $zero
15C4		lis $a1, 0x0
15C8		lis $a2, 0x0
15CC		addi $a0, $sp, 0x10
15D0		addi $a1, $a1, 0x2E18
15D4		addi $a2, $a2, 0x2E14
15D8		jal sub_155C
15DC		addi $a3, $zero, 0x3
15E0		add $a0, $s0, $zero
15E4		addi $a1, $zero, 0x10
15E8		jal sub_1564
15EC		addi $a2, $sp, 0x110
15F0		ld.8 $v0, [$sp + 0x10]
15F4		bneq $zero, $v0, loc_1644
15F8		ld.8 $v1, [$sp + 0x11]
15FC		addi $v0, $zero, 0x1
1600		bneq $v0, $v1, loc_1644
1604		ld.8 $v0, [$sp + 0xEF]
1608		bneq $zero, $v0, loc_1644
160C		addi $v0, $sp, 0x12
1610		addi $v1, $sp, 0xEF
1614		addi $a0, $zero, 0xFF

loc_1618:
1618		ld.8 $a1, [$v0 + 0x0]
161C		bneq $a0, $a1, loc_1644
1620		addi $v0, $v0, 0x1
1624		bne $v1, $v0, loc_1618
1628		ld.8 $a1, [$v0 + 0x0]
162C		addi $a0, $sp, 0xF0
1630		addi $a1, $sp, 0x110
1634		jal sub_165C
1638		addi $a2, $zero, 0x20
163C		slt $v0, $zero, $v0
1640		j loc_164C

loc_1644:
1644		sub $v0, $zero, $v0
1648		addi $v0, $zero, -0x1

loc_164C:
164C		ld.32 $ra, [$sp + 0x134]
1650		ld.32 $s0, [$sp + 0x130]
1654		jr $ra
1658		addi $sp, $sp, 0x138

;------- subroutine -------
sub_165C:
165C		j loc_1D74
1660		nop

;------- subroutine -------
sub_1664:
1664		addi $sp, $sp, -0x18
1668		st.32 [$sp + 0x14], $ra
166C		st.32 [$sp + 0x10], $s0
1670		jal sub_1D9C
1674		add $s0, $a0, $zero
1678		ld.32 $ra, [$sp + 0x14]
167C		add $v0, $s0, $zero
1680		ld.32 $s0, [$sp + 0x10]
1684		jr $ra
1688		addi $sp, $sp, 0x18

;------- subroutine -------
sub_168C:
168C		addi $sp, $sp, -0x48
1690		st.32 [$sp + 0x24], $s1
1694		add $s1, $a0, $zero
1698		st.32 [$sp + 0x44], $ra
169C		st.32 [$sp + 0x40], $fp
16A0		st.32 [$sp + 0x3C], $s7
16A4		add $fp, $a1, $zero
16A8		st.32 [$sp + 0x38], $s6
16AC		st.32 [$sp + 0x34], $s5
16B0		st.32 [$sp + 0x30], $s4
16B4		st.32 [$sp + 0x2C], $s3
16B8		st.32 [$sp + 0x28], $s2
16BC		jal sub_1E14
16C0		st.32 [$sp + 0x20], $s0
16C4		addi $a0, $s1, 0x8
16C8		slt $a1, $a0, $s1
16CC		add $a1, $a1, $fp
16D0		add $s5, $v0, $zero
16D4		jal sub_1E14
16D8		add $s2, $v1, $zero
16DC		addi $a0, $s1, 0x10
16E0		slt $a1, $a0, $s1
16E4		add $a1, $a1, $fp
16E8		add $s4, $v0, $zero
16EC		jal sub_1E14
16F0		add $s3, $v1, $zero
16F4		addi $a0, $s1, 0x1C
16F8		slt $a1, $a0, $s1
16FC		add $a1, $a1, $fp
1700		add $s6, $v1, $zero
1704		jal sub_1E00
1708		add $s7, $v0, $zero
170C		addi $a0, $s1, 0x18
1710		slt $a1, $a0, $s1
1714		add $a1, $a1, $fp
1718		jal sub_1E00
171C		add $s0, $v0, $zero
1720		jal sub_1CFC
1724		add $s1, $v0, $zero
1728		add $fp, $v0, $zero
172C		addi $v0, $zero, 0x33
1730		bneq $v0, $s5, loc_1840
1734		addi $v0, $zero, 0x12
1738		lis $v0, 0x100
173C		bneq $v0, $s2, loc_1840
1740		addi $v0, $zero, 0x12
1744		addi $v0, $zero, 0x1
1748		bneq $v0, $s0, loc_1B48
174C		ld.32 $ra, [$sp + 0x44]
1750		jal sub_14B0
1754		nop
1758		beq $zero, $v0, loc_1B48
175C		ld.32 $ra, [$sp + 0x44]
1760		lis $v0, 0x0
1764		addi $v0, $v0, 0x2D9C
1768		st.32 [$sp + 0x10], $v0
176C		addi $v0, $zero, 0xE
1770		st.32 [$sp + 0x14], $v0
1774		lis $v0, 0x0
1778		addi $v0, $v0, 0x2D98
177C		st.32 [$sp + 0x18], $v0
1780		st.32 [$sp + 0x1C], $s0
1784		add $a0, $s4, $zero
1788		add $a1, $s3, $zero
178C		add $a2, $s1, $zero
1790		jal sub_18C
1794		add $a3, $zero, $zero
1798		add $s2, $v0, $zero
179C		or $v0, $v0, $v1
17A0		bneq $zero, $v0, loc_17EC
17A4		add $s5, $v1, $zero
17A8		lis $v0, 0x0
17AC		addi $v0, $v0, 0x2D80
17B0		st.32 [$sp + 0x10], $v0
17B4		addi $v0, $zero, 0x6
17B8		st.32 [$sp + 0x14], $v0
17BC		lis $v0, 0x0
17C0		addi $v0, $v0, 0x2D7C
17C4		st.32 [$sp + 0x18], $v0
17C8		st.32 [$sp + 0x1C], $s0
17CC		add $a0, $s4, $zero
17D0		add $a1, $s3, $zero
17D4		add $a2, $s1, $zero
17D8		jal sub_18C
17DC		add $a3, $zero, $zero
17E0		add $s2, $v0, $zero
17E4		or $v0, $v0, $v1
17E8		beq $zero, $v0, loc_1B44

loc_17EC:
17EC		add $s5, $v1, $zero
17F0		add $a0, $s2, $zero
17F4		add $a1, $s5, $zero
17F8		jal sub_1E8C
17FC		lis $a2, 0xD280
1800		addi $a0, $s2, 0x4
1804		slt $a1, $a0, $s2
1808		ld.32 $ra, [$sp + 0x44]
180C		ld.32 $fp, [$sp + 0x40]
1810		ld.32 $s7, [$sp + 0x3C]
1814		ld.32 $s6, [$sp + 0x38]
1818		ld.32 $s4, [$sp + 0x30]
181C		ld.32 $s3, [$sp + 0x2C]
1820		ld.32 $s2, [$sp + 0x28]
1824		ld.32 $s1, [$sp + 0x24]
1828		ld.32 $s0, [$sp + 0x20]
182C		add $a1, $a1, $s5
1830		lis $a2, 0xD65F
1834		ld.32 $s5, [$sp + 0x34]
1838		addi $a2, $a2, 0x3C0
183C		j loc_1E8C

loc_1840:
1840		addi $sp, $sp, 0x48
1844		bneq $v0, $s5, loc_188C
1848		addi $v0, $zero, 0x24
184C		lis $v0, 0x100
1850		bneq $v0, $s2, loc_188C
1854		addi $v0, $zero, 0x24
1858		addi $v0, $zero, 0x1
185C		bneq $v0, $s0, loc_1B48
1860		ld.32 $ra, [$sp + 0x44]
1864		ld.32 $fp, [$sp + 0x40]
1868		ld.32 $s7, [$sp + 0x3C]
186C		ld.32 $s6, [$sp + 0x38]
1870		ld.32 $s5, [$sp + 0x34]
1874		ld.32 $s4, [$sp + 0x30]
1878		ld.32 $s3, [$sp + 0x2C]
187C		ld.32 $s2, [$sp + 0x28]
1880		ld.32 $s1, [$sp + 0x24]
1884		ld.32 $s0, [$sp + 0x20]
1888		j loc_14B0

loc_188C:
188C		addi $sp, $sp, 0x48
1890		bneq $v0, $s5, loc_1974
1894		lis $v0, 0x100
1898		bneq $v0, $s2, loc_1974
189C		addi $v0, $zero, 0x1
18A0		bneq $v0, $s0, loc_1B48
18A4		ld.32 $ra, [$sp + 0x44]
18A8		jal sub_14B0
18AC		nop
18B0		beq $zero, $v0, loc_1B48
18B4		ld.32 $ra, [$sp + 0x44]
18B8		lis $v0, 0x0
18BC		addi $v0, $v0, 0x2D3C
18C0		st.32 [$sp + 0x10], $v0
18C4		addi $v0, $zero, 0x10
18C8		st.32 [$sp + 0x14], $v0
18CC		lis $v0, 0x0
18D0		addi $v0, $v0, 0x2D38
18D4		st.32 [$sp + 0x1C], $s0
18D8		add $a2, $s1, $zero
18DC		st.32 [$sp + 0x18], $v0
18E0		add $a0, $s4, $zero
18E4		add $a1, $s3, $zero
18E8		jal sub_18C
18EC		add $a3, $zero, $zero
18F0		add $s0, $v0, $zero
18F4		or $v0, $v0, $v1
18F8		beq $zero, $v0, loc_1B44
18FC		add $s1, $v1, $zero
1900		lis $a2, 0x1000
1904		add $a0, $s0, $zero
1908		add $a1, $v1, $zero
190C		jal sub_1E8C
1910		addi $a2, $a2, 0xC9
1914		addi $a0, $s0, 0x4
1918		slt $a1, $a0, $s0
191C		andi $v0, $s0, 0x4
1920		add $a1, $a1, $s1
1924		beq $zero, $v0, loc_1930
1928		lis $a2, 0x5800
192C		j loc_1938

loc_1930:
1930		addi $a2, $a2, 0x48
1934		addi $a2, $a2, 0x68

loc_1938:
1938		jal sub_1E8C
193C		nop
1940		addi $a0, $s0, 0x8
1944		slt $a1, $a0, $s0
1948		lis $a2, 0xD61F
194C		add $a1, $a1, $s1
1950		jal sub_1E8C
1954		addi $a2, $a2, 0x100
1958		addi $v0, $s0, 0x10
195C		slt $a1, $v0, $s0
1960		addi $a0, $zero, -0x5
1964		lis $a2, 0xD000
1968		and $a0, $a0, $v0
196C		add $a1, $a1, $s1
1970		j loc_1B14

loc_1974:
1974		addi $a2, $a2, 0x70
1978		addi $v0, $zero, 0x1F
197C		bneq $v0, $s5, loc_1A38
1980		lis $v0, 0x100
1984		bneq $v0, $s2, loc_1A38
1988		addi $v0, $zero, 0x1
198C		bneq $v0, $s0, loc_1B48
1990		ld.32 $ra, [$sp + 0x44]
1994		jal sub_14B0
1998		nop
199C		beq $zero, $v0, loc_1B48
19A0		ld.32 $ra, [$sp + 0x44]
19A4		beq $zero, $fp, loc_1B4C
19A8		ld.32 $fp, [$sp + 0x40]
19AC		lis $v1, 0x0
19B0		addi $v1, $v1, 0x2CF4
19B4		sub $v0, $s1, $s7
19B8		st.32 [$sp + 0x10], $v1
19BC		addi $v1, $zero, 0x11
19C0		slt $s1, $s1, $v0
19C4		st.32 [$sp + 0x14], $v1
19C8		lis $v1, 0x0
19CC		sub $s3, $s3, $s1
19D0		add $a2, $v0, $s4
19D4		addi $v1, $v1, 0x2CCC
19D8		slt $v0, $a2, $v0
19DC		st.32 [$sp + 0x18], $v1
19E0		sub $a3, $s3, $s6
19E4		addi $v1, $zero, 0x9
19E8		st.32 [$sp + 0x1C], $v1
19EC		add $a0, $s7, $zero
19F0		add $a1, $s6, $zero
19F4		jal sub_1E8
19F8		add $a3, $v0, $a3
19FC		add $s1, $v0, $zero
1A00		or $v0, $v0, $v1
1A04		beq $zero, $v0, loc_1B44
1A08		add $s0, $v1, $zero
1A0C		lis $a0, 0x0
1A10		jal sub_1D38
1A14		addi $a0, $a0, 0x2CD8
1A18		addi $a0, $zero, 0x8
1A1C		st.32 [$sp + 0x10], $a0
1A20		add $a1, $s0, $zero
1A24		add $a0, $s1, $zero
1A28		add $a2, $v0, $zero
1A2C		jal sub_1DB0
1A30		add $a3, $v1, $zero
1A34		j loc_1B4C

loc_1A38:
1A38		ld.32 $ra, [$sp + 0x44]
1A3C		addi $v0, $zero, 0x1A
1A40		bneq $v0, $s5, loc_1B44
1A44		lis $v0, 0x100
1A48		bneq $v0, $s2, loc_1B44
1A4C		addi $v0, $zero, 0x1
1A50		bneq $v0, $s0, loc_1B48
1A54		ld.32 $ra, [$sp + 0x44]
1A58		lis $v0, 0x0
1A5C		addi $v0, $v0, 0x2CE8
1A60		st.32 [$sp + 0x10], $v0
1A64		addi $v0, $zero, 0x3
1A68		st.32 [$sp + 0x14], $v0
1A6C		lis $v0, 0x0
1A70		addi $v0, $v0, 0x2CE4
1A74		st.32 [$sp + 0x1C], $s0
1A78		add $a2, $s1, $zero
1A7C		st.32 [$sp + 0x18], $v0
1A80		add $a0, $s4, $zero
1A84		add $a1, $s3, $zero
1A88		jal sub_18C
1A8C		add $a3, $zero, $zero
1A90		add $s0, $v0, $zero
1A94		or $v0, $v0, $v1
1A98		beq $zero, $v0, loc_1B44
1A9C		add $s1, $v1, $zero
1AA0		lis $a2, 0x1000
1AA4		add $a0, $s0, $zero
1AA8		add $a1, $v1, $zero
1AAC		jal sub_1E8C
1AB0		addi $a2, $a2, 0xC9
1AB4		addi $a0, $s0, 0x4
1AB8		slt $a1, $a0, $s0
1ABC		andi $v0, $s0, 0x4
1AC0		add $a1, $a1, $s1
1AC4		beq $zero, $v0, loc_1AD0
1AC8		lis $a2, 0x5800
1ACC		j loc_1AD8

loc_1AD0:
1AD0		addi $a2, $a2, 0x48
1AD4		addi $a2, $a2, 0x68

loc_1AD8:
1AD8		jal sub_1E8C
1ADC		nop
1AE0		addi $a0, $s0, 0x8
1AE4		slt $a1, $a0, $s0
1AE8		lis $a2, 0xD61F
1AEC		add $a1, $a1, $s1
1AF0		jal sub_1E8C
1AF4		addi $a2, $a2, 0x100
1AF8		addi $v0, $s0, 0x10
1AFC		slt $a1, $v0, $s0
1B00		addi $a0, $zero, -0x5
1B04		lis $a2, 0xD000
1B08		and $a0, $a0, $v0
1B0C		add $a1, $a1, $s1
1B10		addi $a2, $a2, 0x78

loc_1B14:
1B14		ld.32 $ra, [$sp + 0x44]
1B18		ld.32 $fp, [$sp + 0x40]
1B1C		ld.32 $s7, [$sp + 0x3C]
1B20		ld.32 $s6, [$sp + 0x38]
1B24		ld.32 $s5, [$sp + 0x34]
1B28		ld.32 $s4, [$sp + 0x30]
1B2C		ld.32 $s3, [$sp + 0x2C]
1B30		ld.32 $s2, [$sp + 0x28]
1B34		ld.32 $s1, [$sp + 0x24]
1B38		ld.32 $s0, [$sp + 0x20]
1B3C		addi $a3, $zero, -0x1
1B40		j loc_1EA0

loc_1B44:
1B44		addi $sp, $sp, 0x48

loc_1B48:
1B48		ld.32 $ra, [$sp + 0x44]

loc_1B4C:
1B4C		ld.32 $fp, [$sp + 0x40]
1B50		ld.32 $s7, [$sp + 0x3C]
1B54		ld.32 $s6, [$sp + 0x38]
1B58		ld.32 $s5, [$sp + 0x34]
1B5C		ld.32 $s4, [$sp + 0x30]
1B60		ld.32 $s3, [$sp + 0x2C]
1B64		ld.32 $s2, [$sp + 0x28]
1B68		ld.32 $s1, [$sp + 0x24]
1B6C		ld.32 $s0, [$sp + 0x20]
1B70		jr $ra
1B74		addi $sp, $sp, 0x48

;------- subroutine -------
sub_1B78:
1B78		addi $sp, $sp, -0x28
1B7C		st.32 [$sp + 0x18], $s1
1B80		lis $s1, 0x0
1B84		st.32 [$sp + 0x14], $s0
1B88		addi $a0, $s1, 0x0
1B8C		lis $v0, 0x0
1B90		lis $s0, 0x0
1B94		st.32 [$sp + 0x24], $ra
1B98		st.32 [$sp + 0x20], $s3
1B9C		st.32 [$sp + 0x1C], $s2
1BA0		st.32 [$v0 + 0x2F24], $zero
1BA4		jal sub_1D38
1BA8		ld.32 $s2, [$s0 + 0x2F28]
1BAC		lis $a2, 0x0
1BB0		addi $s1, $s1, 0x0
1BB4		addi $a2, $a2, 0x2F1C
1BB8		sub $a2, $a2, $s1
1BBC		add $a0, $v0, $zero
1BC0		add $a1, $v1, $zero
1BC4		jal sub_1C48
1BC8		addi $s0, $s0, 0x2F28
1BCC		ld.32 $a2, [$s0 + 0x8]
1BD0		add $s3, $v0, $zero
1BD4		lis $a0, 0xD000
1BD8		addi $a1, $zero, -0x1
1BDC		jal sub_1C48
1BE0		ld.32 $s1, [$s0 + 0x4]
1BE4		bne $s3, $s2, loc_1BF0
1BE8		lis $v0, 0x0
1BEC		beq $v0, $s1, loc_1C00

loc_1BF0:
1BF0		lis $v0, 0x0
1BF4		addi $v1, $zero, 0x1
1BF8		st.32 [$v0 + 0x373C], $v1
1BFC		lis $v0, 0x0

loc_1C00:
1C00		st.32 [$v0 + 0x3738], $zero
1C04		ld.32 $ra, [$sp + 0x24]
1C08		ld.32 $s3, [$sp + 0x20]
1C0C		ld.32 $s2, [$sp + 0x1C]
1C10		ld.32 $s1, [$sp + 0x18]
1C14		ld.32 $s0, [$sp + 0x14]
1C18		jr $ra
1C1C		addi $sp, $sp, 0x28

;------- subroutine -------
sub_1C20:
1C20		lis $v0, 0xAA83
1C24		ori $v0, $v0, 0x564; = 0xAA830564 - UNK
1C28		host_call
1C2C		jr $ra
1C30		nop

;------- subroutine -------
sub_1C34:
1C34		lis $v0, 0x3DC
1C38		ori $v0, $v0, 0x1A96; = 0x3DC1A96 - UNK
1C3C		host_call
1C40		jr $ra
1C44		nop

;------- subroutine -------
sub_1C48:
1C48		lis $v0, 0x8E0E
1C4C		ori $v0, $v0, 0x729D; = 0x8E0E729D - UNK
1C50		host_call
1C54		jr $ra
1C58		nop

;------- subroutine -------
sub_1C5C:
1C5C		lis $v0, 0xD36A
1C60		ori $v0, $v0, 0x127B; = 0xD36A127B - UNK
1C64		host_call
1C68		jr $ra
1C6C		nop

;------- subroutine -------
sub_1C70:
1C70		lis $v0, 0xCC4F
1C74		ori $v0, $v0, 0xD892; = 0xCC4FD892 - UNK
1C78		host_call
1C7C		jr $ra
1C80		nop

;------- subroutine -------
sub_1C84:
1C84		lis $v0, 0x686E
1C88		ori $v0, $v0, 0x4E0; = 0x686E04E0 - host_svcSendSyncRequest
1C8C		host_call
1C90		jr $ra
1C94		nop

;------- subroutine -------
sub_1C98:
1C98		lis $v0, 0x419C
1C9C		ori $v0, $v0, 0x3466; = 0x419C3466 - UNK
1CA0		host_call
1CA4		jr $ra
1CA8		nop

loc_1CAC:
1CAC		lis $v0, 0xF243
1CB0		ori $v0, $v0, 0xB10F; = 0xF243B10F - host_aes_enc_cbc
1CB4		host_call
1CB8		jr $ra
1CBC		nop

;------- subroutine -------
sub_1CC0:
1CC0		lis $v0, 0x44AA
1CC4		ori $v0, $v0, 0xA3FC; = 0x44AAA3FC - host_aes_ctr
1CC8		host_call
1CCC		jr $ra
1CD0		nop

;------- subroutine -------
sub_1CD4:
1CD4		lis $v0, 0x1A
1CD8		ori $v0, $v0, 0x6147; = 0x1A6147 - host_parse_ipc_cmd
1CDC		host_call
1CE0		jr $ra
1CE4		nop

;------- subroutine -------
sub_1CE8:
1CE8		lis $v0, 0x4587
1CEC		ori $v0, $v0, 0x2313; = 0x45872313 - host_vm_get_ptr
1CF0		host_call
1CF4		jr $ra
1CF8		nop

;------- subroutine -------
sub_1CFC:
1CFC		lis $v0, 0x671
1D00		ori $v0, $v0, 0xB828; = 0x671B828 - UNK
1D04		host_call
1D08		jr $ra
1D0C		nop

;------- subroutine -------
sub_1D10:
1D10		lis $v0, 0x6A23
1D14		ori $v0, $v0, 0x32BE; = 0x6A2332BE - UNK
1D18		host_call
1D1C		jr $ra
1D20		nop

;------- subroutine -------
sub_1D24:
1D24		lis $v0, 0x9B40
1D28		ori $v0, $v0, 0xC841; = 0x9B40C841 - host_crc32 (ptr r4r5, len r6)
1D2C		host_call
1D30		jr $ra
1D34		nop

;------- subroutine -------
sub_1D38:
1D38		lis $v0, 0x5A66
1D3C		ori $v0, $v0, 0x41E2; = 0x5A6641E2 - host_aes_set_key (ptr r4)
1D40		host_call
1D44		jr $ra
1D48		nop

;------- subroutine -------
sub_1D4C:
1D4C		lis $v0, 0xCC8A
1D50		ori $v0, $v0, 0x94A1; = 0xCC8A94A1 - host_memset
1D54		host_call
1D58		jr $ra
1D5C		nop

;------- subroutine -------
sub_1D60:
1D60		lis $v0, 0xCD86
1D64		ori $v0, $v0, 0x83D; = 0xCD86083D - UNK
1D68		host_call
1D6C		jr $ra
1D70		nop

loc_1D74:
1D74		lis $v0, 0xB66C
1D78		ori $v0, $v0, 0x364C; = 0xB66C364C - host_memcpy
1D7C		host_call
1D80		jr $ra
1D84		nop

;------- subroutine -------
sub_1D88:
1D88		lis $v0, 0x2E29
1D8C		ori $v0, $v0, 0x3BC3; = 0x2E293BC3 - UNK
1D90		host_call
1D94		jr $ra
1D98		nop

;------- subroutine -------
sub_1D9C:
1D9C		lis $v0, 0x74AD
1DA0		ori $v0, $v0, 0xB312; = 0x74ADB312 - host_read_u32
1DA4		host_call
1DA8		jr $ra
1DAC		nop

;------- subroutine -------
sub_1DB0:
1DB0		lis $v0, 0x70B8
1DB4		ori $v0, $v0, 0xF5BF; = 0x70B8F5BF - host_ipc_handle
1DB8		host_call
1DBC		jr $ra
1DC0		nop

;------- subroutine -------
sub_1DC4:
1DC4		lis $v0, 0x4BE3
1DC8		ori $v0, $v0, 0xD010; = 0x4BE3D010 - host_sha2 (ptr r4, len r5, dst ptr r6r7)
1DCC		host_call
1DD0		jr $ra
1DD4		nop

loc_1DD8:
1DD8		lis $v0, 0x8CFF
1DDC		ori $v0, $v0, 0xE3B; = 0x8CFF0E3B - host_vm_memset
1DE0		host_call
1DE4		jr $ra
1DE8		nop

;------- subroutine -------
sub_1DEC:
1DEC		lis $v0, 0x3766
1DF0		ori $v0, $v0, 0x570A; = 0x3766570A - host_get_field_98
1DF4		host_call
1DF8		jr $ra
1DFC		nop

;------- subroutine -------
sub_1E00:
1E00		lis $v0, 0x9321
1E04		ori $v0, $v0, 0x7280; = 0x93217280 - host_sha2_hmac
1E08		host_call
1E0C		jr $ra
1E10		nop

;------- subroutine -------
sub_1E14:
1E14		lis $v0, 0xCFEB
1E18		ori $v0, $v0, 0x35DC; = 0xCFEB35DC - UNK
1E1C		host_call
1E20		jr $ra
1E24		nop

;------- subroutine -------
sub_1E28:
1E28		lis $v0, 0xC8B0
1E2C		ori $v0, $v0, 0x77C8; = 0xC8B077C8 - host_expmod (dst r4, mod r5, exp r6, exp_size r7)
1E30		host_call
1E34		jr $ra
1E38		nop

;------- subroutine -------
sub_1E3C:
1E3C		lis $v0, 0xA049
1E40		ori $v0, $v0, 0xA7D6; = 0xA049A7D6 - host_fat_open_file
1E44		host_call
1E48		jr $ra
1E4C		nop

loc_1E50:
1E50		lis $v0, 0x537
1E54		ori $v0, $v0, 0x648D; = 0x537648D - UNK
1E58		host_call
1E5C		jr $ra
1E60		nop

;------- subroutine -------
sub_1E64:
1E64		lis $v0, 0x28DA
1E68		ori $v0, $v0, 0x2760; = 0x28DA2760 - host_vm_memcmp
1E6C		host_call
1E70		jr $ra
1E74		nop

;------- subroutine -------
sub_1E78:
1E78		lis $v0, 0x1205
1E7C		ori $v0, $v0, 0xF934; = 0x1205F934 - host_search_pattern
1E80		host_call
1E84		jr $ra
1E88		nop

;------- subroutine -------
sub_1E8C:
1E8C		lis $v0, 0xB79
1E90		ori $v0, $v0, 0x44DC; = 0xB7944DC - host_vm_memcpy (dst r4, src r5, size r6)
1E94		host_call
1E98		jr $ra
1E9C		nop

;------- subroutine -------
sub_1EA0:
1EA0		lis $v0, 0x9D39
1EA4		ori $v0, $v0, 0xD484; = 0x9D39D484 - host_rsa_oaep
1EA8		host_call
1EAC		jr $ra
1EB0		nop

;------- subroutine -------
sub_1EB4:
1EB4		j loc_1E50
1EB8		nop

;------- subroutine -------
sub_1EBC:
1EBC		addi $v0, $zero, 0x1
1EC0		st.32 [$a0 + 0x8], $v0
1EC4		addi $v0, $zero, -0x1
1EC8		st.32 [$a0 + 0x0], $a1
1ECC		jr $ra
1ED0		st.32 [$a0 + 0x4], $v0
