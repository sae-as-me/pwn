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
```s

```
## modulo-operation
```s

```
## set-upper-byte
```s

```
## efficient-modulo
```s

```
## byte-extraction
```s

```
## bitwise-and
```s

```
## check-even
```s

```
## memory-read
```s

```
## memory-write
```s

```
## memory-increment
```s

```
## byte-access
```s

```
## momery-size-access
```s

```
## little-endian-write
```s

```
## memory-sum
```s

```
## stack-subtraction
```s

```
## swap-stack-values
```s

```
## average-stack-values
```s

```
## absolute-jump
```s

```
## relative-jump
```s

```
## jump-trampoline
```s

```
## conditional-jump
```s

```
## indirect-jump
```s

```
## average-loop
```s

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
