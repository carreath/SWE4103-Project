DELIMITER //

CREATE OR REPLACE PROCEDURE update_game (
    IN      gameID_in             INT,
    IN      leagueID_in     	    INT,
    IN      homeTeamID_in         INT,
    IN      awayTeamID_in         INT,
    IN      refereeID_in          INT,
    IN      gameTime_in           DATETIME,
    IN      fieldName_in          VARCHAR(32),
    IN      status_in             VARCHAR(16)
)
BEGIN
    UPDATE games
        SET leagueID = leagueID_in,
            homeTeamID = homeTeamID_in,
            awayTeamID = awayTeamID_in,
            refereeID = refereeID_in,
            gameTime = gameTime_in,
            fieldName = fieldName_in,
            status = status_in
        WHERE gameID = gameID_in;
END

//

DELIMITER ;
