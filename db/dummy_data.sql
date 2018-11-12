SELECT 'INSERTING DUMMY DATA' as 'INFO';

INSERT INTO leagues (leagueName, season, pointScheme) VALUES ('Fredericton Soccer League', 'Fall 2018', '3-1-0');

INSERT INTO teams (leagueID, teamName, colour) VALUES (1, 'Blue Birds', '#4b89ed'), (1, 'Tigers', '#d68126'), (1, 'Eagles', '#c1bab2'), (1, 'Goon Squad', '#cad804');

INSERT INTO players (teamID,firstName,lastName) VALUES (4,"Chastity","Hyde"),(3,"Jacqueline","Duffy"),(3,"Leroy","Baldwin"),(2,"Hashim","Lynn"),(2,"Inga","Mcneil"),(4,"Hadassah","Taylor"),(1,"Amanda","Osborn"),(2,"Nevada","Madden"),(4,"Karina","Hicks"),(3,"Dolan","Neal");
INSERT INTO players (teamID,firstName,lastName) VALUES (1,"Demetria","Houston"),(1,"Uriah","Thomas"),(2,"Driscoll","Atkinson"),(2,"Hedy","Bates"),(1,"Ila","Shields"),(2,"Yardley","Clay"),(3,"Chava","Barr"),(2,"Ivana","Warren"),(4,"Althea","Pennington"),(4,"Olivia","Barnett");
INSERT INTO players (teamID,firstName,lastName) VALUES (3,"Barrett","Bond"),(3,"Jarrod","Pittman"),(1,"Reece","Lester"),(3,"Troy","Suarez"),(4,"Rylee","Frank"),(1,"Jocelyn","Espinoza"),(2,"Shay","Buckley"),(1,"Quemby","Hensley"),(3,"Elvis","House"),(2,"Kerry","Cameron");
INSERT INTO players (teamID,firstName,lastName) VALUES (1,"Delilah","Carson"),(4,"Tanner","Stark"),(3,"Rhoda","Greene"),(4,"Oliver","Hopkins"),(1,"Phoebe","Hobbs"),(1,"Graiden","Malone"),(2,"Cole","Ferrell"),(1,"Alisa","Mccormick"),(3,"Ariel","Flores"),(2,"Kylynn","Obrien");

INSERT INTO games (leagueID,homeTeamID,awayTeamID,fieldName,gameTime,status) VALUES ("1",3,2,"FHS Lower","2018-12-05 01:01:16","Scheduled"),("1",4,2,"Barker Street","2018-12-02 16:16:30","Scheduled"),("1",3,2,"Barker Street","2018-12-09 04:08:04","Scheduled"),("1",3,1,"FHS Upper","2018-12-01 18:34:39","Scheduled"),("1",4,2,"FHS Lower","2018-12-13 13:32:06","Scheduled"),("1",4,2,"FHS Upper","2018-11-30 00:20:33","Scheduled"),("1",4,1,"Barker Street","2018-12-06 17:52:24","Scheduled"),("1",4,1,"FHS Lower","2018-12-14 09:27:20","Scheduled"),("1",4,1,"Barker Street","2018-11-26 11:34:13","Scheduled"),("1",4,2,"FHS Lower","2018-11-26 03:44:46","Scheduled");
INSERT INTO games (leagueID,homeTeamID,awayTeamID,fieldName,gameTime,status) VALUES ("1",3,2,"Barker Street","2018-11-04 15:11:00","Scheduled"),("1",3,1,"Devon Middle","2018-12-15 13:eam51:42","Scheduled"),("1",4,2,"FHS Lower","2018-11-25 20:59:55","Scheduled"),("1",4,1,"Devon Middle","2018-12-08 20:07:41","Scheduled"),("1",3,1,"FHS Upper","2018-11-11 18:19:02","Scheduled"),("1",3,2,"FHS Upper","2018-12-31 23:59:05","Scheduled"),("1",4,2,"Barker Street","2018-12-15 09:16:27","Scheduled"),("1",4,2,"Barker Street","2018-11-10 08:44:29","Scheduled"),("1",3,2,"Barker Street","2018-11-12 13:45:07","Scheduled"),("1",4,1,"FHS Lower","2018-12-26 16:59:18","Scheduled");

