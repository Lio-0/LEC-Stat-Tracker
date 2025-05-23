"""run to setup database with proper tables"""

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error

USER = "root"
PASS = ""
HOST = "localhost"

def execute_query(connection, query):
    """Executes string as MySQL query"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_connection(connect_db):
    """Creates a connection to a MySQL instance and database"""
    try:
        if connect_db:
            connection = mysql.connector.connect(user=USER,
                                                 password=PASS,
                                                 host=HOST,
                                                 database="LEC_STATS")
        else:
            connection = mysql.connector.connect(user=USER,
                                                 password=PASS,
                                                 host=HOST)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return connection

if __name__ == "__main__":

    cnx = create_connection(False)
    execute_query(cnx, "DROP DATABASE IF EXISTS LEC_STATS")
    execute_query(cnx, "CREATE DATABASE LEC_STATS")

    cnx = create_connection(True)

    execute_query(cnx, "CREATE TABLE Players (Name VARCHAR(50) PRIMARY KEY NOT NULL,"
    + "RealName VARCHAR(50),"
    + "Role VARCHAR(10)"
    + ");")

    execute_query(cnx, "CREATE TABLE Teams ("
    + "Name VARCHAR(50) PRIMARY KEY NOT NULL,"
    + "Coach VARCHAR(50),"
    + "Top VARCHAR(50),"
    + "Jungle VARCHAR(50),"
    + "Mid VARCHAR(50),"
    + "ADC VARCHAR(50),"
    + "Support VARCHAR(50),"
    + "FOREIGN KEY(Top) REFERENCES Players(Name),"
    + "FOREIGN KEY(Jungle) REFERENCES Players(Name),"
    + "FOREIGN KEY(Mid) REFERENCES Players(Name),"
    + "FOREIGN KEY(ADC) REFERENCES Players(Name),"
    + "FOREIGN KEY(Support) REFERENCES Players(Name)"
    + ");")

    execute_query(cnx, "CREATE TABLE Champions ("
    + "Name VARCHAR(50) PRIMARY KEY NOT NULL,"
    + "ReleaseDate VARCHAR(50)"
    +");")

    execute_query(cnx, "CREATE TABLE Matches ("
    + "MatchID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,"
    + "RedSideTeam VARCHAR(50),"
    + "RedSideTop VARCHAR(50),"
    + "RedSideJgl VARCHAR(50),"
    + "RedSideMid VARCHAR(50),"
    + "RedSideAdc VARCHAR(50),"
    + "RedSideSup VARCHAR(50),"
    + "BlueSideTeam VARCHAR(50),"
    + "BlueSideTop VARCHAR(50),"
    + "BlueSideJgl VARCHAR(50),"
    + "BlueSideMid VARCHAR(50),"
    + "BlueSideAdc VARCHAR(50),"
    + "BlueSideSup VARCHAR(50),"
    + "WinningTeam VARCHAR(50),"
    + "FOREIGN KEY(RedSideTeam) REFERENCES Teams(Name),"
    + "FOREIGN KEY(RedSideTop) REFERENCES Champions(Name),"
    + "FOREIGN KEY(RedSideJgl) REFERENCES Champions(Name),"
    + "FOREIGN KEY(RedSideMid) REFERENCES Champions(Name),"
    + "FOREIGN KEY(RedSideAdc) REFERENCES Champions(Name),"
    + "FOREIGN KEY(RedSideSup) REFERENCES Champions(Name),"
    + "FOREIGN KEY(BlueSideTeam) REFERENCES Teams(Name),"
    + "FOREIGN KEY(BlueSideTop) REFERENCES Champions(Name),"
    + "FOREIGN KEY(BlueSideJgl) REFERENCES Champions(Name),"
    + "FOREIGN KEY(BlueSideMid) REFERENCES Champions(Name),"
    + "FOREIGN KEY(BlueSideAdc) REFERENCES Champions(Name),"
    + "FOREIGN KEY(BlueSideSup) REFERENCES Champions(Name),"
    + "FOREIGN KEY(WinningTeam) REFERENCES Teams(Name)"
    +");")

    #Add initial data to Players, Teams and Champions

    execute_query(cnx, "INSERT INTO Champions(Name, ReleaseDate) VALUES "
        + "('Aatrox', '2013-06-13'),"
        + "('Ahri', '2011-12-14'),"
        + "('Akali', '2010-05-11'),"
        + "('Akshan', '2021-07-22'),"
        + "('Alistar', '2009-02-21'),"
        + "('Ambessa', '2024-11-06'),"
        + "('Amumu', '2009-06-26'),"
        + "('Anivia', '2009-07-10'),"
        + "('Annie', '2009-02-21'),"
        + "('Aphelios', '2019-12-11'),"
        + "('Ashe', '2009-02-21'),"
        + "('Aurelion Sol', '2016-03-24'),"
        + "('Aurora', '2024-07-17'),"
        + "('Azir', '2014-09-16'),"
        + "('Bard', '2015-03-12'),"
        + "('Bel\\'Veth', '2022-06-09'),"
        + "('Blitzcrank', '2009-09-02'),"
        + "('Brand', '2011-04-12'),"
        + "('Braum', '2014-05-12'),"
        + "('Briar', '2023-09-14'),"
        + "('Caitlyn', '2011-01-04'),"
        + "('Camille', '2016-12-07'),"
        + "('Cassiopeia', '2010-12-14'),"
        + "('Cho\\'Gath', '2009-06-26'),"
        + "('Corki', '2009-09-19'),"
        + "('Darius', '2012-05-23'),"
        + "('Diana', '2012-08-07'),"
        + "('Dr. Mundo', '2009-09-02'),"
        + "('Draven', '2012-06-06'),"
        + "('Ekko', '2015-05-29'),"
        + "('Elise', '2012-10-26'),"
        + "('Evelynn', '2009-05-01'),"
        + "('Ezreal', '2010-03-16'),"
        + "('Fiddlesticks', '2009-02-21'),"
        + "('Fiora', '2012-02-29'),"
        + "('Fizz', '2011-11-15'),"
        + "('Galio', '2010-08-10'),"
        + "('Gangplank', '2009-08-19'),"
        + "('Garen', '2010-04-27'),"
        + "('Gnar', '2014-08-14'),"
        + "('Gragas', '2010-02-02'),"
        + "('Graves', '2011-10-19'),"
        + "('Gwen', '2021-04-15'),"
        + "('Hecarim', '2012-04-18'),"
        + "('Heimerdinger', '2009-10-10'),"
        + "('Hwei', '2023-12-06'),"
        + "('Illaoi', '2015-11-24'),"
        + "('Irelia', '2010-11-16'),"
        + "('Ivern', '2016-10-05'),"
        + "('Janna', '2009-09-02'),"
        + "('Jarvan IV', '2011-03-01'),"
        + "('Jax', '2009-02-21'),"
        + "('Jayce', '2012-07-07'),"
        + "('Jhin', '2016-02-01'),"
        + "('Jinx', '2013-10-10'),"
        + "('Kai\\'Sa', '2018-03-07'),"
        + "('Kalista', '2014-11-20'),"
        + "('Karma', '2011-02-01'),"
        + "('Karthus', '2009-06-12'),"
        + "('Kassadin', '2009-08-07'),"
        + "('Katarina', '2009-09-19'),"
        + "('Kayle', '2009-02-21'),"
        + "('Kayn', '2017-07-12'),"
        + "('Kennen', '2010-04-08'),"
        + "('Kha\\'Zix', '2012-09-27'),"
        + "('Kindred', '2015-10-14'),"
        + "('Kled', '2016-08-10'),"
        + "('Kog\\'Maw', '2010-06-24'),"
        + "('K\\'Sante', '2022-11-03'),"
        + "('LeBlanc', '2010-11-02'),"
        + "('Lee Sin', '2011-04-01'),"
        + "('Leona', '2011-07-13'),"
        + "('Lillia', '2020-07-22'),"
        + "('Lissandra', '2013-04-30'),"
        + "('Lucian', '2013-08-22'),"
        + "('Lulu', '2012-03-20'),"
        + "('Lux', '2010-10-19'),"
        + "('Malphite', '2009-09-02'),"
        + "('Malzahar', '2010-06-01'),"
        + "('Maokai', '2011-02-16'),"
        + "('Master Yi', '2009-02-21'),"
        + "('Mel', '2025-01-23'),"
        + "('Miss Fortune', '2010-09-08'),"
        + "('Milio', '2023-03-23'),"
        + "('Mordekaiser', '2010-02-24'),"
        + "('Morgana', '2009-02-21'),"
        + "('Nami', '2012-12-07'),"
        + "('Nasus', '2009-10-01'),"
        + "('Nautilus', '2012-02-14'),"
        + "('Naafiri', '2023-07-20'),"
        + "('Neeko', '2018-12-05'),"
        + "('Nidalee', '2009-12-17'),"
        + "('Nilah', '2022-07-13'),"
        + "('Nocturne', '2011-03-15'),"
        + "('Nunu & Willump', '2009-02-21'),"
        + "('Olaf', '2010-06-09'),"
        + "('Orianna', '2011-06-01'),"
        + "('Ornn', '2017-08-23'),"
        + "('Pantheon', '2010-02-02'),"
        + "('Poppy', '2010-01-13'),"
        + "('Pyke', '2018-05-31'),"
        + "('Qiyana', '2019-06-28'),"
        + "('Quinn', '2013-03-01'),"
        + "('Rakan', '2017-04-19'),"
        + "('Rammus', '2009-07-10'),"
        + "('Rek\\'Sai', '2014-12-11'),"
        + "('Rell', '2020-12-10'),"
        + "('Renata Glasc', '2022-02-17'),"
        + "('Renekton', '2011-01-18'),"
        + "('Rengar', '2012-08-21'),"
        + "('Riven', '2011-09-14'),"
        + "('Rumble', '2011-04-26'),"
        + "('Ryze', '2009-02-21'),"
        + "('Samira', '2020-09-21'),"
        + "('Sejuani', '2012-01-17'),"
        + "('Senna', '2019-11-10'),"
        + "('Seraphine', '2020-10-29'),"
        + "('Sett', '2020-01-14'),"
        + "('Shaco', '2009-10-10'),"
        + "('Shen', '2010-03-24'),"
        + "('Shyvana', '2011-11-01'),"
        + "('Singed', '2009-04-18'),"
        + "('Sion', '2009-02-21'),"
        + "('Sivir', '2009-02-21'),"
        + "('Skarner', '2011-08-09'),"
        + "('Smolder', '2024-01-31'),"
        + "('Sona', '2010-09-21'),"
        + "('Soraka', '2009-02-21'),"
        + "('Swain', '2010-10-05'),"
        + "('Sylas', '2019-01-25'),"
        + "('Syndra', '2012-09-13'),"
        + "('Tahm Kench', '2015-07-09'),"
        + "('Taliyah', '2016-05-18'),"
        + "('Talon', '2011-08-24'),"
        + "('Taric', '2009-08-19'),"
        + "('Teemo', '2009-02-21'),"
        + "('Thresh', '2013-01-23'),"
        + "('Tristana', '2009-02-21'),"
        + "('Trundle', '2010-12-01'),"
        + "('Tryndamere', '2009-05-01'),"
        + "('Twisted Fate', '2009-02-21'),"
        + "('Twitch', '2009-05-01'),"
        + "('Udyr', '2009-12-02'),"
        + "('Urgot', '2010-08-24'),"
        + "('Varus', '2012-05-08'),"
        + "('Vayne', '2011-05-10'),"
        + "('Veigar', '2009-07-24'),"
        + "('Vel\\'Koz', '2014-02-27'),"
        + "('Vex', '2021-09-23'),"
        + "('Vi', '2012-12-19'),"
        + "('Viego', '2021-01-21'),"
        + "('Viktor', '2011-12-29'),"
        + "('Vladimir', '2010-07-27'),"
        + "('Volibear', '2011-11-29'),"
        + "('Warwick', '2009-02-21'),"
        + "('Wukong', '2011-07-26'),"
        + "('Xayah', '2017-04-19'),"
        + "('Xerath', '2011-10-05'),"
        + "('Xin Zhao', '2010-07-13'),"
        + "('Yasuo', '2013-12-13'),"
        + "('Yone', '2020-08-06'),"
        + "('Yorick', '2011-06-22'),"
        + "('Yuumi', '2019-05-14'),"
        + "('Zac', '2013-03-29'),"
        + "('Zed', '2012-11-13'),"
        + "('Zeri', '2022-01-20'),"
        + "('Ziggs', '2012-02-01'),"
        + "('Zilean', '2009-04-18'),"
        + "('Zoe', '2017-11-21'),"
        + "('Zyra', '2012-07-24');")

    execute_query(cnx, "INSERT INTO Players(Name, RealName, Role) VALUES "
    + "('Oscarinin', 'Óscar Muñoz Jiménez', 'Top'),"
    + "('Razork', 'Iván Martín Díaz', 'Jungle'),"
    + "('Humanoid', 'Marek Brázda', 'Mid'),"
    + "('Upset', 'Elias Lipp', 'Adc'),"
    + "('Mikyx', 'Mihael Mehle', 'Support'),"
    + "('BrokenBlade', 'Sergen Çelik', 'Top'),"
    + "('SkewMond', 'Rudy Semaan', 'Jungle'),"
    + "('Caps', 'Rasmus Winther', 'Mid'),"
    + "('Hans Sama', 'Steven Liv', 'Adc'),"
    + "('Labrov', 'Labros Papoutsakis', 'Support'),"
    + "('Lot', 'Eren Yıldız', 'Top'),"
    + "('Closer', 'Can Çelik', 'Jungle'),"
    + "('Jackies', 'Adam Jeřábek', 'Mid'),"
    + "('Noah', 'Oh Hyeon-taek', 'Adc'),"
    + "('Jun', 'Yoon Se-jun', 'Support'),"
    + "('Canna', 'Kim Chang-dong', 'Top'),"
    + "('Yike', 'Martin Sundelin', 'Jungle'),"
    + "('Vladi', 'Vladimiros Kourtidis', 'Mid'),"
    + "('Caliste', 'Caliste Henry-Hennebert', 'Adc'),"
    + "('Targamas', 'Raphaël Crabbé', 'Support'),"
    + "('Myrwn', 'Alex Villarejo', 'Top'),"
    + "('Elyoya', 'Javier Prades Batalla', 'Jungle'),"
    + "('Jojopyun', 'Joseph Joon Pyun', 'Mid'),"
    + "('Supa', 'David Martínez García', 'Adc'),"
    + "('Alvaro', 'Álvaro Fernández del Amo', 'Support'),"
    + "('Adam', 'Adam Maanane', 'Top'),"
    + "('Malrang', 'Kim Geun-seong', 'Jungle'),"
    + "('Larssen', 'Emil Larsson', 'Mid'),"
    + "('Patrik', 'Patrik Jírů', 'Adc'),"
    + "('Execute', 'Lee Jeong-hoon', 'Support'),"
    + "('JNX', 'Janik Bartels', 'Top'),"
    + "('Isma', 'Ismaïl Boualem', 'Jungle'),"
    + "('Reeker', 'Steven Chen', 'Mid'),"
    + "('Rahel', 'Cho Min-seong', 'Adc'),"
    + "('Loopy', 'Kim Dong-hyeon', 'Support'),"
    + "('Irrelevant', 'Joel Miro Scharoll', 'Top'),"
    + "('113', 'Doğukan Balcı', 'Jungle'),"
    + "('Nuc', 'Ilias Bizriken', 'Mid'),"
    + "('Ice', 'Yoon Sang-hoon', 'Adc'),"
    + "('Parus', 'Polat Furkan Çiçek', 'Support'),"
    + "('Carlsen', 'Carl Ulsted Carlsen', 'Top'),"
    + "('Sheo', 'Théo Borile', 'Jungle'),"
    + "('Kamiloo', 'Kamil Haudegond', 'Mid'),"
    + "('Flakked', 'Victor Lirola Tortosa', 'Adc'),"
    + "('Stend', 'Paul Lardin', 'Support'),"
    + "('Naak Nako', 'Kaan Okan', 'Top'),"
    + "('Lyncas', 'Linas Nauncikas', 'Jungle'),"
    + "('Czajek', 'Mateusz Czajka', 'Mid'),"
    + "('Carzzy', 'Matyáš Orság', 'Adc'),"
    + "('Hylissang', 'Zdravets Galabov', 'Support')")

    execute_query(cnx, "INSERT INTO Teams(Name, Coach, Top, Jungle, Mid, ADC, Support) VALUES"
    + "('Fnatic', 'Fabian Lohmann', 'Oscarinin', 'Razork', 'Humanoid', 'Upset', 'Mikyx'),"
    + "('G2 Esports', 'Dylan Falco', 'BrokenBlade', 'SkewMond', 'Caps', 'Hans Sama', 'Labrov'),"
    + "('GIANTX', 'André Guilhoto', 'Lot', 'Closer', 'Jackies', 'Noah', 'Jun'),"
    + "('Karmine Corp', 'Reha Ramanana', 'Canna', 'Yike', 'Vladi', 'Caliste', 'Targamas'),"
    + "('Movistar KOI', 'Tomás Campelos', 'Myrwn', 'Elyoya', 'Jojopyun', 'Supa', 'Alvaro'),"
    + "('Rogue', 'Simon Payne', 'Adam', 'Malrang', 'Larssen', 'Patrik', 'Execute'),"
    + "('SK Gaming', 'David Rodriguez de la Torre', 'JNX', 'Isma', 'Reeker', 'Rahel', 'Loopy'),"
    + "('Team BDS', 'Yanis Kella', 'Irrelevant', '113', 'Nuc', 'Ice', 'Parus'),"
    + "('Team Heretics', 'Victor Machuca Segura', 'Carlsen', 'Sheo', 'Kamiloo', 'Flakked', 'Stend'),"
    + "('Team Vitality', 'James MacCormack', 'Naak Nako', 'Lyncas', 'Czajek', 'Carzzy', 'Hylissang')")

    execute_query(cnx, "" \
        "CREATE PROCEDURE InsertMatch (IN RTeam VARCHAR(50), RTop VARCHAR(50), RJgl VARCHAR(50), " \
        "RMid VARCHAR(50), RAdc VARCHAR(50), RSup VARCHAR(50), BTeam VARCHAR(50), BTop VARCHAR(50), " \
        "BJgl VARCHAR(50), BMid VARCHAR(50), BAdc VARCHAR(50), BSup VARCHAR(50), WTeam VARCHAR(50)) " \
        "BEGIN " \
        "INSERT INTO Matches(RedSideTeam, RedSideTop, RedSideJgl, RedSideMid, " \
        "RedSideAdc, RedSideSup, BlueSideTeam, BlueSideTop, BlueSideJgl, BlueSideMid, " \
        "BlueSideAdc, BlueSideSup, WinningTeam) " \
        "VALUES (RTeam, RTop, RJgl, RMid, RAdc, RSup, BTeam, BTop, BJgl, BMid, BAdc, BSup, WTeam);" \
        "END")

    execute_query(cnx, "" \
        "CREATE FUNCTION GetTeamWinrate (team VARCHAR(50)) " \
        "RETURNS float " \
        "DETERMINISTIC " \
        "BEGIN " \
        "DECLARE wins INT; " \
        "DECLARE played INT; " \
        "SELECT sum(WinningTeam = team) FROM Matches INTO wins; " \
        "SELECT sum(RedSideTeam = team OR BlueSideTeam = team) FROM Matches INTO played; " \
        "RETURN round(wins / played * 100, 2); " \
        "END")

    execute_query(cnx, "" \
        "CREATE FUNCTION GetChampionGamesPlayed (champ VARCHAR(50)) " \
        "RETURNS INT " \
        "DETERMINISTIC  " \
        "BEGIN " \
        "DECLARE played INT; " \
        "SELECT sum(BlueSideTop = champ OR BlueSideJgl = champ OR BlueSideMid = champ OR " \
        "BlueSideAdc = champ OR BlueSideSup = champ OR RedSideTop = champ OR " \
        "RedSideJgl = champ OR RedSideMid = champ OR RedSideAdc = champ OR RedSideSup = champ) FROM Matches INTO played; " \
        "RETURN played; " \
        "END")

    execute_query(cnx, "" \
        "CREATE FUNCTION GetChampionWinrate (champ VARCHAR(50)) " \
        "RETURNS float " \
        "DETERMINISTIC " \
        "BEGIN " \
        "DECLARE redWins INT; " \
        "DECLARE blueWins INT; " \
        "DECLARE played INT; " \
        "SELECT sum(RedSideTop = champ OR RedSideJgl = champ OR RedSideMid = champ OR " \
        "RedSideAdc = champ OR RedSideSup = champ) FROM Matches WHERE RedSideTeam = WinningTeam INTO redWins; " \
        "SELECT sum(BlueSideTop = champ OR BlueSideJgl = champ OR BlueSideMid = champ OR " \
        "BlueSideAdc = champ OR BlueSideSup = champ) FROM Matches WHERE BlueSideTeam = WinningTeam INTO BlueWins; " \
        "SELECT GetChampionGamesPlayed(champ) INTO played; " \
        "IF played = 0 THEN RETURN 0; END IF; " \
        "RETURN ROUND((redWins + blueWins) / played * 100, 2); " \
        "END")
    
    execute_query(cnx, "" \
        "CREATE FUNCTION GetSideWinrate (side VARCHAR(50))" \
        "RETURNS float " \
        "DETERMINISTIC " \
        "BEGIN " \
        "DECLARE redWins INT; " \
        "DECLARE blueWins INT; " \
        "DECLARE totalGames INT; " \
        "SELECT COUNT(*) FROM Matches INTO totalGames; " \
        "SELECT COUNT(*) FROM Matches WHERE RedSideTeam = WinningTeam INTO redWins; " \
        "SELECT COUNT(*) FROM Matches WHERE BlueSideTeam = WinningTeam INTO blueWins; " \
        "IF side = 'Red' THEN RETURN ROUND(redWins / totalGames * 100, 2); END IF; " \
        "RETURN ROUND(blueWins / totalGames * 100, 2); " \
        "END")
    
    #views

    execute_query(cnx, "" \
        "CREATE VIEW TeamStatistics AS " \
        "SELECT t.Name AS TeamName, " \
        "COUNT(m.MatchID) AS TotalGames, " \
        "SUM(CASE WHEN t.Name = m.WinningTeam THEN 1 ELSE 0 END) AS Wins, " \
        "GetTeamWinrate(t.Name) AS WinratePercent " \
        "FROM Teams t " \
        "LEFT JOIN Matches m ON t.Name = m.RedSideTeam OR t.Name = m.BlueSideTeam " \
        "GROUP BY t.Name;")

    execute_query(cnx, ""\
        "CREATE VIEW ChampionStatistics AS " \
        "SELECT c.Name AS ChampionName, " \
        "GetChampionGamesPlayed(c.Name) AS GamesPicked, " \
        "GetChampionWinrate(c.Name) AS WinRate " \
        "FROM Champions c " \
        "GROUP BY c.Name;")

    execute_query(cnx, "" \
        "CREATE VIEW PlayerInfo AS " \
        "SELECT p.Name, p.RealName AS 'Real Name', p.Role, t.Name AS Team " \
        "FROM Players p INNER JOIN Teams t ON " \
        "(p.Name = t.Top OR p.Name = t.Jungle OR p.Name = t.Mid OR p.Name = t.ADC or p.Name = t.Support);")

    execute_query(cnx, "" \
        "CREATE VIEW SideStatistics AS " \
        "SELECT " \
        "GetSideWinrate('Red') AS RedSideWinRate, " \
        "GetSideWinrate('Blue') AS BlueSideWinRate; ")

    execute_query(cnx, "" \
        "CREATE FUNCTION GetFavouriteChamp (player VARCHAR(50)) " \
        "RETURNS VARCHAR(50) " \
        "DETERMINISTIC " \
        "BEGIN " \
	    "DECLARE favourite VARCHAR(50); " \
        "DECLARE prole VARCHAR(10); " \
        "DECLARE pteam VARCHAR(50); " \
	    "SELECT Team FROM Players WHERE (player = Players.Name) INTO pteam; " \
        "SELECT Role FROM Players WHERE (player = Players.Name) INTO prole; " \
        "IF (prole LIKE 'Top') THEN " \
		"SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM " \
		"(SELECT Matches.RedSideTop AS Name FROM Matches " \
		"WHERE Matches.RedSideTeam = pteam UNION ALL " \
		"SELECT Matches.BlueSideTop AS Name FROM Matches " \
		"WHERE Matches.BlueSideTeam = pteam) AS champs1 GROUP BY Name " \
		"ORDER BY count DESC LIMIT 1) AS TOP INTO favourite; " \
	    "END IF; " \
        "IF (prole LIKE 'Jungle') THEN " \
		"SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM " \
		"(SELECT Matches.RedSideJgl AS Name FROM Matches " \
		"WHERE Matches.RedSideTeam = pteam UNION ALL " \
		"SELECT Matches.BlueSideJgl AS Name FROM Matches " \
		"WHERE Matches.BlueSideTeam = pteam) AS champs2 GROUP BY Name " \
		"ORDER BY count DESC LIMIT 1) AS JGL INTO favourite; " \
	    "END IF; " \
	    "IF (prole LIKE 'Mid') THEN " \
		"SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM " \
		"(SELECT Matches.RedSideMid AS Name FROM Matches " \
		"WHERE Matches.RedSideTeam = pteam UNION ALL " \
		"SELECT Matches.BlueSideMid AS Name FROM Matches " \
		"WHERE Matches.BlueSideTeam = pteam) AS champs3 GROUP BY Name " \
		"ORDER BY count DESC LIMIT 1) AS MID INTO favourite; " \
	    "END IF; " \
        "IF (prole LIKE 'Adc') THEN " \
		"SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM " \
		"(SELECT Matches.RedSideAdc AS Name FROM Matches " \
		"WHERE Matches.RedSideTeam = pteam UNION ALL " \
		"SELECT Matches.BlueSideAdc AS Name FROM Matches " \
		"WHERE Matches.BlueSideTeam = pteam) AS champs4 GROUP BY Name " \
		"ORDER BY count DESC LIMIT 1) AS ADC INTO favourite; " \
	    "END IF; " \
        "IF (prole LIKE 'Support') THEN " \
		"SELECT Name FROM (SELECT Name, SUM(Name = Name) AS count FROM " \
		"(SELECT Matches.RedSideSup AS Name FROM Matches " \
		"WHERE Matches.RedSideTeam = pteam UNION ALL " \
		"SELECT Matches.BlueSideSup AS Name FROM Matches " \
		"WHERE Matches.BlueSideTeam = pteam) AS champs5 GROUP BY Name " \
		"ORDER BY count DESC LIMIT 1) AS SUP INTO favourite; " \
	    "END IF;" \
	    "RETURN favourite;" \
        "END")

    cnx.close()

