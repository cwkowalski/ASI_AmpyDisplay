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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -40, 781, 1440))
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
        self.RangeSlider.setGeometry(QtCore.QRect(390, 210, 370, 45))
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
        self.PID_Kd_Label.setGeometry(QtCore.QRect(2, 380, 250, 40))
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
        self.PowerBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.PowerBtn.setGeometry(QtCore.QRect(2, 130, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PowerBtn.setFont(font)
        self.PowerBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/root/radio_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/root/radio_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.PowerBtn.setIcon(icon1)
        self.PowerBtn.setIconSize(QtCore.QSize(50, 50))
        self.PowerBtn.setCheckable(True)
        self.PowerBtn.setAutoExclusive(False)
        self.PowerBtn.setObjectName("PowerBtn")
        self.PID_Kd_Slider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.PID_Kd_Slider.setGeometry(QtCore.QRect(2, 420, 250, 40))
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
        self.PID_Ki_Slider.setGeometry(QtCore.QRect(255, 420, 250, 40))
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
        self.PowerLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PowerLabel.setGeometry(QtCore.QRect(72, 130, 319, 65))
        self.PowerLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.PowerLabel.setObjectName("PowerLabel")
        self.BacklightLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.BacklightLabel.setGeometry(QtCore.QRect(71, 60, 316, 65))
        self.BacklightLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.BacklightLabel.setObjectName("BacklightLabel")
        self.RangeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.RangeLabel.setGeometry(QtCore.QRect(72, 200, 317, 65))
        self.RangeLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.RangeLabel.setObjectName("RangeLabel")
        self.PowerSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.PowerSlider.setGeometry(QtCore.QRect(390, 140, 370, 45))
        self.PowerSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.PowerSlider.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.PowerSlider.setFont(font)
        self.PowerSlider.setStyleSheet("QSlider {\n"
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
        self.PowerSlider.setMaximum(100)
        self.PowerSlider.setPageStep(10)
        self.PowerSlider.setProperty("value", 100)
        self.PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PowerSlider.setInvertedAppearance(False)
        self.PowerSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PowerSlider.setTickInterval(1)
        self.PowerSlider.setObjectName("PowerSlider")
        self.PID_Kp_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PID_Kp_Label.setGeometry(QtCore.QRect(510, 380, 250, 40))
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
        self.PID_Ki_Label.setGeometry(QtCore.QRect(255, 380, 250, 40))
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
        self.groupBox.setGeometry(QtCore.QRect(4, 470, 770, 406))
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
        self.PID_Kp_Slider.setGeometry(QtCore.QRect(510, 420, 250, 40))
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
        self.RangeBtn.setGeometry(QtCore.QRect(2, 200, 65, 65))
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
        self.FluxLabel.setGeometry(QtCore.QRect(72, 270, 317, 65))
        self.FluxLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.FluxLabel.setObjectName("FluxLabel")
        self.RangeBtn_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.RangeBtn_2.setGeometry(QtCore.QRect(2, 270, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RangeBtn_2.setFont(font)
        self.RangeBtn_2.setText("")
        self.RangeBtn_2.setIcon(icon1)
        self.RangeBtn_2.setIconSize(QtCore.QSize(50, 50))
        self.RangeBtn_2.setCheckable(True)
        self.RangeBtn_2.setAutoExclusive(False)
        self.RangeBtn_2.setObjectName("RangeBtn_2")
        self.FluxSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.FluxSlider.setEnabled(True)
        self.FluxSlider.setGeometry(QtCore.QRect(390, 280, 370, 45))
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(OptDialog)
        QtCore.QMetaObject.connectSlotsByName(OptDialog)

    def retranslateUi(self, OptDialog):
        _translate = QtCore.QCoreApplication.translate
        OptDialog.setWindowTitle(_translate("OptDialog", "Form"))
        self.ProgBtn.setText(_translate("OptDialog", "Prog"))
        self.PID_Kd_Label.setText(_translate("OptDialog", "Kd"))
        self.PowerLabel.setText(_translate("OptDialog", "BattA: 12%"))
        self.BacklightLabel.setText(_translate("OptDialog", "Backlight: x.x"))
        self.RangeLabel.setText(_translate("OptDialog", "Range: xx"))
        self.PID_Kp_Label.setText(_translate("OptDialog", "Kp"))
        self.PID_Ki_Label.setText(_translate("OptDialog", "Ki"))
        self.groupBox.setTitle(_translate("OptDialog", "Diagnostics"))
        self.ExitBtn.setText(_translate("OptDialog", "Back"))
        self.ThemeBtn.setText(_translate("OptDialog", "Theme"))
        self.TripReset.setText(_translate("OptDialog", "TripReset"))
        self.FluxLabel.setText(_translate("OptDialog", "Flux: xx.x%"))
import ampy_rc
