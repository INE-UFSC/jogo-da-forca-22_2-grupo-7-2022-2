class Word:
    def get_word(self):
        # Input da palavra a ser adivinhada e mudança para letras maiúsculas
        self.palavra = input('Qual a palavra a ser adivinhada? ').strip().upper()
        while not self.palavra.isalpha():
            self.palavra = input('Digite apenas letras. Qual a palavra a ser adivinhada? ').strip().upper()
        return self.palavra

    def get_letter(self):
        # Input do chute da letra e mudança para maiúscula
        self.resposta = input('Qual a letra a ser posicionada? ').upper().strip()
        while (len(self.resposta) != 1) or not self.resposta.isalpha():
            self.resposta = input('Digite apenas uma letra. Qual a letra a ser posicionada? ').upper().strip()
        return self.resposta
