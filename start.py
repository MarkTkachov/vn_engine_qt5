

import subprocess as sp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    startMenu = QtWidgets.QDialog()
    ui = Ui_startMenu()
    ui.setupUi(startMenu)
    startMenu.show()
    sys.exit(app.exec_())
    return 0


def startPlayer():
    player = sp.Popen(["python3", "scriptplayer.py", "-s"], shell=False)
    sys.exit()

    
def loadSlot(index):
    index = str(index)
    player = sp.Popen(["python3", "scriptplayer.py", "-l", index], shell=False)
    sys.exit()


class Ui_startMenu(object):
    def setupUi(self, startMenu):
        #Start of auto-generated code

        startMenu.setObjectName("startMenu")
        startMenu.resize(640, 480)
        startMenu.setMinimumSize(QtCore.QSize(640, 480))
        startMenu.setMaximumSize(QtCore.QSize(640, 480))
        startMenu.setBaseSize(QtCore.QSize(640, 480))
        startMenu.setToolTipDuration(-6)
        startMenu.setAutoFillBackground(False)
        startMenu.setStyleSheet("#startMenu {\n"
"border-image: url(start_background.png)\n"
"}")
        startMenu.setModal(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(startMenu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 60, 151, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_2.addWidget(self.exitButton, 4, 0, 1, 1)
        self.loadButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadButton1.setObjectName("loadButton1")
        self.gridLayout_2.addWidget(self.loadButton1, 1, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 0, 1, 1)
        self.loadButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadButton2.setObjectName("loadButton2")
        self.gridLayout_2.addWidget(self.loadButton2, 2, 0, 1, 1)
        self.loadButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadButton3.setObjectName("loadButton3")
        self.gridLayout_2.addWidget(self.loadButton3, 3, 0, 1, 1)
        self.logoLabel = QtWidgets.QLabel(startMenu)
        self.logoLabel.setGeometry(QtCore.QRect(9, 9, 441, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setStyleSheet("#logoLable{\n"
"border-image: url(logo.png)\n"
"}")
        self.logoLabel.setText("")
        self.logoLabel.setTextFormat(QtCore.Qt.AutoText)
        self.logoLabel.setPixmap(QtGui.QPixmap("logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setWordWrap(False)
        self.logoLabel.setObjectName("logoLabel")

        self.retranslateUi(startMenu)
        self.exitButton.clicked.connect(startMenu.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(startMenu)
    #End of auto-generated code

        self.connectButtons(startMenu)

        
    def connectButtons(self, startMenu):
        self.startButton.clicked.connect(startPlayer)
        self.loadButton1.clicked.connect(lambda: loadSlot(1))
        self.loadButton2.clicked.connect(lambda: loadSlot(2))
        self.loadButton3.clicked.connect(lambda: loadSlot(3))

    def retranslateUi(self, startMenu):
        _translate = QtCore.QCoreApplication.translate
        startMenu.setWindowTitle(_translate("startMenu", "Start Menu"))
        self.startButton.setText(_translate("startMenu", "Start"))
        self.loadButton1.setText(_translate("startMenu", "Load save 1"))
        self.loadButton2.setText(_translate("startMenu", "Load save 2"))
        self.loadButton3.setText(_translate("startMenu", "Load save 3"))
        self.exitButton.setText(_translate("startMenu", "Exit"))


if __name__ == "__main__":
    main()
