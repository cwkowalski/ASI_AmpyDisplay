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
        self.PID_Kd_Label = QtWidgets.QLabel(OptDialog)
        self.PID_Kd_Label.setGeometry(QtCore.QRect(10, 400, 250, 40))
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
        self.PID_Ki_Label = QtWidgets.QLabel(OptDialog)
        self.PID_Ki_Label.setGeometry(QtCore.QRect(270, 400, 250, 40))
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
        self.PID_Kp_Label = QtWidgets.QLabel(OptDialog)
        self.PID_Kp_Label.setGeometry(QtCore.QRect(530, 400, 250, 40))
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
        self.PID_Kp_Slider = QtWidgets.QSlider(OptDialog)
        self.PID_Kp_Slider.setGeometry(QtCore.QRect(530, 440, 250, 40))
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
        self.PID_Kd_Slider = QtWidgets.QSlider(OptDialog)
        self.PID_Kd_Slider.setGeometry(QtCore.QRect(10, 440, 250, 40))
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
        self.PID_Ki_Slider = QtWidgets.QSlider(OptDialog)
        self.PID_Ki_Slider.setGeometry(QtCore.QRect(270, 440, 250, 40))
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
        self.ExitBtn = QtWidgets.QPushButton(OptDialog)
        self.ExitBtn.setGeometry(QtCore.QRect(690, 0, 100, 55))
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
        self.DisplaySlider = QtWidgets.QSlider(OptDialog)
        self.DisplaySlider.setGeometry(QtCore.QRect(390, 190, 400, 45))
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
        self.DisplaySlider.setMaximum(50)
        self.DisplaySlider.setPageStep(2)
        self.DisplaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.DisplaySlider.setInvertedAppearance(False)
        self.DisplaySlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.DisplaySlider.setTickInterval(1)
        self.DisplaySlider.setObjectName("DisplaySlider")
        self.BacklightLabel = QtWidgets.QLabel(OptDialog)
        self.BacklightLabel.setGeometry(QtCore.QRect(79, 180, 300, 65))
        self.BacklightLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.BacklightLabel.setObjectName("BacklightLabel")
        self.DisplayInvertBtn = QtWidgets.QPushButton(OptDialog)
        self.DisplayInvertBtn.setGeometry(QtCore.QRect(10, 180, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DisplayInvertBtn.setFont(font)
        self.DisplayInvertBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/invert-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DisplayInvertBtn.setIcon(icon)
        self.DisplayInvertBtn.setIconSize(QtCore.QSize(50, 50))
        self.DisplayInvertBtn.setCheckable(True)
        self.DisplayInvertBtn.setAutoExclusive(True)
        self.DisplayInvertBtn.setObjectName("DisplayInvertBtn")
        self.PowerBtn = QtWidgets.QPushButton(OptDialog)
        self.PowerBtn.setGeometry(QtCore.QRect(10, 250, 65, 65))
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
        self.PowerBtn.setAutoExclusive(True)
        self.PowerBtn.setObjectName("PowerBtn")
        self.PowerLabel = QtWidgets.QLabel(OptDialog)
        self.PowerLabel.setGeometry(QtCore.QRect(80, 250, 300, 65))
        self.PowerLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.PowerLabel.setObjectName("PowerLabel")
        self.PowerSlider = QtWidgets.QSlider(OptDialog)
        self.PowerSlider.setGeometry(QtCore.QRect(390, 260, 400, 45))
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
        self.PowerSlider.setMaximum(50)
        self.PowerSlider.setPageStep(2)
        self.PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PowerSlider.setInvertedAppearance(False)
        self.PowerSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.PowerSlider.setTickInterval(1)
        self.PowerSlider.setObjectName("PowerSlider")
        self.RangeLabel = QtWidgets.QLabel(OptDialog)
        self.RangeLabel.setGeometry(QtCore.QRect(80, 320, 300, 65))
        self.RangeLabel.setStyleSheet("QLabel{\n"
"    font: 36pt \"MS Shell Dlg\";\n"
"}")
        self.RangeLabel.setObjectName("RangeLabel")
        self.RangeBtn = QtWidgets.QPushButton(OptDialog)
        self.RangeBtn.setGeometry(QtCore.QRect(10, 320, 65, 65))
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
        self.RangeBtn.setAutoExclusive(True)
        self.RangeBtn.setObjectName("RangeBtn")
        self.RangeSlider = QtWidgets.QSlider(OptDialog)
        self.RangeSlider.setEnabled(True)
        self.RangeSlider.setGeometry(QtCore.QRect(390, 329, 400, 45))
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
        self.RangeSlider.setMaximum(50)
        self.RangeSlider.setPageStep(2)
        self.RangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RangeSlider.setInvertedAppearance(False)
        self.RangeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.RangeSlider.setTickInterval(1)
        self.RangeSlider.setObjectName("RangeSlider")
        self.groupBox = QtWidgets.QGroupBox(OptDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, -1, 770, 175))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(47, 90, 589, 45))
        self.label.setObjectName("label")
        self.ThemeBtn = QtWidgets.QPushButton(OptDialog)
        self.ThemeBtn.setGeometry(QtCore.QRect(690, 65, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ThemeBtn.setFont(font)
        self.ThemeBtn.setStyleSheet("QPushButton { \n"
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
        self.ThemeBtn.setCheckable(True)
        self.ThemeBtn.setChecked(False)
        self.ThemeBtn.setAutoExclusive(True)
        self.ThemeBtn.setObjectName("ThemeBtn")
        self.ProgBtn = QtWidgets.QPushButton(OptDialog)
        self.ProgBtn.setGeometry(QtCore.QRect(690, 130, 100, 55))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProgBtn.setFont(font)
        self.ProgBtn.setStyleSheet("QPushButton { \n"
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
        self.ProgBtn.setCheckable(True)
        self.ProgBtn.setChecked(False)
        self.ProgBtn.setAutoExclusive(True)
        self.ProgBtn.setObjectName("ProgBtn")
        self.PID_Kd_Label.raise_()
        self.PID_Ki_Label.raise_()
        self.PID_Kp_Label.raise_()
        self.PID_Kp_Slider.raise_()
        self.PID_Kd_Slider.raise_()
        self.PID_Ki_Slider.raise_()
        self.DisplaySlider.raise_()
        self.BacklightLabel.raise_()
        self.DisplayInvertBtn.raise_()
        self.PowerBtn.raise_()
        self.PowerLabel.raise_()
        self.PowerSlider.raise_()
        self.RangeLabel.raise_()
        self.RangeBtn.raise_()
        self.RangeSlider.raise_()
        self.groupBox.raise_()
        self.ExitBtn.raise_()
        self.ThemeBtn.raise_()
        self.ProgBtn.raise_()

        self.retranslateUi(OptDialog)
        QtCore.QMetaObject.connectSlotsByName(OptDialog)

    def retranslateUi(self, OptDialog):
        _translate = QtCore.QCoreApplication.translate
        OptDialog.setWindowTitle(_translate("OptDialog", "Form"))
        self.PID_Kd_Label.setText(_translate("OptDialog", "Kd"))
        self.PID_Ki_Label.setText(_translate("OptDialog", "Ki"))
        self.PID_Kp_Label.setText(_translate("OptDialog", "Kp"))
        self.ExitBtn.setText(_translate("OptDialog", "Back"))
        self.BacklightLabel.setText(_translate("OptDialog", "Backlight: x.x"))
        self.PowerLabel.setText(_translate("OptDialog", "Power: xx.xx"))
        self.RangeLabel.setText(_translate("OptDialog", "Range: xx"))
        self.groupBox.setTitle(_translate("OptDialog", "Diagnostics"))
        self.label.setText(_translate("OptDialog", "Hall sensor position, Ebike Flags, Input Voltages"))
        self.ThemeBtn.setText(_translate("OptDialog", "Theme"))
        self.ProgBtn.setText(_translate("OptDialog", "Prog"))
import ampy_rc
