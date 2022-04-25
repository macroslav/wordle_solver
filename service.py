import logging

from data_transformer import DataTransformer
from data_loader import DictionaryLoader
from solver import WordleSolver

DEBUG = 0
LOGGING_LEVEL = logging.DEBUG


def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=LOGGING_LEVEL, format='%(asctime)s %(levelname)s: %(message)s')

    loader = DictionaryLoader(mode=DEBUG)
    dictionary = loader.load()
    logger.debug('Dictionary is loaded')

    transformer = DataTransformer(dictionary)
    list_of_words = transformer.load_result()
    logger.debug(f"Five letter words are loaded")

    solver = WordleSolver(list_of_words)
    logger.debug('Solver is created and started')
    solver.start_solver()

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
