from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys, getopt
import subprocess as sp
import re
import playsound
from pygame import mixer
from functools import partial




def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    opts, args = getopt.getopt(sys.argv[1:], "l:p:s", [])
    for option, opt_arg in opts:
        if option == "-l":
            ui.redirect("loadslots/loadslot" + opt_arg + ".script")
        elif option == "-p":
            ui.openScript(opt_arg)
            ui.readVNScript(MainWindow)
        else:
            ui.readVNScript(MainWindow)
    ui.updateConstElements(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    

def loadSlot(index):
    index = str(index)
    player = sp.Popen(["python3", "scriptplayer.py", "-l", index], shell=False)
    sys.exit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 720))
        MainWindow.setStyleSheet("#MainWindow{\n"
"border-image: url(start_background.png)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_window = QtWidgets.QLabel(self.centralwidget)
        self.txt_window.setGeometry(QtCore.QRect(20, 410, 981, 281))
        self.txt_window.setText("")
        self.txt_window.setPixmap(QtGui.QPixmap("text_window.png"))
        self.txt_window.setScaledContents(True)
        self.txt_window.setObjectName("txt_window")
        self.txt_content = QtWidgets.QLabel(self.centralwidget)
        self.txt_content.setGeometry(QtCore.QRect(60, 440, 900, 220))
        self.txt_content.setMaximumSize(QtCore.QSize(900, 220))
        self.txt_content.setBaseSize(QtCore.QSize(900, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(True)
        self.txt_content.setFont(font)
        self.txt_content.setStyleSheet("#txt_content{\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"")
        self.txt_content.setTextFormat(QtCore.Qt.RichText)
        self.txt_content.setScaledContents(False)
        self.txt_content.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txt_content.setWordWrap(True)
        self.txt_content.setObjectName("txt_content")
        self.name_window = QtWidgets.QLabel(self.centralwidget)
        self.name_window.setEnabled(True)
        self.name_window.setGeometry(QtCore.QRect(29, 355, 300, 71))
        self.name_window.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_window.setLineWidth(0)
        self.name_window.setText("")
        self.name_window.setPixmap(QtGui.QPixmap("name_window.png"))
        self.name_window.setScaledContents(True)
        self.name_window.setObjectName("name_window")
        self.name_txt = QtWidgets.QLabel(self.centralwidget)
        self.name_txt.setGeometry(QtCore.QRect(40, 380, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.name_txt.setFont(font)
        self.name_txt.setStyleSheet("#name_txt{\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.name_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.name_txt.setObjectName("name_txt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        self.menuLoad = QtWidgets.QMenu(self.menubar)
        self.menuLoad.setObjectName("menuLoad")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionBack_to_menu = QtWidgets.QAction(MainWindow)
        self.actionBack_to_menu.setObjectName("actionBack_to_menu")
        self.actionSave_slot_1 = QtWidgets.QAction(MainWindow)
        self.actionSave_slot_1.setObjectName("actionSave_slot_1")
        self.actionLoad_slot_1 = QtWidgets.QAction(MainWindow)
        self.actionLoad_slot_1.setObjectName("actionLoad_slot_1")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSave_slot_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_slot_2.setObjectName("actionSave_slot_2")
        self.actionSave_slot_3 = QtWidgets.QAction(MainWindow)
        self.actionSave_slot_3.setObjectName("actionSave_slot_3")
        self.actionLoad_slot_2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_slot_2.setObjectName("actionLoad_slot_2")
        self.actionLoad_slot_3 = QtWidgets.QAction(MainWindow)
        self.actionLoad_slot_3.setObjectName("actionLoad_slot_3")
        self.menuSave.addAction(self.actionSave_slot_1)
        self.menuSave.addAction(self.actionSave_slot_2)
        self.menuSave.addAction(self.actionSave_slot_3)
        self.menuLoad.addAction(self.actionLoad_slot_1)
        self.menuLoad.addAction(self.actionLoad_slot_2)
        self.menuLoad.addAction(self.actionLoad_slot_3)
        self.menuView.addAction(self.actionClear)
        self.menuExit.addAction(self.actionExit)
        self.menuExit.addAction(self.actionBack_to_menu)
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuLoad.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.clickLabel = QtWidgets.QPushButton(self.centralwidget)
        self.clickLabel.setGeometry(QtCore.QRect(0, 0, 1024, 720))
        self.clickLabel.setText("")
        self.clickLabel.setObjectName("clickLabel")
        self.clickLabel.setFlat(True)
        

        self.choiceLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.choiceLayoutWidget.setGeometry(QtCore.QRect(350, 50, 350, 500))
        self.choiceLayout = QtWidgets.QVBoxLayout(self.choiceLayoutWidget)
        
        self.choiceLayout.setObjectName("choiceLayout")


        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.background = ""
        self.scriptfile = None
        self.linecounter = 0
        self.music = None
        self.chars = []
        self.connectButtons(MainWindow)
        self.openScript("firstScript.script")
        mixer.init()

        for char in self.centralwidget.findChildren(QtWidgets.QLabel):
            char.alias = ""

        


    def playMusic(self, filename):
        mixer.music.load(filename)
        mixer.music.play(-1)
        

    def openScript(self, file):
        if self.scriptfile != None:
            self.scriptfile.close()
        self.scriptfile = open(file)
        self.linecounter = 0
        
    def closeScript(self):
        self.scriptfile.close()

    def readVNScript(self, MainWindow, event=None):
        rawline = self.scriptfile.readline().strip()
        self.linecounter += 1

        #EOF
        if rawline == "END":
            self.closeScript()
            self.backMenu()
            return True

        #ignore one click/stop automatic reading of next line
        if rawline == "STOP":
            return True
        

        #regular text line with name
        line = re.fullmatch(r'^"(?P<name>.+?)" "(?P<text>.+)"$', rawline)
        if line != None:
            self.nameStatus = True
            self.name_window.show()
            self.name_txt.show()
            self.txt_content.setText(line.group("text"))
            self.name_txt.setText(line.group("name"))
            return True

        
        #regular text line without name
        line = re.fullmatch(r'^"(?P<text>.+)"$', rawline)
        if line != None:
            self.nameStatus = False
            self.name_window.hide()
            self.name_txt.hide()
            line = line.group("text")
            self.txt_content.setText(line)
            return True
        

        #play sound
        line = re.fullmatch(r'^PLAY SOUND "(?P<filename>.+)"$', rawline)
        if line != None:
            playsound.playsound(line.group("filename"), False)
            return self.readVNScript(MainWindow)

        #play music
        line = re.fullmatch(r'^PLAY MUSIC "(?P<filename>.+)"$', rawline)
        if line != None:
            self.playMusic(line.group("filename"))
            self.music = line.group("filename")
            return self.readVNScript(MainWindow)

        #set the background
        line = re.fullmatch(r'^SCENE "(?P<filename>.+)"$', rawline)
        if line != None:
            self.background = line.group("filename")
            MainWindow.setStyleSheet("#MainWindow{\nborder-image: url(" + line.group("filename") + ")\n}\n")
            return self.readVNScript(MainWindow)
            
        #show a character sprite
        line = re.fullmatch(r'^SHOW "(?P<filename>.+)" AT (?P<xcord>\d+?)\s(?P<ycord>\d+?) AS\s(?P<name>.+)$' , rawline)
        if line != None:
            char = QtWidgets.QLabel(self.centralwidget)
            pixmap = QPixmap(line.group("filename"))
            pixmap = pixmap.scaledToHeight(720)
            char.alias = line.group("name").strip()
            size = pixmap.size()
            char.setPixmap(pixmap)
            x = int(line.group("xcord"))
            y = int(line.group("ycord"))
            char.setGeometry(x, y, size.width(), size.height())
            char.show()
            self.chars.append({"name": char.alias,
                               "posx": line.group("xcord"),
                               "posy": line.group("ycord"),
                               "file": line.group("filename")})
            self.updateConstElements(MainWindow)            
            return self.readVNScript(MainWindow)
    
        #hide a character sprite
        line = re.fullmatch(r'^HIDE\s(?P<name>.+)$', rawline)
        if line != None:
            for char in self.centralwidget.findChildren(QtWidgets.QLabel):
                if char.alias == line.group("name").strip():
                    char.hide()
            
            self.chars = [char for char in self.chars if char["name"] != line.group("name").strip()]
            return self.readVNScript(MainWindow)

        #add option to the choice menu
        line = re.fullmatch(r'^OPTION "(?P<text>.+?)" TO "(?P<script>.+)"$', rawline)
        if line != None:
            self.txt_content.hide()
            self.txt_window.hide()
            self.name_window.hide()
            self.name_txt.hide()
            choiceOpt = QtWidgets.QPushButton(line.group("text"))
            choiceOpt.clicked.connect(lambda: self.redirect(line.group("script")))
            self.choiceLayout.addWidget(choiceOpt)
            choiceOpt.raise_()
            self.choiceLayoutWidget.raise_()
            self.clickLabel.setEnabled(False)
            return self.readVNScript(MainWindow)
        
        #direct call to change scriptfile
        line = re.fullmatch(r'^GOTO "(?P<filename>.+)" SKIP (?P<lines>.+)$', rawline)
        if line != None:
            self.openScript(line.group("filename"))
            for i in range(int(line.group("lines"))):
                self.scriptfile.readline()
            return True
        

        if line == None:
            return self.readVNScript(MainWindow)
            
        return False

    def makeSave(self, slotindex):
        with open("loadslots/loadslot" + str(slotindex) + ".script", "w") as savefile:
            
            savefile.write(f'SCENE "{self.background}"\n')
            savefile.write(f'PLAY MUSIC "{self.music}"\n')
            for char in self.chars:
                savefile.write(f'SHOW "{char["file"]}" AT {char["posx"]} {char["posy"]} AS {char["name"]}\n')
            if self.nameStatus:
                savefile.write(f'"{self.name_txt.text()}" "{self.txt_content.text()}"\n')
            else:
                savefile.write(f'"{self.txt_content.text()}"\n')
            savefile.write(f'GOTO "{self.scriptfile.name}" SKIP {self.linecounter}\n')

        return True

    def updateConstElements(self, MainWindow):
        self.txt_window.raise_()
        self.txt_content.raise_()
        self.name_window.raise_()
        self.name_txt.raise_()
        self.clickLabel.raise_()
        
    def redirect(self, filename):
        self.clickLabel.setEnabled(True)
        if filename != "":
            self.closeScript()
            player = sp.Popen(["python3", "scriptplayer.py", "-p", filename])
            sys.exit()
        return False

    def clearScreen(self):
        
        if self.txt_window.isVisible():
             self.txt_content.hide()
             self.txt_window.hide()
             self.name_window.hide()
             self.name_txt.hide()
        else:
             self.txt_content.show()
             self.txt_window.show()
             if self.nameStatus:
                self.name_window.show()
                self.name_txt.show()
            
        


    def backMenu(self):
        self.closeScript()
        startmenu = sp.Popen(["python3", "start.py"], shell=False)
        sys.exit()

    def clickOnScreenHandler(self, MainWindow):
        self.clickLabel.setVisible(False)
        self.readVNScript(MainWindow)
        self.clickLabel.setVisible(True)
    
    def connectButtons(self, MainWindow):
        self.actionClear.triggered.connect(self.clearScreen)
        self.actionBack_to_menu.triggered.connect(self.backMenu)
        self.actionLoad_slot_1.triggered.connect(lambda: loadSlot(1))
        self.actionLoad_slot_2.triggered.connect(lambda: loadSlot(2))
        self.actionLoad_slot_3.triggered.connect(lambda: loadSlot(3))
        self.actionSave_slot_1.triggered.connect(lambda: self.makeSave(1))
        self.actionSave_slot_2.triggered.connect(lambda: self.makeSave(2))
        self.actionSave_slot_3.triggered.connect(lambda: self.makeSave(3))
        
        self.clickLabel.mousePressEvent=  lambda x: self.clickOnScreenHandler(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.txt_content.setText(_translate("MainWindow", "Text Label"))
        #self.name_txt.setText(_translate("MainWindow", "NameLabel"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionBack_to_menu.setText(_translate("MainWindow", "Back to menu"))
        self.actionSave_slot_1.setText(_translate("MainWindow", "Save to slot 1"))
        self.actionLoad_slot_1.setText(_translate("MainWindow", "Load slot 1"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSave_slot_2.setText(_translate("MainWindow", "Save to slot 2"))
        self.actionSave_slot_3.setText(_translate("MainWindow", "Save to slot 3"))
        self.actionLoad_slot_2.setText(_translate("MainWindow", "Load slot 2"))
        self.actionLoad_slot_3.setText(_translate("MainWindow", "Load slot 3"))


if __name__ == "__main__":
    main()
    
