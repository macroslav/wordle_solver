from data_loader import DictionaryLoader
# from data_transformer import DataTransformer
from config import HEADERS
import requests
from bs4 import BeautifulSoup

from parser import ParserOzhegov

DEBUG = 1


def main():
    # parser = ParserOzhegov()
    # parser.parse_all_words()
    # parser.save_dictionary()
    loader = DictionaryLoader(mode=DEBUG)
    dictionary = loader.load_from_file('data/dictionary.yaml')
    letter_a = dictionary['а']
    letter_a_5 = [word for word in letter_a if len(word) == 5]
    print(letter_a_5)
    print(len(letter_a_5))


# with open('data/site.html', 'w') as site:
#     site.write(response.text)
# with open('data/site.html', 'r') as site:
#     content = site.read()
#
# soup = BeautifulSoup(content, 'lxml')


# if DEBUG:
#     loader = DictionaryLoader(DEBUG)
#     loader.load_to_file_from_url()


if __name__ == '__main__':
    main()
