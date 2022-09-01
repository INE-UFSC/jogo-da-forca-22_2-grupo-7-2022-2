def get_letter():
    # Input do chute da letra e mudança para maiúscula
    answer = input('Qual a letra a ser posicionada? ').upper().strip()
    while (len(answer) != 1) or not answer.isalpha():
        answer = input('Digite apenas uma letra. Qual a letra a ser posicionada? ').upper().strip()
    return answer
