from bs4 import BeautifulSoup, element
from urllib3 import PoolManager
import html2text
import re


class Downloader:

    def __init__(self):
        self.pool = PoolManager()
        self.htot = html2text.HTML2Text()
        self.htot.body_width = 0
        self.htot.ignore_links = True

    def _get_page(self, url):
        return self.pool.request('GET', url).data.decode()

    def _tag_visible(self, elem):
        if elem.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'article', 'img', 'aside', 'iframe', 'footer']:
            return 0
        if isinstance(elem, element.Comment):
            return 0
        if elem == "\n" or elem.strip() == "":
            return 0
        return 1

    def _apply_formatting(self, elem):
        # formatting
        elem = re.sub(" +", " ", elem)
        return elem

    def _tag_to_text(self, tag):
        return self.htot.handle(str(tag))

    def _text_to_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = list(filter(self._tag_visible, texts))
        return visible_texts


if __name__ == '__main__':

    url = 'https://www.bbc.co.uk/food/recipes/easy_chocolate_cake_31070'

    dd = Downloader()
    page = dd._get_page(url)
    proc_html = dd._text_to_html(page)
    data = '\n'.join(proc_html)
    text = dd.htot.handle(page)
    tt = text.split('\n')
    ll = []
    for t in tt:
        t = t.split()
        if 0 < len(t) < 30:
            print(' '.join(t))
