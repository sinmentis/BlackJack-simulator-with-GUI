# -*- coding:utf-8 -*-
import sys
from Deck_Card_Player import Card, Deck, Player
from PySide2 import QtCore, QtGui, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)

    quit = QtWidgets.QPushButton("Quit")
    quit.resize(75, 30)
    quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

    QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"),
                           app, QtCore.SLOT("quit()"))

    quit.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
