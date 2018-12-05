DELIMITER //

CREATE OR REPLACE PROCEDURE delete_game_member (
    IN      gameID_in    int,
    IN      playerID_in        int
)
BEGIN
    Delete from gameMembers Where playerID = playerID_in and gameID = gameID_in;
END

//

DELIMITER ;