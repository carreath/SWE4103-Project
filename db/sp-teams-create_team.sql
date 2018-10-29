DELIMITER //

CREATE OR REPLACE PROCEDURE create_team (
    IN      teamName_in     VARCHAR(32),
    IN      leagueID_in     	    INT,
    IN      colour_in        VARCHAR(7)
)
BEGIN
    INSERT INTO teams (teamName, leagueID, colour)
        VALUES (teamName_in, leagueID_in, colour_in);
END

//

DELIMITER ;

