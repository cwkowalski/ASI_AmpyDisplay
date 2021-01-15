from PyQt5 import QtCore, QtGui, QtWidgets
from ampy_options import Ui_OptDialog

class optionsDialog(QtWidgets.QWidget):
    def __init__(self, parent, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.parent = parent
        self.ui = Ui_OptDialog()
        self.ui.setupUi(self)
        self.ui.ExitBtn.clicked.connect(lambda: self.hide())
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        print('potatoes')
        # self.VARIABLE = VARIABLE_PASSED_TO_INIT_WHEN_CLASS_INSTANTIATED
        # E.g. to set default values of gui elements.

# Setup PID tuning, range limiter, total power slider...
