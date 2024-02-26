def intro(): # Intro funktio testi
    print('''
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)''')
        
    intro_prompt = input("Do you wish to Start the game? (yes/no): \n").lower()
    if intro_prompt == "yes":
        print("Great! Let's get started!")
    elif intro_prompt == "no":
        print("Goodbye!")

def airplane_model_choice(): #Funktio lentokonemallin valintaan
    airplane_model = input("Choose your airplane model: \n 1. Boeing 737 \n 2. Airbus A320 \n").lower()
    if airplane_model == "1":
        print("You have chosen the Boeing 737")
    elif airplane_model == "2":
        print("You have chosen the Airbus A320")
    else:
        print("Invalid input, please try again")

def intro_airplane_func(): #Funktio joka kutsuu intro ja airplane_model_choice funktiot Testinä
    intro()
    airplane_model_choice()
    
intro_airplane_func()