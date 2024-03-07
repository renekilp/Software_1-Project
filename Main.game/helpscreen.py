from colorama import *
from asciiartfunc import *




def help_screen():
    commands = ['tutorial', 'player info', 'quit', 'credits']
    while True:
        print(f"{Fore.GREEN}Welcome to the help screen!\nHere's a list of all available commands:\n1. Add a command\n2. Add a command\n3. Add a command\n4. Add a command")
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
    Heya! I'm your friendly co-pilot AI O.N.N.I (Omnipotent, Neat, Navigation, Instructor)!
    I'm here to give you some nifty information about the game.
    
    First you have to choose a plane. The only difference between the planes is the co2 usage (and your own preference).
    Your main goal is to hop from airport to airport. You as a player is bombarded with offbeat trivia questions about each country you visit.
    Your journey will be filled with laughter and learning. But remember, with only one wrong answer, your plane will make an emergency landing 
    ending your journey...
    
    After the game ends, your will be scored based on the points, distance and co2 usage.
    How far can you reach without making a mistake? Let's find out! YOU GOT THIS BOSS!
    
    Remember that you can always use the 'help' command if you find yourself stuck. I'm here to help!
    """
    slowly_generate_print(tut_text, delay=0.015)


def player_info():
    playerinfo_ascii()
    print(f"""
    Welcome BOSS! I've been tracking some of your progress...
    
    Your current score is: {score}
    Your current flown distance is: {distance}
    Your current fly time is: {used_time}
    Your current co2 usage is: {used_co2}
    
    Wowee! You are flying like a real captain! Let's push that score up.
    """)
    
    











tutorial_screen()

#   exit, tutorial, player information, credits