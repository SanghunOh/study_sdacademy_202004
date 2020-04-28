-- SQLite
CREATE TABLE ATTACHFILES
(
  FILENAME    TEXT NULL    ,
  UPLOAD_TIME TEXT NULL    ,
  CAPACITY    TEXT NULL    ,
  PROJECT_ID  TEXT NOT NULL,
  MEMBER_ID   TEXT NOT NULL,
  BOARD_ID    TEXT NOT NULL,
  CONSTRAINT FK_PROJECT_TO_ATTACHFILES
    FOREIGN KEY (PROJECT_ID)
    REFERENCES PROJECT (PROJECT_ID),
  CONSTRAINT FK_MEMBER_TO_ATTACHFILES
    FOREIGN KEY (MEMBER_ID)
    REFERENCES MEMBER (MEMBER_ID),
  CONSTRAINT FK_MULTI_BOARD_TO_ATTACHFILES
    FOREIGN KEY (BOARD_ID)
    REFERENCES MULTI_BOARD (BOARD_ID)
);

CREATE TABLE AUTHORITY
(
  RANK         TEXT NULL    ,
  AUTHORITY_ID TEXT NOT NULL,
  PRIMARY KEY (AUTHORITY_ID)
);

CREATE TABLE HOBBY
(
  NAME     TEXT NULL    ,
  HOBBY_ID TEXT NOT NULL,
  PRIMARY KEY (HOBBY_ID)
);

CREATE TABLE LOGHISTORY
(
  LOGIN_TIME  TEXT NULL    ,
  LOGOUT_TIME TEXT NULL    ,
  LOG_ID      TEXT NULL    ,
  MEMBER_ID   TEXT NOT NULL,
  CONSTRAINT FK_MEMBER_TO_LOGHISTORY
    FOREIGN KEY (MEMBER_ID)
    REFERENCES MEMBER (MEMBER_ID)
);

CREATE TABLE MEMBER
(
  MEMBER_ID TEXT NOT NULL,
  PASSWORD  REAL NULL    ,
  ORG_ID    TEXT NOT NULL,
  EMAIL     TEXT NULL    ,
  NAME      TEXT NULL    ,
  PRIMARY KEY (MEMBER_ID),
  CONSTRAINT FK_ORGANIZATION_TO_MEMBER
    FOREIGN KEY (ORG_ID)
    REFERENCES ORGANIZATION (ORG_ID)
);

CREATE TABLE MEMBER_AUTHORITY
(
  AUTHORITY_ID TEXT NOT NULL,
  MEMBER_ID    TEXT NOT NULL,
  CONSTRAINT FK_AUTHORITY_TO_MEMBER_AUTHORITY
    FOREIGN KEY (AUTHORITY_ID)
    REFERENCES AUTHORITY (AUTHORITY_ID),
  CONSTRAINT FK_MEMBER_TO_MEMBER_AUTHORITY
    FOREIGN KEY (MEMBER_ID)
    REFERENCES MEMBER (MEMBER_ID)
);

CREATE TABLE MEMBER_HOBBY
(
  MEMBER_ID TEXT NOT NULL,
  HOBBY_ID  TEXT NOT NULL,
  CONSTRAINT FK_MEMBER_TO_MEMBER_HOBBY
    FOREIGN KEY (MEMBER_ID)
    REFERENCES MEMBER (MEMBER_ID),
  CONSTRAINT FK_HOBBY_TO_MEMBER_HOBBY
    FOREIGN KEY (HOBBY_ID)
    REFERENCES HOBBY (HOBBY_ID)  
);

CREATE TABLE MULTI_BOARD
(
  BOARD_ID  TEXT NOT NULL,
  MEMBER_ID TEXT NOT NULL,
  NAME      TEXT NULL    ,
  GENRE    TEXT  NULL    ,
  PRIMARY KEY (BOARD_ID),
  CONSTRAINT FK_MEMBER_TO_MULTI_BOARD
    FOREIGN KEY (MEMBER_ID)
    REFERENCES MEMBER (MEMBER_ID)
);
CREATE TABLE ORGANIZATION
(
  ORG_NAME   TEXT NULL    ,
  PERSON     INT  NULL    ,
  SERIAL_NUM TEXT NULL    ,
  ORG_ID     TEXT NOT NULL,
  PRIMARY KEY (ORG_ID)
);

