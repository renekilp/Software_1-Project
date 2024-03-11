from gamesql import new_score


def endgame(score): # pelin loppuun sijoittuvat functiot
    player_name = input("What is your name? \n")
    score = int(score)
    new_score(player_name, score)
