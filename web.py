#!/usr/bin/env python
'''
Extra point de la assignatura de sistemes i comunicacions web
'''
import urllib2

class Web(object):
    def get_web(self, page):
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html
    def main(self):
        html=self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        print html
if __name__ == '__main__':
    web = Web()
    web.main()
