**`source aaa.gdb`** 
## level5
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
