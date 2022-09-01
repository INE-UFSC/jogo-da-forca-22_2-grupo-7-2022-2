import re


class Game_check():

    def __init__(self, palavra: set, resposta: set) -> None:
        self.resposta = resposta
        self.palavra = palavra
        pass


    def check(self):
        if self.resposta == self.palavra:
            return True
        else:
            return False
        