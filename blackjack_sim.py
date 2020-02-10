# -*- coding:utf-8 -*-
import sys
from Deck_Card import Card, Deck, Player
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


def test():
    player = Player("Shun")
    deck = Deck()
    deck.shuffle()
    player.get_card(deck.draw())
    player.show_hand()


if __name__ == "__main__":
    # main()
    test()