/* TEAM 1 gameMembers data */
INSERT INTO gameMembers (gameID,teamID,playerID,number,goals) VALUES (4,1,7,10,0),(4,1,11,10,0),(4,1,12,10,0),(4,1,15,10,0),(4,1,23,10,0),(4,1,26,10,0),(4,1,28,10,0),(4,1,31,10,1),(4,1,35,10,0),(4,1,36,10,2),(4,1,38,10,0),(7,1,7,10,0),(7,1,11,10,0),(7,1,12,10,0),(7,1,15,10,0),(7,1,23,10,0),(7,1,26,10,0),(7,1,28,10,0),(7,1,31,10,0),(7,1,35,10,0),(7,1,36,10,0),(7,1,38,10,0),(8,1,7,10,1),(8,1,11,10,0),(8,1,12,10,0),(8,1,15,10,0),(8,1,23,10,0),(8,1,26,10,0),(8,1,28,10,1),(8,1,31,10,0),(8,1,35,10,0),(8,1,36,10,0),(8,1,38,10,1),(9,1,7,10,0),(9,1,11,10,0),(9,1,12,10,0),(9,1,15,10,0),(9,1,23,10,0),(9,1,26,10,0),(9,1,28,10,0),(9,1,31,10,1),(9,1,35,10,0),(9,1,36,10,1),(9,1,38,10,0),(12,1,7,10,0),(12,1,11,10,0),(12,1,12,10,0),(12,1,15,10,0),(12,1,23,10,0),(12,1,26,10,1),(12,1,28,10,0),(12,1,31,10,0),(12,1,35,10,0),(12,1,36,10,0),(12,1,38,10,0),(14,1,7,10,0),(14,1,11,10,0),(14,1,12,10,0),(14,1,15,10,0),(14,1,23,10,0),(14,1,26,10,0),(14,1,28,10,1),(14,1,31,10,0),(14,1,35,10,0),(14,1,36,10,0),(14,1,38,10,0),(15,1,7,10,0),(15,1,11,10,0),(15,1,12,10,0),(15,1,15,10,0),(15,1,23,10,0),(15,1,26,10,1),(15,1,28,10,0),(15,1,31,10,0),(15,1,35,10,0),(15,1,36,10,0),(15,1,38,10,0),(20,1,7,10,2),(20,1,11,10,1),(20,1,12,10,0),(20,1,15,10,0),(20,1,23,10,0),(20,1,26,10,0),(20,1,28,10,1),(20,1,31,10,1),(20,1,35,10,0),(20,1,36,10,0),(20,1,38,10,1);
/* TEAM 2 gameMembers data */
INSERT INTO gameMembers (gameID,teamID,playerID,number,goals) VALUES (1,2,4,10,0),(1,2,5,10,0),(1,2,8,10,1),(1,2,13,10,0),(1,2,14,10,0),(1,2,16,10,0),(1,2,18,10,0),(1,2,27,10,1),(1,2,30,10,0),(1,2,37,10,2),(1,2,40,10,0),(2,2,4,10,0),(2,2,5,10,0),(2,2,8,10,0),(2,2,13,10,1),(2,2,14,10,0),(2,2,16,10,1),(2,2,18,10,0),(2,2,27,10,0),(2,2,30,10,0),(2,2,37,10,0),(2,2,40,10,0),(3,2,4,10,0),(3,2,5,10,0),(3,2,8,10,0),(3,2,13,10,0),(3,2,14,10,1),(3,2,16,10,1),(3,2,18,10,0),(3,2,27,10,0),(3,2,30,10,0),(3,2,37,10,0),(3,2,40,10,0),(5,2,4,10,0),(5,2,5,10,0),(5,2,8,10,0),(5,2,13,10,0),(5,2,14,10,0),(5,2,16,10,0),(5,2,18,10,0),(5,2,27,10,0),(5,2,30,10,0),(5,2,37,10,0),(5,2,40,10,0),(6,2,4,10,0),(6,2,5,10,0),(6,2,8,10,0),(6,2,13,10,0),(6,2,14,10,0),(6,2,16,10,0),(6,2,18,10,0),(6,2,27,10,0),(6,2,30,10,0),(6,2,37,10,0),(6,2,40,10,0),(10,2,4,10,0),(10,2,5,10,0),(10,2,8,10,1),(10,2,13,10,0),(10,2,14,10,2),(10,2,16,10,0),(10,2,18,10,0),(10,2,27,10,0),(10,2,30,10,0),(10,2,37,10,2),(10,2,40,10,1),(11,2,4,10,0),(11,2,5,10,0),(11,2,8,10,0),(11,2,13,10,0),(11,2,14,10,0),(11,2,16,10,0),(11,2,18,10,1),(11,2,27,10,0),(11,2,30,10,0),(11,2,37,10,0),(11,2,40,10,0),(13,2,4,10,2),(13,2,5,10,0),(13,2,8,10,0),(13,2,13,10,0),(13,2,14,10,0),(13,2,16,10,0),(13,2,18,10,0),(13,2,27,10,0),(13,2,30,10,0),(13,2,37,10,0),(13,2,40,10,0),(16,2,4,10,0),(16,2,5,10,0),(16,2,8,10,0),(16,2,13,10,0),(16,2,14,10,1),(16,2,16,10,1),(16,2,18,10,0),(16,2,27,10,0),(16,2,30,10,0),(16,2,37,10,0),(16,2,40,10,0),(17,2,4,10,0),(17,2,5,10,0),(17,2,8,10,0),(17,2,13,10,0),(17,2,14,10,0),(17,2,16,10,0),(17,2,18,10,0),(17,2,27,10,0),(17,2,30,10,0),(17,2,37,10,0),(17,2,40,10,0),(18,2,4,10,0),(18,2,5,10,1),(18,2,8,10,0),(18,2,13,10,0),(18,2,14,10,0),(18,2,16,10,0),(18,2,18,10,0),(18,2,27,10,1),(18,2,30,10,0),(18,2,37,10,0),(18,2,40,10,0),(19,2,4,10,0),(19,2,5,10,0),(19,2,8,10,0),(19,2,13,10,2),(19,2,14,10,0),(19,2,16,10,0),(19,2,18,10,0),(19,2,27,10,0),(19,2,30,10,0),(19,2,37,10,0),(19,2,40,10,0);
/* TEAM 3 gameMembers data */
INSERT INTO gameMembers (gameID,teamID,playerID,number,goals) VALUES (1,3,2,10,0),(1,3,3,10,0),(1,3,10,10,0),(1,3,17,10,2),(1,3,21,10,0),(1,3,22,10,0),(1,3,24,10,0),(1,3,29,10,2),(1,3,33,10,0),(1,3,39,10,0),(3,3,2,10,0),(3,3,3,10,0),(3,3,10,10,0),(3,3,17,10,0),(3,3,21,10,0),(3,3,22,10,0),(3,3,24,10,0),(3,3,29,10,0),(3,3,33,10,1),(3,3,39,10,0),(4,3,2,10,0),(4,3,3,10,0),(4,3,10,10,0),(4,3,17,10,0),(4,3,21,10,1),(4,3,22,10,1),(4,3,24,10,0),(4,3,29,10,0),(4,3,33,10,0),(4,3,39,10,0),(11,3,2,10,0),(11,3,3,10,1),(11,3,10,10,1),(11,3,17,10,0),(11,3,21,10,0),(11,3,22,10,2),(11,3,24,10,1),(11,3,29,10,0),(11,3,33,10,0),(11,3,39,10,0),(12,3,2,10,0),(12,3,3,10,0),(12,3,10,10,0),(12,3,17,10,0),(12,3,21,10,0),(12,3,22,10,1),(12,3,24,10,2),(12,3,29,10,1),(12,3,33,10,0),(12,3,39,10,1),(15,3,2,10,1),(15,3,3,10,1),(15,3,10,10,0),(15,3,17,10,1),(15,3,21,10,0),(15,3,22,10,0),(15,3,24,10,1),(15,3,29,10,0),(15,3,33,10,0),(15,3,39,10,1),(16,3,2,10,0),(16,3,3,10,1),(16,3,10,10,0),(16,3,17,10,0),(16,3,21,10,0),(16,3,22,10,1),(16,3,24,10,0),(16,3,29,10,0),(16,3,33,10,0),(16,3,39,10,0),(19,3,2,10,2),(19,3,3,10,0),(19,3,10,10,0),(19,3,17,10,0),(19,3,21,10,0),(19,3,22,10,0),(19,3,24,10,0),(19,3,29,10,0),(19,3,33,10,0),(19,3,39,10,1);
/* TEAM 4 gameMembers data */
INSERT INTO gameMembers (gameID,teamID,playerID,number,goals) VALUES (2,4,1,10,0),(2,4,6,10,0),(2,4,9,10,0),(2,4,19,10,0),(2,4,20,10,0),(2,4,25,10,0),(2,4,32,10,0),(2,4,34,10,0),(5,4,1,10,0),(5,4,6,10,0),(5,4,9,10,1),(5,4,19,10,0),(5,4,20,10,1),(5,4,25,10,0),(5,4,32,10,0),(5,4,34,10,0),(6,4,1,10,0),(6,4,6,10,0),(6,4,9,10,0),(6,4,19,10,0),(6,4,20,10,0),(6,4,25,10,0),(6,4,32,10,0),(6,4,34,10,0),(7,4,1,10,0),(7,4,6,10,0),(7,4,9,10,0),(7,4,19,10,0),(7,4,20,10,0),(7,4,25,10,0),(7,4,32,10,0),(7,4,34,10,0),(8,4,1,10,0),(8,4,6,10,0),(8,4,9,10,0),(8,4,19,10,0),(8,4,20,10,0),(8,4,25,10,0),(8,4,32,10,0),(8,4,34,10,1),(9,4,1,10,0),(9,4,6,10,0),(9,4,9,10,0),(9,4,19,10,0),(9,4,20,10,0),(9,4,25,10,0),(9,4,32,10,0),(9,4,34,10,0),(10,4,1,10,1),(10,4,6,10,0),(10,4,9,10,0),(10,4,19,10,1),(10,4,20,10,1),(10,4,25,10,0),(10,4,32,10,0),(10,4,34,10,1),(13,4,1,10,0),(13,4,6,10,0),(13,4,9,10,0),(13,4,19,10,0),(13,4,20,10,0),(13,4,25,10,2),(13,4,32,10,0),(13,4,34,10,0),(14,4,1,10,0),(14,4,6,10,0),(14,4,9,10,0),(14,4,19,10,0),(14,4,20,10,2),(14,4,25,10,0),(14,4,32,10,0),(14,4,34,10,0),(17,4,1,10,0),(17,4,6,10,1),(17,4,9,10,0),(17,4,19,10,0),(17,4,20,10,0),(17,4,25,10,0),(17,4,32,10,0),(17,4,34,10,1),(18,4,1,10,0),(18,4,6,10,0),(18,4,9,10,0),(18,4,19,10,0),(18,4,20,10,0),(18,4,25,10,0),(18,4,32,10,0),(18,4,34,10,0),(20,4,1,10,0),(20,4,6,10,1),(20,4,9,10,0),(20,4,19,10,0),(20,4,20,10,0),(20,4,25,10,0),(20,4,32,10,0),(20,4,34,10,0);

