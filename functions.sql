DELIMITER //
CREATE FUNCTION GetTeamWinrate (team VARCHAR(50))  
    RETURNS float  
    DETERMINISTIC  
    BEGIN  
    DECLARE wins INT;  
    DECLARE played INT;  
    SELECT sum(WinningTeam = team) FROM Matches INTO wins;  
    SELECT sum(RedSideTeam = team OR BlueSideTeam = team) FROM Matches INTO played;  
    RETURN round(wins / played * 100, 2);  
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetChampionGamesPlayed (champ VARCHAR(50))  
    RETURNS INT  
    DETERMINISTIC   
    BEGIN  
    DECLARE played INT;  
    SELECT sum(BlueSideTop = champ OR BlueSideJgl = champ OR BlueSideMid = champ OR  
    BlueSideAdc = champ OR BlueSideSup = champ OR RedSideTop = champ OR  
    RedSideJgl = champ OR RedSideMid = champ OR RedSideAdc = champ OR RedSideSup = champ) FROM Matches INTO played;  
    RETURN played;  
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetChampionWinrate (champ VARCHAR(50))  
    RETURNS float  
    DETERMINISTIC  
    BEGIN  
    DECLARE redWins INT;  
    DECLARE blueWins INT;  
    DECLARE played INT;  
    SELECT sum(RedSideTop = champ OR RedSideJgl = champ OR RedSideMid = champ OR  
    RedSideAdc = champ OR RedSideSup = champ) FROM Matches WHERE RedSideTeam = WinningTeam INTO redWins;  
    SELECT sum(BlueSideTop = champ OR BlueSideJgl = champ OR BlueSideMid = champ OR  
    BlueSideAdc = champ OR BlueSideSup = champ) FROM Matches WHERE BlueSideTeam = WinningTeam INTO BlueWins;  
    SELECT GetChampionGamesPlayed(champ) INTO played;  
    IF played = 0 THEN RETURN 0; END IF;  
    RETURN ROUND((redWins + blueWins) / played * 100, 2);  
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetSideWinrate (side VARCHAR(50)) 
RETURNS float  
DETERMINISTIC  
BEGIN  
    DECLARE redWins INT;  
    DECLARE blueWins INT;  
    DECLARE totalGames INT;  
    SELECT COUNT(*) FROM Matches INTO totalGames;  
    SELECT COUNT(*) FROM Matches WHERE RedSideTeam = WinningTeam INTO redWins;  
    SELECT COUNT(*) FROM Matches WHERE BlueSideTeam = WinningTeam INTO blueWins;  
    IF side = 'Red' THEN RETURN ROUND(redWins / totalGames * 100, 2); END IF;  
    RETURN ROUND(blueWins / totalGames * 100, 2);  
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION GetFavouriteChamp (player VARCHAR(50))
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
	DECLARE favourite VARCHAR(50);
    DECLARE prole VARCHAR(10);
    DECLARE pteam VARCHAR(50);

	SELECT Team FROM Players WHERE (player = Players.Name) INTO pteam;
    SELECT Role FROM Players WHERE (player = Players.Name) INTO prole;
	
    IF (prole LIKE "Top") THEN
		SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM 
		(SELECT Matches.RedSideTop AS Name FROM Matches 
		WHERE Matches.RedSideTeam = pteam UNION ALL 
		SELECT Matches.BlueSideTop AS Name FROM Matches 
		WHERE Matches.BlueSideTeam = pteam) AS champs1 GROUP BY Name
		ORDER BY count DESC LIMIT 1) AS TOP INTO favourite;
	END IF;
    IF (prole LIKE "Jungle") THEN
		SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM 
		(SELECT Matches.RedSideJgl AS Name FROM Matches 
		WHERE Matches.RedSideTeam = pteam UNION ALL 
		SELECT Matches.BlueSideJgl AS Name FROM Matches 
		WHERE Matches.BlueSideTeam = pteam) AS champs2 GROUP BY Name
		ORDER BY count DESC LIMIT 1) AS JGL INTO favourite;
	END IF;
	IF (prole LIKE "Mid") THEN
		SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM 
		(SELECT Matches.RedSideMid AS Name FROM Matches 
		WHERE Matches.RedSideTeam = pteam UNION ALL 
		SELECT Matches.BlueSideMid AS Name FROM Matches 
		WHERE Matches.BlueSideTeam = pteam) AS champs3 GROUP BY Name
		ORDER BY count DESC LIMIT 1) AS MID INTO favourite;
	END IF;
    IF (prole LIKE "Adc") THEN
		SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM 
		(SELECT Matches.RedSideAdc AS Name FROM Matches 
		WHERE Matches.RedSideTeam = pteam UNION ALL 
		SELECT Matches.BlueSideAdc AS Name FROM Matches 
		WHERE Matches.BlueSideTeam = pteam) AS champs4 GROUP BY Name
		ORDER BY count DESC LIMIT 1) AS ADC INTO favourite;
	END IF;
    IF (prole LIKE "Support") THEN
		SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM 
		(SELECT Matches.RedSideSup AS Name FROM Matches 
		WHERE Matches.RedSideTeam = pteam UNION ALL 
		SELECT Matches.BlueSideSup AS Name FROM Matches 
		WHERE Matches.BlueSideTeam = pteam) AS champs5 GROUP BY Name
		ORDER BY count DESC LIMIT 1) AS SUP INTO favourite;
	END IF;
    
	RETURN favourite;
END //
DELIMITER ;