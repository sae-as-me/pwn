```sh
as -o yyy.o zzz.s && ld -o xxx yyy.o && /challenge/run xxx
```
## set-register
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,0x1337

```
## set-multiple-registers
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,0x1337
mov r12,0xCAFED00D1337BEEF
mov rsp,0x31337

```
## add-to-register
```s
.intel_syntax noprefix
.global _start
_start:

add rdi,0x331337

```
## linear-equation-registers
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,rdi
imul rax,rsi
add rax,rdx

```
## integer-division
被除数128位：rdx|rax
div之后余数保留在rdx，商在rax
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,rdi
xor rdx,rdx
div rsi

```
## modulo-operation
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,rdi
xor rdx,rdx
div rsi
mov rax,rdx

```
## set-upper-byte
```s
.intel_syntax noprefix
.global _start
_start:

mov ah,0x42

```
## efficient-modulo
```s
.intel_syntax noprefix
.global _start
_start:

mov rcx,rdi
mov rax,0
mov al,cl

mov rbx,0
mov bx,si

```
## byte-extraction
```s
.intel_syntax noprefix
.global _start
_start:

mov rcx,rdi
mov rax,0
shr rcx,32
mov al,cl

```
## bitwise-and
```s
.intel_syntax noprefix
.global _start
_start:

and rdi,rsi
and rax,0
xor rax,rdi

```
## check-even
```s
.intel_syntax noprefix
.global _start
_start:

and rax,0
or rax,1
and rdi,1
xor rax,rdi

```
## memory-read
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,[0x404000]

```
## memory-write
```s
.intel_syntax noprefix
.global _start
_start:

mov [0x404000],rax

```
## memory-increment
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,[0x404000]
mov rbx,[0x404000]
add rbx,0x1337
mov [0x404000],rbx

```
## byte-access
```s
.intel_syntax noprefix
.global _start
_start:

xor rax,rax
mov al,[0x404000]

```
## momery-size-access
```s
.intel_syntax noprefix
.global _start
_start:

xor rax,rax
mov al,[0x404000]

xor rbx,rbx
mov bx,[0x404000]

xor rcx,rcx
mov ecx,[0x404000]

mov rdx,[0x404000]

```
## little-endian-write
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,0xdeadbeef00001337
mov [rdi],rax
mov rax,0xc0ffee0000
mov [rsi],rax

```
## memory-sum
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,0
mov [rsi],rax
mov rax,[rdi]
add [rsi],rax
mov rax,[rdi+8]
add [rsi],rax

```
## stack-subtraction
```s
.intel_syntax noprefix
.global _start
_start:

pop rax
sub rax,rdi
push rax

```
## swap-stack-values
```s
.intel_syntax noprefix
.global _start
_start:

push rdi
push rsi
pop rdi
pop rsi

```
## average-stack-values
```s
.intel_syntax noprefix
.global _start
_start:

mov rdx,0
mov rax,[rsp]
add rax,[rsp+8]
add rax,[rsp+0x10]
add rax,[rsp+0x18]
mov rbx,4
div rbx
push rax

```
## absolute-jump
**jmp reg**
```s
.intel_syntax noprefix
.global _start
_start:

mov rax,0x403000
jmp rax

```
## relative-jump
[.rept-\(ins\)-.endr](https://ftp.gnu.org/old-gnu/Manuals/gas-2.9.1/html_chapter/as_7.html#SEC116)
```s
.intel_syntax noprefix
.global _start
_start:

jmp des
.rept 0x51
    nop
.endr
des:
    mov rax,1

```
## jump-trampoline
```s
.intel_syntax noprefix
.global _start
_start:

jmp des
.rept 0x51
    nop
.endr
des:
    pop rdi
    mov rax,0x403000
    jmp rax

```
## conditional-jump
提示了`dword`，所以是4字节的运算
```s
.intel_syntax noprefix
.global _start
_start:
    mov ebx,[rdi]
    mov eax,[rdi+4]
    mov edx,0

    cmp ebx,0x7f454c46
    jne elif

    add eax,[rdi+8]
    add eax,[rdi+12]

    jmp done
elif:
    cmp ebx,0x00005A4D
    jne else

    sub eax,[rdi+8]
    sub eax,[rdi+12]

    jmp done
else:
    imul eax,[rdi+8]
    imul eax,[rdi+12]
done:
    nop

```
## indirect-jump
```s
.intel_syntax noprefix
.global _start
_start:
    mov rax,rdi
    shr rax,2
    cmp rax,0
    jne else
if0123:
    imul rdi,8
    add rsi,rdi
    jmp [rsi]
else:
    jmp [rsi+0x20]

```
## average-loop
```s
.intel_syntax noprefix
.global _start
_start:
    xor rdx,rdx
    xor rax,rax
    xor rcx,rcx
while:
    add rcx,1

    add rax,[rdi]
    add rdi,8

    cmp rcx,rsi
    jne while

    div rsi

```
## count-non-zero
```s

```
## string-lower
```s

```
## most-common-byte
```s

```
