## @package number_pad

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QWidget

class numberPopup(QWidget):
    def __init__(self, Form, numberSet, callOnSubmit, constantText = "" , *args):
        super().__init__()
        self.numberSet = numberSet
        self.Form = Form
        self.callOnSubmit = callOnSubmit
        self.args = args
        self.constantText = constantText
        self.setObjectName("Form")
        self.resize(800, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton1 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 0, 0, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 0, 1, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 0, 2, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton4.sizePolicy().hasHeightForWidth())
        self.pushButton4.setSizePolicy(sizePolicy)
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton5.sizePolicy().hasHeightForWidth())
        self.pushButton5.setSizePolicy(sizePolicy)
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton6.sizePolicy().hasHeightForWidth())
        self.pushButton6.setSizePolicy(sizePolicy)
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton7.sizePolicy().hasHeightForWidth())
        self.pushButton7.setSizePolicy(sizePolicy)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout.addWidget(self.pushButton7, 2, 0, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton8.sizePolicy().hasHeightForWidth())
        self.pushButton8.setSizePolicy(sizePolicy)
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout.addWidget(self.pushButton8, 2, 1, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton9.sizePolicy().hasHeightForWidth())
        self.pushButton9.setSizePolicy(sizePolicy)
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout.addWidget(self.pushButton9, 2, 2, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton0.sizePolicy().hasHeightForWidth())
        self.pushButton0.setSizePolicy(sizePolicy)
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout.addWidget(self.pushButton0, 3, 1, 1, 1)
        self.pushButton_erase = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_erase.sizePolicy().hasHeightForWidth())
        self.pushButton_erase.setSizePolicy(sizePolicy)
        self.pushButton_erase.setObjectName("pushButton_erase")
        self.gridLayout.addWidget(self.pushButton_erase, 3, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton_submit = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_submit.sizePolicy().hasHeightForWidth())
        self.pushButton_submit.setSizePolicy(sizePolicy)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.verticalLayout.addWidget(self.pushButton_submit)
        #Form.setCentralWidget(Form)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        #Form.setStatusBar(self.statusbar)
        self.lineEdit.setMaxLength(10)
        self.pushButton0.clicked.connect(self.push_button0_clicked)
        self.pushButton1.clicked.connect(self.push_button1_clicked)
        self.pushButton2.clicked.connect(self.push_button2_clicked)
        self.pushButton3.clicked.connect(self.push_button3_clicked)
        self.pushButton4.clicked.connect(self.push_button4_clicked)
        self.pushButton5.clicked.connect(self.push_button5_clicked)
        self.pushButton6.clicked.connect(self.push_button6_clicked)
        self.pushButton7.clicked.connect(self.push_button7_clicked)
        self.pushButton8.clicked.connect(self.push_button8_clicked)
        self.pushButton9.clicked.connect(self.push_button9_clicked)
        self.pushButton_submit.clicked.connect(self.push_buttonsubmit_clicked)
        self.pushButton_erase.clicked.connect(self.pushButton_erase_clicked)
        self.pushButton_clear.clicked.connect(self.pushButton_clear_clicked)                
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exPopup = None
        self.initUI()
    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowFlags(Qt.Popup)
        self.pushButton1.setText(_translate("Form", "1"))
        self.pushButton2.setText(_translate("Form", "2"))
        self.pushButton3.setText(_translate("Form", "3"))
        self.pushButton4.setText(_translate("Form", "4"))
        self.pushButton5.setText(_translate("Form", "5"))
        self.pushButton6.setText(_translate("Form", "6"))
        self.pushButton7.setText(_translate("Form", "7"))
        self.pushButton8.setText(_translate("Form", "8"))
        self.pushButton9.setText(_translate("Form", "9"))
        self.pushButton0.setText(_translate("Form", "0"))
        self.pushButton_erase.setText(_translate("Form", "DEL"))
        self.pushButton_clear.setText(_translate("Form", "C"))
        self.pushButton_submit.setText(_translate("Form", "ENTER"))

    def push_button0_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '0')

    def push_button1_clicked(self): 
        self.lineEdit.setText(self.lineEdit.text() + '1')

    def push_button2_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '2')

    def push_button3_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '3')

    def push_button4_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '4')

    def push_button5_clicked(self): 
        self.lineEdit.setText(self.lineEdit.text() + '5')

    def push_button6_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '6')

    def push_button7_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '7')

    def push_button8_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + '8')

    def push_button9_clicked(self): 
        self.lineEdit.setText(self.lineEdit.text() + '9')

    def push_buttonsubmit_clicked(self):
        print('Debug lineEdit.text:', self.lineEdit.text(), type(self.lineEdit.text()), 'self.numberSet:', self.numberSet, type(self.numberSet))
        if self.lineEdit.text() == self.numberSet:
            print("Correct PIN entered")
            self.callOnSubmit(False)
            self.hide()  # Add conditional for PIN here.
            # self.Form.setEnabled(True)
        else:
            print('Incorrect pin!')

    def pushButton_erase_clicked(self):
        text = self.lineEdit.text()
        textLength = len(text)
        if(textLength):
            newtext = text[:textLength - 1]
            self.lineEdit.setText(newtext)

    def pushButton_clear_clicked(self):
        self.lineEdit.clear()

    def closeEvent(self,event):
        #self.Form.setEnabled(True)
        pass
