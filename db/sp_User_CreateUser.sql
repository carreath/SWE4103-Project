DELIMITER //

CREATE OR REPLACE PROCEDURE create_user (
    IN      firstName       VARCHAR(32),
    IN      lastName        VARCHAR(32),
    IN      email           VARCHAR(64),
    IN      hash            VARCHAR(256)
)
BEGIN
    INSERT INTO users (firstName, lastName, email, hash) 
        VALUES (firstName, lastName, email, hash);
END

//

DELIMITER ;
