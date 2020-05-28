use bigdata;
create table users(
id int not null auto_increment,
email varchar(255) not null,
pw varchar(255) not null,
primary key(id)
);
desc users;
insert into users(email, pw) values('hong1@naver.com','1234');
insert into users(email, pw) values('hong2@naver.com','1234');
insert into users(email, pw) values('hong3@naver.com','1234');
select id, pw from users; 