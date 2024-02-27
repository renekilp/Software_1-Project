import random

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
    "Who is the current president of the United States?", "What is the main component of the Earth's atmosphere?",
    "What is the boiling point of water in Fahrenheit?", "Who wrote 'Pride and Prejudice'?",
    "What is the chemical symbol for oxygen?", "Who discovered America?",
    "What is the study of heredity called?", "Who painted 'The Last Supper'?",
    "What is the capital of Brazil?", "What is the chemical formula for hydrogen peroxide?",
    "Who wrote 'The Catcher in the Rye'?", "What is the largest ocean in the world?",
    "Who invented the telephone?", "What is the main ingredient in hummus?"]
quiz_answers = [
    "Paris", "William Shakespeare", "1912", "Leonardo da Vinci", "Mount Everest", "Thomas Edison", "H2O", "Yen",
    "Albert Einstein", "NaCl", "Harper Lee", "Avocado", "Albert Einstein", "Skin",
    "Michelangelo", "100°C", "Canberra", "Alexander Fleming", "Photosynthesis", "Au",
    "George Orwell", "Blue Whale", "Ludwig van Beethoven", "Diamond", "Vatican City", "Isaac Newton", "8",
    "Vincent van Gogh", "Psychology", "Fe", "F. Scott Fitzgerald", "Mitosis",
    "Yuan", "Tim Berners-Lee", "Antarctica", "Joe Biden", "Nitrogen",
    "212°F", "Jane Austen", "O", "Christopher Columbus", "Genetics", "Leonardo da Vinci", "Brasília", "H2O2",
    "J.D. Salinger", "Pacific Ocean", "Alexander Graham Bell", "Chickpeas"]
random_answers = [
    "Marie Curie", "C", "George Orwell", "Tiger", "Pyotr Ilyich Tchaikovsky",
    "Tungsten", "Monaco", "Louis Pasteur", "9", "Henri Matisse", "Anthropology",
    "N", "Hermann Hesse", "Fusion", "Russian Ruble", "Larry Page", "Gobi Desert",
    "Barack Obama", "Carbon Dioxide", "0°C", "Tennessee Williams", "Cu",
    "Johannes Kepler", "Ganges", "Berlin", "Vacuole", "Salvador Dalí",
    "Matterhorn", "Henry Ford", "NH3", "Pound Sterling", "New York City",
    "Emily Dickinson", "1865", "Mg", "Galileo Galilei", "Mount Kilimanjaro",
    "Mexico City", "Lysosome", "GBP", "Charles Dickens", "1492", "Pablo Picasso",
    "K2", "Nikola Tesla", "CO2", "Euro", "Max Planck", "C6H12O6", "William Golding",
    "Lion", "Wolfgang Amadeus Mozart", "Graphite", "Maldives", "Michael Faraday",
    "Rembrandt", "Sociology", "U", "Mark Twain", "Meiosis", "Indian Rupee",
    "Vint Cerf", "Sahara", "Donald Trump", "Oxygen", "32°F", "Fyodor Dostoevsky",
    "Mount Everest", "Thomas Edison", "H2O", "Yen", "Albert Einstein", "NaCl",
    "Harper Lee", "Avocado", "Albert Einstein", "Skin", "Michelangelo", "100°C",
    "Canberra", "Alexander Fleming", "Photosynthesis", "Au", "Leonardo da Vinci",
    "Brasília", "H2O2", "J.D. Salinger", "Pacific Ocean", "Alexander Graham Bell",
    "Chickpeas", "London", "CO2", "Euro", "Max Planck", "C6H12O6", "William Golding",
    "Lion", "Wolfgang Amadeus Mozart", "Graphite", "Maldives", "Michael Faraday",
    "6", "Rembrandt", "Sociology", "U", "Mark Twain", "Meiosis", "Indian Rupee",
    "Vint Cerf", "Sahara", "Donald Trump", "Oxygen", "32°F", "Fyodor Dostoevsky",
    "Mg", "Galileo Galilei", "Mount Kilimanjaro", "Mexico City", "Lysosome", "GBP",
    "New York City", "Emily Dickinson", "1865", "Salvador Dalí", "Matterhorn",
    "Henry Ford", "NH3", "Pound Sterling", "Marie Curie", "C", "George Orwell",
    "Tiger", "Pyotr Ilyich Tchaikovsky", "Tungsten", "Monaco", "Louis Pasteur",
    "9", "Henri Matisse", "Anthropology", "N", "Hermann Hesse", "Fusion",
    "Russian Ruble", "Larry Page", "Gobi Desert", "Barack Obama", "Carbon Dioxide",
    "0°C", "Tennessee Williams", "Cu", "Johannes Kepler", "Ganges", "Berlin",
    "Vacuole", "Salvador Dalí", "Matterhorn", "Henry Ford", "NH3", "Pound Sterling",
    "New York City", "Emily Dickinson", "1865", "Mg", "Galileo Galilei", "Mount Kilimanjaro",
    "Mexico City", "Lysosome", "GBP"]
asked_question = []
def quiz_asker (quiz_questions):
    length = len(quiz_questions)
    question_number = random.randint(0,length - 1)
    while question_number in asked_question:
        question_number = random.randint(0, length - 1)
    question = quiz_questions[question_number]
    q_answer = quiz_answers[question_number]
    r_answers = random.sample(random_answers, 4)
    r_answers.append(q_answer)
    random.shuffle(r_answers)
    print(f"{question}")
    for i in range(4):
        print(f"{i + 1}. {r_answers[i]}")
    user_answer = input("What is the correct answer? (1, 2, 3, 4, 5): \n")
    asked_question.append(question_number)
    if user_answer == str(r_answers.index(q_answer) + 1):
        print("CORRECT")
        return 1
    else:
        print("FALSE")
        return 0


result = quiz_asker(quiz_questions)
print(f"Result: {result}")