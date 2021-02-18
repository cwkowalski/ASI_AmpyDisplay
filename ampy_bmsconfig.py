# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ampy_bmsconfig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bmscfg(object):
    def setupUi(self, bmscfg):
        bmscfg.setObjectName("bmscfg")
        bmscfg.resize(800, 480)
        self.scrollArea = QtWidgets.QScrollArea(bmscfg)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.scrollArea.setStyleSheet("QScrollBar{\n"
"background: white;}\n"
"QScrollBar{\n"
"width: 25px;}\n"
"\n"
"QPushButton{\n"
"background: transparent;\n"
"border: none}\n"
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
"    padding: 0 0px 0 0px;\n"
"}\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -422, 781, 1440))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(781, 1440))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ReadEepromBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ReadEepromBtn.setGeometry(QtCore.QRect(240, 0, 109, 55))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ReadEepromBtn.setFont(font)
        self.ReadEepromBtn.setStyleSheet("QPushButton { \n"
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
        self.ReadEepromBtn.setCheckable(True)
        self.ReadEepromBtn.setChecked(False)
        self.ReadEepromBtn.setAutoExclusive(True)
        self.ReadEepromBtn.setObjectName("ReadEepromBtn")
        self.WriteEepromBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.WriteEepromBtn.setGeometry(QtCore.QRect(415, 0, 180, 55))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.WriteEepromBtn.setFont(font)
        self.WriteEepromBtn.setStyleSheet("QPushButton { \n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/root/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.WriteEepromBtn.setIcon(icon)
        self.WriteEepromBtn.setIconSize(QtCore.QSize(40, 40))
        self.WriteEepromBtn.setCheckable(True)
        self.WriteEepromBtn.setChecked(False)
        self.WriteEepromBtn.setAutoExclusive(True)
        self.WriteEepromBtn.setObjectName("WriteEepromBtn")
        self.ExitBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ExitBtn.setGeometry(QtCore.QRect(670, 0, 100, 55))
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
        self.AssistBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.AssistBox.setGeometry(QtCore.QRect(5, 885, 765, 554))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.AssistBox.setFont(font)
        self.AssistBox.setStyleSheet("QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: 24 0px 0 0px\n"
"}\n"
"QLabel{\n"
"    font: 14pt \"Luxi Mono\";\n"
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
"margin: 0px 0px;}\n"
"\n"
"QDoubleSpinBox::up-button { \n"
"subcontrol-origin: margin;\n"
"subcontrol-position: center left;\n"
"width: 40px;\n"
"height: 43px;}\n"
"\n"
"QDoubleSpinBox::down-button { \n"
"width: 40px;\n"
"height: 43px;}\n"
"\n"
"QDoubleSpinBox{ font: 16pt \"Luxi Mono\";}")
        self.AssistBox.setObjectName("AssistBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.AssistBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 59, 744, 487))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CUVPSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CUVPSpin.sizePolicy().hasHeightForWidth())
        self.CUVPSpin.setSizePolicy(sizePolicy)
        self.CUVPSpin.setMaximum(4.2)
        self.CUVPSpin.setSingleStep(0.01)
        self.CUVPSpin.setObjectName("CUVPSpin")
        self.gridLayout.addWidget(self.CUVPSpin, 1, 1, 1, 1)
        self.CUVPDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CUVPDelayLabel.setObjectName("CUVPDelayLabel")
        self.gridLayout.addWidget(self.CUVPDelayLabel, 1, 4, 1, 1)
        self.DSGUTDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSGUTDelayLabel.setObjectName("DSGUTDelayLabel")
        self.gridLayout.addWidget(self.DSGUTDelayLabel, 7, 4, 1, 1)
        self.PUVPDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PUVPDelayLabel.setObjectName("PUVPDelayLabel")
        self.gridLayout.addWidget(self.PUVPDelayLabel, 3, 4, 1, 1)
        self.PVOPDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PVOPDelayLabel.setObjectName("PVOPDelayLabel")
        self.gridLayout.addWidget(self.PVOPDelayLabel, 2, 4, 1, 1)
        self.CHGOCDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGOCDelayLabel.setObjectName("CHGOCDelayLabel")
        self.gridLayout.addWidget(self.CHGOCDelayLabel, 8, 4, 1, 1)
        self.CHGOTDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGOTDelayLabel.setObjectName("CHGOTDelayLabel")
        self.gridLayout.addWidget(self.CHGOTDelayLabel, 4, 4, 1, 1)
        self.PUVPLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PUVPLabel.setObjectName("PUVPLabel")
        self.gridLayout.addWidget(self.PUVPLabel, 3, 0, 1, 1)
        self.CHGOT = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGOT.setObjectName("CHGOT")
        self.gridLayout.addWidget(self.CHGOT, 4, 0, 1, 1)
        self.CHGUT = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGUT.setObjectName("CHGUT")
        self.gridLayout.addWidget(self.CHGUT, 5, 0, 1, 1)
        self.DSGOT = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSGOT.setObjectName("DSGOT")
        self.gridLayout.addWidget(self.DSGOT, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 2, 1, 1)
        self.CHGUTReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGUTReleaseLabel.setObjectName("CHGUTReleaseLabel")
        self.gridLayout.addWidget(self.CHGUTReleaseLabel, 5, 2, 1, 1)
        self.CHGOTReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGOTReleaseLabel.setObjectName("CHGOTReleaseLabel")
        self.gridLayout.addWidget(self.CHGOTReleaseLabel, 4, 2, 1, 1)
        self.DSCHOCReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSCHOCReleaseLabel.setObjectName("DSCHOCReleaseLabel")
        self.gridLayout.addWidget(self.DSCHOCReleaseLabel, 9, 2, 1, 1)
        self.DSGUTReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSGUTReleaseLabel.setObjectName("DSGUTReleaseLabel")
        self.gridLayout.addWidget(self.DSGUTReleaseLabel, 7, 2, 1, 1)
        self.CHGOCReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGOCReleaseLabel.setObjectName("CHGOCReleaseLabel")
        self.gridLayout.addWidget(self.CHGOCReleaseLabel, 8, 2, 1, 1)
        self.DSGUT = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSGUT.setObjectName("DSGUT")
        self.gridLayout.addWidget(self.DSGUT, 7, 0, 1, 1)
        self.CHGUTDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGUTDelayLabel.setObjectName("CHGUTDelayLabel")
        self.gridLayout.addWidget(self.CHGUTDelayLabel, 5, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 6, 4, 1, 1)
        self.CHGOTSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGOTSpin.sizePolicy().hasHeightForWidth())
        self.CHGOTSpin.setSizePolicy(sizePolicy)
        self.CHGOTSpin.setMaximum(70.0)
        self.CHGOTSpin.setSingleStep(0.5)
        self.CHGOTSpin.setObjectName("CHGOTSpin")
        self.gridLayout.addWidget(self.CHGOTSpin, 4, 1, 1, 1)
        self.CHGUTSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGUTSpin.sizePolicy().hasHeightForWidth())
        self.CHGUTSpin.setSizePolicy(sizePolicy)
        self.CHGUTSpin.setMaximum(70.0)
        self.CHGUTSpin.setSingleStep(0.5)
        self.CHGUTSpin.setObjectName("CHGUTSpin")
        self.gridLayout.addWidget(self.CHGUTSpin, 5, 1, 1, 1)
        self.DSGOTSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSGOTSpin.sizePolicy().hasHeightForWidth())
        self.DSGOTSpin.setSizePolicy(sizePolicy)
        self.DSGOTSpin.setMaximum(70.0)
        self.DSGOTSpin.setSingleStep(0.5)
        self.DSGOTSpin.setObjectName("DSGOTSpin")
        self.gridLayout.addWidget(self.DSGOTSpin, 6, 1, 1, 1)
        self.DSCHOCReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSCHOCReleaseSpin.sizePolicy().hasHeightForWidth())
        self.DSCHOCReleaseSpin.setSizePolicy(sizePolicy)
        self.DSCHOCReleaseSpin.setMaximum(300.0)
        self.DSCHOCReleaseSpin.setObjectName("DSCHOCReleaseSpin")
        self.gridLayout.addWidget(self.DSCHOCReleaseSpin, 9, 3, 1, 1)
        self.PUVPSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PUVPSpin.sizePolicy().hasHeightForWidth())
        self.PUVPSpin.setSizePolicy(sizePolicy)
        self.PUVPSpin.setMaximum(100.0)
        self.PUVPSpin.setSingleStep(0.1)
        self.PUVPSpin.setObjectName("PUVPSpin")
        self.gridLayout.addWidget(self.PUVPSpin, 3, 1, 1, 1)
        self.POVPReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.POVPReleaseLabel.setObjectName("POVPReleaseLabel")
        self.gridLayout.addWidget(self.POVPReleaseLabel, 2, 2, 1, 1)
        self.PUVPReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PUVPReleaseLabel.setObjectName("PUVPReleaseLabel")
        self.gridLayout.addWidget(self.PUVPReleaseLabel, 3, 2, 1, 1)
        self.CHGOCLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CHGOCLabel.setObjectName("CHGOCLabel")
        self.gridLayout.addWidget(self.CHGOCLabel, 8, 0, 1, 1)
        self.DSGOC = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSGOC.setObjectName("DSGOC")
        self.gridLayout.addWidget(self.DSGOC, 9, 0, 1, 1)
        self.DSCHOCDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DSCHOCDelayLabel.setObjectName("DSCHOCDelayLabel")
        self.gridLayout.addWidget(self.DSCHOCDelayLabel, 9, 4, 1, 1)
        self.POVPLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.POVPLabel.setObjectName("POVPLabel")
        self.gridLayout.addWidget(self.POVPLabel, 2, 0, 1, 1)
        self.COVPDelayLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.COVPDelayLabel.setObjectName("COVPDelayLabel")
        self.gridLayout.addWidget(self.COVPDelayLabel, 0, 4, 1, 1)
        self.DSCHOCSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSCHOCSpin.sizePolicy().hasHeightForWidth())
        self.DSCHOCSpin.setSizePolicy(sizePolicy)
        self.DSCHOCSpin.setMaximum(300.0)
        self.DSCHOCSpin.setSingleStep(0.5)
        self.DSCHOCSpin.setObjectName("DSCHOCSpin")
        self.gridLayout.addWidget(self.DSCHOCSpin, 9, 1, 1, 1)
        self.COVPSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COVPSpin.sizePolicy().hasHeightForWidth())
        self.COVPSpin.setSizePolicy(sizePolicy)
        self.COVPSpin.setMaximum(4.2)
        self.COVPSpin.setSingleStep(0.01)
        self.COVPSpin.setObjectName("COVPSpin")
        self.gridLayout.addWidget(self.COVPSpin, 0, 1, 1, 1)
        self.CHGOCSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGOCSpin.sizePolicy().hasHeightForWidth())
        self.CHGOCSpin.setSizePolicy(sizePolicy)
        self.CHGOCSpin.setMaximum(300.0)
        self.CHGOCSpin.setSingleStep(0.5)
        self.CHGOCSpin.setObjectName("CHGOCSpin")
        self.gridLayout.addWidget(self.CHGOCSpin, 8, 1, 1, 1)
        self.POVPSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.POVPSpin.sizePolicy().hasHeightForWidth())
        self.POVPSpin.setSizePolicy(sizePolicy)
        self.POVPSpin.setMaximum(100.0)
        self.POVPSpin.setSingleStep(0.1)
        self.POVPSpin.setObjectName("POVPSpin")
        self.gridLayout.addWidget(self.POVPSpin, 2, 1, 1, 1)
        self.DSGUTSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSGUTSpin.sizePolicy().hasHeightForWidth())
        self.DSGUTSpin.setSizePolicy(sizePolicy)
        self.DSGUTSpin.setMinimum(-10.0)
        self.DSGUTSpin.setMaximum(80.0)
        self.DSGUTSpin.setSingleStep(0.5)
        self.DSGUTSpin.setObjectName("DSGUTSpin")
        self.gridLayout.addWidget(self.DSGUTSpin, 7, 1, 1, 1)
        self.COVPReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.COVPReleaseLabel.setObjectName("COVPReleaseLabel")
        self.gridLayout.addWidget(self.COVPReleaseLabel, 0, 2, 1, 1)
        self.COVPLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.COVPLabel.setObjectName("COVPLabel")
        self.gridLayout.addWidget(self.COVPLabel, 0, 0, 1, 1)
        self.CUVPLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CUVPLabel.setObjectName("CUVPLabel")
        self.gridLayout.addWidget(self.CUVPLabel, 1, 0, 1, 1)
        self.CUVPReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CUVPReleaseLabel.setObjectName("CUVPReleaseLabel")
        self.gridLayout.addWidget(self.CUVPReleaseLabel, 1, 2, 1, 1)
        self.COVPReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COVPReleaseSpin.sizePolicy().hasHeightForWidth())
        self.COVPReleaseSpin.setSizePolicy(sizePolicy)
        self.COVPReleaseSpin.setMaximum(4.2)
        self.COVPReleaseSpin.setSingleStep(0.01)
        self.COVPReleaseSpin.setObjectName("COVPReleaseSpin")
        self.gridLayout.addWidget(self.COVPReleaseSpin, 0, 3, 1, 1)
        self.CUVPReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CUVPReleaseSpin.sizePolicy().hasHeightForWidth())
        self.CUVPReleaseSpin.setSizePolicy(sizePolicy)
        self.CUVPReleaseSpin.setMaximum(4.2)
        self.CUVPReleaseSpin.setSingleStep(0.1)
        self.CUVPReleaseSpin.setObjectName("CUVPReleaseSpin")
        self.gridLayout.addWidget(self.CUVPReleaseSpin, 1, 3, 1, 1)
        self.POVPReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.POVPReleaseSpin.sizePolicy().hasHeightForWidth())
        self.POVPReleaseSpin.setSizePolicy(sizePolicy)
        self.POVPReleaseSpin.setMaximum(100.0)
        self.POVPReleaseSpin.setSingleStep(0.1)
        self.POVPReleaseSpin.setObjectName("POVPReleaseSpin")
        self.gridLayout.addWidget(self.POVPReleaseSpin, 2, 3, 1, 1)
        self.PUVPReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PUVPReleaseSpin.sizePolicy().hasHeightForWidth())
        self.PUVPReleaseSpin.setSizePolicy(sizePolicy)
        self.PUVPReleaseSpin.setMaximum(100.0)
        self.PUVPReleaseSpin.setSingleStep(0.1)
        self.PUVPReleaseSpin.setObjectName("PUVPReleaseSpin")
        self.gridLayout.addWidget(self.PUVPReleaseSpin, 3, 3, 1, 1)
        self.CHGOTReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGOTReleaseSpin.sizePolicy().hasHeightForWidth())
        self.CHGOTReleaseSpin.setSizePolicy(sizePolicy)
        self.CHGOTReleaseSpin.setMaximum(70.0)
        self.CHGOTReleaseSpin.setSingleStep(0.5)
        self.CHGOTReleaseSpin.setObjectName("CHGOTReleaseSpin")
        self.gridLayout.addWidget(self.CHGOTReleaseSpin, 4, 3, 1, 1)
        self.CHGUTReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGUTReleaseSpin.sizePolicy().hasHeightForWidth())
        self.CHGUTReleaseSpin.setSizePolicy(sizePolicy)
        self.CHGUTReleaseSpin.setMaximum(70.0)
        self.CHGUTReleaseSpin.setSingleStep(0.5)
        self.CHGUTReleaseSpin.setObjectName("CHGUTReleaseSpin")
        self.gridLayout.addWidget(self.CHGUTReleaseSpin, 5, 3, 1, 1)
        self.DSGOTReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSGOTReleaseSpin.sizePolicy().hasHeightForWidth())
        self.DSGOTReleaseSpin.setSizePolicy(sizePolicy)
        self.DSGOTReleaseSpin.setMaximum(70.0)
        self.DSGOTReleaseSpin.setSingleStep(0.5)
        self.DSGOTReleaseSpin.setObjectName("DSGOTReleaseSpin")
        self.gridLayout.addWidget(self.DSGOTReleaseSpin, 6, 3, 1, 1)
        self.DSGUTReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSGUTReleaseSpin.sizePolicy().hasHeightForWidth())
        self.DSGUTReleaseSpin.setSizePolicy(sizePolicy)
        self.DSGUTReleaseSpin.setMaximum(70.0)
        self.DSGUTReleaseSpin.setSingleStep(0.5)
        self.DSGUTReleaseSpin.setObjectName("DSGUTReleaseSpin")
        self.gridLayout.addWidget(self.DSGUTReleaseSpin, 7, 3, 1, 1)
        self.CHGOCReleaseSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGOCReleaseSpin.sizePolicy().hasHeightForWidth())
        self.CHGOCReleaseSpin.setSizePolicy(sizePolicy)
        self.CHGOCReleaseSpin.setMaximum(300.0)
        self.CHGOCReleaseSpin.setObjectName("CHGOCReleaseSpin")
        self.gridLayout.addWidget(self.CHGOCReleaseSpin, 8, 3, 1, 1)
        self.DSGUTDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSGUTDelaySpin.sizePolicy().hasHeightForWidth())
        self.DSGUTDelaySpin.setSizePolicy(sizePolicy)
        self.DSGUTDelaySpin.setMaximum(60.0)
        self.DSGUTDelaySpin.setObjectName("DSGUTDelaySpin")
        self.gridLayout.addWidget(self.DSGUTDelaySpin, 7, 5, 1, 1)
        self.COVPDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COVPDelaySpin.sizePolicy().hasHeightForWidth())
        self.COVPDelaySpin.setSizePolicy(sizePolicy)
        self.COVPDelaySpin.setMaximum(60.0)
        self.COVPDelaySpin.setObjectName("COVPDelaySpin")
        self.gridLayout.addWidget(self.COVPDelaySpin, 0, 5, 1, 1)
        self.CUVPDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CUVPDelaySpin.sizePolicy().hasHeightForWidth())
        self.CUVPDelaySpin.setSizePolicy(sizePolicy)
        self.CUVPDelaySpin.setMaximum(60.0)
        self.CUVPDelaySpin.setObjectName("CUVPDelaySpin")
        self.gridLayout.addWidget(self.CUVPDelaySpin, 1, 5, 1, 1)
        self.POVPDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.POVPDelaySpin.sizePolicy().hasHeightForWidth())
        self.POVPDelaySpin.setSizePolicy(sizePolicy)
        self.POVPDelaySpin.setMaximum(60.0)
        self.POVPDelaySpin.setObjectName("POVPDelaySpin")
        self.gridLayout.addWidget(self.POVPDelaySpin, 2, 5, 1, 1)
        self.PUVPDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PUVPDelaySpin.sizePolicy().hasHeightForWidth())
        self.PUVPDelaySpin.setSizePolicy(sizePolicy)
        self.PUVPDelaySpin.setMaximum(60.0)
        self.PUVPDelaySpin.setObjectName("PUVPDelaySpin")
        self.gridLayout.addWidget(self.PUVPDelaySpin, 3, 5, 1, 1)
        self.CHGOTDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGOTDelaySpin.sizePolicy().hasHeightForWidth())
        self.CHGOTDelaySpin.setSizePolicy(sizePolicy)
        self.CHGOTDelaySpin.setMaximum(60.0)
        self.CHGOTDelaySpin.setObjectName("CHGOTDelaySpin")
        self.gridLayout.addWidget(self.CHGOTDelaySpin, 4, 5, 1, 1)
        self.CHGUTDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGUTDelaySpin.sizePolicy().hasHeightForWidth())
        self.CHGUTDelaySpin.setSizePolicy(sizePolicy)
        self.CHGUTDelaySpin.setMaximum(60.0)
        self.CHGUTDelaySpin.setObjectName("CHGUTDelaySpin")
        self.gridLayout.addWidget(self.CHGUTDelaySpin, 5, 5, 1, 1)
        self.DSGOTDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSGOTDelaySpin.sizePolicy().hasHeightForWidth())
        self.DSGOTDelaySpin.setSizePolicy(sizePolicy)
        self.DSGOTDelaySpin.setMaximum(60.0)
        self.DSGOTDelaySpin.setObjectName("DSGOTDelaySpin")
        self.gridLayout.addWidget(self.DSGOTDelaySpin, 6, 5, 1, 1)
        self.CHGOCDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHGOCDelaySpin.sizePolicy().hasHeightForWidth())
        self.CHGOCDelaySpin.setSizePolicy(sizePolicy)
        self.CHGOCDelaySpin.setMaximum(60.0)
        self.CHGOCDelaySpin.setObjectName("CHGOCDelaySpin")
        self.gridLayout.addWidget(self.CHGOCDelaySpin, 8, 5, 1, 1)
        self.DSCHOCDelaySpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DSCHOCDelaySpin.sizePolicy().hasHeightForWidth())
        self.DSCHOCDelaySpin.setSizePolicy(sizePolicy)
        self.DSCHOCDelaySpin.setMaximum(60.0)
        self.DSCHOCDelaySpin.setObjectName("DSCHOCDelaySpin")
        self.gridLayout.addWidget(self.DSCHOCDelaySpin, 9, 5, 1, 1)
        self.Functions = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.Functions.setGeometry(QtCore.QRect(6, 5, 765, 462))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Functions.setFont(font)
        self.Functions.setStyleSheet("QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: 24 0px 0 0px\n"
"}\n"
"QLabel{\n"
"    font: 24pt \"Luxi Mono\";\n"
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
"margin: 0px 0px;}\n"
"\n"
"QDoubleSpinBox::up-button { \n"
"subcontrol-origin: margin;\n"
"subcontrol-position: center left;\n"
"width: 40px;\n"
"height: 43px;}\n"
"\n"
"QDoubleSpinBox::down-button { \n"
"width: 40px;\n"
"height: 43px;}")
        self.Functions.setObjectName("Functions")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Functions)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 60, 846, 393))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SCReleaseBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SCReleaseBtn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SCReleaseBtn.setFont(font)
        self.SCReleaseBtn.setStyleSheet("QLabel{\n"
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
        self.SCReleaseBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/root/radio_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/root/radio_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SCReleaseBtn.setIcon(icon1)
        self.SCReleaseBtn.setIconSize(QtCore.QSize(45, 45))
        self.SCReleaseBtn.setCheckable(True)
        self.SCReleaseBtn.setAutoExclusive(False)
        self.SCReleaseBtn.setObjectName("SCReleaseBtn")
        self.gridLayout_2.addWidget(self.SCReleaseBtn, 0, 3, 1, 1)
        self.SCReleaseLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SCReleaseLabel.sizePolicy().hasHeightForWidth())
        self.SCReleaseLabel.setSizePolicy(sizePolicy)
        self.SCReleaseLabel.setObjectName("SCReleaseLabel")
        self.gridLayout_2.addWidget(self.SCReleaseLabel, 0, 4, 1, 1)
        self.NTC1Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC1Btn.sizePolicy().hasHeightForWidth())
        self.NTC1Btn.setSizePolicy(sizePolicy)
        self.NTC1Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC1Btn.setFont(font)
        self.NTC1Btn.setStyleSheet("QLabel{\n"
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
        self.NTC1Btn.setText("")
        self.NTC1Btn.setIcon(icon1)
        self.NTC1Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC1Btn.setCheckable(True)
        self.NTC1Btn.setAutoExclusive(False)
        self.NTC1Btn.setObjectName("NTC1Btn")
        self.gridLayout_2.addWidget(self.NTC1Btn, 3, 0, 1, 1)
        self.LEDEnableBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEDEnableBtn.sizePolicy().hasHeightForWidth())
        self.LEDEnableBtn.setSizePolicy(sizePolicy)
        self.LEDEnableBtn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LEDEnableBtn.setFont(font)
        self.LEDEnableBtn.setStyleSheet("QLabel{\n"
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
        self.LEDEnableBtn.setText("")
        self.LEDEnableBtn.setIcon(icon1)
        self.LEDEnableBtn.setIconSize(QtCore.QSize(45, 45))
        self.LEDEnableBtn.setCheckable(True)
        self.LEDEnableBtn.setAutoExclusive(False)
        self.LEDEnableBtn.setObjectName("LEDEnableBtn")
        self.gridLayout_2.addWidget(self.LEDEnableBtn, 2, 0, 1, 1)
        self.BalanceEnableBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BalanceEnableBtn.sizePolicy().hasHeightForWidth())
        self.BalanceEnableBtn.setSizePolicy(sizePolicy)
        self.BalanceEnableBtn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BalanceEnableBtn.setFont(font)
        self.BalanceEnableBtn.setStyleSheet("QLabel{\n"
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
        self.BalanceEnableBtn.setText("")
        self.BalanceEnableBtn.setIcon(icon1)
        self.BalanceEnableBtn.setIconSize(QtCore.QSize(45, 45))
        self.BalanceEnableBtn.setCheckable(True)
        self.BalanceEnableBtn.setAutoExclusive(False)
        self.BalanceEnableBtn.setObjectName("BalanceEnableBtn")
        self.gridLayout_2.addWidget(self.BalanceEnableBtn, 1, 0, 1, 1)
        self.NTC3Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC3Btn.sizePolicy().hasHeightForWidth())
        self.NTC3Btn.setSizePolicy(sizePolicy)
        self.NTC3Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC3Btn.setFont(font)
        self.NTC3Btn.setStyleSheet("QLabel{\n"
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
        self.NTC3Btn.setText("")
        self.NTC3Btn.setIcon(icon1)
        self.NTC3Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC3Btn.setCheckable(True)
        self.NTC3Btn.setAutoExclusive(False)
        self.NTC3Btn.setObjectName("NTC3Btn")
        self.gridLayout_2.addWidget(self.NTC3Btn, 4, 0, 1, 1)
        self.NTC5Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC5Label.sizePolicy().hasHeightForWidth())
        self.NTC5Label.setSizePolicy(sizePolicy)
        self.NTC5Label.setObjectName("NTC5Label")
        self.gridLayout_2.addWidget(self.NTC5Label, 5, 2, 1, 1)
        self.SwitchBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SwitchBtn.sizePolicy().hasHeightForWidth())
        self.SwitchBtn.setSizePolicy(sizePolicy)
        self.SwitchBtn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SwitchBtn.setFont(font)
        self.SwitchBtn.setStyleSheet("QLabel{\n"
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
        self.SwitchBtn.setText("")
        self.SwitchBtn.setIcon(icon1)
        self.SwitchBtn.setIconSize(QtCore.QSize(45, 45))
        self.SwitchBtn.setCheckable(True)
        self.SwitchBtn.setAutoExclusive(False)
        self.SwitchBtn.setObjectName("SwitchBtn")
        self.gridLayout_2.addWidget(self.SwitchBtn, 0, 0, 1, 1)
        self.ChargeBalanceLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChargeBalanceLabel.sizePolicy().hasHeightForWidth())
        self.ChargeBalanceLabel.setSizePolicy(sizePolicy)
        self.ChargeBalanceLabel.setObjectName("ChargeBalanceLabel")
        self.gridLayout_2.addWidget(self.ChargeBalanceLabel, 1, 4, 1, 1)
        self.LEDEnableLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEDEnableLabel.sizePolicy().hasHeightForWidth())
        self.LEDEnableLabel.setSizePolicy(sizePolicy)
        self.LEDEnableLabel.setObjectName("LEDEnableLabel")
        self.gridLayout_2.addWidget(self.LEDEnableLabel, 2, 2, 1, 1)
        self.LEDNumberLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEDNumberLabel.sizePolicy().hasHeightForWidth())
        self.LEDNumberLabel.setSizePolicy(sizePolicy)
        self.LEDNumberLabel.setObjectName("LEDNumberLabel")
        self.gridLayout_2.addWidget(self.LEDNumberLabel, 2, 4, 1, 1)
        self.LEDNumberBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.LEDNumberBtn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LEDNumberBtn.setFont(font)
        self.LEDNumberBtn.setStyleSheet("QLabel{\n"
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
        self.LEDNumberBtn.setText("")
        self.LEDNumberBtn.setIcon(icon1)
        self.LEDNumberBtn.setIconSize(QtCore.QSize(45, 45))
        self.LEDNumberBtn.setCheckable(True)
        self.LEDNumberBtn.setAutoExclusive(False)
        self.LEDNumberBtn.setObjectName("LEDNumberBtn")
        self.gridLayout_2.addWidget(self.LEDNumberBtn, 2, 3, 1, 1)
        self.SwitchLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SwitchLabel.sizePolicy().hasHeightForWidth())
        self.SwitchLabel.setSizePolicy(sizePolicy)
        self.SwitchLabel.setObjectName("SwitchLabel")
        self.gridLayout_2.addWidget(self.SwitchLabel, 0, 2, 1, 1)
        self.ChargeBalanceBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ChargeBalanceBtn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ChargeBalanceBtn.setFont(font)
        self.ChargeBalanceBtn.setStyleSheet("QLabel{\n"
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
        self.ChargeBalanceBtn.setText("")
        self.ChargeBalanceBtn.setIcon(icon1)
        self.ChargeBalanceBtn.setIconSize(QtCore.QSize(45, 45))
        self.ChargeBalanceBtn.setCheckable(True)
        self.ChargeBalanceBtn.setAutoExclusive(False)
        self.ChargeBalanceBtn.setObjectName("ChargeBalanceBtn")
        self.gridLayout_2.addWidget(self.ChargeBalanceBtn, 1, 3, 1, 1)
        self.NTC2Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NTC2Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC2Btn.setFont(font)
        self.NTC2Btn.setStyleSheet("QLabel{\n"
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
        self.NTC2Btn.setText("")
        self.NTC2Btn.setIcon(icon1)
        self.NTC2Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC2Btn.setCheckable(True)
        self.NTC2Btn.setAutoExclusive(False)
        self.NTC2Btn.setObjectName("NTC2Btn")
        self.gridLayout_2.addWidget(self.NTC2Btn, 3, 3, 1, 1)
        self.NTC4Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NTC4Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC4Btn.setFont(font)
        self.NTC4Btn.setStyleSheet("QLabel{\n"
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
        self.NTC4Btn.setText("")
        self.NTC4Btn.setIcon(icon1)
        self.NTC4Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC4Btn.setCheckable(True)
        self.NTC4Btn.setAutoExclusive(False)
        self.NTC4Btn.setObjectName("NTC4Btn")
        self.gridLayout_2.addWidget(self.NTC4Btn, 4, 3, 1, 1)
        self.NTC5Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC5Btn.sizePolicy().hasHeightForWidth())
        self.NTC5Btn.setSizePolicy(sizePolicy)
        self.NTC5Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC5Btn.setFont(font)
        self.NTC5Btn.setStyleSheet("QLabel{\n"
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
        self.NTC5Btn.setText("")
        self.NTC5Btn.setIcon(icon1)
        self.NTC5Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC5Btn.setCheckable(True)
        self.NTC5Btn.setAutoExclusive(False)
        self.NTC5Btn.setObjectName("NTC5Btn")
        self.gridLayout_2.addWidget(self.NTC5Btn, 5, 0, 1, 1)
        self.NTC7Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC7Btn.sizePolicy().hasHeightForWidth())
        self.NTC7Btn.setSizePolicy(sizePolicy)
        self.NTC7Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC7Btn.setFont(font)
        self.NTC7Btn.setStyleSheet("QLabel{\n"
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
        self.NTC7Btn.setText("")
        self.NTC7Btn.setIcon(icon1)
        self.NTC7Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC7Btn.setCheckable(True)
        self.NTC7Btn.setAutoExclusive(False)
        self.NTC7Btn.setObjectName("NTC7Btn")
        self.gridLayout_2.addWidget(self.NTC7Btn, 6, 0, 1, 1)
        self.NTC3Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC3Label.sizePolicy().hasHeightForWidth())
        self.NTC3Label.setSizePolicy(sizePolicy)
        self.NTC3Label.setObjectName("NTC3Label")
        self.gridLayout_2.addWidget(self.NTC3Label, 4, 2, 1, 1)
        self.NTC4Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC4Label.sizePolicy().hasHeightForWidth())
        self.NTC4Label.setSizePolicy(sizePolicy)
        self.NTC4Label.setObjectName("NTC4Label")
        self.gridLayout_2.addWidget(self.NTC4Label, 4, 4, 1, 1)
        self.NTC7Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC7Label.sizePolicy().hasHeightForWidth())
        self.NTC7Label.setSizePolicy(sizePolicy)
        self.NTC7Label.setObjectName("NTC7Label")
        self.gridLayout_2.addWidget(self.NTC7Label, 6, 2, 1, 1)
        self.NTC1Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC1Label.sizePolicy().hasHeightForWidth())
        self.NTC1Label.setSizePolicy(sizePolicy)
        self.NTC1Label.setObjectName("NTC1Label")
        self.gridLayout_2.addWidget(self.NTC1Label, 3, 2, 1, 1)
        self.NTC8Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NTC8Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC8Btn.setFont(font)
        self.NTC8Btn.setStyleSheet("QLabel{\n"
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
        self.NTC8Btn.setText("")
        self.NTC8Btn.setIcon(icon1)
        self.NTC8Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC8Btn.setCheckable(True)
        self.NTC8Btn.setAutoExclusive(False)
        self.NTC8Btn.setObjectName("NTC8Btn")
        self.gridLayout_2.addWidget(self.NTC8Btn, 6, 3, 1, 1)
        self.NTC2Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC2Label.sizePolicy().hasHeightForWidth())
        self.NTC2Label.setSizePolicy(sizePolicy)
        self.NTC2Label.setObjectName("NTC2Label")
        self.gridLayout_2.addWidget(self.NTC2Label, 3, 4, 1, 1)
        self.NTC6Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC6Label.sizePolicy().hasHeightForWidth())
        self.NTC6Label.setSizePolicy(sizePolicy)
        self.NTC6Label.setObjectName("NTC6Label")
        self.gridLayout_2.addWidget(self.NTC6Label, 5, 4, 1, 1)
        self.NTC6Btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NTC6Btn.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.NTC6Btn.setFont(font)
        self.NTC6Btn.setStyleSheet("QLabel{\n"
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
        self.NTC6Btn.setText("")
        self.NTC6Btn.setIcon(icon1)
        self.NTC6Btn.setIconSize(QtCore.QSize(45, 45))
        self.NTC6Btn.setCheckable(True)
        self.NTC6Btn.setAutoExclusive(False)
        self.NTC6Btn.setObjectName("NTC6Btn")
        self.gridLayout_2.addWidget(self.NTC6Btn, 5, 3, 1, 1)
        self.NTC8Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NTC8Label.sizePolicy().hasHeightForWidth())
        self.NTC8Label.setSizePolicy(sizePolicy)
        self.NTC8Label.setObjectName("NTC8Label")
        self.gridLayout_2.addWidget(self.NTC8Label, 6, 4, 1, 1)
        self.BalanceEnableLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BalanceEnableLabel.sizePolicy().hasHeightForWidth())
        self.BalanceEnableLabel.setSizePolicy(sizePolicy)
        self.BalanceEnableLabel.setObjectName("BalanceEnableLabel")
        self.gridLayout_2.addWidget(self.BalanceEnableLabel, 1, 2, 1, 1)
        self.AssistBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.AssistBox_3.setGeometry(QtCore.QRect(5, 440, 768, 468))
        font = QtGui.QFont()
        font.setFamily("Luxi Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.AssistBox_3.setFont(font)
        self.AssistBox_3.setStyleSheet("QGroupBox::title{\n"
"    font = 50pt \"Magneto\";\n"
"    padding: 24 0px 0 0px\n"
"}\n"
"QLabel{\n"
"    font: 14pt \"Luxi Mono\";\n"
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
"margin: 0px 0px;}\n"
"\n"
"QDoubleSpinBox::up-button { \n"
"subcontrol-origin: margin;\n"
"subcontrol-position: center left;\n"
"width: 40px;\n"
"height: 43px;}\n"
"\n"
"QDoubleSpinBox::down-button { \n"
"width: 40px;\n"
"height: 43px;}\n"
"\n"
"QDoubleSpinBox{ font: 16pt \"Luxi Mono\";}")
        self.AssistBox_3.setObjectName("AssistBox_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.AssistBox_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(8, 55, 752, 408))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SelfDischargeLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SelfDischargeLabel.setObjectName("SelfDischargeLabel")
        self.gridLayout_4.addWidget(self.SelfDischargeLabel, 6, 0, 1, 1)
        self.SOC0Label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SOC0Label.setObjectName("SOC0Label")
        self.gridLayout_4.addWidget(self.SOC0Label, 5, 2, 1, 1)
        self.SOC40Label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SOC40Label.setObjectName("SOC40Label")
        self.gridLayout_4.addWidget(self.SOC40Label, 4, 2, 1, 1)
        self.ShuntSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShuntSpin.sizePolicy().hasHeightForWidth())
        self.ShuntSpin.setSizePolicy(sizePolicy)
        self.ShuntSpin.setDecimals(3)
        self.ShuntSpin.setMaximum(4.2)
        self.ShuntSpin.setSingleStep(0.001)
        self.ShuntSpin.setObjectName("ShuntSpin")
        self.gridLayout_4.addWidget(self.ShuntSpin, 1, 1, 1, 1)
        self.SOC100Label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SOC100Label.setObjectName("SOC100Label")
        self.gridLayout_4.addWidget(self.SOC100Label, 3, 0, 1, 1)
        self.SOC60Label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SOC60Label.setObjectName("SOC60Label")
        self.gridLayout_4.addWidget(self.SOC60Label, 4, 0, 1, 1)
        self.SOC20Label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SOC20Label.setObjectName("SOC20Label")
        self.gridLayout_4.addWidget(self.SOC20Label, 5, 0, 1, 1)
        self.FETControlLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.FETControlLabel.setObjectName("FETControlLabel")
        self.gridLayout_4.addWidget(self.FETControlLabel, 6, 2, 1, 1)
        self.CycleCountSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CycleCountSpin.sizePolicy().hasHeightForWidth())
        self.CycleCountSpin.setSizePolicy(sizePolicy)
        self.CycleCountSpin.setMaximum(100000.0)
        self.CycleCountSpin.setSingleStep(1.0)
        self.CycleCountSpin.setObjectName("CycleCountSpin")
        self.gridLayout_4.addWidget(self.CycleCountSpin, 1, 3, 1, 1)
        self.CycleCapSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CycleCapSpin.sizePolicy().hasHeightForWidth())
        self.CycleCapSpin.setSizePolicy(sizePolicy)
        self.CycleCapSpin.setMaximum(200.0)
        self.CycleCapSpin.setSingleStep(0.1)
        self.CycleCapSpin.setObjectName("CycleCapSpin")
        self.gridLayout_4.addWidget(self.CycleCapSpin, 2, 3, 1, 1)
        self.SOC80Spin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOC80Spin.sizePolicy().hasHeightForWidth())
        self.SOC80Spin.setSizePolicy(sizePolicy)
        self.SOC80Spin.setMaximum(4200.0)
        self.SOC80Spin.setSingleStep(0.1)
        self.SOC80Spin.setObjectName("SOC80Spin")
        self.gridLayout_4.addWidget(self.SOC80Spin, 3, 3, 1, 1)
        self.SOC40Spin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOC40Spin.sizePolicy().hasHeightForWidth())
        self.SOC40Spin.setSizePolicy(sizePolicy)
        self.SOC40Spin.setMaximum(4200.0)
        self.SOC40Spin.setSingleStep(0.5)
        self.SOC40Spin.setObjectName("SOC40Spin")
        self.gridLayout_4.addWidget(self.SOC40Spin, 4, 3, 1, 1)
        self.SOC0Spin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOC0Spin.sizePolicy().hasHeightForWidth())
        self.SOC0Spin.setSizePolicy(sizePolicy)
        self.SOC0Spin.setMaximum(4200.0)
        self.SOC0Spin.setSingleStep(0.5)
        self.SOC0Spin.setObjectName("SOC0Spin")
        self.gridLayout_4.addWidget(self.SOC0Spin, 5, 3, 1, 1)
        self.CellCountLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.CellCountLabel.setObjectName("CellCountLabel")
        self.gridLayout_4.addWidget(self.CellCountLabel, 7, 2, 1, 1)
        self.LEDTimerLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.LEDTimerLabel.setObjectName("LEDTimerLabel")
        self.gridLayout_4.addWidget(self.LEDTimerLabel, 7, 0, 1, 1)
        self.SOC20Spin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOC20Spin.sizePolicy().hasHeightForWidth())
        self.SOC20Spin.setSizePolicy(sizePolicy)
        self.SOC20Spin.setMaximum(4200.0)
        self.SOC20Spin.setSingleStep(0.5)
        self.SOC20Spin.setObjectName("SOC20Spin")
        self.gridLayout_4.addWidget(self.SOC20Spin, 5, 1, 1, 1)
        self.SOC60Spin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOC60Spin.sizePolicy().hasHeightForWidth())
        self.SOC60Spin.setSizePolicy(sizePolicy)
        self.SOC60Spin.setMaximum(4200.0)
        self.SOC60Spin.setSingleStep(0.5)
        self.SOC60Spin.setObjectName("SOC60Spin")
        self.gridLayout_4.addWidget(self.SOC60Spin, 4, 1, 1, 1)
        self.SelfDschgSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelfDschgSpin.sizePolicy().hasHeightForWidth())
        self.SelfDschgSpin.setSizePolicy(sizePolicy)
        self.SelfDschgSpin.setMaximum(70.0)
        self.SelfDschgSpin.setSingleStep(0.5)
        self.SelfDschgSpin.setObjectName("SelfDschgSpin")
        self.gridLayout_4.addWidget(self.SelfDschgSpin, 6, 1, 1, 1)
        self.CycleCapLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.CycleCapLabel.setObjectName("CycleCapLabel")
        self.gridLayout_4.addWidget(self.CycleCapLabel, 2, 2, 1, 1)
        self.SOC80Label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.SOC80Label.setObjectName("SOC80Label")
        self.gridLayout_4.addWidget(self.SOC80Label, 3, 2, 1, 1)
        self.SOC100Spin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SOC100Spin.sizePolicy().hasHeightForWidth())
        self.SOC100Spin.setSizePolicy(sizePolicy)
        self.SOC100Spin.setMaximum(4200.0)
        self.SOC100Spin.setSingleStep(0.1)
        self.SOC100Spin.setObjectName("SOC100Spin")
        self.gridLayout_4.addWidget(self.SOC100Spin, 3, 1, 1, 1)
        self.BalanceStartSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BalanceStartSpin.sizePolicy().hasHeightForWidth())
        self.BalanceStartSpin.setSizePolicy(sizePolicy)
        self.BalanceStartSpin.setMaximum(4.2)
        self.BalanceStartSpin.setSingleStep(0.01)
        self.BalanceStartSpin.setObjectName("BalanceStartSpin")
        self.gridLayout_4.addWidget(self.BalanceStartSpin, 0, 1, 1, 1)
        self.LEDTimerSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEDTimerSpin.sizePolicy().hasHeightForWidth())
        self.LEDTimerSpin.setSizePolicy(sizePolicy)
        self.LEDTimerSpin.setMaximum(70.0)
        self.LEDTimerSpin.setSingleStep(0.5)
        self.LEDTimerSpin.setObjectName("LEDTimerSpin")
        self.gridLayout_4.addWidget(self.LEDTimerSpin, 7, 1, 1, 1)
        self.DesignCapSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DesignCapSpin.sizePolicy().hasHeightForWidth())
        self.DesignCapSpin.setSizePolicy(sizePolicy)
        self.DesignCapSpin.setMaximum(200.0)
        self.DesignCapSpin.setSingleStep(0.1)
        self.DesignCapSpin.setObjectName("DesignCapSpin")
        self.gridLayout_4.addWidget(self.DesignCapSpin, 2, 1, 1, 1)
        self.BalanceWindowLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.BalanceWindowLabel.setObjectName("BalanceWindowLabel")
        self.gridLayout_4.addWidget(self.BalanceWindowLabel, 0, 2, 1, 1)
        self.BalanceStartLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.BalanceStartLabel.setObjectName("BalanceStartLabel")
        self.gridLayout_4.addWidget(self.BalanceStartLabel, 0, 0, 1, 1)
        self.ShuntLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.ShuntLabel.setObjectName("ShuntLabel")
        self.gridLayout_4.addWidget(self.ShuntLabel, 1, 0, 1, 1)
        self.CycleCountLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.CycleCountLabel.setObjectName("CycleCountLabel")
        self.gridLayout_4.addWidget(self.CycleCountLabel, 1, 2, 1, 1)
        self.BalanceWindowSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BalanceWindowSpin.sizePolicy().hasHeightForWidth())
        self.BalanceWindowSpin.setSizePolicy(sizePolicy)
        self.BalanceWindowSpin.setDecimals(0)
        self.BalanceWindowSpin.setMaximum(100.0)
        self.BalanceWindowSpin.setSingleStep(1.0)
        self.BalanceWindowSpin.setObjectName("BalanceWindowSpin")
        self.gridLayout_4.addWidget(self.BalanceWindowSpin, 0, 3, 1, 1)
        self.CellCntSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CellCntSpin.sizePolicy().hasHeightForWidth())
        self.CellCntSpin.setSizePolicy(sizePolicy)
        self.CellCntSpin.setMaximum(70.0)
        self.CellCntSpin.setSingleStep(0.5)
        self.CellCntSpin.setObjectName("CellCntSpin")
        self.gridLayout_4.addWidget(self.CellCntSpin, 7, 3, 1, 1)
        self.FETControlSpin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FETControlSpin.sizePolicy().hasHeightForWidth())
        self.FETControlSpin.setSizePolicy(sizePolicy)
        self.FETControlSpin.setMaximum(70.0)
        self.FETControlSpin.setSingleStep(0.5)
        self.FETControlSpin.setObjectName("FETControlSpin")
        self.gridLayout_4.addWidget(self.FETControlSpin, 6, 3, 1, 1)
        self.DesignCapLabel = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.DesignCapLabel.setObjectName("DesignCapLabel")
        self.gridLayout_4.addWidget(self.DesignCapLabel, 2, 0, 1, 1)
        self.AssistBox.raise_()
        self.Functions.raise_()
        self.AssistBox_3.raise_()
        self.ExitBtn.raise_()
        self.WriteEepromBtn.raise_()
        self.ReadEepromBtn.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(bmscfg)
        QtCore.QMetaObject.connectSlotsByName(bmscfg)

    def retranslateUi(self, bmscfg):
        _translate = QtCore.QCoreApplication.translate
        bmscfg.setWindowTitle(_translate("bmscfg", "Form"))
        self.ReadEepromBtn.setText(_translate("bmscfg", "Read"))
        self.WriteEepromBtn.setText(_translate("bmscfg", "Write"))
        self.ExitBtn.setText(_translate("bmscfg", "Back"))
        self.AssistBox.setTitle(_translate("bmscfg", "Protection Configuration"))
        self.CUVPDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.DSGUTDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.PUVPDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.PVOPDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.CHGOCDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.CHGOTDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.PUVPLabel.setText(_translate("bmscfg", "PUVP<sub>mV</sub>"))
        self.CHGOT.setText(_translate("bmscfg", "CHGOT<sub>°C</sub>"))
        self.CHGUT.setText(_translate("bmscfg", "CHGUT<sub>°C</sub>"))
        self.DSGOT.setText(_translate("bmscfg", "DSGOT<sub>°C</sub>"))
        self.label_13.setText(_translate("bmscfg", "Rel<sub>°C</sub>"))
        self.CHGUTReleaseLabel.setText(_translate("bmscfg", "Rel<sub>°C</sub>"))
        self.CHGOTReleaseLabel.setText(_translate("bmscfg", "Rel<sub>°C</sub>"))
        self.DSCHOCReleaseLabel.setText(_translate("bmscfg", "Rel<sub>S</sub>"))
        self.DSGUTReleaseLabel.setText(_translate("bmscfg", "Rel<sub>°C</sub>"))
        self.CHGOCReleaseLabel.setText(_translate("bmscfg", "Rel<sub>S</sub>"))
        self.DSGUT.setText(_translate("bmscfg", "DSGUT<sub>°C</sub>"))
        self.CHGUTDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.label_27.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.POVPReleaseLabel.setText(_translate("bmscfg", "Rel<sub>mV</sub>"))
        self.PUVPReleaseLabel.setText(_translate("bmscfg", "Rel<sub>mV</sub>"))
        self.CHGOCLabel.setText(_translate("bmscfg", "CHGOC<sub>A</sub>"))
        self.DSGOC.setText(_translate("bmscfg", "DSCHOC<sub>A</sub>"))
        self.DSCHOCDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.POVPLabel.setText(_translate("bmscfg", "POVP<sub>mV</sub>"))
        self.COVPDelayLabel.setText(_translate("bmscfg", "Delay<sub>S</sub>"))
        self.COVPReleaseLabel.setText(_translate("bmscfg", "Rel<sub>mV</sub>"))
        self.COVPLabel.setText(_translate("bmscfg", "COVP<sub>mV</sub>"))
        self.CUVPLabel.setText(_translate("bmscfg", "CUVP<sub>mV</sub>"))
        self.CUVPReleaseLabel.setText(_translate("bmscfg", "Rel<sub>mV</sub>"))
        self.Functions.setTitle(_translate("bmscfg", "Functions"))
        self.SCReleaseLabel.setText(_translate("bmscfg", "SC Release"))
        self.NTC5Label.setText(_translate("bmscfg", "NTC5"))
        self.ChargeBalanceLabel.setText(_translate("bmscfg", "Charge Balance"))
        self.LEDEnableLabel.setText(_translate("bmscfg", "LED Enable"))
        self.LEDNumberLabel.setText(_translate("bmscfg", "LED Number"))
        self.SwitchLabel.setText(_translate("bmscfg", "Switch"))
        self.NTC3Label.setText(_translate("bmscfg", "NTC3"))
        self.NTC4Label.setText(_translate("bmscfg", "NTC4"))
        self.NTC7Label.setText(_translate("bmscfg", "NTC7"))
        self.NTC1Label.setText(_translate("bmscfg", "NTC1"))
        self.NTC2Label.setText(_translate("bmscfg", "NTC2"))
        self.NTC6Label.setText(_translate("bmscfg", "NTC6"))
        self.NTC8Label.setText(_translate("bmscfg", "NTC8"))
        self.BalanceEnableLabel.setText(_translate("bmscfg", "Balance Enable"))
        self.AssistBox_3.setTitle(_translate("bmscfg", "Balance And Misc. Configuration"))
        self.SelfDischargeLabel.setText(_translate("bmscfg", "Self-Dschg Rate<sub>%</sub>"))
        self.SOC0Label.setText(_translate("bmscfg", "0% SOC<sub>mV</sub>"))
        self.SOC40Label.setText(_translate("bmscfg", "40% SOC<sub>mV</sub>"))
        self.SOC100Label.setText(_translate("bmscfg", "100% SOC<sub>mV</sub> "))
        self.SOC60Label.setText(_translate("bmscfg", "60% SOC<sub>mV</sub>"))
        self.SOC20Label.setText(_translate("bmscfg", "20% SOC<sub>mV</sub>"))
        self.FETControlLabel.setText(_translate("bmscfg", "FET Control<sub>S</sub>"))
        self.CellCountLabel.setText(_translate("bmscfg", "CellCnt <sup>CAUTION</sup>"))
        self.LEDTimerLabel.setText(_translate("bmscfg", "LED timer<sub>S</sub>"))
        self.CycleCapLabel.setText(_translate("bmscfg", "Cycle Ah"))
        self.SOC80Label.setText(_translate("bmscfg", "80% SOC<sub>mV</sub>"))
        self.BalanceWindowLabel.setText(_translate("bmscfg", "Balance Window<sub>mV</sub>"))
        self.BalanceStartLabel.setText(_translate("bmscfg", "Balance Start<sub>V</sub>"))
        self.ShuntLabel.setText(_translate("bmscfg", "Shunt Ω"))
        self.CycleCountLabel.setText(_translate("bmscfg", "Cycle count"))
        self.DesignCapLabel.setText(_translate("bmscfg", "Design Ah"))
import ampy_rc
