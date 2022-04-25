from typing import Dict
import logging

from config import WORD_LEN


class DataTransformer:
    def __init__(self, dictionary: Dict):
        self.dictionary = dictionary
        self.five_letters_words = []

    def _get_five_letter_words(self):
        for letter, words in self.dictionary.items():
            for word in words:
                if len(word) == WORD_LEN:
                    self.five_letters_words.append(word)

    def _return_five_letters_words(self):
        return self.five_letters_words

    def load_result(self):
        self._get_five_letter_words()
        result_list = self._return_five_letters_words()
        return result_list
