import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
def query_database(sql,fetchall=True): #Tein täst funktion, niin ei tarvi aina tehä cursor ja execute
    cursor = connection.cursor()
    cursor.execute(sql)
    
    if fetchall:
        return cursor.fetchall()
    else:
        return cursor.fetchone()

# query_database("SELECT * FROM airport") TestiTesti

def search_large_airports(): # hakee isojen lentokenttien nimet ja sijainnin
    sql = "SELECT name,latitude_deg,longitude_deg FROM airport where type = 'large_airport'"
    airports = query_database(sql) # airports = suoritetaan query_database funktio, joka hakee tietokannasta tiedot annetulla sql muuttujalla
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
