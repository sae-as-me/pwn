```sh
as -o yyy.o zzz.s && ld -o xxx yyy.o && /challenge/run xxx
```
[system call table](https://x64.syscall.sh/)
## Exit
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:
    mov rdi, 0
    mov rax, 60     # SYS_exit
    syscall

.section .data

```
## Socket
IPv4的`AF_INET`值是**2**

TCP的`SOCK_STREAM`常见是**1**
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2
    mov rsi,1
    mov rdx,0
    mov rax,41
    syscall
exit:
    xor rdi,rdi
    mov rax,60
    syscall

.section .data

```
## Bind
```asm

```
## Listen
```asm

```
## Accept
```asm

```
## Static Response
```asm

```
## Dynamic Response
```asm

```
## Iterative GET Server
```asm

```
## Concurrent GET Server
```asm

```
## Concurrent POST Server
```asm

```
## Web Server
```asm

```
