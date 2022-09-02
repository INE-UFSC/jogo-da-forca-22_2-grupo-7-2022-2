from word import is_valid_word
from random import randint


class MenuControl():

    def show_options(self) -> None:
        state = input("Bem-vindo ao Jogo da forca! :D\nDigite o número referente a opção desejada:\n1: Modo normal\n2: Sorteio de palavras\n").strip()
        while state not in '12' or state == '12':
            state = input("Opção não disponível.\nDigite um número válido referente a opção desejada:\n1: Modo normal\n2: Sorteio de palavras\n").strip()
        if state == '1':
            return self.direct_word()
        elif state == '2':
            return self.many_words()
        #precisa de um retorno aqui heh

    def direct_word(self) -> str:
        # Input da palavra a ser adivinhada e mudança para letras maiúsculas
        word = input('Qual a palavra a ser adivinhada? ').strip().upper()
        while not is_valid_word(word):
            word = input('Digite apenas letras, espaço e hifen. Qual a palavra a ser adivinhada? ').strip().upper()
        return word

    def many_words(self) -> str:
        word_list = []
        run = True
        word_index = 1
        print('Neste modo, você insere várias palavras e nós selecionamos uma para você.')
        print('Pressione enter sem digitar nada para enviar as palavras desejadas.')
        while run:
            print('Digite a palavra', word_index)
            temporary = input()
            if temporary == '':
                run = False
            elif not is_valid_word(temporary):
                print("Digite apenas letras, espaço e hifen.")
            else:
                word_list.append(temporary)
                word_index += 1

        word = word_list[randint(0, len(word_list) - 1)].strip().upper()
        return word
