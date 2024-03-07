import Asciiartfunc
from geopy.distance import geodesic
import math
import mysql.connector
from connection import connector
from intro import intro
import helpscreen
import quiz
import sql

#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

from intro import intro #kutsutaan intro funktio tänne.
from intor import airplane_model_choice

# testataan main funktion toimintaa
def main():
    intro()

main()
search = search_large_airports()
airplane_model = airplane_model_choice()
current_airport = random_fly()
travel_co2(random_fly(), airplane_model)