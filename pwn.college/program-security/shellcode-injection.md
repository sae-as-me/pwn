# level
[x64.syscall.sh](https://x64.syscall.sh/): Your cheat sheet for syscalls. A glance here, and you're always ahead.

[syscalls manpage](https://man7.org/linux/man-pages/man2/syscalls.2.html): Understand not just the calls, but their deeper implications.

[felix cloutier](https://www.felixcloutier.com/x86/): Dive into the heartbeats of instructions, ensuring you're always in step.

[x86asm reference](http://ref.x86asm.net/coder64.html): Decode the bytes into moves, turning the tables on any challenge.

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

## 4

## 5

## 6

## 7

## 8

## 9

## 10

## 11

## 12

## 13

## 14
