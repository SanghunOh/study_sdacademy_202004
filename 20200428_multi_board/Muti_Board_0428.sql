-- SQLite
CREATE TABLE DEPARTMENT
(
  NAME    TEXT NOT NULL,
  DEPT_ID TEXT NULL    ,
  PRIMARY KEY (NAME)
);

CREATE TABLE HOBBY(1)
(
  NAME     TEXT NOT NULL,
  HOBBY_ID      NULL    ,
  PRIMARY KEY (NAME)
);

CREATE TABLE MEMBER(1)
(
  MEMBER_ID REAL NOT NULL,
  NAME      TEXT NOT NULL,
  AGE       REAL NULL    ,
  ADDRESS   TEXT NULL    ,
  SALARY    REAL NULL    ,
  NAME1     TEXT NOT NULL,
  PRIMARY KEY (MEMBER_ID, NAME),
  CONSTRAINT FK_DEPARTMENT_TO_MEMBER(1)
    FOREIGN KEY (NAME1)
    REFERENCES DEPARTMENT (NAME)
);

CREATE TABLE MEMBER_HOBBY
(
  NAME  TEXT NULL    ,
  NAME1      NULL    ,
  NAME2 TEXT NOT NULL,
  NAME3 TEXT NOT NULL,
  CONSTRAINT FK_MEMBER(1)_TO_MEMBER_HOBBY
    FOREIGN KEY (NAME2)
    REFERENCES MEMBER(1) (NAME),
    CONSTRAINT FK_HOBBY(1)_TO_MEMBER_HOBBY
    FOREIGN KEY (NAME3)
    REFERENCES HOBBY(1) (NAME);

);


CREATE TABLE IMAGE
(
  CONTENT_NO1 REAL NOT NULL,
  IMAGE       TEXT NULL,
  CONSTRAINT FK_MUTI_BOARD_TO_IMAGE
    FOREIGN KEY (CONTENT_NO1)
    REFERENCES MUTI_BOARD (CONTENT_NO)    
);

CREATE TABLE MUTI_BOARD
(
  CONTENT_NO REAL NOT NULL,
  TITLE      TEXT NOT NULL,
  COUNTRY    TEXT NULL    ,
  GENRE      TEXT NULL    ,
  MEMBER     TEXT NULL    ,
  MEMBER_ID1 REAL NOT NULL,
  PRIMARY KEY (CONTENT_NO),
  CONSTRAINT FK_MEMBER_TO_MUTI_BOARD
    FOREIGN KEY (MEMBER_ID1)
    REFERENCES MEMBER(MEMBER_ID)
);

drop table IMAGE;
drop table MUTI_BOARD;

select * from MEMBER;
select * from DEPARTMENT;
select * from IMAGE;

drop table IMAGE;


insert into MUTI_BOARD
values(1, '용감한 가족', '한국', '코미디', 'Paul', 1);
insert into MUTI_BOARD
values(2, '용감한 형제', '일본', '호러', 'Teddy', 3);
insert into MUTI_BOARD
values(3, '용감한 친척', '미국', '액션', 'Teddy', 3);

insert into IMAGE
values(1, 'poster.png');
insert into IMAGE
values(1, 'actor.png');
insert into IMAGE
values(2, 'poster02.png');
insert into IMAGE
values(2, 'actor02.png');
insert into IMAGE
values(3, 'poster03.png');
insert into IMAGE
values(3, 'actor03.png');


select TITLE, country, genre, IMAGE, MEMBER from MUTI_BOARD, image
where MUTI_BOARD.CONTENT_NO = image.CONTENT_NO1 

select TITLE, country, genre, MEMBER from MUTI_BOARD, MEMBER
where MEMBER.MEMBER_ID=MUTI_BOARD.MEMBER_ID1

select TITLE, country, genre, image, MEMBER from MUTI_BOARD, image, MEMBER
where MUTI_BOARD.content_no = image.CONTENT_NO1 & MUTI_BOARD.MEMBER_ID1=MEMBER_ID