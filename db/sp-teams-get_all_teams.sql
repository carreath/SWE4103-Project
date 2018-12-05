

DELIMITER //

CREATE OR REPLACE PROCEDURE get_all_teams (
)
BEGIN
    SELECT t.*, CAST(SUM(g.goals) AS INT), CAST(SUM(g.cleanSheet) AS INT), CAST(SUM(g.yellowCards) AS INT), CAST(SUM(g.redCards) AS INT)
          FROM teams t
          JOIN gameMembers g ON t.teamID = g.teamID
          GROUP BY t.teamID
    UNION
    SELECT t.*, 0 AS goals, 0 AS cleanSheet, 0 AS yellowCards, 0 AS redCards
          FROM teams t
          LEFT JOIN gameMembers g ON g.teamID = t.teamID
          WHERE g.teamID IS NULL;
END

//

DELIMITER ;