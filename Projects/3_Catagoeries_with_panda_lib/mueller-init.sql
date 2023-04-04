-- @AUTHOR	 	Lennard Becker
-- @DATE		2023-04-01
-- @Version		init Version
-- @Changelog
--				suffix for primary and foreign keys
--				table name of 'statistics' changed to 'survey'
--				surrogate key for survey added
--				surrogate key for pollster added
--				split resultset into basic and extended
--				rewrite from MySQL to T-Sql


-- ============================================ --
--					DATABASE
-- ============================================ --
-- lines are used to create the database 'mueller'			-> use master is only used, that the database can be dropped, if it already exist
-- dropping a database while in use, is not possible, so 	-> use master

EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'mueller'
GO
USE master;
GO
ALTER DATABASE mueller SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO
DROP DATABASE IF EXISTS mueller;
GO
CREATE DATABASE mueller;
GO
USE mueller;
GO
-- ============================================ --
--					TABLES
-- ============================================ --
-- @TABLE		pollster
-- @CONTENT		contains names of organizations, that did the surveys
-- @ADDITIONS	check if table named 'polls' already exists in database
--				Yes	-> DROP given TABLE by name
--				NO	-> Nothinghappens, just create table afterwards
--				statement was used for all database related tables, just for first init

IF EXISTS (	SELECT * FROM INFORMATION_SCHEMA.TABLES
			WHERE TABLE_NAME = 'questionnaire')
	DROP TABLE polls
GO

CREATE TABLE mueller.dbo.questionnaire(
  textID_pk INTEGER IDENTITY (1,1),
  text   VARCHAR(510) NOT NULL,

  PRIMARY KEY (textID_pk)
);

INSERT INTO questionnaire (text)
VALUES	
	('Do you approve or disapprove of the way Robert Mueller is handling his job as special counsel?'),
	('As you may know, the U.S. Department of Justice appointed Robert Mueller as the special counsel to investigate any alleged coordination between the Russian government and Donald Trumps 2016 presidential campaign. Based on what you know, do you approve or disapprove of the way Robert Mueller is handling his job as special counsel?'),
	('Do you approve or disapprove of the way Robert Mueller is handling his job as special counsel on the Russia probe?'),
	('A special counsel at the U.S. Justice Department, Robert Mueller, has been investigating possible ties between Trumps campaign and the Russian government. Do you approve or disapprove of the way Mueller is handling this investigation?'),
	('Do you approve or disapprove of the way Robert Mueller is handling the investigation into Russian interference in the 2016 election?'),
	('A special counsel at the U.S. Justice Department, Robert Mueller, has been investigating possible ties between Trumps presidential campaign and the Russian govt. Do you approve or disapprove of the way he is handling investigation?'),
	('As you may know, the U.S. Department of Justice appointed Robert Mueller as special counsel to investigate any alleged coordination between the Russian government and Donald Trumps 2016 presidential campaign. Based on what you know, do you approve or disapprove of the way Robert Mueller is handling his job as special counsel?'),
	('Do you approve or disapprove of Robert Muellers investigation of the Trump campaigns ties with Russia and potential obstruction of justice charges against members of the Trump administration?'),
	('Do you approve or disapprove of the way U.S. Justice Department special counsel Robert Mueller is handling the investigation into possible ties between Trumps presidential campaign and the Russian government?'),
	('Do you approve or disapprove of the way that Special Counsel Robert Mueller is handling his job?'),
	('As you may know, special counsel Robert Mueller is investigating Russias role in the 2016 election and its possible ties with Donald Trumps presidential campaign. Do you approve or disapprove of the way Mueller is handling this investigation? Do you approve/disapprove strongly or somewhat?'),
	('Do you approve or disapprove of the job Robert Mueller did as special counsel investigating possible wrongdoing and Russian interference in the 2016 election?'),
	('As you may know, special counsel Robert Mueller has completed his investigation of Russias role in the 2016 election and its possible ties with Donald Trumps presidential campaign. Do you approve or disapprove of the way Mueller handled this investigation? Do you approve/disapprove strongly or somewhat?'),
	('Do you approve or disapprove of the way Robert Mueller has handled his job as special counsel on the Russia probe?'),
	('Do you approve or disapprove of the way Robert Mueller handled the investigation into Russian interference in the 2016 election?');

