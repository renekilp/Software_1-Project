import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def search_large_airports(): # hakee isojen lentokenttien nimet ja sijainnin
    sql = "SELECT name,latitude_deg,longitude_deg FROM airport where type = 'large_airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    if len(airports) == 0:
        print("Airports not found")
    else:
        print("Airports found")
        return airports

def new_score(player_name,score): #tallentaa uuden pistemäärän tietokantaan
    sql = f"INSERT INTO values {player_name},{score}"  #puuttuu taulu
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print("New score added")