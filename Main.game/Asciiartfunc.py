from art import *

def text_to_ascii(text, style='standard'):
    if style == 'standard':
        return text2art(text)
    elif style == 'block':
        return text2art(text, font='block')
    elif style == 'banner':
        return text2art(text, font='banner3')
    else:
        return "Invalid style specified"


text = "Testi"
ascii_art = text_to_ascii(text, style='standard')
print(ascii_art)



def welcome_text__to_ascii(): # WELCOME ASCII 
    welcome_text = "Welcome!"
    ascii_art = text_to_ascii(welcome_text, style='standard')
    print(ascii_art)
