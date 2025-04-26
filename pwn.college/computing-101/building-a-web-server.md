```bash
as -o /tmp/server.o /tmp/server.s && ld -o /tmp/server /tmp/server.o
strace /tmp/server
./run /tmp/server
```

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
```asm


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
