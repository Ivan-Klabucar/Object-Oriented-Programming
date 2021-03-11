	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15	sdk_version 10, 15, 6
	.intel_syntax noprefix
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
Lfunc_begin0:
	.cfi_startproc
	.cfi_personality 155, ___gxx_personality_v0
	.cfi_lsda 16, Lexception0
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 48
	mov	edi, 8
	call	__Znwm
	mov	rcx, rax
	mov	rdx, rax
Ltmp0:
	mov	rdi, rax
	mov	qword ptr [rbp - 32], rcx ## 8-byte Spill
	mov	qword ptr [rbp - 40], rdx ## 8-byte Spill
	call	__ZN7DerivedC1Ev
Ltmp1:
	jmp	LBB0_1
LBB0_1:
	mov	rax, qword ptr [rbp - 40] ## 8-byte Reload
	mov	qword ptr [rbp - 8], rax
	mov	rcx, qword ptr [rbp - 8]
	mov	rdi, rcx
	call	__ZN4Base6metodaEv
	xor	eax, eax
	add	rsp, 48
	pop	rbp
	ret
LBB0_2:
Ltmp2:
                                        ## kill: def $edx killed $edx killed $rdx
	mov	qword ptr [rbp - 16], rax
	mov	dword ptr [rbp - 20], edx
	mov	rdi, qword ptr [rbp - 32] ## 8-byte Reload
	call	__ZdlPv
## %bb.3:
	mov	rdi, qword ptr [rbp - 16]
	call	__Unwind_Resume
	ud2
Lfunc_end0:
	.cfi_endproc
	.section	__TEXT,__gcc_except_tab
	.p2align	2
GCC_except_table0:
Lexception0:
	.byte	255                     ## @LPStart Encoding = omit
	.byte	255                     ## @TType Encoding = omit
	.byte	1                       ## Call site Encoding = uleb128
	.uleb128 Lcst_end0-Lcst_begin0
Lcst_begin0:
	.uleb128 Lfunc_begin0-Lfunc_begin0 ## >> Call Site 1 <<
	.uleb128 Ltmp0-Lfunc_begin0     ##   Call between Lfunc_begin0 and Ltmp0
	.byte	0                       ##     has no landing pad
	.byte	0                       ##   On action: cleanup
	.uleb128 Ltmp0-Lfunc_begin0     ## >> Call Site 2 <<
	.uleb128 Ltmp1-Ltmp0            ##   Call between Ltmp0 and Ltmp1
	.uleb128 Ltmp2-Lfunc_begin0     ##     jumps to Ltmp2
	.byte	0                       ##   On action: cleanup
	.uleb128 Ltmp1-Lfunc_begin0     ## >> Call Site 3 <<
	.uleb128 Lfunc_end0-Ltmp1       ##   Call between Ltmp1 and Lfunc_end0
	.byte	0                       ##     has no landing pad
	.byte	0                       ##   On action: cleanup
Lcst_end0:
	.p2align	2
                                        ## -- End function
	.section	__TEXT,__text,regular,pure_instructions
	.globl	__ZN7DerivedC1Ev        ## -- Begin function _ZN7DerivedC1Ev
	.weak_def_can_be_hidden	__ZN7DerivedC1Ev
	.p2align	4, 0x90
__ZN7DerivedC1Ev:                       ## @_ZN7DerivedC1Ev
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 16
	mov	qword ptr [rbp - 8], rdi
	mov	rdi, qword ptr [rbp - 8]
	call	__ZN7DerivedC2Ev
	add	rsp, 16
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN4Base6metodaEv      ## -- Begin function _ZN4Base6metodaEv
	.weak_definition	__ZN4Base6metodaEv
	.p2align	4, 0x90
__ZN4Base6metodaEv:                     ## @_ZN4Base6metodaEv
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 32
	mov	qword ptr [rbp - 8], rdi
	mov	rax, qword ptr [rbp - 8]
	lea	rdi, [rip + L_.str.2]
	mov	qword ptr [rbp - 16], rax ## 8-byte Spill
	mov	al, 0
	call	_printf
	mov	rcx, qword ptr [rbp - 16] ## 8-byte Reload
	mov	rdx, qword ptr [rcx]
	mov	rdi, rcx
	mov	dword ptr [rbp - 20], eax ## 4-byte Spill
	call	qword ptr [rdx]
	add	rsp, 32
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN7DerivedC2Ev        ## -- Begin function _ZN7DerivedC2Ev
	.weak_def_can_be_hidden	__ZN7DerivedC2Ev
	.p2align	4, 0x90
