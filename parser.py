import requests
from bs4 import BeautifulSoup
import yaml

from config import HEADERS, DICTIONARY_OZHEGOV_URL, ALPHABET


class ParserOzhegov:
    def __init__(self):
        self.dictionary = dict()

    def parse_one_letter(self, letter):
        new_page_exists = True
        page = 1
        all_words = []

        while new_page_exists:
            print(f"PAGE #{page}")
            response = requests.get(f"{DICTIONARY_OZHEGOV_URL}page={page}&letter={letter}", headers=HEADERS)
            if response.status_code == 404:
                new_page_exists = False

            soup = BeautifulSoup(response.text, 'lxml')
            columns = soup.findAll("ul", class_='list-unstyled app-word-list')
            for col in columns:
                col_word_list = col.findAll('li')
                for word_tag in col_word_list:
                    word = word_tag.find('a').text
                    all_words.append(word)

            page += 1

        return all_words

    def parse_all_words(self):
        for letter in ALPHABET[:3]:
            print(f"LETTER '{letter.upper()}' IS GOING")
            self.dictionary[letter] = self.parse_one_letter(letter)

    def save_dictionary(self):
        with open('data/dictionary.yaml', 'w', encoding='utf-8') as result_file:
            data = yaml.dump(self.dictionary, result_file, sort_keys=False,
                             default_flow_style=False, allow_unicode=True)
