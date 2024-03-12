
from asciiartfunc import slowly_generate_print
from colorama import Fore,init
def game_credits_query():

    while True:
        game_credits_input = input("Would you like to see the credits? (y/n)\n").lower()
        
        if game_credits_input == "yes" or game_credits_input == "y":
            print("""Spaghetti coders:
            
    Eemil Nurmi 
    Onni Kivinen 
    Rene Kilpeläinen 
    Patrik Skogberg
            
    Thanks For Playing!!!"""
            )
            return 1
        elif game_credits_input == "no" or game_credits_input == "n":
            print("\nOh man :(")
            print(f"{Fore.GREEN}Thank you for playing!\n{Fore.RESET}")
            return False
        elif game_credits_input == "secret" or "easteregg":
            print("\nSecret airplane models: Peyman and Peltoniemi are open for use\n")
            print("\nSpaghetti coders: \nEemil Nurmi, Onni Kivinen, Rene Kilpeläinen ja Patrik Skogberg\nThanks For Playing!!!")

        else:
            print("\nInvalid input, please try again:\n")




