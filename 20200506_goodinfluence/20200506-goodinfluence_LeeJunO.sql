-- SQLite
-- SELECT index, 지역, 진함, 상호명, 사업장연락처,
-- 사업장주소, 영업시간, 제공품목, 제공대상1, 제공대상2,
-- 후원회원참여여부, 월정기후원, 제공대상2_1, 제공대상2_2, 
-- 제공대상2_3, 제공대상2_4
-- FROM `goodinfluence_table`;


DROP TABLE SHOPINFO;
DROP TABLE SERVICETARGET_1;
DROP TABLE SERVICETARGET_2;

-- SHOPINFO
CREATE TABLE SHOPINFO
(
  SHOPINFO_ID  REAL NOT NULL,
  OWNERNAME    TEXT NULL    ,
  SHOPNAME     TEXT NULL    ,
  ADDRESS      TEXT NULL    ,
  WORKINGHOURS TEXT NULL    ,
  TELEPHONE    TEXT NULL    ,
  PRIMARY KEY (SHOPINFO_ID)
);

INSERT INTO SHOPINFO
SELECT `index`, 진함, 상호명,사업장주소, 영업시간,사업장연락처
FROM goodinfluence_table;

-- SERVICETARGET_1

SELECT SHOPINFO.SHOPINFO_ID,goodinfluence_table.제공대상1,SHOPINFO.SHOPINFO_ID
FROM goodinfluence_table,SHOPINFO;


CREATE TABLE SERVICETARGET_1
(
  ST1_ID      REAL NOT NULL,   
  TARGET      TEXT NULL    ,
  SHOPINFO_ID REAL NOT NULL,
  PRIMARY KEY (SHOPINFO_ID),
  CONSTRAINT FK_SHOPINFO_TO_SERVICETARGET_1
  FOREIGN KEY (SHOPINFO_ID)
  REFERENCES SHOPINFO (SHOPINFO_ID)
);

INSERT INTO SERVICETARGET_1
SELECT rowid,goodinfluence_table.제공대상1,SHOPINFO.SHOPINFO_ID
FROM goodinfluence_table,SHOPINFO;


-- SERVICETARGET_2

SELECT rowid,`index`
FROM goodinfluence_table;

CREATE TABLE SERVICETARGET_2
(
  ST2_ID      TEXT NOT NULL,
  SHOPINFO_ID REAL NOT NULL,
  PRIMARY KEY (ST2_ID)
);

INSERT INTO SERVICETARGET_2
SELECT rowid,`index`
FROM goodinfluence_table;

-- TARGET
-- ERD 설계를 잘못하였다.

CREATE TABLE TARGET
(
  TARGET_ID      TEXT NOT NULL,
  TEAGETNAME TEXT NULL,
  ST2_ID
  PRIMARY KEY (TARGET_ID)
);


SELECT rowid,goodinfluence_table.제공대상2_1,SERVICETARGET_2.ST2_ID
FROM goodinfluence_table,SERVICETARGET_2;

SELECT SERVICETARGET_2.rowid, goodinfluence_table.제공대상2_2
FROM goodinfluence_table , SERVICETARGET_2;

SELECT SERVICETARGET_2.rowid, goodinfluence_table.제공대상2_3
FROM goodinfluence_table , SERVICETARGET_2;

SELECT SERVICETARGET_2.rowid, goodinfluence_table.제공대상2_4
FROM goodinfluence_table , SERVICETARGET_2;

