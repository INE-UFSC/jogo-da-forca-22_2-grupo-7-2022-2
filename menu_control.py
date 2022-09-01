from cProfile import run
from random import randint


class Menu_Control():
    def __init__(self) -> None:
        self.word_list = []
        self.word_index = 1
        self.run = True

    def show_options(self) -> None:

        self.state = input("Bem-vindo ao Jogo da forca! :D\nDigite o numero referente a opcao desejada:\n1: Modo normal\n2: Sorteio de palavras\n")
        if self.state == '1':
            self.direct_word()
        elif self.state == '2':
            self.many_words()
        else:
            print("digite um valor valido.")
        #precisa de um retorno aqui heh

    def direct_word(self) -> str:
        # Input da palavra a ser adivinhada e mudança para letras maiúsculas
        self.word = input('Qual a palavra a ser adivinhada? ').strip().upper()
        while not self.word.isalpha():
            self.word = input('Digite apenas letras. Qual a palavra a ser adivinhada? ').strip().upper()
        return self.word

    def many_words(self) -> list:
        print('Pressione enter sem digitar nada para enviar as palavras desejadas.')
        while self.run:
            print('Digite a palavra ', self.word_index)
            self.temporary = input()
            if self.temporary == '':
                self.run = False
            else:
                self.word_list.append(self.temporary)
                self.word_index += 1

        self.word = self.word_list[randint(0, len(self.word_list) - 1)].strip().upper()
        return self.word
