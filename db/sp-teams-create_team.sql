DELIMITER //

CREATE OR REPLACE PROCEDURE create_team (
    IN      teanName_in     VARCHAR(32),
    IN      colour_in        VARCHAR(7),
    IN      leaguePoints_in         INT,
    IN      wins_in                 INT,
    IN      losses_in               INT,
    IN      draws_in                INT,
)
BEGIN
    INSERT INTO teams (teamName, colour, leaguePoints, wins, losses, draws)
        VALUES (teamName_in, colour_in, leaguePoints_in, wins_in, losses_in, draws_in);
END

//

DELIMITER ;