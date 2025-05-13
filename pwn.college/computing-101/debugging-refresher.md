## 1
```gdb
r
c
```
## 2
```gdb
r
p/x $r12
c
```
## 3
```gdb
r
set disassembly-flavor intel
disas main

c
x/gx $rbp-0x18
```
## 4
```gdb
r
set disassembly-flavor intel
disas main
b *0x00005959c7d80cab
c
x/gx $rbp-0x18
c
...
```
## level5
**`source aaa.gdb`** 
```gdb
r
b *main+709
c
set $i=0
while($i<10)
  set $i--
  set $num=*(unsigned long long*)($rbp-0x18)
  printf "The random num: %llx\n", $num
  c
end
```
## 6
```gdb
r
b *main+686
c
set $i=0
while($i<100)
  set $i--
  set $rax=0
  set $rdx=0
  c
end
```
## 7
```gdb
r
call (void)win()
```
## 8
```gdb
r
disas win
b *0x00005968d9b6295d
call (void)win()
set $rip=0x00005968d9b6296b
c
```
