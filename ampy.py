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
        MainWindow.resize(1876, 1383)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background: solid white; }\n"
"\n"
"QGroupBox{\n"
"    background: solid white;\n"
"    border: 5px solid black;\n"
"    border-radius: 20px;\n"
"    margin-top: 50px;\n"
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
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.profileGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.profileGroup.setGeometry(QtCore.QRect(10, 1120, 521, 231))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(64)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.profileGroup.setFont(font)
        self.profileGroup.setStyleSheet("QLabel{\n"
"font: 80pt \'Mistral\'}\n"
"QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}")
        self.profileGroup.setFlat(False)
        self.profileGroup.setCheckable(False)
        self.profileGroup.setObjectName("profileGroup")
        self.gridLayoutWidget = QtWidgets.QWidget(self.profileGroup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 80, 501, 141))
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
        font.setFamily("Magneto")
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
        font.setFamily("Magneto")
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
        self.AssistBox.setGeometry(QtCore.QRect(10, 700, 521, 171))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(64)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.AssistBox.setFont(font)
        self.AssistBox.setStyleSheet("QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}\n"
"QLabel{\n"
"    font: 70pt \"Magneto\";\n"
"}\n"
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
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 70, 481, 91))
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
        self.AssistSlider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 80px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 60px\n"
"}\n"
"    ")
        self.AssistSlider.setMaximum(9)
        self.AssistSlider.setPageStep(2)
        self.AssistSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AssistSlider.setInvertedAppearance(False)
        self.AssistSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.AssistSlider.setTickInterval(1)
        self.AssistSlider.setObjectName("AssistSlider")
        self.gridLayout_3.addWidget(self.AssistSlider, 0, 1, 1, 1)
        self.SpeedGauge = AnalogGaugeWidget(self.centralwidget)
        self.SpeedGauge.setGeometry(QtCore.QRect(30, 20, 680, 680))
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
        font.setFamily("Magneto")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SpeedGaugeLabelUnits.setFont(font)
        self.SpeedGaugeLabelUnits.setStyleSheet("QLabel{\n"
"    font: 30pt \"Magneto\";\n"
"}")
        self.SpeedGaugeLabelUnits.setObjectName("SpeedGaugeLabelUnits")
        self.PowerGauge = AnalogGaugeWidget(self.centralwidget)
        self.PowerGauge.setGeometry(QtCore.QRect(1180, 20, 680, 680))
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
        font.setFamily("Magneto")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PowerGaugeLabelUnits.setFont(font)
        self.PowerGaugeLabelUnits.setStyleSheet("QLabel{\n"
"    font: 30pt \"Magneto\";\n"
"}")
        self.PowerGaugeLabelUnits.setObjectName("PowerGaugeLabelUnits")
        self.RangeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.RangeBox.setGeometry(QtCore.QRect(9, 900, 521, 201))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(64)
        self.RangeBox.setFont(font)
        self.RangeBox.setStyleSheet("QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}\n"
"\n"
"QLabel{\n"
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
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 80, 501, 127))
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
        self.RangeSlider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 80px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 60px\n"
