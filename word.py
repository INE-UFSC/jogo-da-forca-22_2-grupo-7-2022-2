class Word:
    def get_letter(self):
        # Input do chute da letra e mudança para maiúscula
        self.answer = input('Qual a letra a ser posicionada? ').upper().strip()
        while (len(self.answer) != 1) or not self.answer.isalpha():
            self.answer = input('Digite apenas uma letra. Qual a letra a ser posicionada? ').upper().strip()
        return self.answer
