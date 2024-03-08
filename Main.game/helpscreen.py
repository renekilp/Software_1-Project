from colorama import *
from asciiartfunc import *
from gamecredits import game_credits_query


def help_screen():
    commands = ['tutorial', 'player info', 'quit', 'credits']
    while True:
        print(f"""
        {Fore.GREEN}Welcome to the help screen!
        Here's a list of all available commands:
        
        1. Tutorial
        2. Player info
        3. Quit
        4. Credits
        
        """)
        selected_command = input(f"\n{Fore.YELLOW}Please select a command:\n").lower()
        if selected_command not in commands:
            print("Invalid command! Please choose one of the available commands from the list.")
        elif selected_command == 'tutorial':
            tutorial_screen()
            break
        elif selected_command == 'player info':
            player_info()
            break
        elif selected_command == 'quit':
            quit_game()
            break
        elif selected_command == 'credits':
            credits_screen()
            break


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


def player_info():
    playerinfo_ascii()
    plinfo_text = (f"""
    Welcome BOSS! I've been tracking some of your progress...
    
    The plane you selected is: {airplane_model}
    
    Your current score is: {score}
    Your current flown distance is: {distance}
    Your current fly time is: {used_time}
    Your current co2 usage is: {used_co2}
    
    Wowee! You are flying like a real captain! Let's push that score up.
    
    """)
    slowly_generate_print(plinfo_text, delay=0.015)


def quit_game():
    print("You chose to end the game. Farewell!")
    game_going = False
    return game_going


def credits_screen():
    game_credits_query()


help_screen()

#   exit, tutorial, player information, credits