CREATE TABLE PROJECT
(
  PERIOD     TEXT NULL    ,
  SUBJECT    TEXT NULL    ,
  BUDGET     REAL NULL    ,
  PROJECT_ID TEXT NOT NULL,
  TEACHER_ID TEXT NOT NULL,
  PRIMARY KEY (PROJECT_ID),
  CONSTRAINT FK_TEACHER_TO_PROJECT
    FOREIGN KEY (TEACHER_ID)
    REFERENCES TEACHER (TEACHER_ID)
);

CREATE TABLE TEACHER
(
  NAME         TEXT NULL    ,
  BIRTHDATE    REAL NULL    ,
  TEACHER_ID   TEXT NOT NULL,
  AUTHORITY_ID TEXT NOT NULL,
  ORG_ID       TEXT NOT NULL,
  PRIMARY KEY (TEACHER_ID),
  CONSTRAINT FK_AUTHORITY_TO_TEACHER
    FOREIGN KEY (AUTHORITY_ID)
    REFERENCES AUTHORITY (AUTHORITY_ID),
  CONSTRAINT FK_ORGANIZATION_TO_TEACHER
    FOREIGN KEY (ORG_ID)
    REFERENCES ORGANIZATION (ORG_ID)
);
INSERT INTO ORGANIZATION (ORG_NAME,ORG_ID) VALUES ('IT Billing','org1');
INSERT INTO ORGANIZATION (ORG_NAME,ORG_ID) VALUES ('Engineering','org2');

INSERT INTO MEMBER (MEMBER_ID,NAME,ORG_ID) VALUES ('PAU1','Paul','org1');
INSERT INTO MEMBER (MEMBER_ID,NAME,ORG_ID) VALUES ('ALL1','Allen','org2');
INSERT INTO MEMBER (MEMBER_ID,NAME,ORG_ID) VALUES ('TED1','Teddy','org1');

INSERT INTO MULTI_BOARD (BOARD_ID,MEMBER_ID,NAME,GENRE) VALUES ('board1','PAU1','용감한 가족','한국영화장르');
INSERT INTO MULTI_BOARD (BOARD_ID,MEMBER_ID,NAME,GENRE) VALUES ('board2','TED1','용감한 형제','일본영화장르');
INSERT INTO MULTI_BOARD (BOARD_ID,MEMBER_ID,NAME,GENRE) VALUES ('board3','TED1','용감한 친척','미국영화장르');

INSERT INTO ATTACHFILES (PROJECT_ID, FILENAME, MEMBER_ID, BOARD_ID) VALUES ('FILE1', 'poster.png', 'PAU1', 'board1');
INSERT INTO ATTACHFILES (PROJECT_ID, FILENAME, MEMBER_ID, BOARD_ID) VALUES ('FILE2', 'actor.png', 'PAU1', 'board1');
INSERT INTO ATTACHFILES (PROJECT_ID, FILENAME, MEMBER_ID, BOARD_ID) VALUES ('FILE3', 'poster02.png', 'TED1', 'board2');
INSERT INTO ATTACHFILES (PROJECT_ID, FILENAME, MEMBER_ID, BOARD_ID) VALUES ('FILE4', 'actor02.png', 'TED1', 'board2');
INSERT INTO ATTACHFILES (PROJECT_ID, FILENAME, MEMBER_ID, BOARD_ID) VALUES ('FILE5', 'poster03.png', 'TED1', 'board3');
INSERT INTO ATTACHFILES (PROJECT_ID, FILENAME, MEMBER_ID, BOARD_ID) VALUES ('FILE6', 'actor03.png', 'TED1', 'board3');

SELECT MEMBER.MEMBER_ID, MULTI_BOARD.NAME, MULTI_BOARD.GENRE, ATTACHFILES.FILENAME
FROM MEMBER, MULTI_BOARD, ATTACHFILES
WHERE MEMBER.MEMBER_ID = MULTI_BOARD.MEMBER_ID
AND MEMBER.MEMBER_ID = ATTACHFILES.MEMBER_ID
AND MULTI_BOARD.BOARD_ID = ATTACHFILES.BOARD_ID