__ZN7DerivedC2Ev:                       ## @_ZN7DerivedC2Ev
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 16
	mov	qword ptr [rbp - 8], rdi
	mov	rax, qword ptr [rbp - 8]
	mov	rcx, rax
	mov	rdi, rcx
	mov	qword ptr [rbp - 16], rax ## 8-byte Spill
	call	__ZN4BaseC2Ev
	mov	rax, qword ptr [rip + __ZTV7Derived@GOTPCREL]
	add	rax, 16
	mov	rcx, qword ptr [rbp - 16] ## 8-byte Reload
	mov	qword ptr [rcx], rax
	mov	rdi, rcx
	call	__ZN4Base6metodaEv
	add	rsp, 16
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN4BaseC2Ev           ## -- Begin function _ZN4BaseC2Ev
	.weak_def_can_be_hidden	__ZN4BaseC2Ev
	.p2align	4, 0x90
__ZN4BaseC2Ev:                          ## @_ZN4BaseC2Ev
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 16
	mov	rax, qword ptr [rip + __ZTV4Base@GOTPCREL]
	add	rax, 16
	mov	qword ptr [rbp - 8], rdi
	mov	rcx, qword ptr [rbp - 8]
	mov	qword ptr [rcx], rax
	mov	rdi, rcx
	call	__ZN4Base6metodaEv
	add	rsp, 16
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN7Derived15virtualnaMetodaEv ## -- Begin function _ZN7Derived15virtualnaMetodaEv
	.weak_def_can_be_hidden	__ZN7Derived15virtualnaMetodaEv
	.p2align	4, 0x90
__ZN7Derived15virtualnaMetodaEv:        ## @_ZN7Derived15virtualnaMetodaEv
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 16
	mov	qword ptr [rbp - 8], rdi
	lea	rdi, [rip + L_.str.1]
	mov	al, 0
	call	_printf
	add	rsp, 16
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN4Base15virtualnaMetodaEv ## -- Begin function _ZN4Base15virtualnaMetodaEv
	.weak_def_can_be_hidden	__ZN4Base15virtualnaMetodaEv
	.p2align	4, 0x90
__ZN4Base15virtualnaMetodaEv:           ## @_ZN4Base15virtualnaMetodaEv
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 16
	mov	qword ptr [rbp - 8], rdi
	lea	rdi, [rip + L_.str]
	mov	al, 0
	call	_printf
	add	rsp, 16
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.section	__DATA,__const
	.globl	__ZTV7Derived           ## @_ZTV7Derived
	.weak_def_can_be_hidden	__ZTV7Derived
	.p2align	3
__ZTV7Derived:
	.quad	0
	.quad	__ZTI7Derived
	.quad	__ZN7Derived15virtualnaMetodaEv

	.section	__TEXT,__const
	.globl	__ZTS7Derived           ## @_ZTS7Derived
	.weak_definition	__ZTS7Derived
__ZTS7Derived:
	.asciz	"7Derived"

	.globl	__ZTS4Base              ## @_ZTS4Base
	.weak_definition	__ZTS4Base
__ZTS4Base:
	.asciz	"4Base"

	.section	__DATA,__const
	.globl	__ZTI4Base              ## @_ZTI4Base
	.weak_definition	__ZTI4Base
	.p2align	3
__ZTI4Base:
	.quad	__ZTVN10__cxxabiv117__class_type_infoE+16
	.quad	__ZTS4Base

	.globl	__ZTI7Derived           ## @_ZTI7Derived
	.weak_definition	__ZTI7Derived
	.p2align	3
__ZTI7Derived:
	.quad	__ZTVN10__cxxabiv120__si_class_type_infoE+16
	.quad	__ZTS7Derived
	.quad	__ZTI4Base

	.globl	__ZTV4Base              ## @_ZTV4Base
	.weak_def_can_be_hidden	__ZTV4Base
	.p2align	3
__ZTV4Base:
	.quad	0
	.quad	__ZTI4Base
	.quad	__ZN4Base15virtualnaMetodaEv

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"ja sam bazna implementacija!\n"

L_.str.1:                               ## @.str.1
	.asciz	"ja sam izvedena implementacija!\n"

L_.str.2:                               ## @.str.2
	.asciz	"Metoda kaze: "

.subsections_via_symbols