-- ============================================ --
-- @TABLE		pollster
-- @CONTENT		contains names of organizations, that did the surveys
-- @ADDITIONS	

IF EXISTS (	SELECT * FROM INFORMATION_SCHEMA.TABLES
			WHERE TABLE_NAME = 'pollster')
	DROP TABLE polls
GO

CREATE TABLE mueller.dbo.pollster(
    pollsterID_pk	INTEGER IDENTITY(1,1),
	organization	VARCHAR(255),
	
    PRIMARY KEY (pollsterID_pk)
);

INSERT INTO pollster (organization) 
VALUES
	('CNN/SSRS'),
	('Fox News'),
	('Marist'),
	('Morning Consult'),
	('Quinnipiac'),
	('Washington Post/ABC News'),
	('Washington Post/Schar School'),
	('YouGov/Economist'),
	('YouGov/HuffPost');

-- ============================================ --
-- @TABLE		survey
-- @CONTENT		contains general information about survey like, start, end, sampleSize ...
-- @ADDITIONS	use as main table

IF EXISTS (	SELECT * FROM INFORMATION_SCHEMA.TABLES
			WHERE TABLE_NAME = 'survey')
	DROP TABLE polls
GO

CREATE TABLE survey(
  surveyID_pk	INTEGER IDENTITY (1,1) NOT NULL,
  url			VARCHAR(255) NOT NULL,
  startDate     DATE  NOT NULL,
  endDate       DATE  NOT NULL,
  sampleSize	INTEGER  NOT NULL,
  population	VARCHAR(2) NOT NULL,
  pollsterID_fk	INTEGER NOT NULL,
  textID_fk		INTEGER NOT NULL,

  PRIMARY KEY(surveyID_pk),
  FOREIGN KEY(pollsterID_fk) REFERENCES pollster(pollsterID_pk),
  FOREIGN KEY(textID_fk) REFERENCES questionnaire(textID_pk)
);

