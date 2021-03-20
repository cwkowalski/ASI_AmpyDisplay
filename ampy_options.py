# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ampy_options.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptDialog(object):
    def setupUi(self, OptDialog):
        OptDialog.setObjectName("OptDialog")
        OptDialog.resize(800, 480)
        OptDialog.setStyleSheet("QGroupBox{\n"
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
        self.scrollArea = QtWidgets.QScrollArea(OptDialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.scrollArea.setStyleSheet("QScrollBar{\n"
"background: white;}\n"
"QScrollBar{\n"
"width: 25px;}\n"
"\n"
"QPushButton{\n"
"background: transparent;\n"
"border: none}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -74, 781, 1440))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(781, 1440))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ProgBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ProgBtn.setGeometry(QtCore.QRect(448, 10, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ProgBtn.setFont(font)
        self.ProgBtn.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 30px;\n"
"    font-family: \"Luxi Mono\";\n"
"    font-weight: bold;\n"
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
        self.ProgBtn.setCheckable(True)
        self.ProgBtn.setChecked(False)
        self.ProgBtn.setAutoExclusive(True)
        self.ProgBtn.setObjectName("ProgBtn")
        self.RangeSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.RangeSlider.setEnabled(True)
        self.RangeSlider.setGeometry(QtCore.QRect(390, 280, 370, 45))
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
        self.RangeSlider.setMaximum(200)
        self.RangeSlider.setPageStep(5)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setInvertedAppearance(False)
        self.RangeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.RangeSlider.setTickInterval(1)
        self.RangeSlider.setObjectName("RangeSlider")
        self.DisplayInvertBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.DisplayInvertBtn.setGeometry(QtCore.QRect(2, 60, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DisplayInvertBtn.setFont(font)
        self.DisplayInvertBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/invert-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/root/invert-icon-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.DisplayInvertBtn.setIcon(icon)
        self.DisplayInvertBtn.setIconSize(QtCore.QSize(50, 50))
        self.DisplayInvertBtn.setCheckable(True)
        self.DisplayInvertBtn.setAutoExclusive(False)
        self.DisplayInvertBtn.setObjectName("DisplayInvertBtn")
        self.PID_Kd_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PID_Kd_Label.setGeometry(QtCore.QRect(2, 735, 250, 40))
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
        self.BattPowerBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.BattPowerBtn.setGeometry(QtCore.QRect(2, 130, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BattPowerBtn.setFont(font)
        self.BattPowerBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/root/radio_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/root/radio_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BattPowerBtn.setIcon(icon1)
        self.BattPowerBtn.setIconSize(QtCore.QSize(50, 50))
        self.BattPowerBtn.setCheckable(True)
        self.BattPowerBtn.setAutoExclusive(False)
        self.BattPowerBtn.setObjectName("BattPowerBtn")
        self.PID_Kd_Slider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.PID_Kd_Slider.setGeometry(QtCore.QRect(2, 775, 250, 40))
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
        self.PID_Kd_Slider.setMaximum(9)
        self.PID_Kd_Slider.setPageStep(2)
        self.PID_Kd_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PID_Kd_Slider.setInvertedAppearance(False)
        self.PID_Kd_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PID_Kd_Slider.setTickInterval(1)
        self.PID_Kd_Slider.setObjectName("PID_Kd_Slider")
        self.PID_Ki_Slider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.PID_Ki_Slider.setGeometry(QtCore.QRect(255, 775, 250, 40))
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
        self.PID_Ki_Slider.setMaximum(200)
        self.PID_Ki_Slider.setPageStep(2)
        self.PID_Ki_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PID_Ki_Slider.setInvertedAppearance(False)
        self.PID_Ki_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PID_Ki_Slider.setTickInterval(1)
        self.PID_Ki_Slider.setObjectName("PID_Ki_Slider")
        self.BattPowerLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.BattPowerLabel.setGeometry(QtCore.QRect(72, 130, 319, 65))
        self.BattPowerLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.BattPowerLabel.setObjectName("BattPowerLabel")
        self.BacklightLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.BacklightLabel.setGeometry(QtCore.QRect(71, 60, 316, 65))
        self.BacklightLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.BacklightLabel.setObjectName("BacklightLabel")
        self.RangeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.RangeLabel.setGeometry(QtCore.QRect(72, 270, 317, 65))
        self.RangeLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.RangeLabel.setObjectName("RangeLabel")
        self.BattPowerSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.BattPowerSlider.setGeometry(QtCore.QRect(390, 140, 370, 45))
        self.BattPowerSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.BattPowerSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.BattPowerSlider.setFont(font)
        self.BattPowerSlider.setStyleSheet("QSlider {\n"
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
        self.BattPowerSlider.setMaximum(100)
        self.BattPowerSlider.setPageStep(10)
        self.BattPowerSlider.setProperty("value", 100)
        self.BattPowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BattPowerSlider.setInvertedAppearance(False)
        self.BattPowerSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.BattPowerSlider.setTickInterval(1)
        self.BattPowerSlider.setObjectName("BattPowerSlider")
        self.PID_Kp_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PID_Kp_Label.setGeometry(QtCore.QRect(510, 735, 250, 40))
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
        self.DisplaySlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.DisplaySlider.setGeometry(QtCore.QRect(390, 70, 370, 45))
        self.DisplaySlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.DisplaySlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.DisplaySlider.setFont(font)
        self.DisplaySlider.setStyleSheet("QSlider {\n"
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
        self.DisplaySlider.setMaximum(100)
        self.DisplaySlider.setPageStep(20)
        self.DisplaySlider.setProperty("value", 100)
        self.DisplaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.DisplaySlider.setInvertedAppearance(False)
        self.DisplaySlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.DisplaySlider.setTickInterval(1)
        self.DisplaySlider.setObjectName("DisplaySlider")
        self.PID_Ki_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PID_Ki_Label.setGeometry(QtCore.QRect(255, 735, 250, 40))
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
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(4, 825, 770, 406))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QLabel{font: 18pt \'Luxi Mono\'}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.DiagnosticsUpdateBtn = QtWidgets.QPushButton(self.groupBox)
        self.DiagnosticsUpdateBtn.setGeometry(QtCore.QRect(190, -5, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DiagnosticsUpdateBtn.setFont(font)
        self.DiagnosticsUpdateBtn.setText("")
        self.DiagnosticsUpdateBtn.setIcon(icon1)
        self.DiagnosticsUpdateBtn.setIconSize(QtCore.QSize(50, 50))
        self.DiagnosticsUpdateBtn.setCheckable(True)
        self.DiagnosticsUpdateBtn.setAutoExclusive(False)
        self.DiagnosticsUpdateBtn.setObjectName("DiagnosticsUpdateBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 60, 750, 340))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PID_Kp_Slider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.PID_Kp_Slider.setGeometry(QtCore.QRect(510, 775, 250, 40))
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
        self.PID_Kp_Slider.setMaximum(200)
        self.PID_Kp_Slider.setPageStep(2)
        self.PID_Kp_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PID_Kp_Slider.setInvertedAppearance(False)
        self.PID_Kp_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PID_Kp_Slider.setTickInterval(1)
        self.PID_Kp_Slider.setObjectName("PID_Kp_Slider")
        self.ExitBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ExitBtn.setGeometry(QtCore.QRect(670, 10, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ExitBtn.setFont(font)
        self.ExitBtn.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 30px;\n"
"    font-family: \"Luxi Mono\";\n"
"    font-weight: bold;\n"
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
        self.ThemeBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ThemeBtn.setGeometry(QtCore.QRect(558, 10, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ThemeBtn.setFont(font)
        self.ThemeBtn.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 30px;\n"
"    font-family: \"Luxi Mono\";\n"
"    font-weight: bold;\n"
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
        self.ThemeBtn.setCheckable(True)
        self.ThemeBtn.setChecked(False)
        self.ThemeBtn.setAutoExclusive(True)
        self.ThemeBtn.setObjectName("ThemeBtn")
        self.RangeBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.RangeBtn.setGeometry(QtCore.QRect(2, 270, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RangeBtn.setFont(font)
        self.RangeBtn.setText("")
        self.RangeBtn.setIcon(icon1)
        self.RangeBtn.setIconSize(QtCore.QSize(50, 50))
        self.RangeBtn.setCheckable(True)
        self.RangeBtn.setAutoExclusive(False)
        self.RangeBtn.setObjectName("RangeBtn")
        self.TripReset = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.TripReset.setGeometry(QtCore.QRect(207, 10, 230, 55))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TripReset.setFont(font)
        self.TripReset.setStyleSheet("QPushButton { \n"
"    background: white;\n"
"    font: 30px;\n"
"    font-family: \"Luxi Mono\";\n"
"    font-weight: bold;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/root/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TripReset.setIcon(icon2)
        self.TripReset.setIconSize(QtCore.QSize(50, 50))
        self.TripReset.setObjectName("TripReset")
        self.FluxLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.FluxLabel.setGeometry(QtCore.QRect(72, 340, 317, 65))
        self.FluxLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.FluxLabel.setObjectName("FluxLabel")
        self.FluxBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.FluxBtn.setGeometry(QtCore.QRect(2, 340, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FluxBtn.setFont(font)
        self.FluxBtn.setText("")
        self.FluxBtn.setIcon(icon1)
        self.FluxBtn.setIconSize(QtCore.QSize(50, 50))
        self.FluxBtn.setCheckable(True)
        self.FluxBtn.setAutoExclusive(False)
        self.FluxBtn.setObjectName("FluxBtn")
        self.FluxSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.FluxSlider.setEnabled(True)
        self.FluxSlider.setGeometry(QtCore.QRect(390, 350, 370, 45))
        self.FluxSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.FluxSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.FluxSlider.setFont(font)
        self.FluxSlider.setStyleSheet("QSlider {\n"
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
        self.FluxSlider.setMaximum(4096)
        self.FluxSlider.setPageStep(164)
        self.FluxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FluxSlider.setInvertedAppearance(False)
        self.FluxSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.FluxSlider.setTickInterval(0)
        self.FluxSlider.setObjectName("FluxSlider")
        self.ThrottleBypassBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ThrottleBypassBtn.setGeometry(QtCore.QRect(2, 480, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ThrottleBypassBtn.setFont(font)
        self.ThrottleBypassBtn.setText("")
        self.ThrottleBypassBtn.setIcon(icon1)
        self.ThrottleBypassBtn.setIconSize(QtCore.QSize(50, 50))
        self.ThrottleBypassBtn.setCheckable(True)
        self.ThrottleBypassBtn.setAutoExclusive(False)
        self.ThrottleBypassBtn.setObjectName("ThrottleBypassBtn")
        self.ThrottleBypassLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ThrottleBypassLabel.setGeometry(QtCore.QRect(72, 480, 670, 65))
        self.ThrottleBypassLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.ThrottleBypassLabel.setObjectName("ThrottleBypassLabel")
        self.ThrottleBypassLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ThrottleBypassLabel_2.setGeometry(QtCore.QRect(72, 410, 310, 65))
        self.ThrottleBypassLabel_2.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.ThrottleBypassLabel_2.setObjectName("ThrottleBypassLabel_2")
        self.ThrottleBypassBtn_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ThrottleBypassBtn_2.setGeometry(QtCore.QRect(2, 410, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ThrottleBypassBtn_2.setFont(font)
        self.ThrottleBypassBtn_2.setText("")
        self.ThrottleBypassBtn_2.setIcon(icon1)
        self.ThrottleBypassBtn_2.setIconSize(QtCore.QSize(50, 50))
        self.ThrottleBypassBtn_2.setCheckable(True)
        self.ThrottleBypassBtn_2.setAutoExclusive(False)
        self.ThrottleBypassBtn_2.setObjectName("ThrottleBypassBtn_2")
        self.ThrottleBypassLabel_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ThrottleBypassLabel_3.setGeometry(QtCore.QRect(455, 410, 301, 65))
        self.ThrottleBypassLabel_3.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.ThrottleBypassLabel_3.setObjectName("ThrottleBypassLabel_3")
        self.ThrottleBypassBtn_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ThrottleBypassBtn_3.setGeometry(QtCore.QRect(385, 410, 61, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ThrottleBypassBtn_3.setFont(font)
        self.ThrottleBypassBtn_3.setText("")
        self.ThrottleBypassBtn_3.setIcon(icon1)
        self.ThrottleBypassBtn_3.setIconSize(QtCore.QSize(50, 50))
        self.ThrottleBypassBtn_3.setCheckable(True)
        self.ThrottleBypassBtn_3.setAutoExclusive(False)
        self.ThrottleBypassBtn_3.setObjectName("ThrottleBypassBtn_3")
        self.HackAccessBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.HackAccessBtn.setGeometry(QtCore.QRect(5, 1240, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HackAccessBtn.setFont(font)
        self.HackAccessBtn.setText("")
        self.HackAccessBtn.setIcon(icon1)
        self.HackAccessBtn.setIconSize(QtCore.QSize(50, 50))
        self.HackAccessBtn.setCheckable(True)
        self.HackAccessBtn.setAutoExclusive(False)
        self.HackAccessBtn.setObjectName("HackAccessBtn")
        self.HackAccessLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.HackAccessLabel.setGeometry(QtCore.QRect(75, 1240, 670, 65))
        self.HackAccessLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.HackAccessLabel.setObjectName("HackAccessLabel")
        self.MotPowerLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.MotPowerLabel.setGeometry(QtCore.QRect(70, 200, 319, 65))
        self.MotPowerLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.MotPowerLabel.setObjectName("MotPowerLabel")
        self.MotPowerBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.MotPowerBtn.setGeometry(QtCore.QRect(2, 200, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.MotPowerBtn.setFont(font)
        self.MotPowerBtn.setText("")
        self.MotPowerBtn.setIcon(icon1)
        self.MotPowerBtn.setIconSize(QtCore.QSize(50, 50))
        self.MotPowerBtn.setCheckable(True)
        self.MotPowerBtn.setAutoExclusive(False)
        self.MotPowerBtn.setObjectName("MotPowerBtn")
        self.MotPowerSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.MotPowerSlider.setGeometry(QtCore.QRect(388, 210, 370, 45))
        self.MotPowerSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.MotPowerSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.MotPowerSlider.setFont(font)
        self.MotPowerSlider.setStyleSheet("QSlider {\n"
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
        self.MotPowerSlider.setMaximum(100)
        self.MotPowerSlider.setPageStep(10)
        self.MotPowerSlider.setProperty("value", 100)
        self.MotPowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MotPowerSlider.setInvertedAppearance(False)
        self.MotPowerSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.MotPowerSlider.setTickInterval(1)
        self.MotPowerSlider.setObjectName("MotPowerSlider")
        self.HackAccessLabel_code1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.HackAccessLabel_code1.setGeometry(QtCore.QRect(10, 1325, 194, 65))
        self.HackAccessLabel_code1.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.HackAccessLabel_code1.setObjectName("HackAccessLabel_code1")
        self.HackAccessLabel_code2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.HackAccessLabel_code2.setGeometry(QtCore.QRect(265, 1325, 194, 65))
        self.HackAccessLabel_code2.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.HackAccessLabel_code2.setObjectName("HackAccessLabel_code2")
        self.HackAccessLabel_code3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.HackAccessLabel_code3.setGeometry(QtCore.QRect(540, 1325, 194, 65))
        self.HackAccessLabel_code3.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.HackAccessLabel_code3.setObjectName("HackAccessLabel_code3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(OptDialog)
        QtCore.QMetaObject.connectSlotsByName(OptDialog)

    def retranslateUi(self, OptDialog):
        _translate = QtCore.QCoreApplication.translate
        OptDialog.setWindowTitle(_translate("OptDialog", "Form"))
        self.ProgBtn.setText(_translate("OptDialog", "Prog"))
        self.PID_Kd_Label.setText(_translate("OptDialog", "Kd"))
        self.BattPowerLabel.setText(_translate("OptDialog", "BattAmp: 12%"))
        self.BacklightLabel.setText(_translate("OptDialog", "Backlight: x.x"))
        self.RangeLabel.setText(_translate("OptDialog", "Range: xx"))
        self.PID_Kp_Label.setText(_translate("OptDialog", "Kp"))
        self.PID_Ki_Label.setText(_translate("OptDialog", "Ki"))
        self.groupBox.setTitle(_translate("OptDialog", "Diagnostics"))
        self.ExitBtn.setText(_translate("OptDialog", "Back"))
        self.ThemeBtn.setText(_translate("OptDialog", "Theme"))
        self.TripReset.setText(_translate("OptDialog", "TripReset"))
        self.FluxLabel.setText(_translate("OptDialog", "Flux: xx.x%"))
        self.ThrottleBypassLabel.setText(_translate("OptDialog", "Throttle Bypass Assist Levels"))
        self.ThrottleBypassLabel_2.setText(_translate("OptDialog", "Walk Mode"))
        self.ThrottleBypassLabel_3.setText(_translate("OptDialog", "Engine Brake"))
        self.HackAccessLabel.setText(_translate("OptDialog", "Hack Controller Access Level "))
        self.MotPowerLabel.setText(_translate("OptDialog", "MotAmp: 12%"))
        self.HackAccessLabel_code1.setText(_translate("OptDialog", "1:"))
        self.HackAccessLabel_code2.setText(_translate("OptDialog", "2:"))
        self.HackAccessLabel_code3.setText(_translate("OptDialog", "3:"))
import ampy_rc
