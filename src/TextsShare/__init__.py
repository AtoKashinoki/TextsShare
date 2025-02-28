"""
    Text share process
"""


""" imports """


from .Webpage import Webpage
from .TextGetter import SearchTexts
import qrcode


""" process """


def run(
        route: str = ".",
        target: str = "/*",
        host: str = "127.0.0.1",
):
    texts = SearchTexts(route, target)

    page = ""
    for file, text in texts.items():
        page += "-"*4 + f"{file}"+"-"*(76-len(file))+"<br>"
        page += text.replace("\n", "<br>")+"<br>"+"-"*80+"<br>"
        continue

    Webpage.add_page("/", page)

    qrcode.make(f"http://{host}").show()
    Webpage.run(host, 5000)
    return
