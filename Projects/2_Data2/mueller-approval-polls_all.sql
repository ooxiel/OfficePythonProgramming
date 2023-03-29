-- @AUTHOR: 	Lennard Becker
-- @DATE:		2023-03-28
-- @Version:	V init


-- check, create, use database
DROP DATABASE IF EXISTS mueller;
CREATE DATABASE IF NOT EXISTS mueller;
USE mueller;

-- create table questionnaire
-- table contains all possible questitions that could be asked by organizations

CREATE TABLE IF NOT EXISTS mueller.questionnaire(
  textID INTEGER  NOT NULL AUTO_INCREMENT,
  text   VARCHAR(510) NOT NULL,

  PRIMARY KEY (textID)
);

INSERT INTO questionnaire(textID,text) VALUES (1,'Do you approve or disapprove of the way Robert Mueller is handling his job as special counsel?');
INSERT INTO questionnaire(textID,text) VALUES (2,'As you may know, the U.S. Department of Justice appointed Robert Mueller as the special counsel to investigate any alleged coordination between the Russian government and Donald Trumps 2016 presidential campaign. Based on what you know, do you approve or disapprove of the way Robert Mueller is handling his job as special counsel?');
INSERT INTO questionnaire(textID,text) VALUES (3,'Do you approve or disapprove of the way Robert Mueller is handling his job as special counsel on the Russia probe?');
INSERT INTO questionnaire(textID,text) VALUES (4,'A special counsel at the U.S. Justice Department, Robert Mueller, has been investigating possible ties between Trumps campaign and the Russian government. Do you approve or disapprove of the way Mueller is handling this investigation?');
INSERT INTO questionnaire(textID,text) VALUES (5,'Do you approve or disapprove of the way Robert Mueller is handling the investigation into Russian interference in the 2016 election?');
INSERT INTO questionnaire(textID,text) VALUES (6,'A special counsel at the U.S. Justice Department, Robert Mueller, has been investigating possible ties between Trumps presidential campaign and the Russian govt. Do you approve or disapprove of the way he is handling investigation?');
INSERT INTO questionnaire(textID,text) VALUES (7,'As you may know, the U.S. Department of Justice appointed Robert Mueller as special counsel to investigate any alleged coordination between the Russian government and Donald Trumps 2016 presidential campaign. Based on what you know, do you approve or disapprove of the way Robert Mueller is handling his job as special counsel?');
INSERT INTO questionnaire(textID,text) VALUES (8,'Do you approve or disapprove of Robert Muellers investigation of the Trump campaigns ties with Russia and potential obstruction of justice charges against members of the Trump administration?');
INSERT INTO questionnaire(textID,text) VALUES (9,'Do you approve or disapprove of the way U.S. Justice Department special counsel Robert Mueller is handling the investigation into possible ties between Trumps presidential campaign and the Russian government?');
INSERT INTO questionnaire(textID,text) VALUES (10,'Do you approve or disapprove of the way that Special Counsel Robert Mueller is handling his job?');
INSERT INTO questionnaire(textID,text) VALUES (11,'As you may know, special counsel Robert Mueller is investigating Russias role in the 2016 election and its possible ties with Donald Trumps presidential campaign. Do you approve or disapprove of the way Mueller is handling this investigation? Do you approve/disapprove strongly or somewhat?');
INSERT INTO questionnaire(textID,text) VALUES (12,'Do you approve or disapprove of the job Robert Mueller did as special counsel investigating possible wrongdoing and Russian interference in the 2016 election?');
INSERT INTO questionnaire(textID,text) VALUES (13,'As you may know, special counsel Robert Mueller has completed his investigation of Russias role in the 2016 election and its possible ties with Donald Trumps presidential campaign. Do you approve or disapprove of the way Mueller handled this investigation? Do you approve/disapprove strongly or somewhat?');
INSERT INTO questionnaire(textID,text) VALUES (14,'Do you approve or disapprove of the way Robert Mueller has handled his job as special counsel on the Russia probe?');
INSERT INTO questionnaire(textID,text) VALUES (15,'Do you approve or disapprove of the way Robert Mueller handled the investigation into Russian interference in the 2016 election?');


