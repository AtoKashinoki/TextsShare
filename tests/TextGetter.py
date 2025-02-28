

from os import getcwd
from TextsShare.TextGetter import SearchTexts


if __name__ == '__main__':
    print(getcwd())
    texts = SearchTexts(".")
    print(texts)
    ...
