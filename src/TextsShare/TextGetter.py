"""
    Text getter process
"""


""" import """


from os import path
from glob import glob
from datetime import datetime


""" process """


def convert_day(_datetime: datetime) -> str:
    return _datetime.strftime("%Y-%m-%d")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


class SearchTexts:

    def __init__(
            self,
            directory: str,
            target: str = "/*",
            target_day: str = today()
    ):

        self.__files = {
            file: open(file).read()
            for file, day in {
                file: convert_day(datetime.fromtimestamp(path.getmtime(file)))
                for file in glob(directory+target)
            }.items()
            if day == target_day
        }

        return

    def __iter__(self):
        return self.__files.keys()

    def keys(self):
        return self.__files.keys()

    def values(self):
        return self.__files.values()

    def items(self):
        return self.__files.items()

    def __repr__(self):
        return str(self.__files)

    ...
