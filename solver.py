from typing import List
import random
import itertools

from config import ALPHABET

ALL_CONSONANTS = 'бвгджзйклмнпрстфхцчшщ'
ALL_VOWELS = 'аеёиоуыэюя'
ALL_SIGNS = 'ьъ'


class WordleSolver:
    def __init__(self, words: List):
        """
        Class for solving wordle puzzle
        :param words: List[str] - list of five letter length words
        -------
        Methods

        start_solver - run solving 
        """
        self.words = words
        self.possible_words = []
        self.words_with_unique_letters = []
        self.possible_letters = {index: ALPHABET for index in range(5)}
        self.right_letters = []

    def start_solver(self):
        self.find_words_with_unique_letters()
        # initial_word = self.get_random_word()
        initial_words = ['сынок', 'ампер']
        for initial_word in initial_words:
            print(f"Введите слово {initial_word}")
            attempt_result = input(
                "Введите результат попытки в формате: 0 - неверная буква, 1 - буква НЕ на своем месте, 2 - буква на своем месте. Например 00122\n")
            self.update_possible_letters(attempt_result, initial_word)
        for key, value in self.possible_letters.items():
            print(key, value)

    def update_possible_letters(self, attempt_result: str, word: str):
        for index, result in enumerate(list(attempt_result)):
            if result == '0':
                for key, value in self.possible_letters.items():
                    self.possible_letters[key] = value.replace(word[index], '')
            elif result == '1':
                self.right_letters.append(word[index])
                self.possible_letters[index] = self.possible_letters[index].replace(word[index], '')
            else:
                self.right_letters.append(word[index])
                self.possible_letters[index] = word[index]

    def find_words_with_unique_letters(self):
        for word in self.words:
            if len(word) == len(list(set(word))):
                self.words_with_unique_letters.append(word)

    def update_possible_words(self):
        pass

    def get_random_word(self):
        try:
            return random.choice(self.words_with_unique_letters)
        except Exception as ex:
            return random.choice(self.words)

    def get_find_words_with_unique_letters(self):
        return self.words_with_unique_letters

    def generate_possible_sequences(self):
        """ Generate ALL possible sequences of letters ('words') using some rules """
        permutations = itertools.product(self.possible_letters.values())
        words = [perm for perm in permutations]

        legal_words = self.return_legal_words(words)

    def return_legal_words(self, words):
        """ Return words which only satisfy rules
            words: List[str] - list of sequences

            return
                legal_words: List[str]
        """
