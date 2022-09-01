from hashlib import new
from menu_control import MenuControl
from word import get_letter
from hangman_view import HangmanView

while True:
    new_game_check = False

    menu = MenuControl()
    word = menu.show_options()
    word_check = set(word)
    view = HangmanView(word)

    used_letters = set()
    num_of_errors = len(used_letters)
    num_max_errors = 7

    while True:
        view.draw(used_letters)

        letter = get_letter()
        used_letters.add(letter)

        if used_letters >= word_check:
            print("Você perdeu!")
            view.draw(used_letters)
            break

        elif num_of_errors >= num_max_errors:
            print("Você perdeu!")
            view.draw(used_letters)
            break

    while True:
        
        new_game = input('Você deseja jogar novamente? Sim ou Não? ')
        print("")

        if new_game == "Sim":
            new_game_check = True
            break
        elif new_game == "Não":
            new_game_check = False
            break
        else:
            print('Escreva "Sim" ou "Não".')
    
    if new_game_check == False:
        break