from art import *
from colorama import Fore, Back, Style
import time

#   funktion tarkoitus muuttaa haluttu teksti suoraan haluttuun ascii muotoon
def text_to_ascii(text, style='standard'):
    #   Korvaa parametri 'text' halutulla tekstillä
    #   Korvaa parametri 'style' halutulla tyylillä
    if style == 'standard':
        return text2art(text)
    elif style == 'block':
        return text2art(text, font='block')
    elif style == 'banner':
        return text2art(text, font='banner3')
    #   Tähän funktioon lisätty alustavasti vain 3 esimerrki tyyliä
    #   Luo uusi elif lause, jos haluat uuden tyylin
    else:
        return "Invalid style specified"


def welcome_text_to_ascii(): #   Welcome ascii
    welcome_text = "Welcome!"
    ascii_art = text_to_ascii(welcome_text, style='standard')
    print(Fore.BLUE + ascii_art)
    print(Style.RESET_ALL)

def tutorial_ascii():
    tutorial_text = "TUTORIAL"  #   Tutorial ascii
    ascii_art = text_to_ascii(tutorial_text, style='banner')
    print(Fore.GREEN + "-" * 92 + "\n")
    print(Fore.GREEN + ascii_art)
    print(Fore.GREEN + "-" * 92)
    print(Style.RESET_ALL)

def playerinfo_ascii():
    player_text = "PLAYER INFO" #   player info ascii
    ascii_art = text_to_ascii(player_text, style='banner')
    print(Fore.GREEN + "-" * 92 + "\n")
    print(Fore.GREEN + ascii_art)
    print(Fore.GREEN + "-" * 92)
    print(Style.RESET_ALL)



#   tätä samaa funktioo käytetään pelin alussa feikki lautauspalkissa
#   loin sen tänne uusiks jos haluutte käyttää
def slowly_generate_print(text, delay=0.1):
    #   korvaa text halutulla tekstillä
    #   määritä printin nopeus vaihtamalla delay arvoa
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

