一切的前提，先执行：
```sh
bash && cd /challenge
```
# 命令行运行
## 1
直接run
```sh
./run
```
## 2 密码
```
[INFO] - the challenge will check for a hardcoded password over stdin : ukeoouql
```
run之后输入密码`ukeoouql`

## 3 参数
```
[INFO] - the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 1:sycckvgsxt
```
意思是argv\[1\]为sycckvgsxt
```sh
./run sycckvgsxt
```
## 4 环境变量
```
[INFO] - the challenge will check that env[KEY] holds value VALUE (listed to the right as KEY:VALUE) : hhfegr:qbchuogeyx
```
```sh
hhfegr=qbchuogeyx ./run
```
## 5 重定向输入
```
[INFO] - the challenge will check that input is redirected from a specific file path : /tmp/lxqhch
[INFO] - the challenge will check for a hardcoded password over stdin : pnefcavh
```
```sh
echo -n pnefcavh > /tmp/lxqhch
./run < /tmp/lxqhch
```
## 6 重定向输出
```
[INFO] - the challenge will check that output is redirected to a specific file path : /tmp/icjtji
```
```sh
./run > /tmp/icjtji
```
## 7 清空环境变量
```
[INFO] - the challenge will check that the environment is empty (except LC_CTYPE, which is impossible to get rid of in some cases)
```
```sh
env -i ./run 
```
# .sh脚本内容
写到`/tmp/ss.sh`中，然后执行
```sh
bash /tmp/ss.sh
```
## 8 shell脚本
```
[INFO] - the challenge checks for a specific parent process : shellscript
```
```sh
/challenge/run
```
## 9 密码
```
[INFO] - the challenge will check for a hardcoded password over stdin : sscpluhz
```
```sh
echo -n sscpluhz|./run
```
## 10 参数
```
[INFO] - the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 1:jlfuorcglj
```
```sh
./run jlfuorcglj
```
## 11 
```

```
```sh

```
## 12 
```

```
```sh

```
## 13 
```

```
```sh

```
## 14 
```

```
```sh

```
## 15 
```

```
```sh

```
## 16 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
## 
```

```
```sh

```
