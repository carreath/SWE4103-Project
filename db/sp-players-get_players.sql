DELIMITER //

CREATE OR REPLACE PROCEDURE get_players (
)
BEGIN
    SELECT p.*, CAST(SUM(g.goals) AS INT), CAST(SUM(g.cleanSheet) AS INT), CAST(SUM(g.yellowCards) AS INT), CAST(SUM(g.redCards) AS INT)
      FROM players p
      JOIN gameMembers g on p.playerID = g.playerID
      GROUP BY p.playerID
    UNION
    SELECT p.*, 0 AS goals, 0 AS cleanSheet, 0 AS yellowCards, 0 AS redCards
      FROM players p
      LEFT JOIN gameMembers g on g.playerID = p.playerID
      WHERE g.playerID IS NULL;
END

//

DELIMITER ;