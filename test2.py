import sys
from bs4 import BeautifulSoup
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import requests
class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


url = 'https://investor.apple.com/investor-relations/sec-filings/'
r = Render(url)
result = r.frame.toHtml()
soup = BeautifulSoup(result, "lxml")

article = soup.findAll("div",{"class":"module-sec_download-list-container grid_col grid_col--3-of-12 grid_col--md-1-of-1"})
i = 1
for element in article:
    new = element.find("li", {"class": "module-sec_download-list-item module-sec_pdf"})
    for a in new.find_all('a', href=True):
        print("inside")
        url = "https:" + a['href']
        response = requests.get(url)
        file = open("/home/dip-24/Desktop/test/" + str(i) + ".pdf", 'wb')
        file.write(response.content)
        file.close()
        print("Completed")
        i +=1
        # i+=1
