from PyQt5 import QtCore, QtGui, QtWidgets
from ampy_options import Ui_OptDialog

class optionsDialog(QtWidgets.QWidget):
    displayinvertmsg = QtCore.pyqtSignal(int)
    def __init__(self, parent, *args, **kwargs):
        super(optionsDialog).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.setParent(parent)
        #self.parent = parent
        self.ui = Ui_OptDialog()
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        print('potatoes')
        # self.VARIABLE = VARIABLE_PASSED_TO_INIT_WHEN_CLASS_INSTANTIATED
        # E.g. to set default values of gui elements.
    def initUI(self):
        self.ui.ExitBtn.clicked.connect(lambda: self.hide())
        self.ui.setupUi(self)
        self.ui.DisplayInvertBtn.toggled.connect(lambda: self.displayInvert(self.ui.DisplayInvertBtn.isChecked()))

    def displayInvert(self, bool):
        self.displayinvertmsg.emit(bool)



# Setup PID tuning, range limiter, total power slider...
