DELIMITER //

CREATE OR REPLACE PROCEDURE create_league (
    IN      leagueName_in    VARCHAR(32),
    IN      season_in        VARCHAR(16)
)
BEGIN
    INSERT INTO leagues (leagueName, season)
        VALUES (leagueName_in, season_in);
END

//

DELIMITER ;