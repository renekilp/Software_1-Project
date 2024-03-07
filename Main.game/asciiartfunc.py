from art import *
from colorama import Fore, Back, Style
import time

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

#   Laitoin nää kommentteihin, koska kun importtasin welcome_text_to_ascii() niin tuli erroria, koska nää alapuoliset rivit oli "hardcoded".




def welcome_text_to_ascii(): # WELCOME ASCII 
    welcome_text = "Welcome!"
    ascii_art = text_to_ascii(welcome_text, style='standard')
    print(Fore.BLUE + ascii_art)
    print(Style.RESET_ALL)

def tutorial_ascii():
    tutorial_text = "TUTORIAL"
    ascii_art = text_to_ascii(tutorial_text, style='banner')
    print(Fore.GREEN + "-" * 92 + "\n")
    print(Fore.GREEN + ascii_art)
    print(Fore.GREEN + "-" * 92)
    print(Style.RESET_ALL)

def playerinfo_ascii():
    player_text = "PLAYER INFO"
    ascii_art = text_to_ascii(player_text, style='banner')
    print(Fore.GREEN + "-" * 92 + "\n")
    print(Fore.GREEN + ascii_art)
    print(Fore.GREEN + "-" * 92)
    print(Style.RESET_ALL)



def slowly_generate_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()