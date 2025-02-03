# Showing all of the databases within our localhost
show databases;
use tekbasic_training;


create table t0 (
    c1 int,
    c2 char(5)
);

show tables;

alter table t0 modify column c2 varchar(11);

alter table t0 rename column c2 to c3;

alter table t0 add c2 char(10);

show tables;
select * from t0;


# DML
create table Course(
    id int,
    name varchar(20) not null
);

insert into Course
values (2, "Python");

insert into Course(name, id)
values('Machine Learning', 1);

select name,id from Course;

delete from Course
where id = 1;

select name,id from Course;

alter table Course modify column id int primary key;

update Course set name = 'Javascript' where id = 2;

create user 'test'@'localhost' identified by 'password';
alter user `test`@`localhost` identified  by 'new_password';

select user from mysql.user;

create table AutoIncrementCourse(
                                    id int primary key auto_increment,
                                    name varchar(20) not null
);

insert into AutoIncrementCourse(name)
values ('Python'), ('Javascript'), ('Machine Learning');

# TCL
start transaction;
update AutoIncrementCourse set name = 'Generative AI' where id= 2;
select * from AutoIncrementCourse;

savepoint genai1;

update AutoIncrementCourse set name = 'Generative AI 2' where id= 2;
select * from AutoIncrementCourse;

rollback to genai1;
select * from AutoIncrementCourse;  # We ignore that update for Gen AI 2

update AutoIncrementCourse set name = 'Generative AI 3' where id= 2;
select * from AutoIncrementCourse;
commit;

