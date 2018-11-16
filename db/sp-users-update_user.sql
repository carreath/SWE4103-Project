DELIMITER //

CREATE OR REPLACE PROCEDURE update_user (
    IN      userID_in           INT,
    IN      privilegeID_in      INT,
    IN      userType_in         VARCHAR(32),
    IN      firstName_in        VARCHAR(32),
    IN      lastName_in         VARCHAR(32),
    IN      email_in            VARCHAR(128)
)
BEGIN
    UPDATE users
        SET privilegesID = privilegeID_in, userType = userType_in, firstName = firstName_in, lastName = lastName_in, email = email_in
        WHERE userID = userID_in;
END

//

DELIMITER ;