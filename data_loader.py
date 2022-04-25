import requests
import yaml

from config import DICTIONARY_GIT_URL, DATA_PATH


class DictionaryLoader:
    def __init__(self, mode: int):
        self.url = DICTIONARY_GIT_URL
        self.mode = mode
        self.dictionary = None

    def load(self):
        if self.mode:
            self.load_to_file_from_url()
        self.load_from_file()

    def load_to_file_from_url(self):
        response = requests.get(self.url)
        dictionary = response.content.decode('cp1251')

        with open('data/all_words_russian_dictionary.txt', 'wb') as ru:
            ru.write(dictionary.encode('utf-8'))

    def load_from_file(self, file_path):
        all_words_dictionary = {}
        with open(file_path, 'r', encoding='utf-8') as dictionary_file:
            all_words_dictionary = yaml.safe_load(dictionary_file)

        return all_words_dictionary