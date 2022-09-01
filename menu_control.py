from random import randint


class Menu_Control():

    def show_options(self) -> None:

        state = input("Bem-vindo ao Jogo da forca! :D\nDigite o numero referente a opcao desejada:\n1: Modo normal\n2: Sorteio de palavras\n")
        if state == '1':
            return self.direct_word()
        elif state == '2':
            return self.many_words()
        else:
            print("digite um valor valido.")
        #precisa de um retorno aqui heh

    def direct_word(self) -> str:
        # Input da palavra a ser adivinhada e mudança para letras maiúsculas
        word = input('Qual a palavra a ser adivinhada? ').strip().upper()
        while not word.isalpha():
            word = input('Digite apenas letras. Qual a palavra a ser adivinhada? ').strip().upper()
        return word

    def many_words(self) -> str:
        word_list = []
        run = True
        word_index = 1
        print('Neste modo, voce insere varias palavras e nos selecionamos uma para voce.')
        print('Pressione enter sem digitar nada para enviar as palavras desejadas.')
        while run:
            print('Digite a palavra ', self.word_index)
            temporary = input()
            if temporary == '':
                run = False
            else:
                word_list.append(temporary)
                self.word_index += 1

        word = word_list[randint(0, len(word_list) - 1)].strip().upper()
        return word