/* Privileges */
INSERT INTO privileges (privilegesType, cancelGame, updateScore, createPlayer, createGame, createUser, createTeam, createLeague, assignPlayer, assignManager, assignCoordinator, assignprivileges) VALUES ('Admin',1,1,1,1,1,1,1,1,1,1,1);
INSERT INTO privileges (privilegesType, cancelGame, updateScore, createPlayer, createGame, createUser, createTeam, createLeague, assignPlayer, assignManager, assignCoordinator, assignprivileges) VALUES ('Coordinator',1,1,1,1,0,1,0,1,1,0,0);
INSERT INTO privileges (privilegesType, cancelGame, updateScore, createPlayer, createGame, createUser, createTeam, createLeague, assignPlayer, assignManager, assignCoordinator, assignprivileges) VALUES ('Manager',0,0,1,0,0,0,0,1,0,0,0);
INSERT INTO privileges (privilegesType, cancelGame, updateScore, createPlayer, createGame, createUser, createTeam, createLeague, assignPlayer, assignManager, assignCoordinator, assignprivileges) VALUES ('Referee',0,1,0,0,0,0,0,0,0,0,0);

/* Default Users */
INSERT INTO users (privilegesID, userType, firstName, lastName, email, hash) VALUES (1, 'Admin', 'Site', 'Admin', 'admin@league.ca', '$pbkdf2-sha512$30000$.P.fszZmrBWCkFIqxZhzjrEWAoDQunfu3bt3bs25dw4$NGSfngQSKYV4wlIOmIfijmvXSWb0jsJLWI12XGRVTejxDk2UxV2EsEVs1p.K2QUEhth9A9Cy2b8jjyvDcJRsEA');
INSERT INTO users (privilegesID, userType, firstName, lastName, email, hash) VALUES (2, 'Coordinator', 'League', 'Coordinator', 'coordinator@league.ca', '$pbkdf2-sha512$30000$.P.fszZmrBWCkFIqxZhzjrEWAoDQunfu3bt3bs25dw4$NGSfngQSKYV4wlIOmIfijmvXSWb0jsJLWI12XGRVTejxDk2UxV2EsEVs1p.K2QUEhth9A9Cy2b8jjyvDcJRsEA');
INSERT INTO users (privilegesID, userType, firstName, lastName, email, hash) VALUES (3, 'Manager', 'Team', 'Manager', 'manager@league.ca', '$pbkdf2-sha512$30000$.P.fszZmrBWCkFIqxZhzjrEWAoDQunfu3bt3bs25dw4$NGSfngQSKYV4wlIOmIfijmvXSWb0jsJLWI12XGRVTejxDk2UxV2EsEVs1p.K2QUEhth9A9Cy2b8jjyvDcJRsEA');
INSERT INTO users (privilegesID, userType, firstName, lastName, email, hash) VALUES (4, 'Referee', 'Referee', '', 'referee@league.ca', '$pbkdf2-sha512$30000$.P.fszZmrBWCkFIqxZhzjrEWAoDQunfu3bt3bs25dw4$NGSfngQSKYV4wlIOmIfijmvXSWb0jsJLWI12XGRVTejxDk2UxV2EsEVs1p.K2QUEhth9A9Cy2b8jjyvDcJRsEA');
INSERT INTO users (firstName, lastName, email, hash) VALUES ('Default', 'User', 'user@league.ca', '$pbkdf2-sha512$30000$.P.fszZmrBWCkFIqxZhzjrEWAoDQunfu3bt3bs25dw4$NGSfngQSKYV4wlIOmIfijmvXSWb0jsJLWI12XGRVTejxDk2UxV2EsEVs1p.K2QUEhth9A9Cy2b8jjyvDcJRsEA');