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
        self.RangeBox = QtWidgets.QGroupBox(OptDialog)
        self.RangeBox.setGeometry(QtCore.QRect(18, 14, 296, 137))
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
"margin: 0px 0px;}\n"
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
        self.RangeBox.setObjectName("RangeBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.RangeBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 80, 285, 56))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/radio_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/root/radio_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.RangeBtn.setIcon(icon)
        self.RangeBtn.setIconSize(QtCore.QSize(50, 50))
        self.RangeBtn.setCheckable(True)
        self.RangeBtn.setAutoExclusive(True)
        self.RangeBtn.setObjectName("RangeBtn")
        self.gridLayout_4.addWidget(self.RangeBtn, 0, 0, 1, 1)
        self.PID_Kd_Label = QtWidgets.QLabel(OptDialog)
        self.PID_Kd_Label.setGeometry(QtCore.QRect(29, 146, 233, 41))
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
        self.PID_Ki_Label.setGeometry(QtCore.QRect(15, 261, 253, 41))
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
        self.PID_Kp_Label.setGeometry(QtCore.QRect(18, 366, 256, 41))
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
        self.PID_Kp_Slider.setGeometry(QtCore.QRect(8, 406, 263, 71))
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
        self.PID_Kd_Slider = QtWidgets.QSlider(OptDialog)
        self.PID_Kd_Slider.setGeometry(QtCore.QRect(9, 191, 261, 71))
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
        self.PID_Ki_Slider = QtWidgets.QSlider(OptDialog)
        self.PID_Ki_Slider.setGeometry(QtCore.QRect(5, 301, 269, 71))
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
        self.ExitBtn = QtWidgets.QPushButton(OptDialog)
        self.ExitBtn.setGeometry(QtCore.QRect(326, 27, 45, 40))
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

        self.retranslateUi(OptDialog)
        QtCore.QMetaObject.connectSlotsByName(OptDialog)

    def retranslateUi(self, OptDialog):
        _translate = QtCore.QCoreApplication.translate
        OptDialog.setWindowTitle(_translate("OptDialog", "Form"))
        self.RangeBox.setTitle(_translate("OptDialog", "Range: #"))
        self.PID_Kd_Label.setText(_translate("OptDialog", "Kd"))
        self.PID_Ki_Label.setText(_translate("OptDialog", "Ki"))
        self.PID_Kp_Label.setText(_translate("OptDialog", "Kp"))
        self.ExitBtn.setText(_translate("OptDialog", "g"))
import ampy_rc
