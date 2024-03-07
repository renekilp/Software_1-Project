import mysql.connector
import random
from geopy.distance import geodesic

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
        pass
    else:
        return airports

def new_score(player_name,score): #tallentaa uuden pistemäärän tietokantaan
    sql = f"INSERT INTO values {player_name},{score}"  #puuttuu taulu
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print("New score added")

def random_fly(): #lennättää pelaajan uudelle random lentokentälle
    possible_airports = search_large_airports()
    airport_number = random.randint(0,len(possible_airports)-1)
    user_airport = possible_airports[airport_number]
    return user_airport

def travel_co2(user_airport, airplane_model_input): #laskee lentoajan, co2 päästöt ja matkan
    next_airport = random_fly()
    next_coordinates = [next_airport[1], next_airport[2]]
    current_coordinates = [user_airport[1], user_airport[2]]
    distance = geodesic(next_coordinates, current_coordinates).kilometers
    co2 = 0
    flight_time = 0
    if airplane_model_input == "1": #airbus a320
        co2 = distance * 62.5 #grammaa per kilometri
        flight_time = distance / 830 #kmh
    elif airplane_model_input == "2": #boeing 737
        co2 = distance * 61
        flight_time = distance / 845
    elif airplane_model_input == "3": #saab ja37 viggen
        co2 = distance * 435
        flight_time = distance / 2231
    elif airplane_model_input == "Peltoniemi" or "Peyman":
        co2 = distance * 0.45
        flight_time = distance / 6
    else:
        print("Invalid airplane, cant calculate emission and distance")

    results = [distance, co2, flight_time, next_airport]
    return results
