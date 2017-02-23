#!/usr/bin/env python
'''
Extra point de la assignatura de sistemes i comunicacions web
'''
import urllib2
from bs4 import BeautifulSoup
class Web(object):
    def get_web(self, page):
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html
    def search_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", 'dotd-title')
        print elements.text.strip()

    def main(self):
        html=self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        self.search_text(html)
if __name__ == '__main__':
    web = Web()
    web.main()
