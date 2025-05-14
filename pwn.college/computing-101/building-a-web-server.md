```sh
as -o yyy.o zzz.s && ld -o xxx yyy.o && /challenge/run xxx
```
[system call table](https://x64.syscall.sh/)
[func description](https://man7.org/linux/man-pages/man2/)
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
struct sockaddr*则需要自己构建，其中IPv4的struct sockaddr_in整体结构如下：

![图片](https://github.com/user-attachments/assets/e559ec8e-d362-47d8-af31-bd756614456b)

这里选择把相关的数据压栈
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall num of socket()
    syscall
bind:
    mov rdi,rax                 # the socket file descriptor, gen by socket() and stored in rax
    xor rbx,rbx                 # rbx=0
    push rbx                    # \x00 * 8 : uint8_t __pad[8]
    mov rbx,0x0000000050000002  # little endian [2, 80, 0.0.0.0]:[AF_INET, htons(80), inet_addr("0.0.0.0")] 
    push rbx                    # push to stack, then rsp pointer to this struct sockaddr
    mov rsi,rsp                 
    mov rdx,0x10                # the size of that structure
    mov rax,49                  # syscall num of bind()
    syscall
exit:
    xor rdi,rdi
    mov rax,60
    syscall

.section .data

```
## Listen
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall num of socket
    syscall
    mov r10,rax                 # save sockfd
bind:
    mov rdi,r10                 # the socket file descriptor, gen by socket() and stored in rax
    xor rbx,rbx                 # rbx=0
    push rbx                    # \x00 * 8 : uint8_t __pad[8]
    mov rbx,0x0000000050000002  # little endian [2, 80, 0.0.0.0]:[AF_INET, htons(80), inet_addr("0.0.0.0")] 
    push rbx                    # push to stack, then rsp pointer to this struct sockaddr
    mov rsi,rsp                 
    mov rdx,0x10                # the size of that structure
    mov rax,49                  # syscall num of bind
    syscall
listen:
    mov rdi,r10                 # the socket’s file descriptor
    mov rsi,0                   # a backlog parameter, which sets the maximum number of queued connections
    mov rax,50                  # syscall num of listen
    syscall
exit:
    xor rdi,rdi
    mov rax,60
    syscall

.section .data

```
## Accept
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall num of socket
    syscall
    mov r10,rax                 # save sockfd
bind:
    mov rdi,r10                 # the socket file descriptor, gen by socket() and stored in rax
    xor rbx,rbx                 # rbx=0
    push rbx                    # \x00 * 8 : uint8_t __pad[8]
    mov rbx,0x0000000050000002  # little endian [2, 80, 0.0.0.0]:[AF_INET, htons(80), inet_addr("0.0.0.0")] 
    push rbx                    # push to stack, then rsp pointer to this struct sockaddr
    mov rsi,rsp                 
    mov rdx,0x10                # the size of that structure
    mov rax,49                  # syscall num of bind
    syscall
listen:
    mov rdi,r10                 # the socket’s file descriptor
    mov rsi,0                   # a backlog parameter, which sets the maximum number of queued connections
    mov rax,50                  # syscall num of listen
    syscall
accept:
    mov rdi,r10                 # sockfd
    mov rsi,0                   # NULL
    mov rdx,0                   # NULL
    mov rax,43                  # syscall num of accept
    syscall
exit:
    xor rdi,rdi
    mov rax,60
    syscall

.section .data

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
