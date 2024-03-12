import gameintro
import quizv2
import gamesql
import gamecredits
from helpscreen import help_screen
from endgame import end_game

from colorama import Fore,init
#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

# testataan main funktion toimintaa

score = 0
distance = 0
used_time = 0
co2_used = 0
current_airport = gamesql.random_fly()
game_going = True

if gameintro.starting_screen(): # aloitetaanko peli vai ei

    airplane_model = gameintro.airplane_model_choice() # kysyy ja tallentaa lentokoneenyes
    while game_going:
        print(f"You are at {current_airport[0]}") #printtaa millä lentokentällä olet

        if help_screen(str(airplane_model), co2_used,used_time,distance,score):
            score += 1     # lisää pisteen oikein vastatusta kysymyksestä
            travel_info = gamesql.travel_co2(current_airport, airplane_model) # lentoon liittyvät tiedot
            distance += travel_info[0]
            co2_used += travel_info[1]
            used_time += travel_info[2]
            current_airport = travel_info[3]

            continue_game = input(f"{Fore.GREEN}Do you want to continue? (y/n):\n{Fore.RESET}").lower()
            if continue_game == "y":
                game_going = True
            elif continue_game == "n":
                game_going = end_game(score,co2_used,used_time)
            else:
                print(f"{Fore.YELLOW}Invalid input entered")

        else:
            game_going = end_game(score,co2_used,used_time) # lopettaa pelin puuttuu pelin loppuun kuuluvat funktiot
