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
