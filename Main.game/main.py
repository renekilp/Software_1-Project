import Asciiartfunc
from geopy.distance import geodesic
import math
import mysql.connector

#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

from intro import intro #kutsutaan intro funktio tänne.

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)




# testataan main funktion toimintaa
def main():
    intro()

main()