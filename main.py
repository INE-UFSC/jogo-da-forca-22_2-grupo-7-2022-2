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
    num_max_errors = 7

    while True:
        view.draw(used_letters)
        num_of_errors = len(used_letters.difference(word_check))

        letter = get_letter()
        used_letters.add(letter)
        print(len(used_letters))

        if used_letters >= word_check:
            view.draw(used_letters)
            print("Você ganhou!")
            break

        if num_of_errors >= num_max_errors:
            view.draw(used_letters)
            print("Você perdeu!")
            break

        print(num_of_errors)

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