INSERT INTO survey (url, startDate, endDate, sampleSize, population, pollsterID_fk, textID_fk)
VALUES
	('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/7hxorevceh/econTabReport.pdf','2018-07-15','2017-07-17',1500,'a',8,1),
    ('https://morningconsult.com/wp-content/uploads/2017/07/170708_crosstabs_Politico_v1_TB.pdf','2017-07-20','2017-07-24',3981,'rv',4,2),
    ('http://big.assets.huffingtonpost.com/tabsHPRussiaIndictments20171030.pdf','2017-10-30','2017-10-31',1000,'a',9,3),
    ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2017/11/16/3d2002d2-bff7-11e7-9294-705f80164f6e_page.html','2017-10-29','2017-11-01',1005,'a',6,4),
    ('http://big.assets.huffingtonpost.com/tabsHPMichaelFlynn20171201.pdf','2017-12-01','2017-12-02',1000,'a',9,3),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/jhdmzhxe6k/econTabReport.pdf','2017-12-03','2017-12-05',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2017/images/12/21/rel12c.-.russia.pdf','2017-12-14','2017-12-17',1001,'a',1,5),
    ('http://cdn.cnn.com/cnn/2018/images/01/23/rel1f.-.russia.pdf','2018-01-14','2018-01-18',1005,'a',1,5),
    ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2018/01/29/27f3887a-fe68-11e7-9b5d-bbf0da31214d_page.html','2018-01-15','2018-01-18',1005,'a',6,6),
    ('http://big.assets.huffingtonpost.com/tabsHPRussiainvestigation20180123.pdf','2018-01-23','2018-01-24',1000,'a',9,3),
    ('http://big.assets.huffingtonpost.com/tabsHPMuellerinvestigation20180126.pdf','2018-01-26','2018-01-27',1000,'a',9,3),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/81kgdte5zw/econTabReport.pdf','2018-01-28','2018-01-30',1500,'a',8,1),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/57yxejgrmo/econTabReport.pdf','2018-02-18','2018-02-20',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2018/images/02/26/rel3c.-.russia.pdf','2018-02-20','2018-02-23',1016,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/y3tke5cxwy/econTabReport.pdf','2018-03-10','2018-03-13',1500,'a',8,1),
    ('https://morningconsult.com/wp-content/uploads/2018/03/180322_crosstabs_POLITICO_v1_DK.pdf','2018-03-15','2018-03-19',1994,'rv',4,7),
    ('https://cdn.cnn.com/cnn/2018/images/03/27/rel4b-north.korea2c.russia.pdf','2018-03-22','2018-03-25',1014,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/4l31gznvf1/econTabReport.pdf','2018-04-15','2018-04-17',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2018/images/05/10/rel5f.-.russia.pdf','2018-05-02','2018-05-05',1015,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/kwgrow0dna/econTabReport.pdf','2018-05-06','2018-05-08',1500,'a',8,1),
    ('https://big.assets.huffingtonpost.com/athena/files/2018/05/15/5afb49bbe4b0a59b4dfe6ddd.pdf','2018-05-10','2018-05-12',1000,'a',9,3),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/v00h5ts0qm/econTabReport.pdf','2018-05-27','2018-05-29',1500,'a',8,1),
    ('https://www.foxnews.com/politics/fox-news-poll-results-6-14-18','2018-06-03','2018-06-06',1001,'rv',2,8),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/0kj6rhpqso/econTabReport.pdf','2018-06-10','2018-06-12',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2018/images/06/21/rel6f.-.russia.investigation.pdf','2018-06-14','2018-06-17',1012,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/rbrysksiud/econTabReport.pdf','2018-06-17','2018-06-19',1500,'a',8,1),
    ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2018/07/11/09a17592-8123-11e8-b3b5-b61896f90919_page.html','2018-06-27','2018-07-02',1473,'a',8,9),
    ('https://www.foxnews.com/politics/fox-news-poll-7-12','2018-07-09','2018-07-11',1007,'rv',2,8),
    ('https://big.assets.huffingtonpost.com/athena/files/2018/07/16/5b4ce38be4b0e7c958fe3ea5.pdf','2018-07-13','2018-07-14',1000,'a',9,3),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/wa3gpxn761/econTabReport.pdf','2018-07-22','2018-07-24',1500,'a',8,1),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/fw0vfdqfpc/econTabReport.pdf','2018-07-29','2018-07-31',1500,'a',8,1),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/q6cfmfwwh4/econTabReport.pdf','2018-08-05','2018-08-07',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2018/images/08/13/rel7a.-.trump2c.russia.pdf','2018-08-09','2018-08-12',1002,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/6ote18t1hm/econTabReport.pdf','2018-08-12','2018-08-14',1500,'a',8,1),
    ('https://www.foxnews.com/politics/fox-news-poll-8-22','2018-08-19','2018-08-21',1009,'rv',2,8),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/krhk8brhhw/econTabReport.pdf','2018-08-26','2018-08-28',1500,'a',8,1),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/22joa4cprz/econTabReport.pdf','2018-09-02','2018-09-04',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2018/images/09/11/rel8c.-.russia,.cohen,.impeachment.pdf','2018-09-06','2018-09-09',1003,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/9th9okzc75/econTabReport.pdf','2018-09-16','2018-09-18',1500,'a',8,1),
    ('https://www.foxnews.com/politics/fox-news-poll-9-23','2018-09-16','2018-09-19',1003,'rv',2,8),
    ('http://cdn.cnn.com/cnn/2018/images/10/11/rel9c.-.trump.and.russia.pdf','2018-10-04','2018-10-07',1009,'a',1,5),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/yoolhxrark/econTabReport.pdf','2018-12-02','2018-12-04',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2018/images/12/10/rel12a.-.trump.and.russia.pdf','2018-12-06','2018-12-09',1015,'a',1,5),
    ('https://www.foxnews.com/politics/fox-news-poll-document-12-12-18','2018-12-09','2018-12-11',1006,'rv',2,8),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/ppsei7g0oq/econTabReport.pdf','2018-12-09','2018-12-11',1500,'a',8,1),
    ('https://poll.qu.edu/national/release-detail?ReleaseID=2591','2018-12-12','2018-12-17',1147,'rv',5,10),
    ('https://www.foxnews.com/politics/fox-news-poll-document-1-23-19','2019-01-20','2019-01-22',1008,'rv',2,8),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/183c0vbnai/econTabReport.pdf','2019-01-20','2019-01-22',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2019/images/02/07/rel2c.-.russia.pdf','2019-01-30','2019-02-02',1011,'a',1,5),
    ('https://big.assets.huffingtonpost.com/athena/files/2019/02/13/5c6446b4e4b08da0ec8141f3.pdf','2019-02-07','2019-02-08',1000,'a',9,3),
    ('https://drive.google.com/file/d/1JWqPDt4hMKpZ9hpCAq2pzrOZki-NwSHN/view','2019-02-06','2019-02-10',841,'a',8,11),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/oo6kz6sf4b/econTabReport.pdf','2019-02-24','2019-02-26',1500,'a',8,1),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/9d5s05pspt/econTabReport.pdf','2019-03-03','2019-03-05',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2019/images/03/20/rel4c.-.trump.and.russia.pdf','2019-03-14','2019-03-17',1003,'a',1,5),
    ('https://www.foxnews.com/politics/fox-news-poll-3-24-2019','2019-03-17','2019-03-20',1002,'rv',2,8),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/6ujvi5p8z1/econTabReport.pdf','2019-03-24','2019-03-26',1500,'a',8,1),
    ('http://maristpoll.marist.edu/wp-content/uploads/2019/03/NPR_PBS-NewsHour_Marist-Poll_USA-NOS-and-Tables_1903251153.pdf','2019-03-25','2019-03-27',938,'a',3,12),
    ('https://big.assets.huffingtonpost.com/athena/files/2019/03/28/5c9d2beee4b00ba632795d13.pdf','2019-03-25','2019-03-27',1000,'a',9,3),
    ('https://www.washingtonpost.com/page/2010-2019/WashingtonPost/2019/03/30/National-Politics/Polling/question_21323.xml','2019-03-26','2019-03-29',640,'a',8,13),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/t1fl59zsim/econTabReport.pdf','2019-03-31','2019-04-02',1500,'a',8,1),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/egvqvgp5a7/econTabReport.pdf','2019-04-13','2019-04-16',1500,'a',8,1),
    ('https://big.assets.huffingtonpost.com/athena/files/2019/04/22/5cbe11f6e4b0f7a84a73723d.pdf','2019-04-18','2019-04-19',1000,'a',9,14),
    ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/75p17530i6/econTabReport.pdf','2019-04-21','2019-04-23',1500,'a',8,1),
    ('http://cdn.cnn.com/cnn/2019/images/04/30/rel6c.-.mueller.report.pdf','2019-04-25','2019-04-28',1007,'a',1,15),
    ('http://maristpoll.marist.edu/wp-content/uploads/2019/04/NPR_PBS-NewsHour_Marist-Poll_USA-NOS-and-Tables_1904301401.pdf','2019-04-24','2019-04-29',1017,'a',3,12);
	
