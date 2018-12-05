DELIMITER //

CREATE OR REPLACE PROCEDURE create_game (
    IN      leagueID_in     	    INT,
    IN      homeTeamID_in         INT,
    IN      awayTeamID_in         INT,
    IN      refereeID_in          INT,
    IN      gameTime_in           DATETIME,
    IN      fieldName_in          VARCHAR(32),
    IN      status_in             VARCHAR(16)
)
BEGIN
    INSERT INTO games (leagueID, homeTeamID, awayTeamID, refereeID, gameTime, fieldName, status)
        VALUES (leagueID_in, homeTeamID_in, awayTeamID_in, refereeID_in, gameTime_in, fieldName_in, status_in);
END

//

DELIMITER ;
