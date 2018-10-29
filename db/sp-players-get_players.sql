DELIMITER //

CREATE OR REPLACE PROCEDURE get_players (
)
BEGIN
    SELECT p.*, CAST(SUM(g.goals) AS INT), CAST(SUM(g.cleanSheet) AS INT), CAST(SUM(g.yellowCards) AS INT), CAST(SUM(g.redCards) AS INT)
      FROM players p
      JOIN gameMembers g on p.playerID = g.playerID
      GROUP BY p.playerID;
END

//

DELIMITER ;