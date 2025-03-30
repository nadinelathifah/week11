create database signupdb;
use signupdb;

select * from society_ppf;


create table society_ppf(
SocietyMembershipID int not null primary key auto_increment,
SocietyName varchar (150)
);


create table sign_up_ppf(
MemberID int not null primary key auto_increment,
firstname varchar(100),
lastname varchar(100),
email varchar(100) not null,
SocietyMembershipID int,
foreign key (SocietyMembershipID) references society_ppf(SocietyMembershipID)
);


insert into society_ppf(SocietyName)
values("Eat and Retreat Society"),
("Sci-fi gee Society"),
("The clue seekers Society"),
("Law Society "),
("Foreign Exchange Society")
;

