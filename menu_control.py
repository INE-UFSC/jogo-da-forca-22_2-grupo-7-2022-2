from cProfile import run


class Menu_Control():
    def __init__(self) -> None:
        self.word = None
        self.word_list = []
        self.temporary = None
        self.word_index = 1
        self.run = True
        self.state = None

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
        self.word = input('Digite a palavra a ser procurada:\n')
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

    def get_word_list(self):
        return self.many_words
