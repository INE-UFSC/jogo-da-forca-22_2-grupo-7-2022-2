body_template = """
╭───╮ 
│   0   
│   1   
│  324 
│  5 6
│"""

answer_template = """
│ <word>
┴─<spacer>─┤"""


class HangmanView:
    """
        Class para desenho.
    """

    def __init__(self, word: str):
        self.__word = word
        self.__word_letters = set(word)

    def gen_hidden_word(self, used_letter: set[str]):
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

    def __render_answer(self, word) -> None:
        answer = answer_template
        answer = answer.replace("<word>", word)
        answer = answer.replace("<spacer>", "─" * len(word))
        return answer

    def draw(self, used_letter: set[str], num_of_errors: int) -> None:
        print(self.__render_body(num_of_errors), end='')
        current_word = self.gen_hidden_word(used_letter)
        print(self.__render_answer(current_word))
        print()
