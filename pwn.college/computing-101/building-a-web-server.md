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
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall number of socket
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
    mov rax,49                  # syscall number of bind
    syscall
listen:
    mov rdi,r10                 # the socket’s file descriptor
    mov rsi,0                   # a backlog parameter, which sets the maximum number of queued connections
    mov rax,50                  # syscall number of listen
    syscall
accept:
    mov rdi,r10                 # sockfd
    mov rsi,0                   # NULL
    mov rdx,0                   # NULL
    mov rax,43                  # syscall number of accept
    syscall
    mov r9,rax
read:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # addr to store <read_request>
    mov rdx,0x100               # <read_request_count>
    mov rax,0                   # syscall number of read
    syscall
write:
    mov rdi,r9                  # the value returned from accept
    mov rbx,0x00000000000a0d0a  # '\n\r\n'
    push rbx
    mov rbx,0x0d4b4f2030303220  # ' 200 OK\r'
    push rbx
    mov rbx,0x302e312f50545448  # 'HTTP/1.0'
    push rbx
    mov rsi,rsp                 # a pointer to a data buffer
    mov rdx,19                  # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
close:
    mov rdi,r9                  # the value returned from accept
    mov rax,3                   # syscall number of close
    syscall
exit:
    xor rdi,rdi                 # 0
    mov rax,60                  # syscall number of exit
    syscall

.section .data

```
## Dynamic Response
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall number of socket
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
    mov rax,49                  # syscall number of bind
    syscall
listen:
    mov rdi,r10                 # the socket’s file descriptor
    mov rsi,0                   # a backlog parameter, which sets the maximum number of queued connections
    mov rax,50                  # syscall number of listen
    syscall
accept:
    mov rdi,r10                 # sockfd
    mov rsi,0                   # NULL
    mov rdx,0                   # NULL
    mov rax,43                  # syscall number of accept
    syscall
    mov r9,rax
read1:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # addr to store <read_request>
    mov rdx,0x100               # <read_request_count>
    mov rax,0                   # syscall number of read
    syscall
    mov byte ptr [rsp+20],0      # to make the file string using '\x00'
open:
    mov rdi,rsp
    add rdi,4                   # del 'GET ' and point to '/'
    xor rsi,rsi                 # O_RDONLY
    mov rax,2                   # syscall number of open
    syscall
    mov r8,rax                  # save fd
read2:
    mov rdi,r8                  # the value returned from open
    mov rsi,rsp                 # addr to store <read_file>
    mov rdx,0x100               # <read_file_count>
    mov rax,0                   # syscall number of read
    syscall
    mov r10,rax                 # save read count
close1:
    mov rdi,r8                  # fd by open
    mov rax,3                   # syscall number of close
    syscall
write1:
    mov rdi,r9                  # the value returned from accept
    mov rbx,0x00000000000a0d0a  # '\n\r\n'
    push rbx
    mov rbx,0x0d4b4f2030303220  # ' 200 OK\r'
    push rbx
    mov rbx,0x302e312f50545448  # 'HTTP/1.0'
    push rbx
    mov rsi,rsp                 # a pointer to a data buffer
    mov rdx,19                  # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
write2:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # a pointer to a data buffer-8*3
    add rsi,24                  # a pointer to a data buffer
    mov rdx,r10                 # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
close2:
    mov rdi,r9                  # the value returned from accept
    mov rax,3                   # syscall number of close
    syscall
exit:
    xor rdi,rdi                 # 0
    mov rax,60                  # syscall number of exit
    syscall

.section .data

```
## Iterative GET Server
加点判断条件和jmp跳回
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall number of socket
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
    mov rax,49                  # syscall number of bind
    syscall
listen:
    mov rdi,r10                 # the socket’s file descriptor
    mov rsi,0                   # a backlog parameter, which sets the maximum number of queued connections
    mov rax,50                  # syscall number of listen
    syscall
accept:
    mov rdi,r10                 # sockfd
    mov rsi,0                   # NULL
    mov rdx,0                   # NULL
    mov rax,43                  # syscall number of accept
    syscall
    iferr:
        cmp rax,-1              # return -1 if accept error
        je exit 
    else:
        mov r9,rax              # save accept fd
read1:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # addr to store <read_request>
    mov rdx,0x100               # <read_request_count>
    mov rax,0                   # syscall number of read
    syscall
    mov byte ptr [rsp+20],0     # to make the file string using '\x00'
