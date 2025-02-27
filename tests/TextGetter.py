

from os import getcwd
from TextsShare.TextGetter import TodayTexts


if __name__ == '__main__':
    print(getcwd())
    texts = TodayTexts(".")
    print(texts)
    ...
