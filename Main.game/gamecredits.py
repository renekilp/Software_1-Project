
from asciiartfunc import slowly_generate_print
from colorama import Fore,init
def game_credits_query():

    while True:
        game_credits_input = input(f"{Fore.GREEN}Would you like to see the credits? {Fore.WHITE}({Fore.CYAN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.RESET}\n").lower()
        
        if game_credits_input == "yes" or game_credits_input == "y":
            print(f"""\n{Fore.GREEN}Spaghetti coders:           
- Eemil Nurmi 
- Rene Kilpeläinen 
- Onni Kivinen 
- Patrik Skogberg{Fore.RESET}""")
            
            return 1
        elif game_credits_input == "no" or game_credits_input == "n":
            print("\nOh man :(")
            return False
        elif game_credits_input == "secret" or "easteregg":
            print("\nSecret airplane models: Peyman and Peltoniemi are open for use\n")
            print("\nSpaghetti coders: \nEemil Nurmi, Onni Kivinen, Rene Kilpeläinen ja Patrik Skogberg\nThanks For Playing!!!")

        else:
            print("\nInvalid input, please try again:\n")




