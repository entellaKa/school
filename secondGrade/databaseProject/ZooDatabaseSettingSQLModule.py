import pymysql

sql = """
create database 동물원;
use 동물원; 
 
create table 등급(
등급번호 int primary key auto_increment,
등급 varchar(10),
할인율 float(5,3),
등급기준 int
);

create table 직원(
직원번호 int primary key auto_increment,
이름 varchar(20),
생년월일 date,
핸드폰번호 varchar(15),
주소 varchar(20),
계좌번호 varchar(20),
입사일 date
); 

create table 회원(
아이디 varchar(20) primary key,
패스워드 varchar(20),
이름 varchar(20),
생년월일 date,
핸드폰번호 varchar(15),
포인트 int(6),
등급번호 int,
foreign key (등급번호) references 등급(등급번호)
);


create table 비회원(
비회원번호 varchar(20) primary key,
이름 varchar(20),
생년월일 date,
핸드폰번호 varchar(15));

create table 입장객(
입장번호 int primary key auto_increment,
회원번호 varchar(20),
foreign key (회원번호) references 회원(아이디),
foreign key (회원번호) references 비회원(비회원번호),
결제방법 int,
결제시기 date,
입장시기 date,
동행인_성인 int,
동행인_아이 int,
가격 int);

create table 구역(
구역번호 int primary key auto_increment,
구역이름 varchar(15));

create table 종류(
동물번호 int primary key auto_increment,
종류 varchar(20),
먹이 varchar(10),
구역번호 int,
foreign key (구역번호) references 구역(구역번호));

create table 동물(
개체번호 int primary key auto_increment,
이름 varchar(20),
생일 date,
동물번호 int,
성별 tinyint,
담당사육사 int,
xforeign key (동물번호) references 종류(동물번호),
foreign key (담당사육사) references 직원(직원번호)
);

create table 동물코멘트(
댓글번호 int primary key not null auto_increment,
입장번호 int,
개체번호 int,
코멘트 varchar(1200),
foreign key (입장번호) references 입장객(입장번호),
foreign key (개체번호) references 동물(개체번호));
"""

con = pymysql.connect(host="localhost", user="root", passwd="0000", charset="utf8")
cur = con.cursor()
cur.execute(sql)
con.commit()