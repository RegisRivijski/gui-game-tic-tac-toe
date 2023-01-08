import sys
from GUI_ import Ui_TicTacToe_GUI
from PyQt5 import QtCore, QtGui, QtWidgets


def setSymbolCell(cell):

    def winnerCheck():
        if ui.field[0] == ui.field[1] == ui.field[2] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[0]))
            ui.progressBar.setValue(100)
        elif ui.field[3] == ui.field[4] == ui.field[5] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[3]))
            ui.progressBar.setValue(100)
        elif ui.field[6] == ui.field[7] == ui.field[8] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[6]))
            ui.progressBar.setValue(100)
        elif ui.field[0] == ui.field[3] == ui.field[6] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[3]))
            ui.progressBar.setValue(100)
        elif ui.field[1] == ui.field[4] == ui.field[7] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[1]))
            ui.progressBar.setValue(100)
        elif ui.field[2] == ui.field[5] == ui.field[8] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[2]))
            ui.progressBar.setValue(100)
        elif ui.field[0] == ui.field[4] == ui.field[8] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[5]))
            ui.progressBar.setValue(100)
        elif ui.field[2] == ui.field[4] == ui.field[6] != ' ':
            ui.display.setText('Player {0} win.'.format(ui.field[5]))
            ui.progressBar.setValue(100)


    if  ui.field[cell] == ' ':
        if ui.whoseMove == 0:
            ui.field[cell] =  ui.players[ui.whoseMove]
            ui.whoseMove = 1
        else:
            ui.field[cell] =  ui.players[ui.whoseMove]
            ui.whoseMove = 0
        ui.display.setText('Player {} moves.'.format(ui.players[ui.whoseMove]))
        ui.step += 11

    if cell == 0:
         ui.btn_Cell_1.setText( ui.field[cell])
    elif cell == 1:
         ui.btn_Cell_2.setText( ui.field[cell])
    elif cell == 2:
         ui.btn_Cell_3.setText( ui.field[cell])
    elif cell == 3:
        ui.btn_Cell_4.setText( ui.field[cell])
    elif cell == 4:
         ui.btn_Cell_5.setText( ui.field[cell])
    elif cell == 5:
         ui.btn_Cell_6.setText( ui.field[cell])
    elif cell == 6:
         ui.btn_Cell_7.setText( ui.field[cell])
    elif cell == 7:
         ui.btn_Cell_8.setText( ui.field[cell])
    elif cell == 8:
         ui.btn_Cell_9.setText( ui.field[cell])

    ui.progressBar.setValue(ui.step)
    winnerCheck()

def newGame():
    ui.field = [' ' for _ in range(9)]
    ui.btn_Cell_1.setText('')
    ui.btn_Cell_2.setText('')
    ui.btn_Cell_3.setText('')
    ui.btn_Cell_4.setText('')
    ui.btn_Cell_5.setText('')
    ui.btn_Cell_6.setText('')
    ui.btn_Cell_7.setText('')
    ui.btn_Cell_8.setText('')
    ui.btn_Cell_9.setText('')
    ui.whoseMove = 0
    ui.step = 0
    ui.progressBar.setValue(0)
    ui.display.setText('TicTacToe Game.')

if __name__ == "__main__":
    # Create app
    app = QtWidgets.QApplication(sys.argv)

    # Init
    TicTacToe_GUI = QtWidgets.QMainWindow()
    ui = Ui_TicTacToe_GUI()
    ui.setupUi(TicTacToe_GUI)
    TicTacToe_GUI.show()

    ui.field = [' ' for _ in range(9)]
    ui.players = ['X', 'O']
    ui.whoseMove = 0
    ui.step = 0

    ui.btn_Cell_1.pressed.connect(lambda: setSymbolCell(0))
    ui.btn_Cell_2.pressed.connect(lambda: setSymbolCell(1))
    ui.btn_Cell_3.pressed.connect(lambda: setSymbolCell(2))
    ui.btn_Cell_4.pressed.connect(lambda: setSymbolCell(3))
    ui.btn_Cell_5.pressed.connect(lambda: setSymbolCell(4))
    ui.btn_Cell_6.pressed.connect(lambda: setSymbolCell(5))
    ui.btn_Cell_7.pressed.connect(lambda: setSymbolCell(6))
    ui.btn_Cell_8.pressed.connect(lambda: setSymbolCell(7))
    ui.btn_Cell_9.pressed.connect(lambda: setSymbolCell(8))

    ui.actionNew_Game.triggered.connect(lambda: newGame())
    ui.progressBar.setValue(0)

    # Mainloop
    sys.exit(app.exec_())
