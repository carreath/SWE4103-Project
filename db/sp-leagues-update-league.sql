DELIMITER //

CREATE OR REPLACE PROCEDURE update_league (
    IN      leagueID_in      INT
    IN      leagueName_in    VARCHAR(32),
    IN      season_in        VARCHAR(16),
    IN      pointScheme_in   VARCHAR(32),
    IN      coordinatorID_in INT
)
BEGIN
    UPDATE leagues
        SET leagueName = leagueName_in,
            season = season_in,
            coordinatorID = coordinatorID_in,
            pointScheme = pointScheme_in
        WHERE leagueID = leagueID_in;
END

//

DELIMITER ;