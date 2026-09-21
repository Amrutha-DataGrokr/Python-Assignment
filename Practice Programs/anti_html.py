"""
5. Write a program anti_html.py that takes a URL as an argument, downloads the HTML from
the web, and prints it after stripping HTML tags."""

import sys
from urllib.request import urlopen
from html.parser import HTMLParser


class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return "".join(self.text)


url = sys.argv[1]

html = urlopen(url).read().decode("utf-8")

parser = HTMLStripper()
parser.feed(html)

print(parser.get_text())