# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ampy.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1872, 1402)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background: solid white; }\n"
"\n"
"QGroupBox{\n"
"    background: solid white;\n"
"    border: 5px solid black;\n"
"    border-radius: 20px;\n"
"    margin-top: 50px\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 25px;\n"
"    padding: -40 0 0 0\n"
"}\n"
"\n"
"QPushButton { \n"
"    background: white;\n"
"    font: 80px;\n"
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
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: black;\n"
"     width: 1px;\n"
" }")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.profileGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.profileGroup.setGeometry(QtCore.QRect(10, 910, 521, 231))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(80)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.profileGroup.setFont(font)
        self.profileGroup.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}")
        self.profileGroup.setFlat(False)
        self.profileGroup.setCheckable(False)
        self.profileGroup.setObjectName("profileGroup")
        self.gridLayoutWidget = QtWidgets.QWidget(self.profileGroup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 501, 135))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ProfileRb2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ProfileRb2.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProfileRb2.setFont(font)
        self.ProfileRb2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/radio_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/root/radio_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ProfileRb2.setIcon(icon)
        self.ProfileRb2.setIconSize(QtCore.QSize(125, 125))
        self.ProfileRb2.setCheckable(True)
        self.ProfileRb2.setAutoExclusive(True)
        self.ProfileRb2.setObjectName("ProfileRb2")
        self.gridLayout.addWidget(self.ProfileRb2, 0, 1, 1, 1)
        self.ProfileRb1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProfileRb1.setFont(font)
        self.ProfileRb1.setText("")
        self.ProfileRb1.setIcon(icon)
        self.ProfileRb1.setIconSize(QtCore.QSize(125, 125))
        self.ProfileRb1.setCheckable(True)
        self.ProfileRb1.setAutoExclusive(True)
        self.ProfileRb1.setObjectName("ProfileRb1")
        self.gridLayout.addWidget(self.ProfileRb1, 0, 0, 1, 1)
        self.ProfileRb3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProfileRb3.setFont(font)
        self.ProfileRb3.setText("")
        self.ProfileRb3.setIcon(icon)
        self.ProfileRb3.setIconSize(QtCore.QSize(125, 125))
        self.ProfileRb3.setCheckable(True)
        self.ProfileRb3.setAutoExclusive(True)
        self.ProfileRb3.setObjectName("ProfileRb3")
        self.gridLayout.addWidget(self.ProfileRb3, 0, 2, 1, 1)
        self.AssistBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AssistBox.setGeometry(QtCore.QRect(10, 700, 521, 201))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(80)
        self.AssistBox.setFont(font)
        self.AssistBox.setStyleSheet("QLabel{\n"
"font: 80pt \'Arial\'}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid;\n"
"height: 30px; \n"
"margin: 0px;}\n"
"QSlider::handle:horizontal {\n"
"background-color: black;\n"
"border: 5px solid;\n"
"height: 50px;\n"
"width: 70px; \n"
"margin: 0px 0px;}")
        self.AssistBox.setObjectName("AssistBox")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.AssistBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 109, 481, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.AssistSlider = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.AssistSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.AssistSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.AssistSlider.setFont(font)
        self.AssistSlider.setMaximum(9)
        self.AssistSlider.setPageStep(2)
        self.AssistSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AssistSlider.setInvertedAppearance(False)
        self.AssistSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.AssistSlider.setTickInterval(1)
        self.AssistSlider.setObjectName("AssistSlider")
        self.gridLayout_3.addWidget(self.AssistSlider, 0, 1, 1, 1)
        self.SpeedGauge = AnalogGaugeWidget(self.centralwidget)
        self.SpeedGauge.setGeometry(QtCore.QRect(20, 10, 680, 680))
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
        self.SpeedGaugeLabel.setGeometry(QtCore.QRect(190, 420, 301, 221))
        font = QtGui.QFont()
        font.setPointSize(200)
        self.SpeedGaugeLabel.setFont(font)
        self.SpeedGaugeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SpeedGaugeLabel.setObjectName("SpeedGaugeLabel")
        self.SpeedGaugeLabelUnits = QtWidgets.QLabel(self.SpeedGauge)
        self.SpeedGaugeLabelUnits.setGeometry(QtCore.QRect(490, 600, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(40)
        self.SpeedGaugeLabelUnits.setFont(font)
        self.SpeedGaugeLabelUnits.setObjectName("SpeedGaugeLabelUnits")
        self.PowerGauge = AnalogGaugeWidget(self.centralwidget)
        self.PowerGauge.setGeometry(QtCore.QRect(1180, 10, 680, 680))
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
        self.PowerGaugeLabel.setGeometry(QtCore.QRect(90, 520, 441, 161))
        font = QtGui.QFont()
        font.setPointSize(130)
        self.PowerGaugeLabel.setFont(font)
        self.PowerGaugeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PowerGaugeLabel.setObjectName("PowerGaugeLabel")
        self.PowerGaugeLabelUnits = QtWidgets.QLabel(self.PowerGauge)
        self.PowerGaugeLabelUnits.setGeometry(QtCore.QRect(530, 620, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.PowerGaugeLabelUnits.setFont(font)
        self.PowerGaugeLabelUnits.setObjectName("PowerGaugeLabelUnits")
        self.RangeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.RangeBox.setGeometry(QtCore.QRect(9, 1150, 521, 201))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(80)
        self.RangeBox.setFont(font)
        self.RangeBox.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}\n"
"QCheckBox::indicator {\n"
"     width: 60px;\n"
"     height: 60px;\n"
" }\n"
"QCheckbox::indicator:checked{image: url(:/root/radio_on.png);}\n"
"QCheckbox::indicator:checked{image: url(:/root/radio_off.png);}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid;\n"
"height: 30px; \n"
"margin: 0px;}\n"
"QSlider::handle:horizontal {\n"
"background-color: black;\n"
"border: 5px solid;\n"
"height: 100px;\n"
"width: 70px; \n"
"margin: 0px 0px;}")
        self.RangeBox.setObjectName("RangeBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.RangeBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 100, 501, 81))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.RangeSlider = QtWidgets.QSlider(self.gridLayoutWidget_4)
        self.RangeSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.RangeSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.RangeSlider.setFont(font)
        self.RangeSlider.setMaximum(50)
        self.RangeSlider.setPageStep(2)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setInvertedAppearance(False)
        self.RangeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.RangeSlider.setTickInterval(1)
        self.RangeSlider.setObjectName("RangeSlider")
        self.gridLayout_4.addWidget(self.RangeSlider, 0, 1, 1, 1)
        self.RangeCheck = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.RangeCheck.setEnabled(True)
        self.RangeCheck.setText("")
        self.RangeCheck.setIconSize(QtCore.QSize(16, 13))
        self.RangeCheck.setObjectName("RangeCheck")
        self.gridLayout_4.addWidget(self.RangeCheck, 0, 0, 1, 1)
        self.TripBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TripBox.setGeometry(QtCore.QRect(540, 700, 1321, 651))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(100)
        self.TripBox.setFont(font)
        self.TripBox.setStyleSheet("QLabel{\n"
"font: 40pt \'Arial\'}\n"
"QCheckBox::indicator {\n"
"     width: 60px;\n"
"     height: 60px;\n"
" }\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid;\n"
"height: 30px; \n"
"margin: 0px;}\n"
"QSlider::handle:horizontal {\n"
"background-color: black;\n"
"border: 5px solid;\n"
"height: 100px;\n"
"width: 70px; \n"
"margin: 0px 0px;}")
        self.TripBox.setObjectName("TripBox")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.TripBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 130, 1301, 511))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.TripBoxGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.TripBoxGrid.setContentsMargins(0, 0, 0, 0)
        self.TripBoxGrid.setObjectName("TripBoxGrid")
        self.Trip_1_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_2.setObjectName("Trip_1_2")
        self.TripBoxGrid.addWidget(self.Trip_1_2, 0, 1, 1, 1)
        self.Trip_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_1_1.setFont(font)
        self.Trip_1_1.setObjectName("Trip_1_1")
        self.TripBoxGrid.addWidget(self.Trip_1_1, 0, 0, 1, 1)
        self.Trip_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_1.setObjectName("Trip_2_1")
        self.TripBoxGrid.addWidget(self.Trip_2_1, 1, 0, 1, 1)
        self.Trip_2_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_3.setObjectName("Trip_2_3")
        self.TripBoxGrid.addWidget(self.Trip_2_3, 5, 1, 1, 1)
        self.Trip_1_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_4.setObjectName("Trip_1_4")
        self.TripBoxGrid.addWidget(self.Trip_1_4, 6, 0, 1, 1)
        self.Trip_2_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_2.setObjectName("Trip_2_2")
        self.TripBoxGrid.addWidget(self.Trip_2_2, 1, 1, 1, 1)
        self.Trip_2_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_4.setObjectName("Trip_2_4")
        self.TripBoxGrid.addWidget(self.Trip_2_4, 6, 1, 1, 1)
        self.Trip_1_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_3.setObjectName("Trip_1_3")
        self.TripBoxGrid.addWidget(self.Trip_1_3, 5, 0, 1, 1)
        self.Trip_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_1.setObjectName("Trip_3_1")
        self.TripBoxGrid.addWidget(self.Trip_3_1, 0, 2, 1, 1)
        self.Trip_3_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_2.setObjectName("Trip_3_2")
        self.TripBoxGrid.addWidget(self.Trip_3_2, 1, 2, 1, 1)
        self.Trip_3_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_3.setObjectName("Trip_3_3")
        self.TripBoxGrid.addWidget(self.Trip_3_3, 5, 2, 1, 1)
        self.Trip_3_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_4.setObjectName("Trip_3_4")
        self.TripBoxGrid.addWidget(self.Trip_3_4, 6, 2, 1, 1)
        self.TripReset = QtWidgets.QPushButton(self.TripBox)
        self.TripReset.setGeometry(QtCore.QRect(910, 30, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TripReset.setFont(font)
        self.TripReset.setStyleSheet("")
        self.TripReset.setIconSize(QtCore.QSize(12, 16))
        self.TripReset.setObjectName("TripReset")
        self.Trip_Selector_1 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_1.setGeometry(QtCore.QRect(290, 10, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impactt")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_1.setFont(font)
        self.Trip_Selector_1.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impactt\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_1.setCheckable(True)
        self.Trip_Selector_1.setChecked(False)
        self.Trip_Selector_1.setObjectName("Trip_Selector_1")
        self.Trip_Selector_2 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_2.setGeometry(QtCore.QRect(440, 10, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impactt")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_2.setFont(font)
        self.Trip_Selector_2.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impactt\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_2.setCheckable(True)
        self.Trip_Selector_2.setChecked(False)
        self.Trip_Selector_2.setObjectName("Trip_Selector_2")
        self.Trip_Selector_3 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_3.setGeometry(QtCore.QRect(590, 10, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impactt")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_3.setFont(font)
        self.Trip_Selector_3.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impactt\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_3.setCheckable(True)
        self.Trip_Selector_3.setChecked(False)
        self.Trip_Selector_3.setObjectName("Trip_Selector_3")
        self.Trip_Selector_4 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_4.setGeometry(QtCore.QRect(740, 10, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impactt")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_4.setFont(font)
        self.Trip_Selector_4.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impactt\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.Trip_Selector_4.setCheckable(True)
        self.Trip_Selector_4.setChecked(False)
        self.Trip_Selector_4.setObjectName("Trip_Selector_4")
        self.FaultReset = QtWidgets.QPushButton(self.centralwidget)
        self.FaultReset.setGeometry(QtCore.QRect(1020, 550, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FaultReset.setFont(font)
        self.FaultReset.setIconSize(QtCore.QSize(12, 16))
        self.FaultReset.setObjectName("FaultReset")
        self.ProfileRb1Label = QtWidgets.QLabel(self.centralwidget)
        self.ProfileRb1Label.setGeometry(QtCore.QRect(80, 1000, 41, 127))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(80)
        self.ProfileRb1Label.setFont(font)
        self.ProfileRb1Label.setObjectName("ProfileRb1Label")
        self.ProfileRb2Label = QtWidgets.QLabel(self.centralwidget)
        self.ProfileRb2Label.setGeometry(QtCore.QRect(250, 1000, 43, 127))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(80)
        self.ProfileRb2Label.setFont(font)
        self.ProfileRb2Label.setObjectName("ProfileRb2Label")
        self.ProfileRb3Label = QtWidgets.QLabel(self.centralwidget)
        self.ProfileRb3Label.setGeometry(QtCore.QRect(420, 1000, 41, 127))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(80)
        self.ProfileRb3Label.setFont(font)
        self.ProfileRb3Label.setObjectName("ProfileRb3Label")
        self.BatteryVoltageBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatteryVoltageBar.setGeometry(QtCore.QRect(720, 490, 441, 51))
        self.BatteryVoltageBar.setMinimum(52)
        self.BatteryVoltageBar.setMaximum(89)
        self.BatteryVoltageBar.setProperty("value", 52)
        self.BatteryVoltageBar.setTextVisible(False)
        self.BatteryVoltageBar.setOrientation(QtCore.Qt.Horizontal)
        self.BatteryVoltageBar.setObjectName("BatteryVoltageBar")
        self.BatteryVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryVoltageLabel.setGeometry(QtCore.QRect(720, 410, 211, 80))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BatteryVoltageLabel.setFont(font)
        self.BatteryVoltageLabel.setStyleSheet("QLabel{\n"
"    font: 50pt \"Impact\";\n"
"}")
        self.BatteryVoltageLabel.setObjectName("BatteryVoltageLabel")
        self.MotorTemperatureBar = QtWidgets.QProgressBar(self.centralwidget)
        self.MotorTemperatureBar.setGeometry(QtCore.QRect(720, 360, 441, 51))
        self.MotorTemperatureBar.setMaximum(110)
        self.MotorTemperatureBar.setProperty("value", 75)
        self.MotorTemperatureBar.setTextVisible(False)
        self.MotorTemperatureBar.setOrientation(QtCore.Qt.Horizontal)
        self.MotorTemperatureBar.setObjectName("MotorTemperatureBar")
        self.MotorTemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.MotorTemperatureLabel.setGeometry(QtCore.QRect(720, 280, 421, 80))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.MotorTemperatureLabel.setFont(font)
        self.MotorTemperatureLabel.setStyleSheet("QLabel{\n"
"    font: 50pt \"Impact\";\n"
"}")
        self.MotorTemperatureLabel.setObjectName("MotorTemperatureLabel")
        self.BatterySOCBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatterySOCBar.setGeometry(QtCore.QRect(720, 630, 441, 51))
        self.BatterySOCBar.setMaximum(100)
        self.BatterySOCBar.setProperty("value", 75)
        self.BatterySOCBar.setTextVisible(False)
        self.BatterySOCBar.setOrientation(QtCore.Qt.Horizontal)
        self.BatterySOCBar.setObjectName("BatterySOCBar")
        self.BatterySOCLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatterySOCLabel.setGeometry(QtCore.QRect(720, 550, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BatterySOCLabel.setFont(font)
        self.BatterySOCLabel.setStyleSheet("QLabel{\n"
"    font: 50pt \"Impact\";\n"
"}")
        self.BatterySOCLabel.setObjectName("BatterySOCLabel")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(720, 10, 451, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time.setFont(font)
        self.Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Time.setObjectName("Time")
        self.LockButton = QtWidgets.QPushButton(self.centralwidget)
        self.LockButton.setGeometry(QtCore.QRect(1060, 160, 101, 111))
        font = QtGui.QFont()
        font.setFamily("tt-icon-font")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LockButton.setFont(font)
        self.LockButton.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 120px;\n"
"    font-family: \"tt-icon-font\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.LockButton.setIconSize(QtCore.QSize(16, 16))
        self.LockButton.setCheckable(True)
        self.LockButton.setObjectName("LockButton")
        self.BatteryVoltageDropLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryVoltageDropLabel.setGeometry(QtCore.QRect(940, 410, 221, 80))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BatteryVoltageDropLabel.setFont(font)
        self.BatteryVoltageDropLabel.setStyleSheet("QLabel{\n"
"    font: 50pt \"Impact\";\n"
"}")
        self.BatteryVoltageDropLabel.setObjectName("BatteryVoltageDropLabel")
        self.CheckEngineButton = QtWidgets.QPushButton(self.centralwidget)
        self.CheckEngineButton.setGeometry(QtCore.QRect(720, 160, 121, 111))
        font = QtGui.QFont()
        font.setFamily("tt-icon-font")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CheckEngineButton.setFont(font)
        self.CheckEngineButton.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 120px;\n"
"    font-family: \"tt-icon-font\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.CheckEngineButton.setCheckable(True)
        self.CheckEngineButton.setChecked(False)
        self.CheckEngineButton.setObjectName("CheckEngineButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1872, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profileGroup.setTitle(_translate("MainWindow", "Profiles"))
        self.AssistBox.setTitle(_translate("MainWindow", "Assist: #"))
        self.SpeedGaugeLabel.setText(_translate("MainWindow", "88"))
        self.SpeedGaugeLabelUnits.setText(_translate("MainWindow", "mph"))
        self.PowerGaugeLabel.setText(_translate("MainWindow", "24.00"))
        self.PowerGaugeLabelUnits.setText(_translate("MainWindow", "kW"))
        self.RangeBox.setTitle(_translate("MainWindow", "Range: #"))
        self.TripBox.setTitle(_translate("MainWindow", "Trip"))
        self.Trip_1_2.setText(_translate("MainWindow", "Trip Regen"))
        self.Trip_1_1.setText(_translate("MainWindow", "Trip Distance"))
        self.Trip_2_1.setText(_translate("MainWindow", "Trip Wh/mi"))
        self.Trip_2_3.setText(_translate("MainWindow", "Estimated Range "))
        self.Trip_1_4.setText(_translate("MainWindow", "Estimated Range "))
        self.Trip_2_2.setText(_translate("MainWindow", "Instant Wh/mi"))
        self.Trip_2_4.setText(_translate("MainWindow", "Estimated Range "))
        self.Trip_1_3.setText(_translate("MainWindow", "Estimated Range "))
        self.Trip_3_1.setText(_translate("MainWindow", "Trip Regen"))
        self.Trip_3_2.setText(_translate("MainWindow", "Trip Regen"))
        self.Trip_3_3.setText(_translate("MainWindow", "Trip Regen"))
        self.Trip_3_4.setText(_translate("MainWindow", "Trip Regen"))
        self.TripReset.setText(_translate("MainWindow", "RST"))
        self.Trip_Selector_1.setText(_translate("MainWindow", "1"))
        self.Trip_Selector_2.setText(_translate("MainWindow", "2"))
        self.Trip_Selector_3.setText(_translate("MainWindow", "3"))
        self.Trip_Selector_4.setText(_translate("MainWindow", "4"))
        self.FaultReset.setText(_translate("MainWindow", "RST"))
        self.ProfileRb1Label.setText(_translate("MainWindow", "123"))
        self.ProfileRb2Label.setText(_translate("MainWindow", "2"))
        self.ProfileRb3Label.setText(_translate("MainWindow", "3"))
        self.BatteryVoltageLabel.setText(_translate("MainWindow", "V: 88.2"))
        self.MotorTemperatureLabel.setText(_translate("MainWindow", "MotTemp"))
        self.BatterySOCLabel.setText(_translate("MainWindow", "SOC:"))
        self.Time.setText(_translate("MainWindow", "Time of day"))
        self.LockButton.setText(_translate("MainWindow", "<"))
        self.BatteryVoltageDropLabel.setText(_translate("MainWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">d</span>: -8.5</p></body></html>"))
        self.CheckEngineButton.setText(_translate("MainWindow", "W"))
from analoggaugewidget import AnalogGaugeWidget
import ampy_rc
