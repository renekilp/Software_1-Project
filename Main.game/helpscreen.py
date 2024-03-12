from colorama import *
from asciiartfunc import *
from gamecredits import game_credits_query
from quizv2 import question_query_from_database


def help_screen(airplane_model, co2_used,used_time,distance,score):
    commands = ['quiz','tutorial', 'player info', 'quit', 'credits', '1', '2', '3', '4', '5']

    print(f"""
        {Fore.GREEN}Welcome to the help screen!
        Here's a list of all available commands:
        1. quiz
        2. tutorial
        3. player info
        4. quit
        5. credits
        
        """)
    help_command = input("Enter command\n").lower()
    if help_command not in commands:
        print("Invalid command! Please use one of the commands listed above.")
    elif help_command == 'quiz' or help_command == "1":
        return question_query_from_database()
    elif help_command == 'tutorial' or help_command == "2":
        tutorial_screen()
    elif help_command == 'player info' or help_command == "3":
        player_info(airplane_model, co2_used,used_time,distance,score)
    elif help_command == 'quit' or help_command == "4":
        quit_game()
    elif help_command == 'credits' or help_command == "5":
        credits_screen()



def tutorial_screen():
    tutorial_ascii()
    tut_text = """
    Heya! I'm your friendly co-pilot A.I O.N.N.I (Omnipotent, Neat, Navigation, Instructor)!
    I'm here to give you some nifty information about the game.
    
    First you have to choose a plane. The only difference between the planes is the co2 usage (and your own preference).
    Your main goal is to hop from airport to airport. You as a player is bombarded with offbeat trivia questions about each country you visit.
    Your journey will be filled with laughter and learning. But remember, with only one wrong answer, your plane will make an emergency landing 
    ending your journey...
    
    After the game ends, your will be scored based on the points, distance and co2 usage.
    How far can you reach without making a mistake? Let's find out! YOU GOT THIS BOSS!
    
    Remember that you can always use the 'help' command to see all the available commands!
    (even play this short tutorial again if you so desire.)
    """
    slowly_generate_print(tut_text, delay=0.015)
    print(Style.RESET_ALL)
    return help_screen()


def player_info(airplane_model, co2_used,used_time,distance,score):
    playerinfo_ascii()
    if airplane_model == "1":
        airplane_model = "Boeing 737"
    elif airplane_model == "2":
        airplane_model =  "Airbus a320"
    elif airplane_model == "3":
        airplane_model = "Saab JA37 Viggen"
    elif airplane_model == "Peltoniemi" or airplane_model == "Peyman":
        airplane_model = "Peltoniemi" or "Peyman"
    else:
        airplane_model = "Invalid airplane model"

    plinfo_text = (f"""{Fore.GREEN}
    Welcome BOSS! I've been tracking some of your progress...
    
    The plane you selected is: {airplane_model}
    
    Your current score is: {score}
    Your current flown distance is: {distance:.2f} kilometers
    Your current fly time is: {used_time / 24:.2f} days
    Your current co2 usage is: {co2_used / 1000:.2f} kilogramms
    
    Wowee! You are flying like a real captain! Let's push that score up.
    
    """)
    slowly_generate_print(plinfo_text, delay=0.015)
    print(Style.RESET_ALL)
    return help_screen()

def quit_game():
    print(f"{Fore.YELLOW}You chose to end the game. Farewell!")

    return False


def credits_screen():
    game_credits_query()




#   exit, tutorial, player information, credits