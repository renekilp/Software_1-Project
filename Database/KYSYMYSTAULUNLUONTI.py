'''
------------------------------------------------------------------------------------------------------
AJA TÄMÄ OHJELMA VAIN KERRAN, JOTTA SAADAAN KYSYMYSTAULU LUOTUA JA KYSYMYKSET LISÄTTYÄ TÄHÄN TAULUUN.
------------------------------------------------------------------------------------------------------
Ohjelma jolla luodaan valmiiseen (flight_game) tietokantaan uusi taulu (questions), 
jossa omat sarakkeet (id:lle, kysymyksille, oikeille vastauksille ja neljälle väärälle vastaukselle).
'''

# YHTEYDEN OTTO MYSQL-TIETOKANTAAN
import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
#HUOM JOS HALUTAAN LISÄTÄ KYSYMYKSIÄ, KYSYMYSTEN JA VASTAUSTEN SEKÄ NELJÄN VÄÄRÄN VASTAUKSEN TÄYTYY OLLA SAMASSA JÄRJESTYKSESSÄ!!!

# Kysymykset
quiz_questions = [
    "What is the capital of France?", "Who wrote 'Romeo and Juliet'?",
    "What year did the Titanic sink?", "Who painted the Mona Lisa?",
    "What is the tallest mountain in the world?", "Who invented the lightbulb?",
    "What is the chemical symbol for water?", "What is the currency of Japan?",
    "Who is known as the father of modern physics?", "What is the chemical formula for table salt?",
    "Who is the author of 'To Kill a Mockingbird'?", "What is the main ingredient in guacamole?",
    "Who wrote the theory of relativity?", "What is the largest organ in the human body?",
    "Who painted the ceiling of the Sistine Chapel?", "What is the boiling point of water in Celsius?",
    "What is the capital of Australia?", "Who discovered penicillin?",
    "What is the process by which plants make their food called?", "What is the chemical symbol for gold?",
    "Who wrote '1984'?", "What is the largest mammal in the world?",
    "Who composed the famous 'Moonlight Sonata'?", "What is the hardest natural substance on Earth?",
    "What is the smallest country in the world?", "Who discovered gravity?",
    "What is the square root of 64?", "Who painted 'The Starry Night'?",
    "What is the study of the human mind and behavior called?",
    "What is the chemical symbol for iron?", "Who wrote 'The Great Gatsby'?",
    "What is the process of cellular division called?", "What is the currency of China?",
    "Who is often credited with inventing the internet?", "What is the largest desert in the world?",
    "Who is the current president of the United States (2024)?", "What is the main component of the Earth's atmosphere?",
    "What is the boiling point of water in Fahrenheit?", "Who wrote 'Pride and Prejudice'?",
    "What is the chemical symbol for oxygen?", "Who is said to have discovered America?",
    "What is the study of heredity called?", "Who painted 'The Last Supper'?",
    "What is the capital of Brazil?", "What is the chemical formula for hydrogen peroxide?",
    "Who wrote 'The Catcher in the Rye'?", "What is the largest ocean in the world?",
    "Who invented the telephone?", "What is the main ingredient in hummus?"]

# Oikeat vastaukset (SAMASSA JÄRJESTYKSESSÄ KUIN KYSYMYKSET)
quiz_answers = [
    "Paris", "William Shakespeare", "1912", "Leonardo da Vinci", "Mount Everest", "Thomas Edison", "H2O", "Yen",
    "Albert Einstein", "NaCl", "Harper Lee", "Avocado", "Albert Einstein", "Skin",
    "Michelangelo", "100°C", "Canberra", "Alexander Fleming", "Photosynthesis", "Au",
    "George Orwell", "Blue Whale", "Ludwig van Beethoven", "Diamond", "Vatican City", "Isaac Newton", "8",
    "Vincent van Gogh", "Psychology", "Fe", "F. Scott Fitzgerald", "Mitosis",
    "Yuan", "Tim Berners-Lee", "Antarctica", "Joe Biden", "Nitrogen",
    "212°F", "Jane Austen", "O", "Christopher Columbus", "Genetics", "Leonardo da Vinci", "Brasília", "H2O2",
    "J.D. Salinger", "Pacific Ocean", "Alexander Graham Bell", "Chickpeas"]

