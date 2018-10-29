DELIMITER //

CREATE OR REPLACE PROCEDURE get_players (
)
BEGIN
    SELECT p.*, SUM(g.goals), SUM(g.cleanSheet), SUM(g.yellowCards), SUM(g.redCards)
      FROM players p
      JOIN gameMembers g on p.playerID = g.playerID
      GROUP BY p.playerID;
END

//

DELIMITER ;