"}\n"
"    ")
        self.RangeSlider.setMaximum(50)
        self.RangeSlider.setPageStep(2)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setInvertedAppearance(False)
        self.RangeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.RangeSlider.setTickInterval(1)
        self.RangeSlider.setObjectName("RangeSlider")
        self.gridLayout_4.addWidget(self.RangeSlider, 0, 1, 1, 1)
        self.RangeBtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RangeBtn.setFont(font)
        self.RangeBtn.setText("")
        self.RangeBtn.setIcon(icon)
        self.RangeBtn.setIconSize(QtCore.QSize(100, 100))
        self.RangeBtn.setCheckable(True)
        self.RangeBtn.setAutoExclusive(True)
        self.RangeBtn.setObjectName("RangeBtn")
        self.gridLayout_4.addWidget(self.RangeBtn, 0, 0, 1, 1)
        self.TripBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TripBox.setGeometry(QtCore.QRect(540, 700, 1321, 651))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(100)
        self.TripBox.setFont(font)
        self.TripBox.setStyleSheet("QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: -25 0px 0 0px\n"
"}\n"
"\n"
"QLabel{\n"
"font: 40pt \'Magneto\'}\n"
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
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 130, 1301, 391))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.TripBoxGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.TripBoxGrid.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.TripBoxGrid.setContentsMargins(0, 0, 0, 0)
        self.TripBoxGrid.setObjectName("TripBoxGrid")
        self.Trip_4_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_4_1.setObjectName("Trip_4_1")
        self.TripBoxGrid.addWidget(self.Trip_4_1, 6, 1, 1, 1)
        self.Trip_1_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_2.setObjectName("Trip_1_2")
        self.TripBoxGrid.addWidget(self.Trip_1_2, 0, 3, 1, 1)
        self.Trip_4_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_4_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_4_2_prefix.setObjectName("Trip_4_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_4_2_prefix, 6, 2, 1, 1)
        self.Trip_1_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_1_3_prefix.setObjectName("Trip_1_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_1_3_prefix, 0, 4, 1, 1)
        self.Trip_3_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_3_1_prefix.setObjectName("Trip_3_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_3_1_prefix, 5, 0, 1, 1)
        self.Trip_2_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_2_3_prefix.setObjectName("Trip_2_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_2_3_prefix, 1, 4, 1, 1)
        self.Trip_3_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_1.setObjectName("Trip_3_1")
        self.TripBoxGrid.addWidget(self.Trip_3_1, 5, 1, 1, 1)
        self.Trip_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_1.setObjectName("Trip_2_1")
        self.TripBoxGrid.addWidget(self.Trip_2_1, 1, 1, 1, 1)
        self.Trip_4_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_4_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_4_3_prefix.setObjectName("Trip_4_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_4_3_prefix, 6, 4, 1, 1)
        self.Trip_3_3_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_3_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_3_3_prefix.setObjectName("Trip_3_3_prefix")
        self.TripBoxGrid.addWidget(self.Trip_3_3_prefix, 5, 4, 1, 1)
        self.Trip_1_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_1_1.setFont(font)
        self.Trip_1_1.setObjectName("Trip_1_1")
        self.TripBoxGrid.addWidget(self.Trip_1_1, 0, 1, 1, 1)
        self.Trip_2_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_2_2_prefix.setObjectName("Trip_2_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_2_2_prefix, 1, 2, 1, 1)
        self.Trip_1_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_1_1_prefix.setFont(font)
        self.Trip_1_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_1_1_prefix.setObjectName("Trip_1_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_1_1_prefix, 0, 0, 1, 1)
        self.Trip_1_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_1_2_prefix.setObjectName("Trip_1_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_1_2_prefix, 0, 2, 1, 1)
        self.Trip_4_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_4_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_4_1_prefix.setObjectName("Trip_4_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_4_1_prefix, 6, 0, 1, 1)
        self.Trip_2_1_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_1_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_2_1_prefix.setObjectName("Trip_2_1_prefix")
        self.TripBoxGrid.addWidget(self.Trip_2_1_prefix, 1, 0, 1, 1)
        self.Trip_3_2_prefix = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_2_prefix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Trip_3_2_prefix.setObjectName("Trip_3_2_prefix")
        self.TripBoxGrid.addWidget(self.Trip_3_2_prefix, 5, 2, 1, 1)
        self.Trip_2_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_2.setObjectName("Trip_2_2")
        self.TripBoxGrid.addWidget(self.Trip_2_2, 1, 3, 1, 1)
        self.Trip_4_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_4_2.setObjectName("Trip_4_2")
        self.TripBoxGrid.addWidget(self.Trip_4_2, 6, 3, 1, 1)
        self.Trip_3_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_2.setObjectName("Trip_3_2")
        self.TripBoxGrid.addWidget(self.Trip_3_2, 5, 3, 1, 1)
        self.Trip_1_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_1_3.setObjectName("Trip_1_3")
        self.TripBoxGrid.addWidget(self.Trip_1_3, 0, 5, 1, 1)
        self.Trip_2_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_2_3.setObjectName("Trip_2_3")
        self.TripBoxGrid.addWidget(self.Trip_2_3, 1, 5, 1, 1)
        self.Trip_3_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_3_3.setObjectName("Trip_3_3")
        self.TripBoxGrid.addWidget(self.Trip_3_3, 5, 5, 1, 1)
        self.Trip_4_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.Trip_4_3.setObjectName("Trip_4_3")
        self.TripBoxGrid.addWidget(self.Trip_4_3, 6, 5, 1, 1)
        self.Trip_Selector_1 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_1.setGeometry(QtCore.QRect(690, 20, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_1.setFont(font)
        self.Trip_Selector_1.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impact\";\n"
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
        self.Trip_Selector_1.setChecked(True)
        self.Trip_Selector_1.setAutoExclusive(True)
        self.Trip_Selector_1.setObjectName("Trip_Selector_1")
        self.Trip_Selector_2 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_2.setGeometry(QtCore.QRect(840, 20, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_2.setFont(font)
        self.Trip_Selector_2.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impact\";\n"
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
        self.Trip_Selector_2.setAutoExclusive(True)
        self.Trip_Selector_2.setObjectName("Trip_Selector_2")
        self.Trip_Selector_3 = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_3.setGeometry(QtCore.QRect(990, 20, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_3.setFont(font)
        self.Trip_Selector_3.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"Impact\";\n"
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
        self.Trip_Selector_3.setAutoExclusive(True)
        self.Trip_Selector_3.setObjectName("Trip_Selector_3")
        self.TripReset = QtWidgets.QPushButton(self.TripBox)
        self.TripReset.setGeometry(QtCore.QRect(400, 60, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TripReset.setFont(font)
        self.TripReset.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius:30px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.TripReset.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/root/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TripReset.setIcon(icon1)
        self.TripReset.setIconSize(QtCore.QSize(60, 60))
        self.TripReset.setObjectName("TripReset")
        self.Trip_Selector_Debug = QtWidgets.QPushButton(self.TripBox)
        self.Trip_Selector_Debug.setGeometry(QtCore.QRect(1140, 20, 121, 111))
        font = QtGui.QFont()
        font.setFamily("tt-icon-font")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Trip_Selector_Debug.setFont(font)
        self.Trip_Selector_Debug.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 100px;\n"
"    font-family: \"tt-icon-font\";\n"
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
        self.Trip_Selector_Debug.setCheckable(True)
        self.Trip_Selector_Debug.setChecked(False)
        self.Trip_Selector_Debug.setAutoExclusive(True)
        self.Trip_Selector_Debug.setObjectName("Trip_Selector_Debug")
        self.PID_Kp_Slider = QtWidgets.QSlider(self.TripBox)
        self.PID_Kp_Slider.setGeometry(QtCore.QRect(10, 570, 431, 71))
        self.PID_Kp_Slider.setSizeIncrement(QtCore.QSize(0, 0))
        self.PID_Kp_Slider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.PID_Kp_Slider.setFont(font)
        self.PID_Kp_Slider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 80px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 60px\n"
"}\n"
"    ")
        self.PID_Kp_Slider.setMaximum(200)
        self.PID_Kp_Slider.setPageStep(2)
        self.PID_Kp_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PID_Kp_Slider.setInvertedAppearance(False)
        self.PID_Kp_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PID_Kp_Slider.setTickInterval(1)
        self.PID_Kp_Slider.setObjectName("PID_Kp_Slider")
        self.PID_Ki_Slider = QtWidgets.QSlider(self.TripBox)
        self.PID_Ki_Slider.setGeometry(QtCore.QRect(440, 570, 441, 71))
        self.PID_Ki_Slider.setSizeIncrement(QtCore.QSize(0, 0))
        self.PID_Ki_Slider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.PID_Ki_Slider.setFont(font)
        self.PID_Ki_Slider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 80px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 60px\n"
"}\n"
"    ")
        self.PID_Ki_Slider.setMaximum(200)
        self.PID_Ki_Slider.setPageStep(2)
        self.PID_Ki_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PID_Ki_Slider.setInvertedAppearance(False)
        self.PID_Ki_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PID_Ki_Slider.setTickInterval(1)
        self.PID_Ki_Slider.setObjectName("PID_Ki_Slider")
        self.PID_Kd_Slider = QtWidgets.QSlider(self.TripBox)
        self.PID_Kd_Slider.setGeometry(QtCore.QRect(880, 570, 431, 71))
        self.PID_Kd_Slider.setSizeIncrement(QtCore.QSize(0, 0))
        self.PID_Kd_Slider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.PID_Kd_Slider.setFont(font)
        self.PID_Kd_Slider.setStyleSheet("QSlider {\n"
"    border-style: none;\n"
"    border-color: gray;\n"
"    border-width: 4px;\n"
"    border-radius: 18px;\n"
"    height: 80px\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 4px solid gray;\n"
"    border-radius: 18px;\n"
"    height: 60px\n"
"}\n"
"    ")
        self.PID_Kd_Slider.setMaximum(9)
        self.PID_Kd_Slider.setPageStep(2)
        self.PID_Kd_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PID_Kd_Slider.setInvertedAppearance(False)
        self.PID_Kd_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PID_Kd_Slider.setTickInterval(1)
        self.PID_Kd_Slider.setObjectName("PID_Kd_Slider")
        self.PID_Kp_Label = QtWidgets.QLabel(self.TripBox)
        self.PID_Kp_Label.setGeometry(QtCore.QRect(20, 530, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PID_Kp_Label.setFont(font)
        self.PID_Kp_Label.setStyleSheet("QLabel{\n"
"    font: 30pt \"Magneto\";\n"
"}")
        self.PID_Kp_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.PID_Kp_Label.setObjectName("PID_Kp_Label")
        self.PID_Ki_Label = QtWidgets.QLabel(self.TripBox)
        self.PID_Ki_Label.setGeometry(QtCore.QRect(450, 530, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PID_Ki_Label.setFont(font)
        self.PID_Ki_Label.setStyleSheet("QLabel{\n"
"    font: 30pt \"Magneto\";\n"
"}")
        self.PID_Ki_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.PID_Ki_Label.setObjectName("PID_Ki_Label")
        self.PID_Kd_Label = QtWidgets.QLabel(self.TripBox)
        self.PID_Kd_Label.setGeometry(QtCore.QRect(880, 530, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PID_Kd_Label.setFont(font)
        self.PID_Kd_Label.setStyleSheet("QLabel{\n"
"    font: 30pt \"Magneto\";\n"
"}")
        self.PID_Kd_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.PID_Kd_Label.setObjectName("PID_Kd_Label")
        self.BatteryVoltageBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatteryVoltageBar.setGeometry(QtCore.QRect(700, 490, 491, 51))
        self.BatteryVoltageBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;\n"
"     width: 44px;\n"
"     margin:2px;\n"
" }\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 5px;\n"
"border-radius: 10px\n"
"}")
        self.BatteryVoltageBar.setMinimum(52)
        self.BatteryVoltageBar.setMaximum(89)
        self.BatteryVoltageBar.setProperty("value", 89)
        self.BatteryVoltageBar.setTextVisible(False)
        self.BatteryVoltageBar.setOrientation(QtCore.Qt.Horizontal)
        self.BatteryVoltageBar.setObjectName("BatteryVoltageBar")
        self.BatteryVoltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryVoltageLabel.setGeometry(QtCore.QRect(720, 389, 441, 91))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(58)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BatteryVoltageLabel.setFont(font)
        self.BatteryVoltageLabel.setStyleSheet("QLabel{\n"
"    font: 58pt \"Magneto\";\n"
"}")
        self.BatteryVoltageLabel.setObjectName("BatteryVoltageLabel")
        self.MotorTemperatureBar = QtWidgets.QProgressBar(self.centralwidget)
        self.MotorTemperatureBar.setGeometry(QtCore.QRect(730, 330, 421, 51))
        self.MotorTemperatureBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;\n"
"     width: 37px;\n"
"     margin:2px;\n"
" }\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 5px;\n"
"border-radius: 10px\n"
"}")
        self.MotorTemperatureBar.setMaximum(110)
        self.MotorTemperatureBar.setProperty("value", 110)
        self.MotorTemperatureBar.setTextVisible(False)
        self.MotorTemperatureBar.setOrientation(QtCore.Qt.Horizontal)
        self.MotorTemperatureBar.setObjectName("MotorTemperatureBar")
        self.MotorTemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.MotorTemperatureLabel.setGeometry(QtCore.QRect(730, 230, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(64)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.MotorTemperatureLabel.setFont(font)
        self.MotorTemperatureLabel.setStyleSheet("QLabel{\n"
"    font: 64pt \"Magneto\";\n"
"}")
        self.MotorTemperatureLabel.setObjectName("MotorTemperatureLabel")
        self.BatterySOCBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BatterySOCBar.setGeometry(QtCore.QRect(640, 630, 611, 51))
        self.BatterySOCBar.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: black;\n"
"     width: 56px;\n"
"     margin:2px;\n"
" }\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: gray;\n"
"    border-width: 5px;\n"
"border-radius: 10px\n"
"}")
        self.BatterySOCBar.setMaximum(100)
        self.BatterySOCBar.setProperty("value", 100)
        self.BatterySOCBar.setTextVisible(False)
        self.BatterySOCBar.setOrientation(QtCore.Qt.Horizontal)
        self.BatterySOCBar.setObjectName("BatterySOCBar")
        self.BatterySOCLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatterySOCLabel.setGeometry(QtCore.QRect(670, 550, 551, 81))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(64)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BatterySOCLabel.setFont(font)
        self.BatterySOCLabel.setStyleSheet("QLabel{\n"
"    font: 64pt \"Magneto\";\n"
"}")
        self.BatterySOCLabel.setObjectName("BatterySOCLabel")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(680, 0, 541, 131))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(78)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time.setFont(font)
        self.Time.setStyleSheet("QLabel{\n"
"    font: 78pt \"Magneto\";\n"
"}\n"
"\n"
"# \"Harlow Solid Italic\"")
        self.Time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Time.setObjectName("Time")
        self.LockButton = QtWidgets.QPushButton(self.centralwidget)
        self.LockButton.setGeometry(QtCore.QRect(1050, 110, 101, 111))
        font = QtGui.QFont()
        font.setFamily("tt-icon-font")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LockButton.setFont(font)
        self.LockButton.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 96px;\n"
"    font-family: \"tt-icon-font\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius: 30px\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.LockButton.setIconSize(QtCore.QSize(16, 16))
        self.LockButton.setCheckable(True)
        self.LockButton.setObjectName("LockButton")
        self.CheckEngineButton = QtWidgets.QPushButton(self.centralwidget)
        self.CheckEngineButton.setGeometry(QtCore.QRect(880, 110, 121, 111))
        font = QtGui.QFont()
        font.setFamily("tt-icon-font")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CheckEngineButton.setFont(font)
        self.CheckEngineButton.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 96px;\n"
"    font-family: \"tt-icon-font\";\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.CheckEngineButton.setCheckable(True)
        self.CheckEngineButton.setChecked(False)
        self.CheckEngineButton.setObjectName("CheckEngineButton")
        self.BatterySOCReset = QtWidgets.QPushButton(self.centralwidget)
        self.BatterySOCReset.setGeometry(QtCore.QRect(730, 110, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BatterySOCReset.setFont(font)
        self.BatterySOCReset.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    border-style: inset;\n"
"    border-color: dark grey;\n"
"    border-width: 6px;\n"
"    border-radius:30px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-style:outset;\n"
"\n"
"}")
        self.BatterySOCReset.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/root/icon_charged.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BatterySOCReset.setIcon(icon2)
        self.BatterySOCReset.setIconSize(QtCore.QSize(76, 96))
        self.BatterySOCReset.setObjectName("BatterySOCReset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1876, 21))
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
        self.Trip_4_1.setText(_translate("MainWindow", "4_1"))
        self.Trip_1_2.setText(_translate("MainWindow", "1_2"))
        self.Trip_4_2_prefix.setText(_translate("MainWindow", "4_2"))
        self.Trip_1_3_prefix.setText(_translate("MainWindow", "1_3"))
        self.Trip_3_1_prefix.setText(_translate("MainWindow", "3_1"))
        self.Trip_2_3_prefix.setText(_translate("MainWindow", "2_3"))
        self.Trip_3_1.setText(_translate("MainWindow", "3_1"))
        self.Trip_2_1.setText(_translate("MainWindow", "2_1"))
        self.Trip_4_3_prefix.setText(_translate("MainWindow", "4_3"))
        self.Trip_3_3_prefix.setText(_translate("MainWindow", "3_3"))
        self.Trip_1_1.setText(_translate("MainWindow", "1_1"))
        self.Trip_2_2_prefix.setText(_translate("MainWindow", "2_2"))
        self.Trip_1_1_prefix.setText(_translate("MainWindow", "1_1"))
        self.Trip_1_2_prefix.setText(_translate("MainWindow", "1_2"))
        self.Trip_4_1_prefix.setText(_translate("MainWindow", "4_1"))
        self.Trip_2_1_prefix.setText(_translate("MainWindow", "2_1"))
        self.Trip_3_2_prefix.setText(_translate("MainWindow", "3_2"))
        self.Trip_2_2.setText(_translate("MainWindow", "2_2"))
        self.Trip_4_2.setText(_translate("MainWindow", "4_2"))
        self.Trip_3_2.setText(_translate("MainWindow", "3_2"))
        self.Trip_1_3.setText(_translate("MainWindow", "1_3"))
        self.Trip_2_3.setText(_translate("MainWindow", "2_3"))
        self.Trip_3_3.setText(_translate("MainWindow", "3_3"))
        self.Trip_4_3.setText(_translate("MainWindow", "4_3"))
        self.Trip_Selector_1.setText(_translate("MainWindow", "1"))
        self.Trip_Selector_2.setText(_translate("MainWindow", "2"))
        self.Trip_Selector_3.setText(_translate("MainWindow", "3"))
        self.Trip_Selector_Debug.setText(_translate("MainWindow", "g"))
        self.PID_Kp_Label.setText(_translate("MainWindow", "Kp"))
        self.PID_Ki_Label.setText(_translate("MainWindow", "Ki"))
        self.PID_Kd_Label.setText(_translate("MainWindow", "Kd"))
        self.BatteryVoltageLabel.setText(_translate("MainWindow", "V:"))
        self.MotorTemperatureLabel.setText(_translate("MainWindow", "T"))
        self.BatterySOCLabel.setText(_translate("MainWindow", "SOC:"))
        self.Time.setText(_translate("MainWindow", "12:34:56"))
        self.LockButton.setText(_translate("MainWindow", "<"))
        self.CheckEngineButton.setText(_translate("MainWindow", "W"))
from analoggaugewidget import AnalogGaugeWidget
import ampy_rc
