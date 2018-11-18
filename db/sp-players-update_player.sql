DELIMITER //

CREATE OR REPLACE PROCEDURE update_player (
    IN      playerID_in         INT,
    IN      teamID_in           INT,
    IN      firstName_in        VARCHAR(32),
    IN      lastName_in         VARCHAR(32),
    IN      email_in            VARCHAR(128),
    IN      number_in           INT
)
BEGIN
    UPDATE players
        SET teamID = teamID_in, firstName = firstName_in, lastName = lastName_in, email = email_in, number = number_in
        WHERE playerID = playerID_in;
END

//

DELIMITER ;