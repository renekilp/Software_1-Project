from colorama import *

def help_screen():
    commands = ['tutorial', 'player info', 'quit', 'credits']
    while True:
        print(f"{Fore.GREEN}Welcome to the help screen!\nHere's a list of all available commands:\n1. Add a command\n2. Add a command\n3. Add a command\n4. Add a command")
        selected_command = input(f"\n{Fore.YELLOW}Please select a command:\n").lower()
        if selected_command not in commands:
            print("Invalid command! Please choose one of the available commands from the list.")
        elif selected_command == 'tutorial':
            tutorial_screen()
        elif selected_command == 'player info':
            player_info()
        elif selected_command == 'quit':
            quit_game()
        elif selected_command == 'credits':
            credits_screen()







help_screen()

#   exit, tutorial, player information, credits