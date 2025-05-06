## newline troubles
```sh
echo -n 'khmissww' | ./runme
```
## reasoning about files
```sh
echo -n raedtcpz > /tmp/bllt
cd /tmp
/challenge/runme
```
## decoding hex
```py
# pwntools provides functions for converting to / from
# hexadecimal representations of byte strings
enhex(b'/flag')      # = '2f666c6167'
unhex('2f666c6167')  # = b'/flag'
```
```py
from pwn import *
p=process("/challenge/runme")

p.send(unhex('c994be86fdbfc5a5'))
print(p.recvall().decode())
```
## encoding practice
```py

from pwn import *
p=process("/challenge/runme")
correct_password = b"\xbc\xe0\xaa\xb2\xde\xee\x98\x9f"

p.send(bin(int(bytes.hex(correct_password),16))[2:])

print(p.recvall().decode())
```
## hex-encoding ascii
```py

from pwn import *
p=process("/challenge/runme")
correct_password = b"eewqcnzx"

ans=enhex(correct_password)
print('send:',ans)

p.send(ans)
print(p.recvall().decode())

```
## nested encoding
```py

from pwn import *
correct_password = b"vsxoinjj"

ans=enhex(enhex(enhex(enhex(correct_password).encode()).encode()).encode())
print('send:',ans)

f=open('/tmp/aaa','w')
f.write(ans)
f.close()

```
## hex-encoding utf-8
```py

from pwn import *
correct_password = "📣 🎮 🐸 🆖".encode("utf-8")

ans=enhex(correct_password)
print('send:',ans)

f=open('/tmp/aaa','w')
f.write(ans)
f.close()

p=process(["/challenge/runme",'/tmp/aaa'])
print(p.recvall().decode())

```
## utf mixups
```py

from pwn import *
correct_password = b"amoozuff"

ans=correct_password.decode().encode('utf-16')
print('send:',ans)

f=open('/tmp/aaa','wb')
f.write(ans)
f.close()

p=process(["/challenge/runme",'/tmp/aaa'])
print(p.recvall().decode())

```
## modifying encoded data
```py

from pwn import *
p=process('/challenge/runme')

correct_password = b"\x8a\x00\x9e\xce\x00\xb8\x83R"

ans=enhex(correct_password)[::-1]
print('send:',ans)

p.send(ans)
print(p.recvall().decode())

```
## decoding base64
```py
# pwntools provides functions for converting to / from
# base64 representations of byte strings
b64e(b'/flag')    # = 'L2ZsYWc='
b64d('L2ZsYWc=')  # = b'/flag'
```
```py

from pwn import *
p=process('/challenge/runme')

correct_password = b"cp5gjPNqjBQ="

ans=b64d(correct_password.decode())
print('send:',ans)

p.send(ans)
print(p.recvall().decode())

```
## encoding base64
```py
# pwntools provides functions for converting to / from
# base64 representations of byte strings
b64e(b'/flag')    # = 'L2ZsYWc='
b64d('L2ZsYWc=')  # = b'/flag'
```
```py

from pwn import *
p=process('/challenge/runme')

correct_password = b"\xe2\twT\x88\xa7\xae\xd3"

ans=b64e(correct_password)
print('send:',ans)

p.send(ans)
print(p.recvall().decode())

```
## dealing with obfuscation
```py

from pwn import *
p=process('/challenge/runme')

correct_password = b"\x7f?rAL\x81\xa7d"[::-1]

ans=b64e(correct_password)
print('send:',ans)

p.send(ans)
print(p.recvall().decode())

```
## dealing with obfuscation 2
```py

from pwn import *
import base64

p=process('/challenge/runme')

def encode_to_bits(s):
    return b"".join(format(c, "08b").encode("latin1") for c in s)

correct_password = b"\x08\x9e\xb3zP\x03\x02\x03"

correct_password = base64.b64encode(correct_password)
correct_password = correct_password.hex().encode("l1")
correct_password = encode_to_bits(correct_password)
correct_password = correct_password[::-1]

ans=enhex(correct_password)
ans=enhex(ans.encode())
ans=enhex(ans.encode())[::-1]
print('send:',ans)

p.send(ans)
print(p.recvall().decode())

```
