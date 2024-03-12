import time
from colorama import Fore, Style

#       funktion tarkoitus luoda feikki latauspalkki
#       parametria muuttamalla voidaan itse määrittää tulostuksen nopeus
def fakeloading(delay=0.025):
    print(Fore.GREEN)
    loadingbar = "█████████████████████████████████████████████████████████████████████████████████\n"
    print("                                 LOADING GAME...")
    for char in loadingbar:
        print(char, end='', flush=True)
        time.sleep(delay)
        #       tulostaa symbolit yksi kerrallaan määritetyllä delay arvolla
    print(Style.RESET_ALL)
    print("\n" * 30)
    #   en oikein löytänyt toimivaa tapaa tyhjentää pycharm terminal feediä
    #   jos joku keksii paremman tavan niin saa muuttaa :)



#       funktion tarkoitus tulostaa hitaasti pelin title screen
def slowly_generate_title(delay=0.25):
        print(Fore.CYAN)
        print("███████╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗     ██████╗ ██╗   ██╗██╗███████╗")
        time.sleep(delay)
        print(r"██╔════╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔═══██╗██║   ██║██║╚══███╔╝")
        time.sleep(delay)
        print(r"█████╗  ██║     ██║██║  ███╗███████║   ██║       ██║   ██║██║   ██║██║  ███╔╝")
        time.sleep(delay)
        print(r"██╔══╝  ██║     ██║██║   ██║██╔══██║   ██║       ██║▄▄ ██║██║   ██║██║ ███╔╝")
        time.sleep(delay)
        print(r"██║     ███████╗██║╚██████╔╝██║  ██║   ██║       ╚██████╔╝╚██████╔╝██║███████╗")
        time.sleep(delay)
        print("╚═╝     ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝")
        time.sleep(delay)
        print(r"                .                                           __")
        time.sleep(delay)
        print(r"       _(  )_( )_               ,                           \  \     _ _")
        time.sleep(delay)
        print(r"      (_   _    _)      .                    .               \**\ ___\/ \ ")
        time.sleep(delay)
        print(r"        (_) (__)                    _(  )_( )_              X*#####*+^^\_\ ")
        time.sleep(delay)
        print(r"                                 . (_   _    _)               o/\  \ ")
        time.sleep(delay)
        print(r"                                     (_) (__)                    \__\ ")
        time.sleep(delay)
        print(r"   .                                            .                     ,")
        time.sleep(delay)
        print(r"          .     *            .                    .             .          ,")
        time.sleep(delay)
        print(r"                                 .                         .")
        time.sleep(delay)
        print(r"____^/\___^--⏚___/\____O_x_____________/\/\---/\_____⏚_____---______________")
        time.sleep(delay)
        print(r"              .-. _______|^         ⏚       ⏚⏚         --  __")
        time.sleep(delay)
        print(r"              |=|/     /  \         ⏚⏚   ^^ ^  '\ ^          ^       ---")
        time.sleep(delay)
        print(r"___--  ^      | |_____|_""_|")
        time.sleep(delay)
        print(r"              |_|_[X]_|____|          --   ⏚        -    ⏚        --  -  ")
        time.sleep(delay)
        print(r"   /\^   ^  ^    ^  ⏚    -         ---  __       ^          ")
        print(Style.RESET_ALL)


