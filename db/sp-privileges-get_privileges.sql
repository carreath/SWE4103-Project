DELIMITER //

CREATE OR REPLACE PROCEDURE get_privileges (
    IN      privilegesID_in     INT
)
BEGIN
    SELECT *
        FROM privileges
        WHERE privilegesID = privilegesID_in;
END

//

DELIMITER ;