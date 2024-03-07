import gameintro
import quiz
import gamesql

#import quiz <<- pitää kutsua tyyppisesti from quiz import quiz_asker tms. -onni

# testataan main funktion toimintaa

score = 0
distance = 0
used_time = 0
co2_used = 0
current_airport = gamesql.random_fly()
game_going = True

gameintro.starting_screen()
airplane_model = gameintro.airplane_model_choice()

while game_going:

    if quiz.quiz_asker():
        score += 1     # lisää pisteen oikein vastatusta kysymyksestä
        travel_info = gamesql.travel_co2(current_airport, airplane_model) # lentoon liittyvät tiedot
        distance += travel_info[0]
        co2_used += travel_info[1]
        used_time += travel_info[2]
        current_airport = travel_info[3]

    else:
        game_going = False # lopettaa pelin puuttuu pelin loppuun kuuluvat funktiot
