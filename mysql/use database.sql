# show databases;

# 注释
/*
 注
 释 
 */

#use sakila; # 使用数据库
#select database(); # 查看当前使用的数据库

# create database testBase charset utf8; # 创建自己的数据库
# drop database testbase; # 删除数据库
#show databases;

use world;
show tables; #要先选择数据库

create table student(
id int,
name varchar(10),#表示10个字符的字符串  #主要类型有timestamp float 
gender varchar(1),
age int
);

drop table student; # 删表
drop table if exists;

use world;
insert into student(id) value(1),(2),(3); # 在student的表里的id列插入值1、2、3三行
insert into student(id,name,gender,age) value(4,'z1jhp','女',2), (5,'zfjdx','男',9), (6,'lj8l','女',2);

delete from student where id>5 #删除表内的行，按where后的条件删，不写条件删全部,比较符合有> < >= !=

update student set name = '哈利波特' where id=1 # 在id等于1的地方把name改成哈利波特

select name,gender from student # 从student里面选择这两个列进行展示
select * from student #查看全部列
select * from student where id<100

# by 和 select后面的内容相同
select gender, avg(age),max(age) from student group by gender #在学生表里面将每行按gender分组（男女两组），分组后求出每组的平均年龄，并将select gender作为avg 的前置说明
# 还有sum avg min max count(求数量)

# asc(ascend) ->升序 desc(descend) ->降序
select * from student where age>3 order by age asc
select * from student where age>0 order by age asc limit 3 #限制三条，如果3改成 3,3 就表示从第三条往后取三条显示
# 执行顺序：from,where,group by与函数，select，order by,limit