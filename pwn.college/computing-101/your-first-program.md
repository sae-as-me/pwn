## your first register
```s
mov rax,60
```
## your first syscall
```s
mov rax,60
syscall
```
## exit codes
```s
mov rax,60
mov rdi,42
syscall
```
## building executables
```sh
as -o yyy.o zzz.s && ld -o xxx yyy.o && /challenge/check xxx
```
```s
.intel_syntax noprefix
.global _start
_start:
mov rax,60
mov rdi,42
syscall

```
## moving between registers
```s
.intel_syntax noprefix
.global _start
_start:
mov rax,60
mov rdi,rsi
syscall

```
