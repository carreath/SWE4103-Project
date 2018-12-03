DELIMITER //

CREATE OR REPLACE PROCEDURE create_game_member (
    IN      gameID_in    int,
    IN      playerID_in        int,
    IN      teamID_in   int,
    IN      number_in   int,
    IN      goals_in   int,
    IN      cleanSheet_in   int,
    IN      yellowCards_in   int,
    IN      redCards_in   int
)
BEGIN
    INSERT INTO gameMembers (gameID, playerID, teamID, number, goals, cleanSheet, yellowCards, redCards)
        VALUES (gameID_in, playerID_in, teamID_in, number_in, goals_in, cleanSheet_in, yellowCards_in, redCards_in);
END

//

DELIMITER ;