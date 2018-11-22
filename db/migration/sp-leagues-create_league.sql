DELIMITER //

CREATE OR REPLACE PROCEDURE create_league (
    IN      leagueName_in    VARCHAR(32),
    IN      season_in        VARCHAR(16),
    IN      pointScheme_in   VARCHAR(32)
)
BEGIN
    INSERT INTO leagues (leagueName, season, pointScheme)
        VALUES (leagueName_in, season_in, pointScheme_in);
END

//

DELIMITER ;