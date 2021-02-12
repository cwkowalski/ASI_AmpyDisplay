# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ampy_bms.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BMSDialog(object):
    def setupUi(self, BMSDialog):
        BMSDialog.setObjectName("BMSDialog")
        BMSDialog.resize(800, 480)
        BMSDialog.setStyleSheet("QGroupBox{\n"
"    background: solid white;\n"
"    border: 5px solid black;\n"
"    border-radius: 20px;\n"
"    margin-top: 25px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 240px;\n"
"    padding: -15 0px 0 0px;\n"
"    font: 40pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.ExitBtn = QtWidgets.QPushButton(BMSDialog)
        self.ExitBtn.setGeometry(QtCore.QRect(695, 10, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ExitBtn.setFont(font)
        self.ExitBtn.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 30px;\n"
"    font-family: \"Impact\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 3px;\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.ExitBtn.setCheckable(True)
        self.ExitBtn.setChecked(False)
        self.ExitBtn.setAutoExclusive(True)
        self.ExitBtn.setObjectName("ExitBtn")
        self.ChargeLevelSlider = QtWidgets.QSlider(BMSDialog)
        self.ChargeLevelSlider.setGeometry(QtCore.QRect(147, 80, 650, 45))
        self.ChargeLevelSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.ChargeLevelSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.ChargeLevelSlider.setFont(font)
        self.ChargeLevelSlider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 40px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background-color: black;\n"
"border: 5px solid;\n"
"border-radius: 12px;\n"
"width: 30px; \n"
"margin: 0px 0px;}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 28px\n"
"}\n"
"    ")
        self.ChargeLevelSlider.setMinimum(3700)
        self.ChargeLevelSlider.setMaximum(4200)
        self.ChargeLevelSlider.setPageStep(20)
        self.ChargeLevelSlider.setProperty("value", 3700)
        self.ChargeLevelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ChargeLevelSlider.setInvertedAppearance(False)
        self.ChargeLevelSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.ChargeLevelSlider.setTickInterval(1)
        self.ChargeLevelSlider.setObjectName("ChargeLevelSlider")
        self.ChargeLevelLabel = QtWidgets.QLabel(BMSDialog)
        self.ChargeLevelLabel.setGeometry(QtCore.QRect(5, 65, 141, 65))
        self.ChargeLevelLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.ChargeLevelLabel.setObjectName("ChargeLevelLabel")
        self.PowerLabel = QtWidgets.QLabel(BMSDialog)
        self.PowerLabel.setGeometry(QtCore.QRect(5, 0, 170, 40))
        self.PowerLabel.setStyleSheet("QLabel{\n"
"    font: 30pt \"Luxi Mono\";\n"
"}")
        self.PowerLabel.setObjectName("PowerLabel")
        self.VRangeLabel = QtWidgets.QLabel(BMSDialog)
        self.VRangeLabel.setGeometry(QtCore.QRect(190, 0, 201, 37))
        self.VRangeLabel.setStyleSheet("QLabel{\n"
"    font: 18pt \"Luxi Moni\";\n"
"}")
        self.VRangeLabel.setObjectName("VRangeLabel")
        self.VDiffLabel = QtWidgets.QLabel(BMSDialog)
        self.VDiffLabel.setGeometry(QtCore.QRect(189, 40, 125, 37))
        self.VDiffLabel.setStyleSheet("QLabel{\n"
"    font: 18pt \"Luxi Moni\";\n"
"}")
        self.VDiffLabel.setObjectName("VDiffLabel")
        self.CurrentLabel = QtWidgets.QLabel(BMSDialog)
        self.CurrentLabel.setGeometry(QtCore.QRect(5, 30, 170, 45))
        self.CurrentLabel.setStyleSheet("QLabel{\n"
"    font: 30pt \"Luxi Mono\";\n"
"}")
        self.CurrentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CurrentLabel.setObjectName("CurrentLabel")
        self.ChargeTimeLabel = QtWidgets.QLabel(BMSDialog)
        self.ChargeTimeLabel.setGeometry(QtCore.QRect(410, 0, 201, 37))
        self.ChargeTimeLabel.setStyleSheet("QLabel{\n"
"    font: 18pt \"Luxi Moni\";\n"
"}")
        self.ChargeTimeLabel.setObjectName("ChargeTimeLabel")
        self.label_7 = QtWidgets.QLabel(BMSDialog)
        self.label_7.setGeometry(QtCore.QRect(173, 85, 340, 37))
        self.label_7.setStyleSheet("QLabel{\n"
"    font: 18pt \"Luxi Moni\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.BalanceLevelSlider = QtWidgets.QSlider(BMSDialog)
        self.BalanceLevelSlider.setGeometry(QtCore.QRect(145, 138, 650, 45))
        self.BalanceLevelSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.BalanceLevelSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.BalanceLevelSlider.setFont(font)
        self.BalanceLevelSlider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 40px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background-color: black;\n"
"border: 5px solid;\n"
"border-radius: 12px;\n"
"width: 30px; \n"
"margin: 0px 0px;}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 28px\n"
"}\n"
"    ")
        self.BalanceLevelSlider.setMinimum(3000)
        self.BalanceLevelSlider.setMaximum(3000)
        self.BalanceLevelSlider.setPageStep(20)
        self.BalanceLevelSlider.setProperty("value", 3000)
        self.BalanceLevelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BalanceLevelSlider.setInvertedAppearance(False)
        self.BalanceLevelSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.BalanceLevelSlider.setTickInterval(1)
        self.BalanceLevelSlider.setObjectName("BalanceLevelSlider")
        self.BalanceVLabel = QtWidgets.QLabel(BMSDialog)
        self.BalanceVLabel.setGeometry(QtCore.QRect(3, 123, 141, 65))
        self.BalanceVLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.BalanceVLabel.setObjectName("BalanceVLabel")
        self.label_8 = QtWidgets.QLabel(BMSDialog)
        self.label_8.setGeometry(QtCore.QRect(175, 143, 340, 37))
        self.label_8.setStyleSheet("QLabel{\n"
"    font: 18pt \"Luxi Moni\";\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(BMSDialog)
        self.label_10.setGeometry(QtCore.QRect(8, 166, 786, 37))
        self.label_10.setStyleSheet("QLabel{\n"
"    font: 12pt \"Luxi Moni\";\n"
"}")
        self.label_10.setObjectName("label_10")
        self.groupBox = QtWidgets.QGroupBox(BMSDialog)
        self.groupBox.setGeometry(QtCore.QRect(5, 171, 790, 304))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QLabel{font: 18pt \'Luxi Mono\'}\n"
"QProgressBar{font: 10pt \'Luxi Mono\';\n"
"margin: 0px;\n"
"padding: 0px}\n"
"QPushButton{background: white;\n"
"border: none;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 35, 771, 265))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.C3Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C3Label.setObjectName("C3Label")
        self.gridLayout.addWidget(self.C3Label, 2, 0, 1, 1)
        self.C3Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C3Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C3Bar.setMinimum(2500)
        self.C3Bar.setMaximum(4200)
        self.C3Bar.setProperty("value", 2499)
        self.C3Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C3Bar.setTextVisible(True)
        self.C3Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C3Bar.setObjectName("C3Bar")
        self.gridLayout.addWidget(self.C3Bar, 2, 2, 1, 1)
        self.C1Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C1Label.setObjectName("C1Label")
        self.gridLayout.addWidget(self.C1Label, 0, 0, 1, 1)
        self.C15Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C15Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C15Bar.setMinimum(2500)
        self.C15Bar.setMaximum(4200)
        self.C15Bar.setProperty("value", 2499)
        self.C15Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C15Bar.setTextVisible(True)
        self.C15Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C15Bar.setObjectName("C15Bar")
        self.gridLayout.addWidget(self.C15Bar, 0, 9, 1, 1)
        self.C5Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C5Label.setObjectName("C5Label")
        self.gridLayout.addWidget(self.C5Label, 4, 0, 1, 1)
        self.C15Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C15Label.setObjectName("C15Label")
        self.gridLayout.addWidget(self.C15Label, 0, 7, 1, 1)
        self.C5Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C5Balance.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/bms-led-red.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/root/bms-led-green.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.C5Balance.setIcon(icon)
        self.C5Balance.setCheckable(True)
        self.C5Balance.setObjectName("C5Balance")
        self.gridLayout.addWidget(self.C5Balance, 4, 1, 1, 1)
        self.C6Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C6Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C6Bar.setMinimum(2500)
        self.C6Bar.setMaximum(4200)
        self.C6Bar.setProperty("value", 2499)
        self.C6Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C6Bar.setTextVisible(True)
        self.C6Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C6Bar.setObjectName("C6Bar")
        self.gridLayout.addWidget(self.C6Bar, 5, 2, 1, 1)
        self.C15Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C15Balance.setText("")
        self.C15Balance.setIcon(icon)
        self.C15Balance.setCheckable(True)
        self.C15Balance.setObjectName("C15Balance")
        self.gridLayout.addWidget(self.C15Balance, 0, 8, 1, 1)
        self.C8Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C8Label.setObjectName("C8Label")
        self.gridLayout.addWidget(self.C8Label, 0, 4, 1, 1)
        self.C1Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C1Balance.setText("")
        self.C1Balance.setIcon(icon)
        self.C1Balance.setCheckable(True)
        self.C1Balance.setObjectName("C1Balance")
        self.gridLayout.addWidget(self.C1Balance, 0, 1, 1, 1)
        self.C2Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C2Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C2Bar.setMinimum(2500)
        self.C2Bar.setMaximum(4200)
        self.C2Bar.setProperty("value", 2499)
        self.C2Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C2Bar.setTextVisible(True)
        self.C2Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C2Bar.setObjectName("C2Bar")
        self.gridLayout.addWidget(self.C2Bar, 1, 2, 1, 1)
        self.C3Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C3Balance.setText("")
        self.C3Balance.setIcon(icon)
        self.C3Balance.setCheckable(True)
        self.C3Balance.setObjectName("C3Balance")
        self.gridLayout.addWidget(self.C3Balance, 2, 1, 1, 1)
        self.C4Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C4Balance.setText("")
        self.C4Balance.setIcon(icon)
        self.C4Balance.setCheckable(True)
        self.C4Balance.setObjectName("C4Balance")
        self.gridLayout.addWidget(self.C4Balance, 3, 1, 1, 1)
        self.C1Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C1Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C1Bar.setMinimum(2500)
        self.C1Bar.setMaximum(4200)
        self.C1Bar.setProperty("value", 3700)
        self.C1Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C1Bar.setTextVisible(True)
        self.C1Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C1Bar.setObjectName("C1Bar")
        self.gridLayout.addWidget(self.C1Bar, 0, 2, 1, 1)
        self.C8Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C8Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C8Bar.setMinimum(2500)
        self.C8Bar.setMaximum(4200)
        self.C8Bar.setProperty("value", 2499)
        self.C8Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C8Bar.setTextVisible(True)
        self.C8Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C8Bar.setObjectName("C8Bar")
        self.gridLayout.addWidget(self.C8Bar, 0, 6, 1, 1)
        self.C4Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C4Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C4Bar.setMinimum(2500)
        self.C4Bar.setMaximum(4200)
        self.C4Bar.setProperty("value", 2499)
        self.C4Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C4Bar.setTextVisible(True)
        self.C4Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C4Bar.setObjectName("C4Bar")
        self.gridLayout.addWidget(self.C4Bar, 3, 2, 1, 1)
        self.C2Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C2Balance.setText("")
        self.C2Balance.setIcon(icon)
        self.C2Balance.setCheckable(True)
        self.C2Balance.setObjectName("C2Balance")
        self.gridLayout.addWidget(self.C2Balance, 1, 1, 1, 1)
        self.C2Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C2Label.setObjectName("C2Label")
        self.gridLayout.addWidget(self.C2Label, 1, 0, 1, 1)
        self.C8Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C8Balance.setText("")
        self.C8Balance.setIcon(icon)
        self.C8Balance.setCheckable(True)
        self.C8Balance.setObjectName("C8Balance")
        self.gridLayout.addWidget(self.C8Balance, 0, 5, 1, 1)
        self.C4Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C4Label.setObjectName("C4Label")
        self.gridLayout.addWidget(self.C4Label, 3, 0, 1, 1)
        self.C5Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C5Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C5Bar.setMinimum(2500)
        self.C5Bar.setMaximum(4200)
        self.C5Bar.setProperty("value", 2499)
        self.C5Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C5Bar.setTextVisible(True)
        self.C5Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C5Bar.setObjectName("C5Bar")
        self.gridLayout.addWidget(self.C5Bar, 4, 2, 1, 1)
        self.C7Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C7Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C7Bar.setMinimum(2500)
        self.C7Bar.setMaximum(4200)
        self.C7Bar.setProperty("value", 2499)
        self.C7Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C7Bar.setTextVisible(True)
        self.C7Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C7Bar.setObjectName("C7Bar")
        self.gridLayout.addWidget(self.C7Bar, 6, 2, 1, 1)
        self.C6Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C6Label.setObjectName("C6Label")
        self.gridLayout.addWidget(self.C6Label, 5, 0, 1, 1)
        self.C6Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C6Balance.setText("")
        self.C6Balance.setIcon(icon)
        self.C6Balance.setCheckable(True)
        self.C6Balance.setObjectName("C6Balance")
        self.gridLayout.addWidget(self.C6Balance, 5, 1, 1, 1)
        self.C7Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C7Label.setObjectName("C7Label")
        self.gridLayout.addWidget(self.C7Label, 6, 0, 1, 1)
        self.C7Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C7Balance.setText("")
        self.C7Balance.setIcon(icon)
        self.C7Balance.setCheckable(True)
        self.C7Balance.setObjectName("C7Balance")
        self.gridLayout.addWidget(self.C7Balance, 6, 1, 1, 1)
        self.C9Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C9Balance.setText("")
        self.C9Balance.setIcon(icon)
        self.C9Balance.setCheckable(True)
        self.C9Balance.setObjectName("C9Balance")
        self.gridLayout.addWidget(self.C9Balance, 1, 5, 1, 1)
        self.C9Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C9Label.setObjectName("C9Label")
        self.gridLayout.addWidget(self.C9Label, 1, 4, 1, 1)
        self.C10Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C10Label.setObjectName("C10Label")
        self.gridLayout.addWidget(self.C10Label, 2, 4, 1, 1)
        self.C11Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C11Label.setObjectName("C11Label")
        self.gridLayout.addWidget(self.C11Label, 3, 4, 1, 1)
        self.C12Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C12Label.setObjectName("C12Label")
        self.gridLayout.addWidget(self.C12Label, 4, 4, 1, 1)
        self.C13Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C13Label.setObjectName("C13Label")
        self.gridLayout.addWidget(self.C13Label, 5, 4, 1, 1)
        self.C14Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C14Label.setObjectName("C14Label")
        self.gridLayout.addWidget(self.C14Label, 6, 4, 1, 1)
        self.C16Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C16Label.setObjectName("C16Label")
        self.gridLayout.addWidget(self.C16Label, 1, 7, 1, 1)
        self.C17Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C17Label.setObjectName("C17Label")
        self.gridLayout.addWidget(self.C17Label, 2, 7, 1, 1)
        self.C18Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C18Label.setObjectName("C18Label")
        self.gridLayout.addWidget(self.C18Label, 3, 7, 1, 1)
        self.C19Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C19Label.setObjectName("C19Label")
        self.gridLayout.addWidget(self.C19Label, 4, 7, 1, 1)
        self.C20Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C20Label.setObjectName("C20Label")
        self.gridLayout.addWidget(self.C20Label, 5, 7, 1, 1)
        self.C21Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.C21Label.setObjectName("C21Label")
        self.gridLayout.addWidget(self.C21Label, 6, 7, 1, 1)
        self.C10Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C10Balance.setText("")
        self.C10Balance.setIcon(icon)
        self.C10Balance.setCheckable(True)
        self.C10Balance.setObjectName("C10Balance")
        self.gridLayout.addWidget(self.C10Balance, 2, 5, 1, 1)
        self.C11Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C11Balance.setText("")
        self.C11Balance.setIcon(icon)
        self.C11Balance.setCheckable(True)
        self.C11Balance.setObjectName("C11Balance")
        self.gridLayout.addWidget(self.C11Balance, 3, 5, 1, 1)
        self.C12Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C12Balance.setText("")
        self.C12Balance.setIcon(icon)
        self.C12Balance.setCheckable(True)
        self.C12Balance.setObjectName("C12Balance")
        self.gridLayout.addWidget(self.C12Balance, 4, 5, 1, 1)
        self.C13Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C13Balance.setText("")
        self.C13Balance.setIcon(icon)
        self.C13Balance.setCheckable(True)
        self.C13Balance.setObjectName("C13Balance")
        self.gridLayout.addWidget(self.C13Balance, 5, 5, 1, 1)
        self.C14Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C14Balance.setText("")
        self.C14Balance.setIcon(icon)
        self.C14Balance.setCheckable(True)
        self.C14Balance.setObjectName("C14Balance")
        self.gridLayout.addWidget(self.C14Balance, 6, 5, 1, 1)
        self.C9Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C9Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C9Bar.setMinimum(2500)
        self.C9Bar.setMaximum(4200)
        self.C9Bar.setProperty("value", 2499)
        self.C9Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C9Bar.setTextVisible(True)
        self.C9Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C9Bar.setObjectName("C9Bar")
        self.gridLayout.addWidget(self.C9Bar, 1, 6, 1, 1)
        self.C10Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C10Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C10Bar.setMinimum(2500)
        self.C10Bar.setMaximum(4200)
        self.C10Bar.setProperty("value", 2499)
        self.C10Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C10Bar.setTextVisible(True)
        self.C10Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C10Bar.setObjectName("C10Bar")
        self.gridLayout.addWidget(self.C10Bar, 2, 6, 1, 1)
        self.C11Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C11Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C11Bar.setMinimum(2500)
        self.C11Bar.setMaximum(4200)
        self.C11Bar.setProperty("value", 2499)
        self.C11Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C11Bar.setTextVisible(True)
        self.C11Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C11Bar.setObjectName("C11Bar")
        self.gridLayout.addWidget(self.C11Bar, 3, 6, 1, 1)
        self.C12Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C12Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C12Bar.setMinimum(2500)
        self.C12Bar.setMaximum(4200)
        self.C12Bar.setProperty("value", 2499)
        self.C12Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C12Bar.setTextVisible(True)
        self.C12Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C12Bar.setObjectName("C12Bar")
        self.gridLayout.addWidget(self.C12Bar, 4, 6, 1, 1)
        self.C13Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C13Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C13Bar.setMinimum(2500)
        self.C13Bar.setMaximum(4200)
        self.C13Bar.setProperty("value", 2499)
        self.C13Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C13Bar.setTextVisible(True)
        self.C13Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C13Bar.setObjectName("C13Bar")
        self.gridLayout.addWidget(self.C13Bar, 5, 6, 1, 1)
        self.C14Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C14Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C14Bar.setMinimum(2500)
        self.C14Bar.setMaximum(4200)
        self.C14Bar.setProperty("value", 2499)
        self.C14Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C14Bar.setTextVisible(True)
        self.C14Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C14Bar.setObjectName("C14Bar")
        self.gridLayout.addWidget(self.C14Bar, 6, 6, 1, 1)
        self.C16Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C16Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C16Bar.setMinimum(2500)
        self.C16Bar.setMaximum(4200)
        self.C16Bar.setProperty("value", 2499)
        self.C16Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C16Bar.setTextVisible(True)
        self.C16Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C16Bar.setObjectName("C16Bar")
        self.gridLayout.addWidget(self.C16Bar, 1, 9, 1, 1)
        self.C17Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C17Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C17Bar.setMinimum(2500)
        self.C17Bar.setMaximum(4200)
        self.C17Bar.setProperty("value", 2499)
        self.C17Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C17Bar.setTextVisible(True)
        self.C17Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C17Bar.setObjectName("C17Bar")
        self.gridLayout.addWidget(self.C17Bar, 2, 9, 1, 1)
        self.C18Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C18Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C18Bar.setMinimum(2500)
        self.C18Bar.setMaximum(4200)
        self.C18Bar.setProperty("value", 2499)
        self.C18Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C18Bar.setTextVisible(True)
        self.C18Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C18Bar.setObjectName("C18Bar")
        self.gridLayout.addWidget(self.C18Bar, 3, 9, 1, 1)
        self.C19Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C19Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C19Bar.setMinimum(2500)
        self.C19Bar.setMaximum(4200)
        self.C19Bar.setProperty("value", 2499)
        self.C19Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C19Bar.setTextVisible(True)
        self.C19Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C19Bar.setObjectName("C19Bar")
        self.gridLayout.addWidget(self.C19Bar, 4, 9, 1, 1)
        self.C20Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C20Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C20Bar.setMinimum(2500)
        self.C20Bar.setMaximum(4200)
        self.C20Bar.setProperty("value", 2499)
        self.C20Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C20Bar.setTextVisible(True)
        self.C20Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C20Bar.setObjectName("C20Bar")
        self.gridLayout.addWidget(self.C20Bar, 5, 9, 1, 1)
        self.C21Bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.C21Bar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: rgb(30, 255, 30);}\n"
"QProgressBar {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px}")
        self.C21Bar.setMinimum(2500)
        self.C21Bar.setMaximum(4200)
        self.C21Bar.setProperty("value", 2499)
        self.C21Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.C21Bar.setTextVisible(True)
        self.C21Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.C21Bar.setObjectName("C21Bar")
        self.gridLayout.addWidget(self.C21Bar, 6, 9, 1, 1)
        self.C16Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C16Balance.setText("")
        self.C16Balance.setIcon(icon)
        self.C16Balance.setCheckable(True)
        self.C16Balance.setObjectName("C16Balance")
        self.gridLayout.addWidget(self.C16Balance, 1, 8, 1, 1)
        self.C17Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C17Balance.setText("")
        self.C17Balance.setIcon(icon)
        self.C17Balance.setCheckable(True)
        self.C17Balance.setObjectName("C17Balance")
        self.gridLayout.addWidget(self.C17Balance, 2, 8, 1, 1)
        self.C18Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C18Balance.setText("")
        self.C18Balance.setIcon(icon)
        self.C18Balance.setCheckable(True)
        self.C18Balance.setObjectName("C18Balance")
        self.gridLayout.addWidget(self.C18Balance, 3, 8, 1, 1)
        self.C19Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C19Balance.setText("")
        self.C19Balance.setIcon(icon)
        self.C19Balance.setCheckable(True)
        self.C19Balance.setObjectName("C19Balance")
        self.gridLayout.addWidget(self.C19Balance, 4, 8, 1, 1)
        self.C20Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C20Balance.setText("")
        self.C20Balance.setIcon(icon)
        self.C20Balance.setCheckable(True)
        self.C20Balance.setObjectName("C20Balance")
        self.gridLayout.addWidget(self.C20Balance, 5, 8, 1, 1)
        self.C21Balance = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C21Balance.setText("")
        self.C21Balance.setIcon(icon)
        self.C21Balance.setCheckable(True)
        self.C21Balance.setObjectName("C21Balance")
        self.gridLayout.addWidget(self.C21Balance, 6, 8, 1, 1)
        self.ExitBtn_2 = QtWidgets.QPushButton(BMSDialog)
        self.ExitBtn_2.setGeometry(QtCore.QRect(585, 10, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ExitBtn_2.setFont(font)
        self.ExitBtn_2.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 30px;\n"
"    font-family: \"Impact\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 3px;\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.ExitBtn_2.setCheckable(True)
        self.ExitBtn_2.setChecked(False)
        self.ExitBtn_2.setAutoExclusive(True)
        self.ExitBtn_2.setObjectName("ExitBtn_2")

        self.retranslateUi(BMSDialog)
        QtCore.QMetaObject.connectSlotsByName(BMSDialog)

    def retranslateUi(self, BMSDialog):
        _translate = QtCore.QCoreApplication.translate
        BMSDialog.setWindowTitle(_translate("BMSDialog", "Form"))
        self.ExitBtn.setText(_translate("BMSDialog", "Back"))
        self.ChargeLevelLabel.setText(_translate("BMSDialog", "xx.x<sub>%</sub>"))
        self.PowerLabel.setText(_translate("BMSDialog", "xxxx.x<sub>w</sub>"))
        self.VRangeLabel.setText(_translate("BMSDialog", "Range: 3.59~3.61<sub>v</sub>"))
        self.VDiffLabel.setText(_translate("BMSDialog", "Diff: x.xxx<sub>v</sub>"))
        self.CurrentLabel.setText(_translate("BMSDialog", "xx.x<sub>A</sub>"))
        self.ChargeTimeLabel.setText(_translate("BMSDialog", "Rem: 72:59"))
        self.label_7.setText(_translate("BMSDialog", "Slider: Single cut-off voltage"))
        self.BalanceVLabel.setText(_translate("BMSDialog", "xx.x<sub>V</sub>"))
        self.label_8.setText(_translate("BMSDialog", "Slider: Balanced turn-on voltage"))
        self.label_10.setText(_translate("BMSDialog", "Consider replacing TripReset or moving into ampy_options, to add BMS button to home"))
        self.C3Label.setText(_translate("BMSDialog", "03"))
        self.C3Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C1Label.setText(_translate("BMSDialog", "01"))
        self.C15Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C5Label.setText(_translate("BMSDialog", "05"))
        self.C15Label.setText(_translate("BMSDialog", "15"))
        self.C6Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C8Label.setText(_translate("BMSDialog", "08"))
        self.C2Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C1Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C8Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C4Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C2Label.setText(_translate("BMSDialog", "02"))
        self.C4Label.setText(_translate("BMSDialog", "04"))
        self.C5Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C7Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C6Label.setText(_translate("BMSDialog", "06"))
        self.C7Label.setText(_translate("BMSDialog", "07"))
        self.C9Label.setText(_translate("BMSDialog", "09"))
        self.C10Label.setText(_translate("BMSDialog", "10"))
        self.C11Label.setText(_translate("BMSDialog", "11"))
        self.C12Label.setText(_translate("BMSDialog", "12"))
        self.C13Label.setText(_translate("BMSDialog", "13"))
        self.C14Label.setText(_translate("BMSDialog", "14"))
        self.C16Label.setText(_translate("BMSDialog", "16"))
        self.C17Label.setText(_translate("BMSDialog", "17"))
        self.C18Label.setText(_translate("BMSDialog", "18"))
        self.C19Label.setText(_translate("BMSDialog", "19"))
        self.C20Label.setText(_translate("BMSDialog", "20"))
        self.C21Label.setText(_translate("BMSDialog", "21"))
        self.C9Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C10Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C11Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C12Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C13Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C14Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C16Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C17Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C18Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C19Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C20Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.C21Bar.setFormat(_translate("BMSDialog", "%vmV"))
        self.ExitBtn_2.setText(_translate("BMSDialog", "Config"))
import ampy_rc
