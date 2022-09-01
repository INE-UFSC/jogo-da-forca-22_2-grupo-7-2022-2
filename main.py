from menu_control import MenuControl
from word import get_letter
from hangman_view import HangmanView

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
        # Ganhou
        pass
    elif num_of_errors >= num_max_errors:
        # Perdeu
        pass