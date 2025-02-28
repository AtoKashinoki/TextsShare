"""
    Webpage tools

This file contains the Webpage-relate tools used for create webpages.
"""


""" imports """


from flask import Flask
from CodingTools.Wrapper import initialize


""" webpage process  """


@initialize(
    Flask(__name__,)
)
class Webpage:
    """ Management web page class """

    """ Initializer """
    def __init__(self, app: Flask):
        """ Initialize web page app """
        self.__app = app
        self.__pages = {}
        return

    """ flask """
    __app: Flask
    @property
    def app(self): return self.__app

    """ webpage """
    __pages: dict[str, str]
    @property
    def pages(self): return self.__pages

    def add_page(self, page_route: str, webpage: str) -> None:
        """ Add web page in self """
        self.__pages[page_route] = webpage
        return

    def del_page(self, page_route: str) -> None:
        """ Delete web page in self """
        del self.__pages[page_route]
        return

    """ run """
    def __gen_page(self, _page_route: str, _webpage: str) -> None:
        """ Generate webpage """
        @self.__app.route(f'/{_page_route}')
        def page(): return _webpage
        return

    def __gen_pages(self) -> None:
        """ Generate webpages """
        for page_route, webpage in self.__pages.items():
            self.__gen_page(page_route, webpage)
            continue
        return

    def run(self, host, port) -> None:
        """ Run web page """
        self.__gen_pages()
        self.__app.run(host=host, port=port)
        return

    ...


Webpage: Webpage