-- create table pollster
-- table contains all possible organizations that asked the possible questitions

CREATE TABLE IF NOT EXISTS mueller.pollster(
    organization VARCHAR(255),

    PRIMARY KEY (organization)
);

INSERT INTO pollster (organization) VALUES('CNN/SSRS');
INSERT INTO pollster (organization) VALUES('Fox News');
INSERT INTO pollster (organization) VALUES('Marist');
INSERT INTO pollster (organization) VALUES('Morning Consult');
INSERT INTO pollster (organization) VALUES('Quinnipiac');
INSERT INTO pollster (organization) VALUES('Washington Post/ABC News');
INSERT INTO pollster (organization) VALUES('Washington Post/Schar School');
INSERT INTO pollster (organization) VALUES('YouGov/Economist');
INSERT INTO pollster (organization) VALUES('YouGov/HuffPost');

-- create table statistics
-- table contains basic information about every survey, like start, end, pollster, question, sample size ...

CREATE TABLE IF NOT EXISTS mueller.statistics(
  url        VARCHAR(255) NOT NULL,
  start      DATE  NOT NULL,
  end        DATE  NOT NULL,
  sampleSize INTEGER  NOT NULL,
  population VARCHAR(2) NOT NULL,
  organization    VARCHAR(255) NOT NULL,
  textID     INTEGER NOT NULL,

  PRIMARY KEY(url),
  FOREIGN KEY(organization) REFERENCES pollster(organization),
  FOREIGN KEY(textID) REFERENCES questionnaire(textID)
);

INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/7hxorevceh/econTabReport.pdf','2018-07-15','2017-07-17',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://morningconsult.com/wp-content/uploads/2017/07/170708_crosstabs_Politico_v1_TB.pdf','2017-07-20','2017-07-24',3981,'rv','Morning Consult',2);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://big.assets.huffingtonpost.com/tabsHPRussiaIndictments20171030.pdf','2017-10-30','2017-10-31',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2017/11/16/3d2002d2-bff7-11e7-9294-705f80164f6e_page.html','2017-10-29','2017-11-01',1005,'a','Washington Post/ABC News',4);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://big.assets.huffingtonpost.com/tabsHPMichaelFlynn20171201.pdf','2017-12-01','2017-12-02',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/jhdmzhxe6k/econTabReport.pdf','2017-12-03','2017-12-05',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2017/images/12/21/rel12c.-.russia.pdf','2017-12-14','2017-12-17',1001,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/01/23/rel1f.-.russia.pdf','2018-01-14','2018-01-18',1005,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2018/01/29/27f3887a-fe68-11e7-9b5d-bbf0da31214d_page.html','2018-01-15','2018-01-18',1005,'a','Washington Post/ABC News',6);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://big.assets.huffingtonpost.com/tabsHPRussiainvestigation20180123.pdf','2018-01-23','2018-01-24',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://big.assets.huffingtonpost.com/tabsHPMuellerinvestigation20180126.pdf','2018-01-26','2018-01-27',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/81kgdte5zw/econTabReport.pdf','2018-01-28','2018-01-30',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/57yxejgrmo/econTabReport.pdf','2018-02-18','2018-02-20',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/02/26/rel3c.-.russia.pdf','2018-02-20','2018-02-23',1016,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/y3tke5cxwy/econTabReport.pdf','2018-03-10','2018-03-13',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://morningconsult.com/wp-content/uploads/2018/03/180322_crosstabs_POLITICO_v1_DK.pdf','2018-03-15','2018-03-19',1994,'rv','Morning Consult',7);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://cdn.cnn.com/cnn/2018/images/03/27/rel4b-north.korea2c.russia.pdf','2018-03-22','2018-03-25',1014,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/4l31gznvf1/econTabReport.pdf','2018-04-15','2018-04-17',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/05/10/rel5f.-.russia.pdf','2018-05-02','2018-05-05',1015,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/kwgrow0dna/econTabReport.pdf','2018-05-06','2018-05-08',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2018/05/15/5afb49bbe4b0a59b4dfe6ddd.pdf','2018-05-10','2018-05-12',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/v00h5ts0qm/econTabReport.pdf','2018-05-27','2018-05-29',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-results-6-14-18','2018-06-03','2018-06-06',1001,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/0kj6rhpqso/econTabReport.pdf','2018-06-10','2018-06-12',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/06/21/rel6f.-.russia.investigation.pdf','2018-06-14','2018-06-17',1012,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/rbrysksiud/econTabReport.pdf','2018-06-17','2018-06-19',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2018/07/11/09a17592-8123-11e8-b3b5-b61896f90919_page.html','2018-06-27','2018-07-02',1473,'a','Washington Post/Schar School',9);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-7-12','2018-07-09','2018-07-11',1007,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2018/07/16/5b4ce38be4b0e7c958fe3ea5.pdf','2018-07-13','2018-07-14',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/wa3gpxn761/econTabReport.pdf','2018-07-22','2018-07-24',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/fw0vfdqfpc/econTabReport.pdf','2018-07-29','2018-07-31',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/q6cfmfwwh4/econTabReport.pdf','2018-08-05','2018-08-07',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/08/13/rel7a.-.trump2c.russia.pdf','2018-08-09','2018-08-12',1002,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/6ote18t1hm/econTabReport.pdf','2018-08-12','2018-08-14',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-8-22','2018-08-19','2018-08-21',1009,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/krhk8brhhw/econTabReport.pdf','2018-08-26','2018-08-28',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/22joa4cprz/econTabReport.pdf','2018-09-02','2018-09-04',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/09/11/rel8c.-.russia,.cohen,.impeachment.pdf','2018-09-06','2018-09-09',1003,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/9th9okzc75/econTabReport.pdf','2018-09-16','2018-09-18',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-9-23','2018-09-16','2018-09-19',1003,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/10/11/rel9c.-.trump.and.russia.pdf','2018-10-04','2018-10-07',1009,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/yoolhxrark/econTabReport.pdf','2018-12-02','2018-12-04',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2018/images/12/10/rel12a.-.trump.and.russia.pdf','2018-12-06','2018-12-09',1015,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-document-12-12-18','2018-12-09','2018-12-11',1006,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/ppsei7g0oq/econTabReport.pdf','2018-12-09','2018-12-11',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://poll.qu.edu/national/release-detail?ReleaseID=2591','2018-12-12','2018-12-17',1147,'rv','Quinnipiac',10);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-document-1-23-19','2019-01-20','2019-01-22',1008,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/183c0vbnai/econTabReport.pdf','2019-01-20','2019-01-22',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2019/images/02/07/rel2c.-.russia.pdf','2019-01-30','2019-02-02',1011,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2019/02/13/5c6446b4e4b08da0ec8141f3.pdf','2019-02-07','2019-02-08',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://drive.google.com/file/d/1JWqPDt4hMKpZ9hpCAq2pzrOZki-NwSHN/view','2019-02-06','2019-02-10',841,'a','Washington Post/Schar School',11);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/oo6kz6sf4b/econTabReport.pdf','2019-02-24','2019-02-26',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/9d5s05pspt/econTabReport.pdf','2019-03-03','2019-03-05',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2019/images/03/20/rel4c.-.trump.and.russia.pdf','2019-03-14','2019-03-17',1003,'a','CNN/SSRS',5);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.foxnews.com/politics/fox-news-poll-3-24-2019','2019-03-17','2019-03-20',1002,'rv','Fox News',8);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/6ujvi5p8z1/econTabReport.pdf','2019-03-24','2019-03-26',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://maristpoll.marist.edu/wp-content/uploads/2019/03/NPR_PBS-NewsHour_Marist-Poll_USA-NOS-and-Tables_1903251153.pdf','2019-03-25','2019-03-27',938,'a','Marist',12);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2019/03/28/5c9d2beee4b00ba632795d13.pdf','2019-03-25','2019-03-27',1000,'a','YouGov/HuffPost',3);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://www.washingtonpost.com/page/2010-2019/WashingtonPost/2019/03/30/National-Politics/Polling/question_21323.xml','2019-03-26','2019-03-29',640,'a','Washington Post/Schar School',13);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/t1fl59zsim/econTabReport.pdf','2019-03-31','2019-04-02',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/egvqvgp5a7/econTabReport.pdf','2019-04-13','2019-04-16',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2019/04/22/5cbe11f6e4b0f7a84a73723d.pdf','2019-04-18','2019-04-19',1000,'a','YouGov/HuffPost',14);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/75p17530i6/econTabReport.pdf','2019-04-21','2019-04-23',1500,'a','YouGov/Economist',1);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://cdn.cnn.com/cnn/2019/images/04/30/rel6c.-.mueller.report.pdf','2019-04-25','2019-04-28',1007,'a','CNN/SSRS',15);
INSERT INTO statistics(url,start,end,sampleSize,population,organization,textID) VALUES ('http://maristpoll.marist.edu/wp-content/uploads/2019/04/NPR_PBS-NewsHour_Marist-Poll_USA-NOS-and-Tables_1904301401.pdf','2019-04-24','2019-04-29',1017,'a','Marist',12);

