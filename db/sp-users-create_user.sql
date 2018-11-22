DELIMITER //

CREATE OR REPLACE PROCEDURE create_user (
    IN      firstName_in     VARCHAR(32),
    IN      lastName_in      VARCHAR(32),
    IN      email_in         VARCHAR(64),
    IN      hash_in          VARCHAR(256)
)
BEGIN
    INSERT INTO users (firstName, lastName, email, hash) 
        VALUES (firstName_in, lastName_in, email_in, hash_in);
END

//

DELIMITER ;