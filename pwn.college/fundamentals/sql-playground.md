```sql
select * from assets
```
```sql
select * from details where flag_tag==1337
```
```sql
select datum from resources where flag_tag==1337
```
`%`=`.*`, `_`=`.`
```sql
select datum from fragments where datum like 'pwn.college%'
```
```sql
select record from secrets where flag_tag == 'yep'
```
这里少了一条
```sql
select substr(field, 1, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 6, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 11, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 16, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 21, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 26, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 31, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 36, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 41, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 46, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 51, 5) from repository where substr(field, 1, 11) = 'pwn.college' UNION ALL select substr(field, 56, 5) from repository where substr(field, 1, 11) = 'pwn.college' 
```
```sql
select entry from payloads where flag_tag == 1337 and entry like 'pwn.college%'
```
```sql
select payload from entries where payload like 'pwn.college%' limit 1
```
```sql
select tbl_name from sqlite_master
select * from ZFOyqLMr
```
