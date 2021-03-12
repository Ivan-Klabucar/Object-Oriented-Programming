	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15	sdk_version 10, 15, 6
	.intel_syntax noprefix
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	sub	rsp, 32
	mov	dword ptr [rbp - 4], 0
	mov	edi, 16
	call	__Znwm
	mov	rdi, rax
	mov	qword ptr [rbp - 24], rax ## 8-byte Spill
	call	__ZN9CoolClassC1Ev
	mov	rax, qword ptr [rbp - 24] ## 8-byte Reload
	mov	qword ptr [rbp - 16], rax
	lea	rdi, [rbp - 8]
	mov	esi, 42
	call	__ZN13PlainOldClass3setEi
	mov	rax, qword ptr [rbp - 16]
	mov	rcx, qword ptr [rax]
	mov	rdi, rax
	mov	esi, 42
	call	qword ptr [rcx]
	xor	eax, eax
	add	rsp, 32
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN9CoolClassC1Ev      ## -- Begin function _ZN9CoolClassC1Ev
	.weak_def_can_be_hidden	__ZN9CoolClassC1Ev
	.p2align	4, 0x90
__ZN9CoolClassC1Ev:                     ## @_ZN9CoolClassC1Ev
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
	call	__ZN9CoolClassC2Ev
	add	rsp, 16
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN13PlainOldClass3setEi ## -- Begin function _ZN13PlainOldClass3setEi
	.weak_definition	__ZN13PlainOldClass3setEi
	.p2align	4, 0x90
__ZN13PlainOldClass3setEi:              ## @_ZN13PlainOldClass3setEi
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	mov	qword ptr [rbp - 8], rdi
	mov	dword ptr [rbp - 12], esi
	mov	rax, qword ptr [rbp - 8]
	mov	ecx, dword ptr [rbp - 12]
	mov	dword ptr [rax], ecx
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN9CoolClassC2Ev      ## -- Begin function _ZN9CoolClassC2Ev
	.weak_def_can_be_hidden	__ZN9CoolClassC2Ev
	.p2align	4, 0x90
__ZN9CoolClassC2Ev:                     ## @_ZN9CoolClassC2Ev
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
	mov	rax, qword ptr [rip + __ZTV9CoolClass@GOTPCREL]
	add	rax, 16
	mov	rcx, qword ptr [rbp - 16] ## 8-byte Reload
	mov	qword ptr [rcx], rax
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
	mov	rax, qword ptr [rip + __ZTV4Base@GOTPCREL]
	add	rax, 16
	mov	qword ptr [rbp - 8], rdi
	mov	rcx, qword ptr [rbp - 8]
	mov	qword ptr [rcx], rax
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN9CoolClass3setEi    ## -- Begin function _ZN9CoolClass3setEi
	.weak_def_can_be_hidden	__ZN9CoolClass3setEi
	.p2align	4, 0x90
__ZN9CoolClass3setEi:                   ## @_ZN9CoolClass3setEi
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	mov	qword ptr [rbp - 8], rdi
	mov	dword ptr [rbp - 12], esi
	mov	rax, qword ptr [rbp - 8]
	mov	ecx, dword ptr [rbp - 12]
	mov	dword ptr [rax + 8], ecx
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.globl	__ZN9CoolClass3getEv    ## -- Begin function _ZN9CoolClass3getEv
	.weak_def_can_be_hidden	__ZN9CoolClass3getEv
	.p2align	4, 0x90
__ZN9CoolClass3getEv:                   ## @_ZN9CoolClass3getEv
	.cfi_startproc
## %bb.0:
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset rbp, -16
	mov	rbp, rsp
	.cfi_def_cfa_register rbp
	mov	qword ptr [rbp - 8], rdi
	mov	rax, qword ptr [rbp - 8]
	mov	eax, dword ptr [rax + 8]
	pop	rbp
	ret
	.cfi_endproc
                                        ## -- End function
	.section	__DATA,__const
	.globl	__ZTV9CoolClass         ## @_ZTV9CoolClass
	.weak_def_can_be_hidden	__ZTV9CoolClass
	.p2align	3
__ZTV9CoolClass:
	.quad	0
	.quad	__ZTI9CoolClass
	.quad	__ZN9CoolClass3setEi
	.quad	__ZN9CoolClass3getEv

	.section	__TEXT,__const
	.globl	__ZTS9CoolClass         ## @_ZTS9CoolClass
	.weak_definition	__ZTS9CoolClass
__ZTS9CoolClass:
	.asciz	"9CoolClass"

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

	.globl	__ZTI9CoolClass         ## @_ZTI9CoolClass
	.weak_definition	__ZTI9CoolClass
	.p2align	3
__ZTI9CoolClass:
	.quad	__ZTVN10__cxxabiv120__si_class_type_infoE+16
	.quad	__ZTS9CoolClass
	.quad	__ZTI4Base

	.globl	__ZTV4Base              ## @_ZTV4Base
	.weak_def_can_be_hidden	__ZTV4Base
	.p2align	3
__ZTV4Base:
	.quad	0
	.quad	__ZTI4Base
	.quad	___cxa_pure_virtual
	.quad	___cxa_pure_virtual

.subsections_via_symbols
