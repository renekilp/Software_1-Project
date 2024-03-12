import random
import mysql.connector
from colorama import Fore,init
import endgame

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def question_query_from_database(co2_used,used_time,distance,score):
    '''
    Tässä funktiossa ensin arvotaan id numero, käyttäen 
    Sitten haetaan yksitellen tietokannasta tässä järjestyksessä: kysymys, oikea vastaus ja neljä väärää vastausta, alussa arvotulla id numerolla.
    Sitten jokainen vastaus muutetaan stringiksi.
    '''
    cursor = connection.cursor() # Yhdistetään tietokantaan
    
    # Haetaan tietokannasta kuinka monta riviä eli kysymystä taulussa on.
    cursor.execute("SELECT COUNT(*) FROM questions")
    amount_of_rows_in_table = cursor.fetchone()

    # Muuttuja joka arvotaan väliltä 1-49, joka on tietokannassa olevien kysymysten määrä tällä hetkellä.
    random_id_number_for_question = random.randint(1, amount_of_rows_in_table[0]) # <-- Tämä on se arvottu id numero indeksistä 0 alkaen.
    
    # print(random_id_number_for_question) # --> TESTI NIIN NÄEN MIKÄ ID NUMERO ON VALITTU, JA VOIN VERRATA TAULUKKOON.

    # Seuraavaksi haetaan kysymys taulusta, alussa arvotulla id numerolla.
    cursor.execute(f"SELECT question FROM questions WHERE id='{random_id_number_for_question}'")
    chosen_question_from_database = cursor.fetchone() 

    # Haetaan oikea vastaus tietokannasta.
    cursor.execute(f"SELECT correct_answer FROM questions WHERE id='{random_id_number_for_question}'")
    correct_answer_from_database = cursor.fetchone()
    

    # Haetaan kaikki väärät vastaukset tietokannasta
    cursor.execute(f"SELECT wrong_answer_1, wrong_answer_2, wrong_answer_3, wrong_answer_4 FROM questions WHERE id='{random_id_number_for_question}'")
    wrong_answers_from_database = cursor.fetchone()

    # Muunnetaan (1) oikea vastaus ja (4) väärää vastausta omiksi muuttujiksi, mitkä haettiin edellisessä cursorissa.
    # Lisätään indeksit loppuun, jotta tulostamisen ulkoasussa ei ole (' ') merkkejä. Eli muuttuja on pelkkä sarakkeen sisältö.
    correct_answer = correct_answer_from_database[0] # <-- Tämä on oikea vastaus.
    wrong_answer_1 = wrong_answers_from_database[0]  # <-- Tämä on väärä vastaus 1.
    wrong_answer_2 = wrong_answers_from_database[1]  # <-- Tämä on väärä vastaus 2.
    wrong_answer_3 = wrong_answers_from_database[2]  # <-- Tämä on väärä vastaus 3.
    wrong_answer_4 = wrong_answers_from_database[3]  # <-- Tämä on väärä vastaus 4.

    # Lisätään kaikki vastaukset listaan
    all_answers_list = [correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3, wrong_answer_4]
    
    # Sekoitetaan vastaukset, jotta oikea vastaus ei ole aina ensimmäisenä.
    random.shuffle(all_answers_list)
    
    # Tulostetaan kysymys ja sekoitetut vastaukset käyttäjälle, tarvitaan kuitenkin lisätä indexit niin saadaan kaikki siitä sekoitetusta listasta.
    print(f"{Fore.GREEN}\n{chosen_question_from_database[0]} Choose the right answer (1-5):") # Tässä tulostetaan, se kysymys mikä on arvottu funktion alussa.
    print(f"1. {all_answers_list[0]}") # 0-indeksin vastaus
    print(f"2. {all_answers_list[1]}") # 1-  ---||---
    print(f"3. {all_answers_list[2]}") # 2-  ---||---
    print(f"4. {all_answers_list[3]}") # 3-  ---||---
    print(f"5. {all_answers_list[4]}{Fore.RESET}") # 4-  ---||---
    
    # Käyttäjän syöte.
    user_input = input(f"\n{Fore.GREEN}Your answer (1-5):\n{Fore.RESET}")

    # Tarkistetaan että käyttäjän syöte koostuu ainoastaan numeroista 1-5. Jos ei, kysytään uudestaan.
    while user_input not in ["1", "2", "3", "4", "5"] or user_input == "": # eli "Kun syöte ei ole mikään 'näistä' tai 'näistä'"
        print(f"\n{Fore.YELLOW}Invalid input.{Fore.RESET}")
        user_input = input(f"{Fore.GREEN}Choose the right answer (1-5):\n{Fore.RESET}")
    
    # Koska listan indeksit alkavat nollasta, ja syöte on 1-5 niin täytyy vähentää yhdellä. Ja tarkistetaan onko vastaus oikein.
    if all_answers_list[int(user_input)-1] == correct_answer:
        print(f"{Fore.GREEN}\nCORRECT!\n{Fore.RESET}")
        return True # Palautetaan True, jos vastaus on oikein.
    
    # Muussa tapauksessa tulostetaan oikea vastaus ja peli loppuu.
    else:
        print(f"{Fore.RED}\nWRONG! {Fore.YELLOW}The correct answer was: {correct_answer}.{Fore.RESET}")
        endgame.end_game(score,co2_used,used_time)
        exit()

# testi_piste_lista = []

# def quiz_query_function():

    # Jos edellinen funktio palauttaa arvon True, niin kysytään haluaako pelaaja jatkaa.

         

# quiz_query_function() # Kutsutaan funktiota

# print(f"Your score is: {sum(testi_piste_lista)}") # Tulostetaan pisteet, jotka on kerätty listassa.