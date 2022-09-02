from menu_control import MenuControl
from word import get_letter, remove_accents
from hangman_view import HangmanView
from os import system, name as os_name

def clear_screen():
    # windows
    if os_name == 'nt':
        system('cls')
    # linux, mac, etc
    elif os_name == 'posix':
        system('clear')

youwin = """ 
__   _____  _   _  __      _____ _  _   _ 
 \ \ / / _ \| | | | \ \    / /_ _| \| | | |
  \ V / (_) | |_| |  \ \/\/ / | || .` | |_|
   |_| \___/ \___/    \_/\_/ |___|_|\_| (_)"""

trophy = """
              '._==_==_=_.'     
              .-\\:      /-.    
             | (|:.     |) |    
              '-|:.     |-'     
                \\::.    /      
                 '::. .'        
                   ) (          
                 _.' '._        
                '-------'       """


gameover = """
   ___   _   __  __ ___ _____   _____ ___ 
  / __| /_\ |  \/  | __/ _ \ \ / / __| _ \\
 | (_ |/ _ \| |\/| | _| (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___\___/ \_/ |___|_|_\\"""

hangman = """
            ___ ___ ___ ___ ___  
            |___|___|___|___|___| 
            | |       | |          
            | |       | |          
            | |       | |          
            |_|       |_|          
            | |      /   \         
            | |     | X X |        
            | |      \___/         
            |_|      _____        
            | |     / / \ \       
            | |    / /| |\ \      
            | |   /_/ | | \_\     
            |_|      _|_|_        
            | |     / / \ \       
            | |    / /   \ \      
            | |   /_/     \_\     
            |_|                   
            | |                   
            | |                   
            | |                   
            |_|                   """

while True:
    new_game_check = False

    menu = MenuControl()
    word = menu.show_options()
    word_check = set(remove_accents(word))
    view = HangmanView(word)
    used_letters = set()

    if ' ' in word:
        used_letters.add(' ')
    if '-' in word:
        used_letters.add('-')

    num_max_errors = 6

    while True:
        view.draw(used_letters)
        num_of_errors = len(used_letters.difference(word_check))

        letter = get_letter()
        used_letters.add(letter)
        print(len(used_letters))

        if used_letters >= word_check:
            view.draw(used_letters)
            print(trophy)
            print(youwin)
            print()
            break

        if num_of_errors >= num_max_errors:
            view.draw(used_letters)

            print(hangman)
            print(gameover)
            print()
            break

    while True:

        new_game = input('Você deseja jogar novamente? Sim ou Não? ')
        print("")

        if remove_accents(new_game).lower() == "sim":
            new_game_check = True
            break
        elif remove_accents(new_game).lower() == "nao":
            new_game_check = False
            break
        else:
            print('Escreva "Sim" ou "Não".')
    clear_screen()

    if new_game_check == False:
        break
