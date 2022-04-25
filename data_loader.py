import requests
import yaml

from config import DATA_PATH, DICTIONARY_OZHEGOV_YAML_PATH
from parser import ParserOzhegov


class DictionaryLoader:
    def __init__(self, mode: int):
        self.mode = mode
        self.dictionary = {}
        self.parser = None
        self.dictionary_path = DICTIONARY_OZHEGOV_YAML_PATH

    def load(self):
        if self.mode:
            self.load_to_file_from_url()
        self.load_from_file()
        return self.dictionary

    def load_to_file_from_url(self):
        self.parser = ParserOzhegov(self.dictionary_path)
        self.parser.parse_all_words()
        self.parser.save_dictionary()

    def load_from_file(self):
        with open(self.dictionary_path, 'r', encoding='utf-8') as dictionary_file:
            self.dictionary = yaml.safe_load(dictionary_file)
