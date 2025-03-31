create database sign;
use sign;

select * from society;

create table society(
SocietyID int NOT NULL PRIMARY key auto_increment,
society_name varchar (150)
);

select * from student;

create table student(
MemberID int not null primary key auto_increment,
firstname varchar(100),
lastname varchar(100),
email varchar(100) not null,
SocietyID int,
foreign key (SocietyID) references society(SocietyID)
);


insert into society(society_name)
values("Eat and Retreat Society"),
("Sci-fi gee Society"),
("The clue seekers Society"),
("Law Society "),
("Foreign Exchange Society")
;