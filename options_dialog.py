from PyQt5 import QtCore, QtWidgets
from ampy_options import Ui_OptDialog

class optionsDialog(QtWidgets.QWidget):
    displayinvertmsg = QtCore.pyqtSignal(int)
    def __init__(self, displayinvert_bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.displayinvert_bool = displayinvert_bool
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.setParent(parent)
        #self.parent = parent
        self.ui = Ui_OptDialog()
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        self.ui.ExitBtn.clicked.connect(lambda: self.hide())
        self.ui.DisplayInvertBtn.toggled.connect(lambda: self.displayInvert(self.ui.DisplayInvertBtn.isChecked()))
        self.ui.DisplayInvertBtn.setChecked(self.displayinvert_bool)
    def displayInvert(self, bool):
        self.displayinvertmsg.emit(bool)




# Setup PID tuning, range limiter, total power slider...
