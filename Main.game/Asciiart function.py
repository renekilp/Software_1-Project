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