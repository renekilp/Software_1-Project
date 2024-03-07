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

# testataan main funktion toimintaa
def main():
    intro()

main()