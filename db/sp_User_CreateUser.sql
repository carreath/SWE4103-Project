DELIMITER //

CREATE OR REPLACE PROCEDURE create_user (
    IN      userType        VARCHAR(16),
    IN      firstName       VARCHAR(32),
    IN      lastName        VARCHAR(32),
    IN      email           VARCHAR(64),
    IN      hash            VARCHAR(128)
)
BEGIN
    INSERT INTO users (userType, firstName, lastName, email, hash) 
        VALUES (userType, firstName, lastName, email, hash);
END

//

DELIMITER ;