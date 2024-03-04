import Asciiartfunc
from geopy.distance import geodesic
import math
import mysql.connector
import connection

#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

from intro import intro #kutsutaan intro funktio tänne.

# testataan main funktion toimintaa
def main(sql_connection):
    intro()

main()