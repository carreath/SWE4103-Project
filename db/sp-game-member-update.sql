

DELIMITER //

CREATE OR REPLACE PROCEDURE update_game_member (
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
    Update gameMembers Set teamID = teamID_in, number = number_in, goals = goals_in, cleanSheet = cleanSheet_in, yellowCards = yellowCards_in, redCards = redCards_in
    Where playerID = playerID_in and gameID = gameID_in;
END

//

DELIMITER ;