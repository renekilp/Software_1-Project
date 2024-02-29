import Asciiartfunc
from geopy.distance import geodesic
import math
import mysql.connector
import quiz


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)