open:
    mov rdi,rsp
    add rdi,4                   # del 'GET ' and point to '/'
    xor rsi,rsi                 # O_RDONLY
    mov rax,2                   # syscall number of open
    syscall
    mov r8,rax                  # save fd
read2:
    mov rdi,r8                  # the value returned from open
    mov rsi,rsp                 # addr to store <read_file>
    mov rdx,0x100               # <read_file_count>
    mov rax,0                   # syscall number of read
    syscall
    mov r12,rax                 # save read count
close1:
    mov rdi,r8                  # fd by open
    mov rax,3                   # syscall number of close
    syscall
write1:
    mov rdi,r9                  # the value returned from accept
    mov rbx,0x00000000000a0d0a  # '\n\r\n'
    push rbx
    mov rbx,0x0d4b4f2030303220  # ' 200 OK\r'
    push rbx
    mov rbx,0x302e312f50545448  # 'HTTP/1.0'
    push rbx
    mov rsi,rsp                 # a pointer to a data buffer
    mov rdx,19                  # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
write2:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # a pointer to a data buffer-8*3
    add rsi,24                  # a pointer to a data buffer
    mov rdx,r12                 # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
close2:
    mov rdi,r9                  # the value returned from accept
    mov rax,3                   # syscall number of close
    syscall
    jmp accept
exit:
    xor rdi,rdi                 # 0
    mov rax,60                  # syscall number of exit
    syscall

.section .data

```
## Concurrent GET Server
```asm
.intel_syntax noprefix
.globl _start

.section .text

_start:

socket:
    mov rdi,2                   # AF_INET for IPv4 is 2
    mov rsi,1                   # SOCK_STREAM for TCP is 1
    mov rdx,0                   # the protocol (usually set to 0 to choose the default)
    mov rax,41                  # syscall number of socket
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
    mov rax,49                  # syscall number of bind
    syscall
listen:
    mov rdi,r10                 # the socket’s file descriptor
    mov rsi,0                   # a backlog parameter, which sets the maximum number of queued connections
    mov rax,50                  # syscall number of listen
    syscall
accept:
    mov rdi,r10                 # sockfd
    mov rsi,0                   # NULL
    mov rdx,0                   # NULL
    mov rax,43                  # syscall number of accept
    syscall
    iferr:
        cmp rax,-1              # return -1 if accept error
        je exit 
    else:
        mov r9,rax              # save accept fd
fork:
    mov rax,57                  # syscall number of fork
    syscall
    ifnochild:
        cmp rax,0               # is it parent process?
        jne close2              # the parent process immediately returns to accept additional connections
close3:
    mov rdi,r10                 # parent process fd
    mov rax,3
    syscall
read1:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # addr to store <read_request>
    mov rdx,0x100               # <read_request_count>
    mov rax,0                   # syscall number of read
    syscall
    mov byte ptr [rsp+20],0      # to make the file string using '\x00'
open:
    mov rdi,rsp
    add rdi,4                   # del 'GET ' and point to '/'
    xor rsi,rsi                 # O_RDONLY
    mov rax,2                   # syscall number of open
    syscall
    mov r8,rax                  # save fd
read2:
    mov rdi,r8                  # the value returned from open
    mov rsi,rsp                 # addr to store <read_file>
    mov rdx,0x100               # <read_file_count>
    mov rax,0                   # syscall number of read
    syscall
    mov r12,rax                 # save read count
close1:
    mov rdi,r8                  # fd by open
    mov rax,3                   # syscall number of close
    syscall
write1:
    mov rdi,r9                  # the value returned from accept
    mov rbx,0x00000000000a0d0a  # '\n\r\n'
    push rbx
    mov rbx,0x0d4b4f2030303220  # ' 200 OK\r'
    push rbx
    mov rbx,0x302e312f50545448  # 'HTTP/1.0'
    push rbx
    mov rsi,rsp                 # a pointer to a data buffer
    mov rdx,19                  # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
write2:
    mov rdi,r9                  # the value returned from accept
    mov rsi,rsp                 # a pointer to a data buffer-8*3
    add rsi,24                  # a pointer to a data buffer
    mov rdx,r12                 # the number of bytes to write
    mov rax,1                   # syscall number of write
    syscall
    jmp exit                    # child process exit
close2:
    mov rdi,r9                  # the value returned from accept
    mov rax,3                   # syscall number of close
    syscall
    jmp accept
exit:
    xor rdi,rdi                 # 0
    mov rax,60                  # syscall number of exit
    syscall

.section .data

```
## Concurrent POST Server
```asm

```
## Web Server
```asm

```
