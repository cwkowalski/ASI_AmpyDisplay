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
        MainWindow.resize(1872, 1404)
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
" }")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.profileGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.profileGroup.setGeometry(QtCore.QRect(10, 950, 521, 401))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(100)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.profileGroup.setFont(font)
        self.profileGroup.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}")
        self.profileGroup.setFlat(False)
        self.profileGroup.setCheckable(False)
        self.profileGroup.setObjectName("profileGroup")
        self.gridLayoutWidget = QtWidgets.QWidget(self.profileGroup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 120, 501, 274))
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
        self.gridLayout.addWidget(self.ProfileRb2, 1, 1, 1, 1)
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
        self.gridLayout.addWidget(self.ProfileRb1, 1, 0, 1, 1)
        self.ProfileRb1Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ProfileRb1Label.setObjectName("ProfileRb1Label")
        self.gridLayout.addWidget(self.ProfileRb1Label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ProfileRb3Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ProfileRb3Label.setObjectName("ProfileRb3Label")
        self.gridLayout.addWidget(self.ProfileRb3Label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
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
        self.gridLayout.addWidget(self.ProfileRb3, 1, 2, 1, 1)
        self.ProfileRb2Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ProfileRb2Label.setObjectName("ProfileRb2Label")
        self.gridLayout.addWidget(self.ProfileRb2Label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.AssistBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AssistBox.setGeometry(QtCore.QRect(10, 729, 521, 201))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(100)
        self.AssistBox.setFont(font)
        self.AssistBox.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}\n"
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
        self.SpeedGauge.setGeometry(QtCore.QRect(600, 10, 680, 680))
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
        font.setPointSize(40)
        self.SpeedGaugeLabelUnits.setFont(font)
        self.SpeedGaugeLabelUnits.setObjectName("SpeedGaugeLabelUnits")
        self.PowerGauge = AnalogGaugeWidget(self.centralwidget)
        self.PowerGauge.setGeometry(QtCore.QRect(600, 670, 680, 680))
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
        self.label = QtWidgets.QLabel(self.PowerGauge)
        self.label.setGeometry(QtCore.QRect(530, 620, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.RangeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.RangeBox.setGeometry(QtCore.QRect(1340, 1130, 520, 221))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(100)
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
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 120, 501, 91))
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
        self.RangeBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.RangeBox_2.setGeometry(QtCore.QRect(1340, 10, 520, 1111))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(100)
        self.RangeBox_2.setFont(font)
        self.RangeBox_2.setStyleSheet("QLabel{\n"
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
        self.RangeBox_2.setObjectName("RangeBox_2")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.RangeBox_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(9, 139, 1121, 961))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 10, 0, 1, 1)
        self.TripDistance = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.TripDistance.setObjectName("TripDistance")
        self.gridLayout_6.addWidget(self.TripDistance, 2, 0, 1, 1)
        self.EstRange = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.EstRange.setObjectName("EstRange")
        self.gridLayout_6.addWidget(self.EstRange, 8, 0, 1, 1)
        self.WhmiInstantaneous = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.WhmiInstantaneous.setObjectName("WhmiInstantaneous")
        self.gridLayout_6.addWidget(self.WhmiInstantaneous, 0, 0, 1, 1)
        self.TripRegen = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.TripRegen.setObjectName("TripRegen")
        self.gridLayout_6.addWidget(self.TripRegen, 9, 0, 1, 1)
        self.WhmiTrip = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.WhmiTrip.setObjectName("WhmiTrip")
        self.gridLayout_6.addWidget(self.WhmiTrip, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.RangeBox_2)
        self.pushButton.setGeometry(QtCore.QRect(260, 60, 241, 71))
        self.pushButton.setObjectName("pushButton")
        self.StatusGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.StatusGroupBox.setGeometry(QtCore.QRect(10, 10, 521, 711))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(100)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.StatusGroupBox.setFont(font)
        self.StatusGroupBox.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}")
        self.StatusGroupBox.setTitle("")
        self.StatusGroupBox.setFlat(False)
        self.StatusGroupBox.setCheckable(False)
        self.StatusGroupBox.setObjectName("StatusGroupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.StatusGroupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 501, 641))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.VoltageDrop = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.VoltageDrop.setObjectName("VoltageDrop")
        self.gridLayout_2.addWidget(self.VoltageDrop, 2, 0, 1, 1)
        self.BatterySOC = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.BatterySOC.setObjectName("BatterySOC")
        self.gridLayout_2.addWidget(self.BatterySOC, 1, 0, 1, 1)
        self.Time = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(80)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.gridLayout_2.addWidget(self.Time, 0, 0, 1, 1)
        self.FaultCodes = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(80)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FaultCodes.setFont(font)
        self.FaultCodes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FaultCodes.setTextFormat(QtCore.Qt.PlainText)
        self.FaultCodes.setObjectName("FaultCodes")
        self.gridLayout_2.addWidget(self.FaultCodes, 3, 0, 1, 1)
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
        self.ProfileRb1Label.setText(_translate("MainWindow", "1"))
        self.ProfileRb3Label.setText(_translate("MainWindow", "3"))
        self.ProfileRb2Label.setText(_translate("MainWindow", "2"))
        self.AssistBox.setTitle(_translate("MainWindow", "Assist: #"))
        self.SpeedGaugeLabel.setText(_translate("MainWindow", "88"))
        self.SpeedGaugeLabelUnits.setText(_translate("MainWindow", "mph"))
        self.PowerGaugeLabel.setText(_translate("MainWindow", "24.00"))
        self.label.setText(_translate("MainWindow", "kW"))
        self.RangeBox.setTitle(_translate("MainWindow", "Range: #"))
        self.RangeBox_2.setTitle(_translate("MainWindow", "Trip"))
        self.TripDistance.setText(_translate("MainWindow", "Trip Distance"))
        self.EstRange.setText(_translate("MainWindow", "Estimated Range (Trip Wh/mi & SOC)"))
        self.WhmiInstantaneous.setText(_translate("MainWindow", "Instantaneous Wh/mi"))
        self.TripRegen.setText(_translate("MainWindow", "Trip %Regen (wh / negative wh"))
        self.WhmiTrip.setText(_translate("MainWindow", "Trip Wh/mi"))
        self.pushButton.setText(_translate("MainWindow", "RESET"))
        self.VoltageDrop.setText(_translate("MainWindow", "Voltage Drop "))
        self.BatterySOC.setText(_translate("MainWindow", "Battery SOC"))
        self.Time.setText(_translate("MainWindow", "Time of day"))
        self.FaultCodes.setText(_translate("MainWindow", "Fault Codes"))
from analoggaugewidget import AnalogGaugeWidget
import ampy_rc
