from menu_control import MenuControl
from word import get_letter, remove_accents
from hangman_view import HangmanView

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
            print("Você ganhou!")
            break

        if num_of_errors >= num_max_errors:
            view.draw(used_letters)
            print("Você perdeu!")
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

    if new_game_check == False:
        break
