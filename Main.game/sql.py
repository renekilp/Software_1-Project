import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def search_large_airports():
    sql = "SELECT * FROM airport where type = 'large_airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    if len(airports) == 0:
        print("No airports found")
    else:
        return airports
