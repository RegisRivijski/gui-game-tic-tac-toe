# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TicTacToe_GUI(object):
    def setupUi(self, TicTacToe_GUI):
        TicTacToe_GUI.setObjectName("TicTacToe_GUI")
        TicTacToe_GUI.resize(301, 401)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TicTacToe_GUI.sizePolicy().hasHeightForWidth())
        TicTacToe_GUI.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TicTacToe_GUI.setWindowIcon(icon)
        TicTacToe_GUI.setStyleSheet("background-color: rgb(131, 131, 131)")
        self.centralwidget = QtWidgets.QWidget(TicTacToe_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Cell_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_1.setGeometry(QtCore.QRect(0, 0, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_1.setFont(font)
        self.btn_Cell_1.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_1.setObjectName("btn_Cell_1")
        self.btn_Cell_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_2.setGeometry(QtCore.QRect(100, 0, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_2.setFont(font)
        self.btn_Cell_2.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_2.setObjectName("btn_Cell_2")
        self.btn_Cell_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_3.setGeometry(QtCore.QRect(200, 0, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_3.setFont(font)
        self.btn_Cell_3.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_3.setObjectName("btn_Cell_3")
        self.btn_Cell_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_4.setGeometry(QtCore.QRect(0, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_4.setFont(font)
        self.btn_Cell_4.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_4.setObjectName("btn_Cell_4")
        self.btn_Cell_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_5.setGeometry(QtCore.QRect(100, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_5.setFont(font)
        self.btn_Cell_5.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_5.setObjectName("btn_Cell_5")
        self.btn_Cell_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_6.setGeometry(QtCore.QRect(200, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_6.setFont(font)
        self.btn_Cell_6.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_6.setObjectName("btn_Cell_6")
        self.btn_Cell_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_7.setGeometry(QtCore.QRect(0, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_7.setFont(font)
        self.btn_Cell_7.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_7.setObjectName("btn_Cell_7")
        self.btn_Cell_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_8.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_8.setFont(font)
        self.btn_Cell_8.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_8.setObjectName("btn_Cell_8")
        self.btn_Cell_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cell_9.setGeometry(QtCore.QRect(200, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cell_9.setFont(font)
        self.btn_Cell_9.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(99, 99, 98);\n"
"    color: rgb(230, 196, 0)\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(255, 85, 0)\n"
"}")
        self.btn_Cell_9.setObjectName("btn_Cell_9")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 300, 301, 23))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 320, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(24)
        self.display.setFont(font)
        self.display.setStyleSheet("    background-color: rgb(56, 56, 56);\n"
"    color: rgb(255, 170, 0)")
        self.display.setObjectName("display")
        TicTacToe_GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TicTacToe_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        TicTacToe_GUI.setMenuBar(self.menubar)
        self.actionNew_Game = QtWidgets.QAction(TicTacToe_GUI)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionSettings = QtWidgets.QAction(TicTacToe_GUI)
        self.actionSettings.setObjectName("actionSettings")
        self.actionPlayer_vs_Player = QtWidgets.QAction(TicTacToe_GUI)
        self.actionPlayer_vs_Player.setObjectName("actionPlayer_vs_Player")
        self.actionPlayer_vs_PC = QtWidgets.QAction(TicTacToe_GUI)
        self.actionPlayer_vs_PC.setObjectName("actionPlayer_vs_PC")
        self.menuGame.addAction(self.actionNew_Game)
        self.menubar.addAction(self.menuGame.menuAction())

        self.retranslateUi(TicTacToe_GUI)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe_GUI)

    def retranslateUi(self, TicTacToe_GUI):
        _translate = QtCore.QCoreApplication.translate
        TicTacToe_GUI.setWindowTitle(_translate("TicTacToe_GUI", "Крестики нолики"))
        self.btn_Cell_1.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_2.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_3.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_4.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_5.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_6.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_7.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_8.setText(_translate("TicTacToe_GUI", ""))
        self.btn_Cell_9.setText(_translate("TicTacToe_GUI", ""))
        self.display.setText(_translate("TicTacToe_GUI", "TicTacToe Game."))
        self.menuGame.setTitle(_translate("TicTacToe_GUI", "Game"))
        self.actionNew_Game.setText(_translate("TicTacToe_GUI", "New Game"))
        self.actionNew_Game.setShortcut(_translate("TicTacToe_GUI", "Ctrl+N"))
        self.actionSettings.setText(_translate("TicTacToe_GUI", "Settings"))
        self.actionPlayer_vs_Player.setText(_translate("TicTacToe_GUI", "Player vs Player"))
        self.actionPlayer_vs_PC.setText(_translate("TicTacToe_GUI", "Player vs PC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TicTacToe_GUI = QtWidgets.QMainWindow()
    ui = Ui_TicTacToe_GUI()
    ui.setupUi(TicTacToe_GUI)
    TicTacToe_GUI.show()
    sys.exit(app.exec_())
