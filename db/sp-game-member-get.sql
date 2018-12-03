DELIMITER //

CREATE OR REPLACE PROCEDURE get_game_roster (
    IN      gameID_in        INT
)
BEGIN
	SELECT p.playerID, p.firstName, p.lastName, p.email, p.loanedGames, g.*, game.homeTeamID, game.awayTeamID
      FROM players p
      Join gameMembers g on g.playerID = p.playerID
      Join games game on game.gameID = g.gameID
      Where g.gameID = gameID_in
      order by g.teamID;
END

//

DELIMITER ;