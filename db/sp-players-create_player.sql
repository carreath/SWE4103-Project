DELIMITER //

CREATE OR REPLACE PROCEDURE create_player (
    IN      teamID_in        INT,
    IN      firstName_in     VARCHAR(32),
    IN      lastName_in      VARCHAR(32),
    IN      email_in         VARCHAR(64),
    IN      number_in        INT
)
BEGIN
    INSERT INTO players(teamID, firstName, lastName, email, number)
      VALUES (teamID_in, firstName_in, lastName_in, email_in, number_in);
END

//

DELIMITER ;