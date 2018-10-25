SELECT 'INSERTING DUMMY DATA' as 'INFO';

INSERT INTO leagues (leagueName, season) VALUES ('Fredericton Soccer League', 'Fall 2018');

INSERT INTO teams (leagueID, teamName, colour) VALUES (1, 'Blue Birds', '#4b89ed'), (1, 'Tigers', '#d68126'), (1, 'Eagles', '#c1bab2'), (1, 'Goon Squad', '#cad804');

INSERT INTO players (teamID,firstName,lastName) VALUES (4,"Chastity","Hyde"),(3,"Jacqueline","Duffy"),(3,"Leroy","Baldwin"),(2,"Hashim","Lynn"),(2,"Inga","Mcneil"),(4,"Hadassah","Taylor"),(1,"Amanda","Osborn"),(2,"Nevada","Madden"),(4,"Karina","Hicks"),(3,"Dolan","Neal");
INSERT INTO players (teamID,firstName,lastName) VALUES (1,"Demetria","Houston"),(1,"Uriah","Thomas"),(2,"Driscoll","Atkinson"),(2,"Hedy","Bates"),(1,"Ila","Shields"),(2,"Yardley","Clay"),(3,"Chava","Barr"),(2,"Ivana","Warren"),(4,"Althea","Pennington"),(4,"Olivia","Barnett");
INSERT INTO players (teamID,firstName,lastName) VALUES (3,"Barrett","Bond"),(3,"Jarrod","Pittman"),(1,"Reece","Lester"),(3,"Troy","Suarez"),(4,"Rylee","Frank"),(1,"Jocelyn","Espinoza"),(2,"Shay","Buckley"),(1,"Quemby","Hensley"),(3,"Elvis","House"),(2,"Kerry","Cameron");
INSERT INTO players (teamID,firstName,lastName) VALUES (1,"Delilah","Carson"),(4,"Tanner","Stark"),(3,"Rhoda","Greene"),(4,"Oliver","Hopkins"),(1,"Phoebe","Hobbs"),(1,"Graiden","Malone"),(2,"Cole","Ferrell"),(1,"Alisa","Mccormick"),(3,"Ariel","Flores"),(2,"Kylynn","Obrien");