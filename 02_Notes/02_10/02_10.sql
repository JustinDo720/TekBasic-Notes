show databases;

use tekbasic_training;

show tables;

select * from autoincrementcourse;

# DDL
create table Student(
    id int primary key auto_increment,
    fullname varchar(20) not null,
    course_id int not null,
    phone_number char(11) unique,
    # Define foriegn key on table level
    foreign key(course_id) references autoincrementcourse(id)

);

insert into Student(fullname, course_id, phone_number)
    values('Thy N', 3, '123123'),
          ('Thy N', 2, '1231233'),
          ('Justin D', 3, '123');

select fullname, course_id from Student;


create table `countries`(
    `COUNTRY_ID` varchar(2) primary key,
    `COUNTRY_NAME` varchar(40) DEFAULT NULL,
    `REGION_ID` decimal(10,0) default null
);

insert into `countries`(`COUNTRY_ID`, `COUNTRY_NAME`, `REGION_ID`)
values ('C1','United State',1001),
       ('C4','Vietnam',NULL),
       ('C5','Indonesia',NULL),
       ('C2','England',1002),
       ('C3','Netherland',1002),
       ('C7','Poland',1004),
       ('C8','Cananda',1001),
       ('C9','Thailand',1005),
       ('D1','Singapore',1005);

select * from countries
where `REGION_ID` = 1001;

select * from `countries`
# Desc but Asc by default
ORDER BY `COUNTRY_ID` desc;

select * from `countries`
order by `REGION_ID`, `COUNTRY_NAME`;

select `REGION_ID`, count(*) from `countries`
group by `REGION_ID`;

select * from countries where not (`REGION_ID` = 1001);

select * from countries
where `COUNTRY_NAME` like '___a__';