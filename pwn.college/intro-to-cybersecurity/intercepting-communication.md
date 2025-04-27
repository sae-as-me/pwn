```sh
/challenge/run
```
## scan1
```sh
for i in $(seq 255); do
  timeout 1 ping 10.0.0.$i
done
```

