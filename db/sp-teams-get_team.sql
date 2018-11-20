DELIMITER //

CREATE OR REPLACE PROCEDURE get_team (
    IN      teamID_in     INT
)
BEGIN
    SELECT * FROM teams WHERE teamID = teamID_in;
END

//

DELIMITER ;