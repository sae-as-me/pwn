## loading from memory
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[133700]

mov rax,60
syscall

```
## more loading practice
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[123400]

mov rax,60
syscall

```
## dereferencing pointers
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[rax]

mov rax,60
syscall

```
## dereferencing yourself
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[rdi]

mov rax,60
syscall

```
## dereferencing with offsets
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[rdi+8]

mov rax,60
syscall

```
## stored addresses
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[567800]
mov rdi,[rdi]

mov rax,60
syscall

```
## double dereference
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[rax]
mov rdi,[rdi]

mov rax,60
syscall

```
## triple dereference
```s
.intel_syntax noprefix
.global _start
_start:

mov rdi,[rdi]
mov rdi,[rdi]
mov rdi,[rdi]

mov rax,60
syscall

```
