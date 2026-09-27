


CREATE TABLE test(
a  varchar,
b  integer,
c integer,
d integer,
e varchar
)


SELECT * FROM test

SELECT * FROM test
WHERE actual_amount > 2000

SELECT * FROM test
WHERE actual_amount < 2000

SELECT * FROM test
WHERE budget_amount > 2000

SELECT * FROM test
WHERE budget_amount < 2000


SELECT sum(actual_amount) from test

SELECT sum(budget_amount) from test

SELECT AVG(budget_amount) from test

SELECT AVG(actual_amount) from test


SELECT max(actual_amount) from test







alter table test rename column a to
category

alter table test rename column b to
budget_amount
alter table test rename column c to
actual_amount
alter table test rename column description to
difference
alter table test rename column e to
description


insert into test(category,budget_amount,actual_amount,difference,description)
values ('water','1000','700','300','for next three month')


delete rwos


SELECT sum(budget_amount) from test

CREATE TABLE salary(
category varchar(20) not null,
actual_amount  numeric not null,
notes varchar(20) not null
)

select * from salary

INSERT into salary(category,actual_amount,notes)
values('salary','50000','salary for one month')

INSERT into salary(category,actual_amount,notes)
values('other','10000','earn from business')


ALTER TABLE test
add column payment varchar(10),
add column vendors varchar(20)


INSERT into test(payment)
values('paid')

SELECT * FROM test


