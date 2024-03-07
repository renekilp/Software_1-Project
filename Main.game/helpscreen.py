from colorama import *
from Asciiartfunc import tutorial_ascii




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
    print(
        "First you have to choose a plane. The only difference between the planes is the co2 usage (and your own preference).\n"
        "\nYour main goal is to hop from airport to airport. You as a player is bombarded with offbeat trivia questions about each country you visit.\n"
        "Your journey will be filled with laughter and learning. But remember, with only one wrong answer, your plane will make an emergency landing "
        "ending your journey...\n"
        "How far can you reach without making a mistake? Let's find out!\n"
        "\nAfter the game ends, your will be scored based on the points, distance and co2 usage.\n"
        "\nRemember that you can always use the 'help' command if you find yourself stuck."
    )

def player_info():
    pass










def tutorial_screen():
    pass

#   exit, tutorial, player information, credits