import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui


class Browser(QMainWindow):

    def __init__(self):
        super(Browser, self).__init__()
        self.setWindowIcon(QtGui.QIcon("C:/Users/hp/Pictures/download2.jpeg"))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # create a navigation bar

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("<-", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("->", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("@", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("^", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_edit = QLineEdit()
        self.url_edit.returnPressed.connect(self.nav_url)
        navbar.addWidget(self.url_edit)
        self.browser.urlChanged.connect(self.update_url)


    def nav_url(self):
        url = self.url_edit.text()
        self.browser.setUrl(QUrl(url))



    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))


    def update_url(self, q):
        self.url_edit.setText(q.toString())



app = QApplication(sys.argv)
app.setApplicationName("Falcon")
window = Browser()
app.exec_()
