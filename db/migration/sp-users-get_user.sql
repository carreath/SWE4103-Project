DELIMITER //

CREATE OR REPLACE PROCEDURE get_user (
    IN      email_in        VARCHAR(64)
)
BEGIN
    SELECT *
        FROM users
        WHERE email = email_in;
END

//

DELIMITER ;