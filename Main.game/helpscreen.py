from colorama import *
from asciiartfunc import *
from gamecredits import game_credits_query
from quizv2 import question_query_from_database

def help_screen():
    commands = ['quiz','tutorial', 'player info', 'quit', 'credits']

    print(f"""
        {Fore.GREEN}Welcome to the help screen!
        Here's a list of all available commands:
        1. quiz
        2. tutorial
        3. player info
        4. quit
        5. credits
        
        """)
    help_command = input("Enter command").lower()
    if help_command not in commands:
        print("Invalid command! Please use one of the commands listed above.")
    elif help_command == 'tutorial':
        tutorial_screen()
    elif help_command == 'player info':
        player_info()
    elif help_command == 'quit':
        quit_game()
    elif help_command == 'credits':
        credits_screen()
    elif help_command == 'quiz':
        return question_query_from_database()


def tutorial_screen():
    tutorial_ascii()
    tut_text = f"""{Fore.GREEN}
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


def player_info():
    playerinfo_ascii()
    plinfo_text = (f"""{Fore.GREEN}
    Welcome BOSS! I've been tracking some of your progress...
    
    The plane you selected is: {airplane_model}
    
    Your current score is: {score}
    Your current flown distance is: {distance}
    Your current fly time is: {used_time}
    Your current co2 usage is: {used_co2}
    
    Wowee! You are flying like a real captain! Let's push that score up.
    
    """)
    slowly_generate_print(plinfo_text, delay=0.015)
    print(Style.RESET_ALL)

def quit_game():
    print(f"{Fore.YELLOW}You chose to end the game. Farewell!")
    game_going = False
    return game_going


def credits_screen():
    game_credits_query()




#   exit, tutorial, player information, credits