-- ============================================ --
-- @TABLE		basicResultset
-- @CONTENT		contains all generealized results of one survey
-- @ADDITIONS	special, a resultset can not exist without related statistic entry -> if an entry in survey is deleted, it related resultset is deleted as well

CREATE TABLE mueller.dbo.basicResultset(
  basicResultID_pk  INTEGER IDENTITY (1,1) NOT NULL,
  approve           TINYINT NOT NULL,
  disapprove        TINYINT NOT NULL,
  unsure            TINYINT NOT NULL,
  surveyID_fk		INTEGER NOT NULL,
  

  PRIMARY KEY(basicResultID_pk),
  FOREIGN KEY(surveyID_fk) REFERENCES survey(surveyID_pk) ON DELETE CASCADE
);

INSERT INTO basicResultset (approve, disapprove, unsure, surveyID_fk)
VALUES
	(37, 30, 33,1),
    (40, 27, 33, 2),
	(39, 26, 34, 3),
    (58, 28, 14, 4),
    (36, 28, 35, 5),
    (36, 25, 38, 6),
    (47, 34, 19, 7),
    (47, 33, 20, 8),
    (50, 31, 19, 9),
    (37, 25, 38, 10),
    (34, 26, 39, 11),
    (34, 29, 37, 12),
    (39, 25, 36, 13),
    (37, 33, 21, 14),
    (37, 27, 36, 15),
    (45, 27, 27, 16),
    (38, 35, 17, 17),
    (37, 29, 33, 18),
    (44, 38, 18, 19),
    (36, 30, 34, 20),
    (38, 32, 30, 21),
    (38, 31, 31, 22),
    (55, 37, 8, 23),
    (23, 30, 36, 24),
    (41, 39, 21, 25),
    (35, 29, 36, 26),
    (49, 45, 4, 27),
    (48, 40, 12, 28),
    (36, 33, 30, 29),
    (35, 30, 15, 30),
    (36, 32, 31, 31),
    (35, 32, 33, 32),
    (47, 39, 31, 33),
    (38, 31, 32, 34),
    (59, 37, 4, 35),
    (34, 31, 35, 36),
    (39, 29, 30, 37),
    (50, 38, 12, 38),
    (42, 32, 26, 39),
    (55, 39, 7, 40),
    (48, 36, 16, 41),
    (38, 31, 30, 42),
    (43, 40, 16, 43),
    (56, 37, 7, 44),
    (41, 33, 26, 45),
    (45, 38, 17, 46),
    (49, 34, 17, 47),
    (40, 30, 30, 48),
    (44, 41, 15, 49),
    (36, 33, 31, 50),
    (51, 34, 15, 51),
    (40, 30, 30, 52),
    (37, 34, 28, 53),
    (48, 37, 15, 54),
    (52, 36, 12, 55),
    (48, 25, 27, 56),
    (51, 27, 22, 57),
    (43, 27, 30, 58),
    (53, 30, 17, 59),
    (48, 25, 27, 60),
    (45, 23, 32, 61),
    (44, 28, 27, 62),
    (47, 27, 26, 63),
    (59, 30, 11, 64),
    (54, 26, 20, 65);

