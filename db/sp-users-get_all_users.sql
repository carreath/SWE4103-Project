DELIMITER //

CREATE OR REPLACE PROCEDURE get_all_users ()
BEGIN
    SELECT *
        FROM users;
END

//

DELIMITER ;
