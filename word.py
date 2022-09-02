from unicodedata import normalize
import re


def remove_accents(word):
    return normalize('NFKD', word).encode('ASCII', 'ignore').decode('utf8')

def is_valid_word(word):
    return re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ\- ]+$', word)


def get_letter():
    # Input do chute da letra e mudança para maiúscula
    answer = input('Qual a letra a ser posicionada? ').upper().strip()
    while (len(answer) != 1) or not is_valid_word(answer):
        answer = input('Digite apenas uma letra. Qual a letra a ser posicionada? ').upper().strip()
    return remove_accents(answer)
