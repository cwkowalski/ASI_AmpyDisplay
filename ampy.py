# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ampy_800_480.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background: solid white; }\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.SpeedGauge = AnalogGaugeWidget(self.centralwidget)
        self.SpeedGauge.setGeometry(QtCore.QRect(5, 10, 290, 290))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SpeedGauge.sizePolicy().hasHeightForWidth())
        self.SpeedGauge.setSizePolicy(sizePolicy)
        self.SpeedGauge.setMinimumSize(QtCore.QSize(100, 100))
        self.SpeedGauge.setMaximumSize(QtCore.QSize(700, 1000))
        self.SpeedGauge.setBaseSize(QtCore.QSize(300, 300))
        self.SpeedGauge.setStyleSheet("")
        self.SpeedGauge.setObjectName("SpeedGauge")
        self.SpeedGaugeLabel = QtWidgets.QLabel(self.SpeedGauge)
        self.SpeedGaugeLabel.setGeometry(QtCore.QRect(40, 170, 147, 126))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SpeedGaugeLabel.setFont(font)
        self.SpeedGaugeLabel.setStyleSheet("QLabel{\n"
"    font: 70pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.SpeedGaugeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SpeedGaugeLabel.setObjectName("SpeedGaugeLabel")
        self.SpeedGaugeLabelUnits = QtWidgets.QLabel(self.SpeedGauge)
        self.SpeedGaugeLabelUnits.setGeometry(QtCore.QRect(188, 255, 62, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SpeedGaugeLabelUnits.setFont(font)
        self.SpeedGaugeLabelUnits.setStyleSheet("QLabel{\n"
"    font: 16pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    font-style: oblique;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.SpeedGaugeLabelUnits.setObjectName("SpeedGaugeLabelUnits")
        self.PowerGauge = AnalogGaugeWidget(self.centralwidget)
        self.PowerGauge.setGeometry(QtCore.QRect(505, 10, 290, 290))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PowerGauge.sizePolicy().hasHeightForWidth())
        self.PowerGauge.setSizePolicy(sizePolicy)
        self.PowerGauge.setMinimumSize(QtCore.QSize(100, 100))
        self.PowerGauge.setMaximumSize(QtCore.QSize(700, 800))
        self.PowerGauge.setBaseSize(QtCore.QSize(300, 300))
        self.PowerGauge.setStyleSheet("")
        self.PowerGauge.setObjectName("PowerGauge")
        self.PowerGaugeLabel = QtWidgets.QLabel(self.PowerGauge)
        self.PowerGaugeLabel.setGeometry(QtCore.QRect(23, 200, 204, 99))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PowerGaugeLabel.setFont(font)
        self.PowerGaugeLabel.setStyleSheet("QLabel{\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.PowerGaugeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PowerGaugeLabel.setObjectName("PowerGaugeLabel")
        self.PowerGaugeLabelUnits = QtWidgets.QLabel(self.PowerGauge)
        self.PowerGaugeLabelUnits.setGeometry(QtCore.QRect(226, 255, 44, 34))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.PowerGaugeLabelUnits.setFont(font)
        self.PowerGaugeLabelUnits.setStyleSheet("QLabel{\n"
"    font: 16pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    font-style: oblique;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.PowerGaugeLabelUnits.setObjectName("PowerGaugeLabelUnits")
        self.TripBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TripBox.setGeometry(QtCore.QRect(220, 245, 576, 231))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(40)
        self.TripBox.setFont(font)
        self.TripBox.setStyleSheet("QGroupBox{\n"
"    background: solid white;\n"
"    border: 5px solid black;\n"
"    border-radius: 10px;\n"
"    margin-top: 50px;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 25px;\n"
"    padding: -25 0px 0 0px;}\n"
"QLabel{\n"
"    font: 18pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black}\n"
"QCheckBox::indicator {\n"
"     width: 60px;\n"
"     height: 60px; }\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid;\n"
"height: 30px; \n"
"margin: 0px;}\n"
"QSlider::handle:horizontal {\n"
"background-color: black;\n"
"border: 5px solid;\n"
"height: 100px;\n"
"width: 70px; \n"
"margin: 0px 0px;}\n"
"QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;}\n"
"QPushButton::pressed {\n"
"    border-style:outset;}")
        self.TripBox.setTitle("")
        self.TripBox.setObjectName("TripBox")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.TripBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(9, 55, 561, 106))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.TripBoxGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.TripBoxGrid.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.TripBoxGrid.setContentsMargins(0, 0, 0, 0)
        self.TripBoxGrid.setObjectName("TripBoxGrid")
        self.Trip_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_1.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Trip_1_1.setFont(font)
        self.Trip_1_1.setObjectName("Trip_1_1")
        self.TripBoxGrid.addWidget(self.Trip_1_1, 0, 1, 1, 1)
        self.Trip_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_1.setObjectName("Trip_3_1")
        self.TripBoxGrid.addWidget(self.Trip_3_1, 5, 1, 1, 1)
        self.Trip_3_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_1_prefix.setMinimumSize(QtCore.QSize(0, 30))
        self.Trip_3_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_3_1_prefix.setObjectName("Trip_3_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_3_1_prefix, 5, 0, 1, 1)
        self.Trip_2_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_2_3_prefix.setObjectName("Trip_2_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_2_3_prefix, 1, 4, 1, 1)
        self.Trip_2_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_2_2_prefix.setObjectName("Trip_2_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_2_2_prefix, 1, 2, 1, 1)
        self.Trip_3_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_3_2_prefix.setObjectName("Trip_3_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_3_2_prefix, 5, 2, 1, 1)
        self.Trip_1_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_3_prefix.setMinimumSize(QtCore.QSize(80, 0))
        self.Trip_1_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_1_3_prefix.setObjectName("Trip_1_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_1_3_prefix, 0, 4, 1, 1)
        self.Trip_1_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_2_prefix.setMinimumSize(QtCore.QSize(80, 0))
        self.Trip_1_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_1_2_prefix.setObjectName("Trip_1_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_1_2_prefix, 0, 2, 1, 1)
        self.Trip_2_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_1_prefix.setMinimumSize(QtCore.QSize(0, 30))
        self.Trip_2_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_2_1_prefix.setObjectName("Trip_2_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_2_1_prefix, 1, 0, 1, 1)
        self.Trip_1_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_2.setMinimumSize(QtCore.QSize(80, 0))
        self.Trip_1_2.setObjectName("Trip_1_2")
        self.TripBoxGrid.addWidget(self.Trip_1_2, 0, 3, 1, 1)
        self.Trip_3_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_2.setObjectName("Trip_3_2")
        self.TripBoxGrid.addWidget(self.Trip_3_2, 5, 3, 1, 1)
        self.Trip_2_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_2.setObjectName("Trip_2_2")
        self.TripBoxGrid.addWidget(self.Trip_2_2, 1, 3, 1, 1)
        self.Trip_2_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_3.setObjectName("Trip_2_3")
        self.TripBoxGrid.addWidget(self.Trip_2_3, 1, 5, 1, 1)
        self.Trip_3_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_3.setObjectName("Trip_3_3")
        self.TripBoxGrid.addWidget(self.Trip_3_3, 5, 5, 1, 1)
        self.Trip_1_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_3.setMinimumSize(QtCore.QSize(80, 0))
        self.Trip_1_3.setObjectName("Trip_1_3")
        self.TripBoxGrid.addWidget(self.Trip_1_3, 0, 5, 1, 1)
        self.Trip_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_1.setObjectName("Trip_2_1")
        self.TripBoxGrid.addWidget(self.Trip_2_1, 1, 1, 1, 1)
        self.Trip_3_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_3_3_prefix.setObjectName("Trip_3_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_3_3_prefix, 5, 4, 1, 1)
        self.Trip_1_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_1_prefix.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Trip_1_1_prefix.setFont(font)
        self.Trip_1_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_1_1_prefix.setObjectName("Trip_1_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_1_1_prefix, 0, 0, 1, 1)
        self.CheckEngineButton = QtWidgets.QPushButton(self.TripBox)
        self.CheckEngineButton.setGeometry(QtCore.QRect(220, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CheckEngineButton.setFont(font)
        self.CheckEngineButton.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.CheckEngineButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/Warning_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CheckEngineButton.setIcon(icon)
        self.CheckEngineButton.setIconSize(QtCore.QSize(50, 45))
        self.CheckEngineButton.setCheckable(True)
        self.CheckEngineButton.setChecked(False)
        self.CheckEngineButton.setObjectName("CheckEngineButton")
        self.BatterySOCReset = QtWidgets.QPushButton(self.TripBox)
        self.BatterySOCReset.setGeometry(QtCore.QRect(290, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BatterySOCReset.setFont(font)
        self.BatterySOCReset.setStyleSheet("")
        self.BatterySOCReset.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/root/icon_charged.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BatterySOCReset.setIcon(icon1)
        self.BatterySOCReset.setIconSize(QtCore.QSize(55, 55))
        self.BatterySOCReset.setObjectName("BatterySOCReset")
        self.OptionsBtn = QtWidgets.QPushButton(self.TripBox)
        self.OptionsBtn.setGeometry(QtCore.QRect(430, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.OptionsBtn.setFont(font)
        self.OptionsBtn.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.OptionsBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/root/Settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OptionsBtn.setIcon(icon2)
        self.OptionsBtn.setIconSize(QtCore.QSize(55, 55))
        self.OptionsBtn.setCheckable(True)
        self.OptionsBtn.setChecked(False)
        self.OptionsBtn.setAutoExclusive(True)
        self.OptionsBtn.setObjectName("OptionsBtn")
        self.Trip_Selector_1 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_1.setGeometry(QtCore.QRect(10, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Trip_Selector_1.setFont(font)
        self.Trip_Selector_1.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_1.setCheckable(True)
        self.Trip_Selector_1.setChecked(True)
        self.Trip_Selector_1.setAutoExclusive(True)
        self.Trip_Selector_1.setObjectName("Trip_Selector_1")
        self.Trip_Selector_2 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_2.setGeometry(QtCore.QRect(80, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Trip_Selector_2.setFont(font)
        self.Trip_Selector_2.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_2.setCheckable(True)
        self.Trip_Selector_2.setChecked(False)
        self.Trip_Selector_2.setAutoExclusive(True)
        self.Trip_Selector_2.setObjectName("Trip_Selector_2")
        self.TripReset = QtWidgets.QPushButton(self.TripBox)
        self.TripReset.setGeometry(QtCore.QRect(360, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TripReset.setFont(font)
        self.TripReset.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.TripReset.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/root/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TripReset.setIcon(icon3)
        self.TripReset.setIconSize(QtCore.QSize(50, 50))
        self.TripReset.setObjectName("TripReset")
        self.LockButton = QtWidgets.QPushButton(self.TripBox)
        self.LockButton.setGeometry(QtCore.QRect(500, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LockButton.setFont(font)
        self.LockButton.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.LockButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/root/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LockButton.setIcon(icon4)
        self.LockButton.setIconSize(QtCore.QSize(55, 50))
        self.LockButton.setCheckable(False)
        self.LockButton.setObjectName("LockButton")
        self.Trip_Selector_3 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_3.setGeometry(QtCore.QRect(150, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Trip_Selector_3.setFont(font)
        self.Trip_Selector_3.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_3.setCheckable(True)
        self.Trip_Selector_3.setChecked(False)
        self.Trip_Selector_3.setAutoExclusive(True)
        self.Trip_Selector_3.setObjectName("Trip_Selector_3")
        self.Reverse = QtWidgets.QPushButton(self.TripBox)
        self.Reverse.setGeometry(QtCore.QRect(220, 160, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Reverse.setFont(font)
        self.Reverse.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 48pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 4px;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Reverse.setCheckable(True)
        self.Reverse.setChecked(False)
        self.Reverse.setAutoExclusive(False)
        self.Reverse.setObjectName("Reverse")
        self.gridLayoutWidget_5.raise_()
        self.BatterySOCReset.raise_()
        self.OptionsBtn.raise_()
        self.Trip_Selector_1.raise_()
        self.Trip_Selector_2.raise_()
        self.TripReset.raise_()
        self.LockButton.raise_()
        self.Trip_Selector_3.raise_()
        self.Reverse.raise_()
        self.CheckEngineButton.raise_()
        self.BatteryVoltageBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatteryVoltageBar.setGeometry(QtCore.QRect(296, 205, 210, 23))
        self.BatteryVoltageBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;}\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 3px;\n"
"border-radius: 6px\n"
"}")
        self.BatteryVoltageBar.setMinimum(52)
        self.BatteryVoltageBar.setMaximum(89)
        self.BatteryVoltageBar.setProperty("value", 78)
        self.BatteryVoltageBar.setTextVisible(False)
        self.BatteryVoltageBar.setOrientation(QtCore.Qt.Horizontal)
        self.BatteryVoltageBar.setObjectName("BatteryVoltageBar")
        self.BatteryVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryVoltageLabel.setGeometry(QtCore.QRect(302, 168, 126, 36))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BatteryVoltageLabel.setFont(font)
        self.BatteryVoltageLabel.setStyleSheet("QLabel{\n"
"    font: 25pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.BatteryVoltageLabel.setObjectName("BatteryVoltageLabel")
        self.MotorTemperatureBar = QtWidgets.QProgressBar(self.centralwidget)
        self.MotorTemperatureBar.setGeometry(QtCore.QRect(311, 145, 180, 23))
        self.MotorTemperatureBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;}\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 3px;\n"
"border-radius: 6px\n"
"}")
        self.MotorTemperatureBar.setMaximum(120)
        self.MotorTemperatureBar.setProperty("value", 90)
        self.MotorTemperatureBar.setTextVisible(False)
        self.MotorTemperatureBar.setOrientation(QtCore.Qt.Horizontal)
        self.MotorTemperatureBar.setObjectName("MotorTemperatureBar")
        self.MotorTemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.MotorTemperatureLabel.setGeometry(QtCore.QRect(318, 110, 175, 40))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.MotorTemperatureLabel.setFont(font)
        self.MotorTemperatureLabel.setStyleSheet("QLabel{\n"
"    font: 25pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.MotorTemperatureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MotorTemperatureLabel.setObjectName("MotorTemperatureLabel")
        self.BatterySOCBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatterySOCBar.setGeometry(QtCore.QRect(271, 265, 260, 23))
        self.BatterySOCBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;}\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 3px;\n"
"border-radius: 6px\n"
"}")
        self.BatterySOCBar.setMaximum(100)
        self.BatterySOCBar.setProperty("value", 50)
        self.BatterySOCBar.setTextVisible(False)
        self.BatterySOCBar.setOrientation(QtCore.Qt.Horizontal)
        self.BatterySOCBar.setObjectName("BatterySOCBar")
        self.BatterySOCLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatterySOCLabel.setGeometry(QtCore.QRect(273, 234, 260, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BatterySOCLabel.setFont(font)
        self.BatterySOCLabel.setStyleSheet("QLabel{\n"
"    font: 25pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.BatterySOCLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BatterySOCLabel.setObjectName("BatterySOCLabel")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(273, -5, 250, 46))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setStyleSheet("QLabel{\n"
"    font: 36pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Time.setObjectName("Time")
        self.MotorTemperatureLine = QtWidgets.QFrame(self.centralwidget)
        self.MotorTemperatureLine.setGeometry(QtCore.QRect(433, 165, 20, 8))
        self.MotorTemperatureLine.setStyleSheet("QObject{color:black}")
        self.MotorTemperatureLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MotorTemperatureLine.setLineWidth(3)
        self.MotorTemperatureLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.MotorTemperatureLine.setObjectName("MotorTemperatureLine")
        self.AssistSlider = QtWidgets.QSlider(self.centralwidget)
        self.AssistSlider.setGeometry(QtCore.QRect(10, 340, 200, 36))
        self.AssistSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.AssistSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.AssistSlider.setFont(font)
        self.AssistSlider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 80px\n"
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
        self.AssistSlider.setMaximum(9)
        self.AssistSlider.setPageStep(2)
        self.AssistSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AssistSlider.setInvertedAppearance(False)
        self.AssistSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.AssistSlider.setTickInterval(1)
        self.AssistSlider.setObjectName("AssistSlider")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 409, 211, 65))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ProfileRb2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ProfileRb2.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProfileRb2.setFont(font)
        self.ProfileRb2.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}\n"
"QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}\n"
"\n"
"\n"
"QPushButton { \n"
"    background: white;\n"
"    font: 80px \"Magneto\";\n"
"    border : none}\n"
"\n"
"QRadioButton {\n"
"    border: 20;\n"
"    padding: 10px;\n"
"    background: white;\n"
"    selectionbackgroundcolor: dark grey;\n"
"    font: 50px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"border : 5px solid black; \n"
"width : 25px;\n"
"height : 50px; \n"
"border radius : 1px}\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 60px;\n"
"     height: 60px;\n"
" }")
        self.ProfileRb2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/root/radio_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/root/radio_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ProfileRb2.setIcon(icon5)
        self.ProfileRb2.setIconSize(QtCore.QSize(55, 55))
        self.ProfileRb2.setCheckable(True)
        self.ProfileRb2.setAutoExclusive(True)
        self.ProfileRb2.setObjectName("ProfileRb2")
        self.gridLayout.addWidget(self.ProfileRb2, 0, 1, 1, 1)
        self.ProfileRb1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProfileRb1.setFont(font)
        self.ProfileRb1.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}\n"
"QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}\n"
"\n"
"\n"
"QPushButton { \n"
"    background: white;\n"
"    font: 80px \"Magneto\";\n"
"    border : none}\n"
"\n"
"QRadioButton {\n"
"    border: 20;\n"
"    padding: 10px;\n"
"    background: white;\n"
"    selectionbackgroundcolor: dark grey;\n"
"    font: 50px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"border : 5px solid black; \n"
"width : 25px;\n"
"height : 50px; \n"
"border radius : 1px}\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 60px;\n"
"     height: 60px;\n"
" }")
        self.ProfileRb1.setText("")
        self.ProfileRb1.setIcon(icon5)
        self.ProfileRb1.setIconSize(QtCore.QSize(55, 55))
        self.ProfileRb1.setCheckable(True)
        self.ProfileRb1.setAutoExclusive(True)
        self.ProfileRb1.setObjectName("ProfileRb1")
        self.gridLayout.addWidget(self.ProfileRb1, 0, 0, 1, 1)
        self.ProfileRb3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProfileRb3.setFont(font)
        self.ProfileRb3.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}\n"
"QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}\n"
"\n"
"\n"
"QPushButton { \n"
"    background: white;\n"
"    font: 80px \"Magneto\";\n"
"    border : none}\n"
"\n"
"QRadioButton {\n"
"    border: 20;\n"
"    padding: 10px;\n"
"    background: white;\n"
"    selectionbackgroundcolor: dark grey;\n"
"    font: 50px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"border : 5px solid black; \n"
"width : 25px;\n"
"height : 50px; \n"
"border radius : 1px}\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 60px;\n"
"     height: 60px;\n"
" }")
        self.ProfileRb3.setText("")
        self.ProfileRb3.setIcon(icon5)
        self.ProfileRb3.setIconSize(QtCore.QSize(55, 55))
        self.ProfileRb3.setCheckable(True)
        self.ProfileRb3.setAutoExclusive(True)
        self.ProfileRb3.setObjectName("ProfileRb3")
        self.gridLayout.addWidget(self.ProfileRb3, 0, 2, 1, 1)
        self.BatteryVoltageDropLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryVoltageDropLabel.setGeometry(QtCore.QRect(430, 175, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BatteryVoltageDropLabel.setFont(font)
        self.BatteryVoltageDropLabel.setStyleSheet("QLabel{\n"
"    font: 16pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.BatteryVoltageDropLabel.setObjectName("BatteryVoltageDropLabel")
        self.BatterySOCLine = QtWidgets.QFrame(self.centralwidget)
        self.BatterySOCLine.setGeometry(QtCore.QRect(390, 285, 20, 8))
        self.BatterySOCLine.setStyleSheet("QObject{color:black}")
        self.BatterySOCLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BatterySOCLine.setLineWidth(3)
        self.BatterySOCLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.BatterySOCLine.setObjectName("BatterySOCLine")
        self.Profile1Label = QtWidgets.QLabel(self.centralwidget)
        self.Profile1Label.setGeometry(QtCore.QRect(6, 385, 66, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Profile1Label.setFont(font)
        self.Profile1Label.setStyleSheet("QLabel{\n"
"    font: 16pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    font-style: oblique;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.Profile1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Profile1Label.setObjectName("Profile1Label")
        self.Profile2Label = QtWidgets.QLabel(self.centralwidget)
        self.Profile2Label.setGeometry(QtCore.QRect(80, 385, 62, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Profile2Label.setFont(font)
        self.Profile2Label.setStyleSheet("QLabel{\n"
"    font: 16pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    font-style: oblique;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.Profile2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Profile2Label.setObjectName("Profile2Label")
        self.Profile3Label = QtWidgets.QLabel(self.centralwidget)
        self.Profile3Label.setGeometry(QtCore.QRect(150, 385, 62, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Profile3Label.setFont(font)
        self.Profile3Label.setStyleSheet("QLabel{\n"
"    font: 16pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    font-style: oblique;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.Profile3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Profile3Label.setObjectName("Profile3Label")
        self.AssistSliderLabel = QtWidgets.QLabel(self.centralwidget)
        self.AssistSliderLabel.setGeometry(QtCore.QRect(15, 305, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AssistSliderLabel.setFont(font)
        self.AssistSliderLabel.setStyleSheet("QLabel{\n"
"    font: 25pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    font-style: oblique;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.AssistSliderLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AssistSliderLabel.setObjectName("AssistSliderLabel")
        self.WhmiBar = QtWidgets.QProgressBar(self.centralwidget)
        self.WhmiBar.setGeometry(QtCore.QRect(310, 90, 180, 23))
        self.WhmiBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;}\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 3px;\n"
"border-radius: 6px\n"
"}")
        self.WhmiBar.setMaximum(100)
        self.WhmiBar.setProperty("value", 50)
        self.WhmiBar.setTextVisible(False)
        self.WhmiBar.setOrientation(QtCore.Qt.Horizontal)
        self.WhmiBar.setObjectName("WhmiBar")
        self.WhmiLabel = QtWidgets.QLabel(self.centralwidget)
        self.WhmiLabel.setGeometry(QtCore.QRect(310, 50, 175, 40))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.WhmiLabel.setFont(font)
        self.WhmiLabel.setStyleSheet("QLabel{\n"
"    font: 25pt \"Luxi Mono\";\n"
"    font-weight: bold;\n"
"    color: black\n"
"}\n"
"\n"
"")
        self.WhmiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WhmiLabel.setObjectName("WhmiLabel")
        self.BatteryVoltageLine = QtWidgets.QFrame(self.centralwidget)
        self.BatteryVoltageLine.setGeometry(QtCore.QRect(430, 225, 20, 8))
        self.BatteryVoltageLine.setStyleSheet("QObject{color:black}")
        self.BatteryVoltageLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BatteryVoltageLine.setLineWidth(3)
        self.BatteryVoltageLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.BatteryVoltageLine.setObjectName("BatteryVoltageLine")
        self.BatteryVoltageLine.raise_()
        self.MotorTemperatureLine.raise_()
        self.BatterySOCLine.raise_()
        self.BatterySOCLabel.raise_()
        self.BatteryVoltageDropLabel.raise_()
        self.BatteryVoltageLabel.raise_()
        self.WhmiLabel.raise_()
        self.MotorTemperatureLabel.raise_()
        self.SpeedGauge.raise_()
        self.PowerGauge.raise_()
        self.TripBox.raise_()
        self.BatteryVoltageBar.raise_()
        self.MotorTemperatureBar.raise_()
        self.BatterySOCBar.raise_()
        self.Time.raise_()
        self.AssistSlider.raise_()
        self.gridLayoutWidget.raise_()
        self.Profile1Label.raise_()
        self.Profile2Label.raise_()
        self.Profile3Label.raise_()
        self.AssistSliderLabel.raise_()
        self.WhmiBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SpeedGaugeLabel.setText(_translate("MainWindow", "66"))
        self.SpeedGaugeLabelUnits.setText(_translate("MainWindow", "mph"))
        self.PowerGaugeLabel.setText(_translate("MainWindow", "24.00"))
        self.PowerGaugeLabelUnits.setText(_translate("MainWindow", "kW"))
        self.Trip_1_1.setText(_translate("MainWindow", "1_1"))
        self.Trip_3_1.setText(_translate("MainWindow", "3_1"))
        self.Trip_3_1_prefix.setText(_translate("MainWindow", "3_1"))
        self.Trip_2_3_prefix.setText(_translate("MainWindow", "2_3"))
        self.Trip_2_2_prefix.setText(_translate("MainWindow", "2_2"))
        self.Trip_3_2_prefix.setText(_translate("MainWindow", "3_2"))
        self.Trip_1_3_prefix.setText(_translate("MainWindow", "1_3"))
        self.Trip_1_2_prefix.setText(_translate("MainWindow", "1_2"))
        self.Trip_2_1_prefix.setText(_translate("MainWindow", "2_1"))
        self.Trip_1_2.setText(_translate("MainWindow", "1_2"))
        self.Trip_3_2.setText(_translate("MainWindow", "3_2"))
        self.Trip_2_2.setText(_translate("MainWindow", "2_2"))
        self.Trip_2_3.setText(_translate("MainWindow", "2_3"))
        self.Trip_3_3.setText(_translate("MainWindow", "3_3"))
        self.Trip_1_3.setText(_translate("MainWindow", "1_3"))
        self.Trip_2_1.setText(_translate("MainWindow", "2_1"))
        self.Trip_3_3_prefix.setText(_translate("MainWindow", "3_3"))
        self.Trip_1_1_prefix.setText(_translate("MainWindow", "1_1"))
        self.Trip_Selector_1.setText(_translate("MainWindow", "1"))
        self.Trip_Selector_2.setText(_translate("MainWindow", "2"))
        self.Trip_Selector_3.setText(_translate("MainWindow", "3"))
        self.Reverse.setText(_translate("MainWindow", "D"))
        self.BatteryVoltageLabel.setText(_translate("MainWindow", "79.123"))
        self.MotorTemperatureLabel.setText(_translate("MainWindow", "XX°C"))
        self.BatterySOCLabel.setText(_translate("MainWindow", "xx.x% SOC"))
        self.Time.setText(_translate("MainWindow", "12:34:56"))
        self.BatteryVoltageDropLabel.setText(_translate("MainWindow", "-17.1"))
        self.Profile1Label.setText(_translate("MainWindow", "Plaid"))
        self.Profile2Label.setText(_translate("MainWindow", "Mad"))
        self.Profile3Label.setText(_translate("MainWindow", "Eco"))
        self.AssistSliderLabel.setText(_translate("MainWindow", "Assist:"))
        self.WhmiLabel.setText(_translate("MainWindow", "12.3<sub>Wh/mi</sub>"))
from analoggaugewidget import AnalogGaugeWidget
import ampy_rc