-- ============================================ --
-- @TABLE		extendedResultset
-- @CONTENT		contains all specific results of one survey; specific approve of Republican and Democrats
-- @ADDITIONS	special, a resultset can not exist without related statistic entry -> if an entry in survey is deleted, it related resultset is deleted as well

CREATE TABLE mueller.dbo.extendedResultset(
	extendedResultID_pk INTEGER IDENTITY (1,1) NOT NULL,
	approveRepublicans	TINYINT NOT NULL,
	approveDemocrats	TINYINT NOT NULL,
	surveyID_fk			INTEGER NOT NULL,

	PRIMARY KEY(extendedResultID_pk),
	FOREIGN KEY(surveyID_fk) REFERENCES survey(surveyID_pk) ON DELETE CASCADE
);

INSERT INTO extendedResultset (approveRepublicans, approveDemocrats, surveyID_fk) 
VALUES
	(17, 62, 1),
    (31, 53, 2),
	(25, 60, 3),
    (38, 78, 4),
    (17, 58, 5),
    (22, 61, 6),
    (31, 63, 7),
    (26, 68, 8),
    (28, 71, 9),
    (25, 59, 10),
    (18, 58, 11),
    (18, 57, 12),
    (23, 62, 13),
    (28, 66, 14),
    (20, 57, 15),
    (35, 62, 16),
    (29, 69, 17),
    (19, 61, 18),
    (17, 64, 19),
    (14, 63, 20),
    (19, 70, 21),
    (16, 68, 22),
    (23, 84, 23),
    (13, 66, 24),
    (20, 62, 25),
    (16, 64, 26),
    (20, 76, 27),
    (25, 72, 28),
    (18, 66, 29),
    (15, 62, 30),
    (16, 65, 31),
    (15, 61, 32),
    (22, 72, 33),
    (21, 65, 34),
    (26, 84, 35),
    (15, 65, 36),
    (13, 68, 37),
    (23, 73, 38),
    (23, 68, 39),
    (25, 82, 40),
    (23, 73, 41),
    (16, 70, 42),
    (21, 71, 43),
    (27, 82, 44),
    (21, 68, 45),
    (17, 72, 46),
    (21, 80, 47),
    (22, 66, 48),
    (20, 67, 49),
    (16, 63, 50),
    (22, 77, 51),
    (22, 62, 52),
    (15, 65, 53),
    (20, 75, 54),
    (23, 82, 55),
    (35, 72, 56),
    (47, 53, 57),
    (44, 51, 58),
    (46, 62, 59),
    (42, 63, 60),
    (35, 62, 61),
    (39, 59, 62),
    (37, 64, 63),
    (50, 69, 64),
    (47, 61, 65);