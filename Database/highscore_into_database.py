import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def high_score_taulun_luonti():
    kursori = yhteys.cursor()
    kursori.execute('''
            CREATE TABLE IF NOT EXISTS high_score 
            (id INTEGER PRIMARY KEY AUTO_INCREMENT,
            player_name TEXT,
            player_score TEXT)''')
    
    yhteys.commit()
    kursori.close()
    print("1. Taulu (high_score) luotu tietokantaan.")

high_score_taulun_luonti()


