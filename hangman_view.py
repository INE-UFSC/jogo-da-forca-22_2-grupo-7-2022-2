body_template = """
╭───╮ 
│   0   
│   1   
│  324 
│  5 6
│"""

current_answer_template = """
│ <word>
┴─<spacer>─┤"""


class HangmanView:
    """
        Class para desenho.
    """

    def __init__(self, word: str):
        self.__word = word
        self.__word_letters = set(word)

    def gen_hidden_word(self, used_letter):
        remaining_letters = self.__word_letters.difference(used_letter)

        word_with_letters_hidden = self.__word
        for letter in remaining_letters:
            word_with_letters_hidden = word_with_letters_hidden.replace(letter, '_')
        return word_with_letters_hidden

    def __render_body(self, num_of_errors: int) -> str:
        body = body_template
        error_characters = ['│', 'O', '|', '/', '\\', '/', '\\']
        num_of_errors_limited = min(num_of_errors, len(error_characters))

        for index in range(num_of_errors_limited):
            body = body.replace(str(index), error_characters[index])

        for index in range(num_of_errors_limited, len(error_characters)):
            body = body.replace(str(index), ' ')
        return body

    def __render_current_answer(self, word) -> None:
        current_answer = current_answer_template
        current_answer = current_answer.replace("<word>", word)
        current_answer = current_answer.replace("<spacer>", "─" * len(word))
        return current_answer

    def __render_wrong_answers(self, used_letters) -> None:
        wrong_letters_list = list(used_letters.difference(self.__word_letters))
        wrong_letters_list.sort()
        wrong_answers = ', '.join(wrong_letters_list)

        return wrong_answers

    def draw(self, used_letters) -> None:
        num_of_errors = len(used_letters.difference(self.__word_letters))

        body = self.__render_body(num_of_errors)

        current_answer = self.gen_hidden_word(used_letters)
        current_answer_render = self.__render_current_answer(current_answer)

        print(body, end='')
        print(current_answer_render)
        print()

        if(num_of_errors > 0):
            wrong_answer = self.__render_wrong_answers(used_letters)
            print(" Letras erradas:", wrong_answer)
            print()