class Word:
    def get_word(self):
        # Input da palavra a ser adivinhada e mudança para letras maiúsculas
        self.word = input('Qual a palavra a ser adivinhada? ').strip().upper()
        while not self.word.isalpha():
            self.word = input('Digite apenas letras. Qual a palavra a ser adivinhada? ').strip().upper()
        return self.word

    def get_letter(self):
        # Input do chute da letra e mudança para maiúscula
        self.answer = input('Qual a letra a ser posicionada? ').upper().strip()
        while (len(self.answer) != 1) or not self.answer.isalpha():
            self.answer = input('Digite apenas uma letra. Qual a letra a ser posicionada? ').upper().strip()
        return self.answer
