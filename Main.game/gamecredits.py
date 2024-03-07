
from asciiartfunc import slowly_generate_print

def game_credits_query():

    while True:
        game_credits_input = input("Would you like to see the credits? (yes/no)\n").lower()
        
        if game_credits_input == "yes" or game_credits_input == "y":
            print("\n\nYIPPIIII \n")
            return 1
        elif game_credits_input == "no" or game_credits_input == "n":
            print("\nAw Shucks :(\n")
            return False
        else:
            print("\nInvalid input, please try again:\n")

game_credits_query()