-- create table statistics
-- table contains all results one the given surveys
-- as special, a resultset can not exist without related statistic entry -> if an entry in statistics is deleted, it related resultset is deleted as well

CREATE TABLE IF NOT EXISTS mueller.resultset(
  url               VARCHAR(255) NOT NULL,
  resultID          INTEGER NOT NULL,
  approve           TINYINT NOT NULL,
  disapprove        TINYINT NOT NULL,
  unsure            TINYINT NOT NULL,
  approveRepublican TINYINT NOT NULL,
  approveDemocrats  TINYINT NOT NULL,

  PRIMARY KEY(resultID),
  FOREIGN KEY(url) REFERENCES statistics(url) ON DELETE CASCADE
);

INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-results-6-14-18',1,55,37,8,23,84);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-8-22',2,59,37,4,26,84);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-3-24-2019',3,52,36,12,23,82);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-9-23',4,55,39,7,25,82);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-document-12-12-18',5,56,37,7,27,82);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-document-1-23-19',6,49,34,17,21,80);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2017/11/16/3d2002d2-bff7-11e7-9294-705f80164f6e_page.html',7,58,28,14,38,78);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://drive.google.com/file/d/1JWqPDt4hMKpZ9hpCAq2pzrOZki-NwSHN/view',8,51,34,15,21,77);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2018/07/11/09a17592-8123-11e8-b3b5-b61896f90919_page.html',9,49,45,5,20,76);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2019/images/03/20/rel4c.-.trump.and.russia.pdf',10,48,37,15,20,75);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/10/11/rel9c.-.trump.and.russia.pdf',11,48,36,16,23,73);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/09/11/rel8c.-.russia,.cohen,.impeachment.pdf',12,50,38,12,23,73);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://poll.qu.edu/national/release-detail?ReleaseID=2591',13,45,38,17,17,72);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/08/13/rel7a.-.trump2c.russia.pdf',14,47,39,13,22,72);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.foxnews.com/politics/fox-news-poll-7-12',15,48,40,12,25,72);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/6ujvi5p8z1/econTabReport.pdf',16,48,25,27,35,72);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/12/10/rel12a.-.trump.and.russia.pdf',17,43,40,16,21,71);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.washingtonpost.com/politics/polling/department-justice-mueller-russian/2018/01/29/27f3887a-fe68-11e7-9b5d-bbf0da31214d_page.html',18,50,31,19,28,71);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/yoolhxrark/econTabReport.pdf',19,38,31,30,16,70);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2018/05/15/5afb49bbe4b0a59b4dfe6ddd.pdf',20,38,32,30,19,70);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://cdn.cnn.com/cnn/2018/images/03/27/rel4b-north.korea2c.russia.pdf',21,48,35,17,29,69);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2019/images/04/30/rel6c.-.mueller.report.pdf',22,59,30,11,50,69);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/22joa4cprz/econTabReport.pdf',23,39,29,30,13,68);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/v00h5ts0qm/econTabReport.pdf',24,38,31,31,16,68);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/ppsei7g0oq/econTabReport.pdf',25,41,33,26,21,68);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/9th9okzc75/econTabReport.pdf',26,42,32,26,23,68);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/01/23/rel1f.-.russia.pdf',27,47,33,20,26,68);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2019/images/02/07/rel2c.-.russia.pdf',28,44,41,15,20,67);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/0kj6rhpqso/econTabReport.pdf',29,34,30,36,13,66);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2018/07/16/5b4ce38be4b0e7c958fe3ea5.pdf',30,36,33,30,18,66);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/183c0vbnai/econTabReport.pdf',31,40,30,30,22,66);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/02/26/rel3c.-.russia.pdf',32,47,33,21,28,66);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/9d5s05pspt/econTabReport.pdf',33,37,34,28,15,65);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/krhk8brhhw/econTabReport.pdf',34,34,31,35,15,65);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/fw0vfdqfpc/econTabReport.pdf',35,36,32,31,16,65);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/6ote18t1hm/econTabReport.pdf',36,38,31,32,21,65);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/rbrysksiud/econTabReport.pdf',37,35,29,36,16,64);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/05/10/rel5f.-.russia.pdf',38,44,38,18,17,64);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/75p17530i6/econTabReport.pdf',39,47,27,26,37,64);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/kwgrow0dna/econTabReport.pdf',40,36,30,34,14,63);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2019/02/13/5c6446b4e4b08da0ec8141f3.pdf',41,36,33,31,16,63);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2017/images/12/21/rel12c.-.russia.pdf',42,47,34,19,31,63);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/t1fl59zsim/econTabReport.pdf',43,48,25,27,42,63);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/wa3gpxn761/econTabReport.pdf',44,35,30,35,15,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/7hxorevceh/econTabReport.pdf',45,37,30,33,17,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://cdn.cnn.com/cnn/2018/images/06/21/rel6f.-.russia.investigation.pdf',46,41,39,21,20,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/oo6kz6sf4b/econTabReport.pdf',47,40,30,30,22,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/57yxejgrmo/econTabReport.pdf',48,39,25,36,23,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://morningconsult.com/wp-content/uploads/2018/03/180322_crosstabs_POLITICO_v1_DK.pdf',49,45,27,27,35,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/egvqvgp5a7/econTabReport.pdf',50,45,23,32,35,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://www.washingtonpost.com/page/2010-2019/WashingtonPost/2019/03/30/National-Politics/Polling/question_21323.xml',51,53,30,17,46,62);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/q6cfmfwwh4/econTabReport.pdf',52,35,32,33,15,61);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/4l31gznvf1/econTabReport.pdf',53,37,29,33,19,61);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/jhdmzhxe6k/econTabReport.pdf',54,36,25,38,22,61);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://maristpoll.marist.edu/wp-content/uploads/2019/04/NPR_PBS-NewsHour_Marist-Poll_USA-NOS-and-Tables_1904301401.pdf',55,54,26,20,47,61);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://big.assets.huffingtonpost.com/tabsHPRussiaIndictments20171030.pdf',56,39,26,34,25,60);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://big.assets.huffingtonpost.com/tabsHPRussiainvestigation20180123.pdf',57,37,25,38,25,59);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2019/04/22/5cbe11f6e4b0f7a84a73723d.pdf',58,44,28,27,39,59);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://big.assets.huffingtonpost.com/tabsHPMichaelFlynn20171201.pdf',59,36,28,35,17,58);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://big.assets.huffingtonpost.com/tabsHPMuellerinvestigation20180126.pdf',60,34,26,39,18,58);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/81kgdte5zw/econTabReport.pdf',61,34,29,37,18,57);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/y3tke5cxwy/econTabReport.pdf',62,37,27,36,20,57);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://morningconsult.com/wp-content/uploads/2017/07/170708_crosstabs_Politico_v1_TB.pdf',63,40,27,33,31,53);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('http://maristpoll.marist.edu/wp-content/uploads/2019/03/NPR_PBS-NewsHour_Marist-Poll_USA-NOS-and-Tables_1903251153.pdf',64,51,27,22,47,53);
INSERT INTO resultset(url,resultID,approve,disapprove,unsure,approveRepublican,approveDemocrats) VALUES ('https://big.assets.huffingtonpost.com/athena/files/2019/03/28/5c9d2beee4b00ba632795d13.pdf',65,43,27,30,44,51);


SELECT * FROM statistics;
SELECT * FROM pollster;
SELECT * FROM resultset;
SELECT * FROM questionnaire;