class Game_check:

    def __init__(self, palavra: str, resposta: str) -> None:
        self.resposta = resposta
        self.palavra = palavra
        pass


    def word_check(self):
        if self.resposta == self.palavra:
            return True
        else:
            return False