DELIMITER //

CREATE OR REPLACE PROCEDURE get_game_team_lineup (
    IN      gameID_in        INT
)
BEGIN
	SELECT g.homeTeamID, g.awayTeamID
      FROM games g
      Where g.gameID = gameID_in;
END

//

DELIMITER ;