# Väärät vastaukset 4KPL VÄÄRIÄ VASTAUKSIA/PER KYSYMYS (SAMASSA JÄRJESTYKSESSÄ KUIN KYSYMYKSET)
fake_answers = [
    "London", "Rome", "Madrid", "Berlin",
    "Charles Dickens", "Jane Austen", "Fyodor Dostoevsky", "Stephen King",
    "1908", "1910", "1915", "1920",
    "Vincent van Gogh", "Pablo Picasso", "Rembrandt", "Claude Monet",
    "Mount Kilimanjaro", "K2", "Matterhorn", "Mount Fuji",
    "Nikola Tesla", "Alexander Graham Bell", "Michael Faraday", "Isaac Newton",
    "CO2", "HCl", "NH3", "H2O2",
    "Euro", "Dollar", "Rupee", "Yenish",
    "Galileo Galilei", "Johannes Kepler", "Aristotle", "Isaac Newton",
    "NaOH", "NaHCO3", "NaClO", "NaBr",
    "Ernest Hemingway", "Mark Twain", "J.K. Rowling", "George Orwell",
    "Tomato", "Lettuce", "Onion", "Cucumber",
    "Isaac Newton", "Charles Darwin", "Stephen Hawking", "Marie Curie",
    "Heart", "Brain", "Liver", "Stomach",
    "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Salvador Dalí",
    "50°C", "150°C", "200°C", "75°C",
    "Sydney", "Melbourne", "Perth", "Brisbane",
    "Louis Pasteur", "Marie Curie", "Gregor Mendel", "Jonas Salk",
    "Respiration", "Fermentation", "Transpiration", "Oxidation",
    "Ag", "Fe", "Hg", "Pb",
    "Aldous Huxley", "Ray Bradbury", "Ernest Hemingway", "J.R.R. Tolkien",
    "Elephant", "Giraffe", "Hippopotamus", "Rhinoceros",
    "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Franz Schubert", "Antonio Vivaldi",
    "Graphite", "Quartz", "Tungsten", "Steel",
    "Monaco", "Nauru", "Luxembourg", "Singapore",
    "Galileo Galilei", "Albert Einstein", "Nicolaus Copernicus", "Archimedes",
    "16", "4", "6", "2",
    "Pablo Picasso", "Claude Monet", "Edvard Munch", "Salvador Dalí",
    "Biology", "Neuroscience", "Anthropology", "Sociology",
    "Au", "Cu", "Hg", "Ag",
    "Jane Austen", "Ernest Hemingway", "Mark Twain", "Charles Dickens",
    "Meiosis", "Fertilization", "Differentiation", "Apoptosis",
    "Dollar", "Pound", "Yen", "Euro",
    "Al Gore", "Bill Gates", "Steve Jobs", "Mark Zuckerberg",
    "Sahara", "Gobi Desert", "Kalahari Desert", "Great Victoria Desert",
    "Joe Biden", "Barack Obama", "Donald Trump", "George W. Bush",
    "Oxygen", "Carbon Dioxide", "Argon", "Methane",
    "100°F", "150°F", "180°F", "200°F",
    "Pound Sterling", "Charles Dickens", "Emily Brontë", "Charlotte Brontë",
    "O2", "N2", "H2", "C",
    "Leif Erikson", "Amerigo Vespucci", "Vasco da Gama", "John Cabot",
    "Microbiology", "Botany", "Zoology", "Anatomy",
    "Michelangelo", "Raphael", "Titian", "Sandro Botticelli",
    "Bogotá", "Santiago", "Buenos Aires", "Quito",
    "H2O3", "H3O2", "HO2", "H2O4",
    "J.K. Rowling", "Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain",
    "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Southern Ocean",
    "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi", "Samuel Morse",
    "Olive oil", "Tahini", "Garlic", "Lemon juice"]

def kysymystaulun_luonti():
    '''
    Funktiolla luodaan kysymystaulu, jos sitä ei ole jo olemassa.
    id sarake, jossa Primary Key
    question-sarake - sarake kysymykselle (TEXT) syötteelle.
    correct_answer-sarake - oikea vastaus (TEXT) --||--
    ja neljä väärää vastausta wrong_answer_? (TEXT) sarakkeet.
    
    Auto_increment on käytössä, jotta jokaiselle kysymykselle saadaan uniikki id.
    '''
    kursori = yhteys.cursor() #luodaan kursori, ja executessa suoritetaan
    kursori.execute('''
            CREATE TABLE IF NOT EXISTS questions 
            (id INTEGER PRIMARY KEY AUTO_INCREMENT,
            question TEXT,
            correct_answer TEXT,
            wrong_answer_1 TEXT, 
            wrong_answer_2 TEXT,
            wrong_answer_3 TEXT,
            wrong_answer_4 TEXT)''')
    yhteys.commit() #tallennetaan muutokset ja suljetaan kursori
    kursori.close()
    print("\n1. Taulu luotu tietokantaan.")


def lisaa_kysymykset_tauluun(quiz_questions, quiz_answers):
    # Funktio kysymysten lisäämiseen tietokantaan    
    
    kursori = yhteys.cursor()

    # Lisää kysymykset tietokantaan kohtiin quiz_questions kysymys ja quiz_answers vastaus.
    for kysymys, oikea_vastaus in zip(quiz_questions, quiz_answers):
        # Luo uusi rivi tauluun
        kursori.execute("INSERT INTO questions (question, correct_answer) VALUES (%s, %s)",
                        (kysymys, oikea_vastaus))
    
    # Commitataan muutokset ja suljetaan
    yhteys.commit()
    kursori.close()
    print("2. Kysymykset ja niiden oikeat vastaukset lisätty tauluun.")


def väärät_vastaukset_per_rivi():
    kursori = yhteys.cursor()
    id = 1 # 1 koska se on ensimmäinen id
    
    for i in range(0, len(fake_answers), 4): # aloitetaan nollasta, mennään niin monelle riville kuin fake_answersissa on alkioita, ja lisätään 4 kerrallaan joka riville.
        kursori.execute(f"UPDATE questions SET wrong_answer_1 = %s, wrong_answer_2 = %s, wrong_answer_3 = %s, wrong_answer_4 = %s WHERE id = %s",
                        (fake_answers[i], fake_answers[i+1], fake_answers[i+2], fake_answers[i+3], id)) # 0 indeksistä alkaen, lisätään 1, 2 ja 3 indeksit, ja lisätään ne tietokantaan.
        id += 1 # lisätään id:eeseen 1 että päästään seuraavalle riville
    
    # Commitataan muutokset ja suljetaan
    yhteys.commit()
    kursori.close()
    print("3. Väärät vastaukset (4kpl) jokaiselle kysymykselle lisätty tauluun.\n")


kysymystaulun_luonti()
lisaa_kysymykset_tauluun(quiz_questions, quiz_answers)
väärät_vastaukset_per_rivi()