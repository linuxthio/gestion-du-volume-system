

#!/usr/bin/python

# code generer par :djibysoft

from PySide6.QtWidgets import QApplication,QHBoxLayout, QHBoxLayout, QLabel,QPushButton,QTextEdit, QLineEdit, QVBoxLayout, QWidget, QRadioButton, QButtonGroup

import os, sys
import wget
from PySide6.QtCore import QUrl
# from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class Fen(QWidget):
    def __init__(self):
        super(Fen, self).__init__()
        self.setWindowTitle("Gestion du volume")
        self.setGeometry(200, 200, 300, 250)
        self.setFixedSize(300, 80)
        self.vbox=QHBoxLayout()
        self.vbroot=QVBoxLayout()
        self.setLayout(self.vbroot)
        self.auteur=QLabel("DjibySoft 2021")


        self.volup='qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "increase_volume"'
        self.voldown='qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "decrease_volume"'
        self.volmute='qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "mute"'

        self.btnup=QPushButton("+")
        self.btndown=QPushButton("-")
        self.btnmute=QPushButton("x")

        self.btnup.clicked.connect(lambda x: os.system(self.volup))
        self.btndown.clicked.connect(lambda x: os.system(self.voldown))
        self.btnmute.clicked.connect(lambda x: os.system(self.volmute))

        self.vbox.addWidget(self.btnup)
        self.vbox.addWidget(self.btndown)
        self.vbox.addWidget(self.btnmute)

        self.vbroot.addWidget(self.auteur)
        self.vbroot.addLayout(self.vbox)



a = QApplication(sys.argv)
f = Fen()

f.show()
a.exec_()
   
    
