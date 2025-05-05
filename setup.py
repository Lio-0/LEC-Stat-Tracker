"""run to setup database with proper tables"""

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error

def execute_query(connection, query):
    """Executes string as MySQL query"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

try:
    cnx = mysql.connector.connect(user='root',
                                  password='',
                                  host='localhost')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    execute_query(cnx, "DROP DATABASE IF EXISTS LEC_STATS")
    execute_query(cnx, "CREATE DATABASE LEC_STATS")

    cnx = mysql.connector.connect(user='root',
                                  password='Liooil10!',
                                  host='localhost',
                                  database="LEC_STATS")

    execute_query(cnx, "CREATE TABLE Players (Name VARCHAR(50) PRIMARY KEY NOT NULL,"
    + "RealName VARCHAR(50),"
    + "Role VARCHAR(10),"
    + "Team VARCHAR(50)"
    + ");")

    execute_query(cnx, "CREATE TABLE Teams ("
    + "TeamName VARCHAR(50) PRIMARY KEY NOT NULL,"
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

    execute_query(cnx, "ALTER TABLE Players "
        + "ADD CONSTRAINT fk1 "
	    + "FOREIGN KEY (Team) "
	    + "REFERENCES Teams(TeamName)")
    cnx.close()
