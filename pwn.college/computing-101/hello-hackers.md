## writing output
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,1
mov rsi,1337000
mov rdx,1

mov rax,1
syscall

```
## chaining syscalls
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,1
mov rsi,1337000
mov rdx,1

mov rax,1
syscall

mov rdi,42

mov rax,60
syscall

```
## writing strings
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,1
mov rsi,1337000
mov rdx,14

mov rax,1
syscall

mov rdi,42

mov rax,60
syscall

```
## reading data
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,0
mov rsi,1337000
mov rdx,8

mov rax,0
syscall

mov rdi,1
mov rsi,1337000
mov rdx,8

mov rax,1
syscall

mov rdi,42

mov rax,60
syscall

```
