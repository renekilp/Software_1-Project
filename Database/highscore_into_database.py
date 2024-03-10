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
            player_name VARCHAR(255),
            player_score INTEGER)''')
    
    yhteys.commit()
    kursori.close()
    print("1. Taulu (high_score) luotu tietokantaan.")

high_score_taulun_luonti()


def peyman_tauluun(player_name, player_score):
    player_name = "Peyman"
    player_score = 100
    
    kursori = yhteys.cursor()
    kursori.execute("INSERT INTO high_score (player_name, player_score) VALUES (%s, %s)",
                    (player_name, player_score))
    yhteys.commit()
    kursori.close()
    print("2. Peyman pisteillä 100 lisätty tauluun.")


def matti_tauluun(player_name, player_score):
    player_name = "Matti"
    player_score = 100
    
    kursori = yhteys.cursor()
    kursori.execute("INSERT INTO high_score (player_name, player_score) VALUES (%s, %s)",
                    (player_name, player_score))
    yhteys.commit()
    kursori.close()
    print("3. Matti pisteillä 100 lisätty tauluun.")

peyman_tauluun("Peyman", 100)
matti_tauluun("Matti", 100)