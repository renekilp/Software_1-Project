import Asciiartfunc
from geopy.distance import geodesic
import math
import mysql.connector
from connection import connector
import gameintro
import helpscreen
import quiz
import gamesql

#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

# testataan main funktion toimintaa

score = 0
distance = 0
used_time = 0
co2_used = 0
starting_screen()
search = search_large_airports()
airplane_model = airplane_model_choice()
current_airport = random_fly()
print(f" You are in {current_airport}!")
travel_result = travel_co2(current_airport, airplane_model)
distance = distance + travel_result[0]
co2_used = co2_used + travel_result[1]
used_time = used_time + travel_result[2]
quiz_asker()
if quiz_asker() == 1:
    score += 1
elif quiz_asker() == 0:
    pass