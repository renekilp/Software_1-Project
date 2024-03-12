import gamecredits
import gamesql
from colorama import Fore,init
init(autoreset=True)


def end_game(score,co2_used,used_time):
    print(f"{Fore.GREEN}Your final score is: {score}")
    print(f"Your final co2 and your flight time is: \n {co2_used:.2f} gramms and {used_time / 24:.2f} days")

    gamesql.top_players()
    while True:
        player_input = input("\nWould you like to save your score? (y/n) \n").lower()
        if player_input == "y":
            gamesql.new_score(player_name=input("Enter your name\n"),score = score)
            break
        elif player_input == "n":
            gamecredits.game_credits_query()
            print("Thanks for playing!")
            break
        else:
            print("Invalid input")
    exit()
