DELIMITER //

CREATE OR REPLACE PROCEDURE get_team_roster (
    IN      teamID_in        INT
)
BEGIN
    SELECT p.*
      FROM players p
      Where p.teamID = teamID_in
      Order BY p.playerID;
END

//

DELIMITER ;