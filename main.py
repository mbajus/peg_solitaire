import copy, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_box(object):
    def setupUi(self, box, txt):
        box.setObjectName("box")
        box.resize(270, 70)
        box.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.frame = QtWidgets.QFrame(box)
        self.frame.setGeometry(QtCore.QRect(0, 0, 270, 70))
        self.frame.setStyleSheet("background-color: rgb(125, 157, 156);")
        self.boxbtn = QtWidgets.QDialogButtonBox(self.frame)
        self.boxbtn.setGeometry(QtCore.QRect(115, 40, 40, 20))
        self.boxbtn.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.boxLabel = QtWidgets.QLabel(self.frame)
        self.boxLabel.setGeometry(QtCore.QRect(10, 0, 250, 40))
        self.boxLabel.setText(txt)
        self.boxbtn.accepted.connect(box.accept)
        self.boxbtn.rejected.connect(box.reject)
        QtCore.QMetaObject.connectSlotsByName(box)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 510)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 510))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(240, 235, 227);\n""")
        self.centralwidget.setObjectName("centralwidget")
        self.board = QtWidgets.QFrame(self.centralwidget)
        self.board.setGeometry(QtCore.QRect(0, 60, 450, 450))
        self.board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.board.setObjectName("board")

        self.boardMenu = QtWidgets.QFrame(self.centralwidget)
        self.boardMenu.setGeometry(QtCore.QRect(0, 60, 450, 450))
        self.boardMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.boardMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.boardMenu.setObjectName("boardMenu")
        self.label_2 = QtWidgets.QLabel(self.boardMenu)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 150, 30))
        font15 = QtGui.QFont()
        font15.setFamily("Bahnschrift")
        font15.setPointSize(15)
        self.label_2.setFont(font15)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("How to play!")
        self.label_3 = QtWidgets.QLabel(self.boardMenu)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 180, 180))
        font12 = QtGui.QFont()
        font12.setFamily("Bahnschrift")
        font12.setPointSize(10)
        self.label_3.setFont(font12)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("In each game, the rules are the same. You may remove pegs by jumping over them with another peg, as in checkers. Your goal is to jump these pegs over each other, one by one, until only a single peg is remaining. That\'s it!")
        self.label_4 = QtWidgets.QLabel(self.boardMenu)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 190, 30))
        self.label_4.setFont(font12)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("<a href=\"https://en.wikipedia.org/wiki/Peg_solitaire\">PEG SOLITAIRE on Wikipedia</a>")
        self.label_5 = QtWidgets.QLabel(self.boardMenu)
        self.label_5.setGeometry(QtCore.QRect(240, 150, 150, 30))
        self.label_5.setFont(font15)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Features!")      
        self.label_6 = QtWidgets.QLabel(self.boardMenu)
        self.label_6.setGeometry(QtCore.QRect(250, 180, 180, 110))
        self.label_6.setFont(font12)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("1. You can choose the peg solitaire scheme from the list in the upper section. To start just choose the New game button.")
        self.label_7 = QtWidgets.QLabel(self.boardMenu)
        self.label_7.setGeometry(QtCore.QRect(250, 290, 170, 130))
        self.label_7.setFont(font12)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_7.setText("2. You can create your own scheme by typing the name of scheme and going to the creator by \"Go to creator!\"\nSingle tap for initial hole, double tap for the blank place.")
        self.label_8 = QtWidgets.QLabel(self.boardMenu)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 140, 20))
        font13 = QtGui.QFont()
        font13.setFamily("Bahnschrift")
        font13.setPointSize(13)
        font13.setUnderline(True)
        self.label_8.setFont(font13)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("Create new scheme:")
        self.lineEdit = QtWidgets.QLineEdit(self.boardMenu)
        self.lineEdit.setGeometry(QtCore.QRect(60, 60, 150, 30))
        font11 = QtGui.QFont()
        font11.setFamily("Bahnschrift")
        font11.setPointSize(11)
        self.lineEdit.setFont(font11)
        self.lineEdit.setMaxLength(18)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("type scheme name")
        self.schemBtn = QtWidgets.QPushButton(self.boardMenu, clicked = lambda: self.goCreator())
        self.schemBtn.setGeometry(QtCore.QRect(230, 60, 150, 30))
        self.schemBtn.setObjectName("schemBtn")
        self.schemBtn.setText("Go to creator!")
        self.line = QtWidgets.QFrame(self.boardMenu)
        self.line.setGeometry(QtCore.QRect(220, 150, 20, 260))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.board.setHidden(True)

        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("blank.png"))
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("full.png"))
        self.icon2.addPixmap(QtGui.QPixmap("active.png"), QtGui.QIcon.Active)
        self.icon22 = QtGui.QIcon()
        self.icon22.addPixmap(QtGui.QPixmap("full.png"))        
        self.icon3 = QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap("empty.png"))
        
        self.btn_board = [[""] * 9 for i in range(9)]
        self.btn_group = QtWidgets.QButtonGroup(self.board)
        self.btn_group.setExclusive(True)
        for i in range(9):
            for j in range(9):
                self.btn_board[i][j] = QtWidgets.QPushButton(self.board)
                self.btn_board[i][j].setFlat(True)
                self.btn_board[i][j].setEnabled(False)
                self.btn_board[i][j].setGeometry(QtCore.QRect(j*50, i*50, 50, 50))
                self.btn_board[i][j].setIconSize(QtCore.QSize(45, 45))
                self.btn_board[i][j].setCheckable(True)
                self.btn_board[i][j].setObjectName("btn_board"+str(i)+str(j))
                self.btn_group.addButton(self.btn_board[i][j])
                self.btn_board[i][j].clicked.connect(lambda: self.boardPressed())
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 450, 60))
        self.frame.setStyleSheet("background-color: rgb(125, 157, 156);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 60))
        font1 = QtGui.QFont()
        font1.setFamily("Niagara Solid")
        font1.setPointSize(36)
        self.label.setFont(font1)
        self.label.setObjectName("label")
        self.btnMenu = QtWidgets.QPushButton(self.frame, clicked = lambda: self.goMenu())
        self.btnMenu.setGeometry(QtCore.QRect(380, 30, 60, 20))
        self.btnMenu.setObjectName("btnMenu")
        self.btnSave = QtWidgets.QPushButton(self.frame, clicked = lambda: self.goSave())
        self.btnSave.setGeometry(QtCore.QRect(380, 30, 60, 20))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.setHidden(True)
        self.btnNew = QtWidgets.QPushButton(self.frame, clicked = lambda: self.newGame())
        self.btnNew.setGeometry(QtCore.QRect(310, 30, 60, 20))
        self.btnNew.setObjectName("btnNew")      
        self.comboSche = QtWidgets.QComboBox(self.frame)
        self.comboSche.setGeometry(QtCore.QRect(180, 30, 120, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboSche.sizePolicy().hasHeightForWidth())
        self.comboSche.setSizePolicy(sizePolicy)
        self.comboSche.setObjectName("comboSche")
        self.reloadBoardSchemes()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def countFull(self, x):
        n = 0
        for i in range(9):
            n += self.gboard[i].count(x)
        return n

    def checkEnd(self):
        for i in range(9):
            for j in range(9):
                if self.gboard[i][j] == 2:
                    for n in [[1,0], [-1,0], [0,1], [0,-1]]:
                        if (i+2*n[0] >= 0) and (i+2*n[0] <= 8) and (j+2*n[1] >= 0) and (j+2*n[1] <= 8):
                            if (self.gboard[i+1*n[0]][j+1*n[1]] == 1) and (self.gboard[i+2*n[0]][j+2*n[1]] == 1):
                                return True
        return False

    def boardPressed(self):
        for i in range(9):
            for j in range(9):
                if self.btn_board[i][j].isChecked():
                    pos = [i,j]
                    break
        if self.btnSave.isHidden() == True:           
            if self.lastclicked == None:
                self.lastclicked = pos   
            elif self.gboard[self.lastclicked[0]][self.lastclicked[1]] == 1 and self.gboard[pos[0]][pos[1]] == 2:
                x , y = pos[0]-self.lastclicked[0], pos[1]-self.lastclicked[1]
                if (abs(x) == 2 and abs(y) == 0) or (abs(x) == 0 and abs(y) == 2):
                    x, y = int(x/2), int(y/2)
                    if self.gboard[self.lastclicked[0]+x][self.lastclicked[1]+y] == 1:
                        self.gboard[self.lastclicked[0]][self.lastclicked[1]] = 2
                        self.gboard[pos[0]][pos[1]] = 1
                        self.gboard[self.lastclicked[0]+x][self.lastclicked[1]+y] = 2
            self.lastclicked = pos
            self.reloadBoard()
            if not self.checkEnd():
                self.popbox("You lose, no more moves available!\nStart new game.")
        else:
            if self.gboard[pos[0]][pos[1]] == 2:
                self.gboard[pos[0]][pos[1]] = 0
            else:
                self.gboard[pos[0]][pos[1]] += 1
            self.reloadBoard()

    def goSave(self):
        if self.countFull(2) < 1:
            self.popbox("There should be at least one open circle!")
        elif not self.checkEnd():
            self.popbox("There is no move to do.\nChange the scheme!")
        else:
            f = open('boardshapes.txt', 'a')
            matrix = "\n"
            for i in range(9):
                for j in range(9):
                    matrix += str(self.gboard[i][j])
            f.write(matrix + ";" + self.lineEdit.text())
            f.close()
            self.btnMenu.setHidden(False)
            self.comboSche.setHidden(False)
            self.btnNew.setHidden(False)
            self.btnSave.setHidden(True)
            self.boardMenu.setHidden(False)
            self.board.setHidden(True)
            self.lineEdit.clear()
            self.reloadBoardSchemes()

    def goCreator(self):
        self.lineEdit.setText(self.lineEdit.text().strip())
        if self.lineEdit.text() in self.boardsschemes.keys():
            self.popbox("There is a scheme with that same name.\nPlease use another one!")
        elif self.lineEdit.text() == "":
            self.popbox("Please type a scheme name.")
        else:
            self.btnMenu.setHidden(True)
            self.comboSche.setHidden(True)
            self.btnNew.setHidden(True)
            self.btnSave.setHidden(False)
            self.boardMenu.setHidden(True)
            self.board.setHidden(False)
            self.gboard = [[1] * 9 for i in range(9)]
            self.reloadBoard()

    def popbox(self, txt):
        box = QtWidgets.QDialog()
        ui = Ui_box()
        ui.setupUi(box, txt)
        box.show()
        box.exec_()

    def reloadBoard(self):
        if self.btnSave.isHidden() == True:
            if self.checkEnd():
                MainWindow.setWindowTitle(f"Peg Solitaire - {self.countFull(1)-1} pegs remaining!")
            elif self.countFull(1) == 1:
                MainWindow.setWindowTitle(f"Peg Solitaire - YOU WON!")
            else:
                MainWindow.setWindowTitle(f"Peg Solitaire - YOU LOSE! with {self.countFull(1)-1} pegs remaning!")
        for i in range(9):
            for j in range(9):
                self.btn_board[i][j].setChecked(False)
                if self.gboard[i][j] == 0:
                    if self.btnSave.isHidden() == True:
                        self.btn_board[i][j].setEnabled(False)
                    else:
                        self.btn_board[i][j].setEnabled(True)
                    self.btn_board[i][j].setIcon(self.icon1)
                elif self.gboard[i][j] == 1:
                    self.btn_board[i][j].setEnabled(True)
                    if self.btnSave.isHidden() == True:
                        self.btn_board[i][j].setIcon(self.icon2)
                    else:
                        self.btn_board[i][j].setIcon(self.icon22)
                elif self.gboard[i][j] == 2:
                    self.btn_board[i][j].setEnabled(True)                    
                    self.btn_board[i][j].setIcon(self.icon3)

    def goMenu(self):
        self.board.setHidden(True)
        self.boardMenu.setHidden(False) 
        MainWindow.setWindowTitle(f"Peg Solitaire")
        self.lineEdit.clear()    
    
    def newGame(self):
        self.board.setHidden(False)
        self.boardMenu.setHidden(True)
        self.gboard = copy.deepcopy(self.boardsschemes[self.comboSche.currentText()])
        self.btn_group.setExclusive(False)
        self.lastclicked = None
        self.reloadBoard()
        self.btn_group.setExclusive(True)

    def reloadBoardSchemes(self):
        f = open('boardshapes.txt')
        self.comboSche.clear()
        self.boardsschemes = dict()
        for line in f:
            table = [[""] * 9 for i in range(9)]
            for i, x in enumerate(line[:81]):
                table[i // 9][i - (i // 9) * 9] = int(x)
            self.boardsschemes[line[82:].rstrip()] = table
            self.comboSche.addItem(line[82:].rstrip())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Peg Solitaire"))
        self.label.setText(_translate("MainWindow", " PEG SOLITAIRE"))
        self.btnMenu.setText(_translate("MainWindow", "Menu"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnNew.setText(_translate("MainWindow", "New game")) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())