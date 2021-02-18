from PyQt5 import QtCore, QtWidgets
from ampy_bms import Ui_BMSDialog

from jbdMain import JBD

class bmsDialog(QtWidgets.QWidget):
    #bmspoll = QtCore.pyqtSignal(int) # jbdcell/jbdbasic for cellv, balance state.
    bmscut = QtCore.pyqtSignal(int)
    bmsbal = QtCore.pyqtSignal(int)
    #bmsbasicreceiver = QtCore.pyqtSignal(object)
    #bmseepromreciever = QtCore.pyqtSignal(object)
    def __init__(self, *args, **kwargs):
        super(bmsDialog, self).__init__(parent=None, *args, **kwargs) # can be inherited with parent = parent
        #self.parent = parent
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.setParent(parent)
        #self.parent = parent
        self.ui = Ui_BMSDialog()
        self.basicMsg = None
        self.eepromMsg = None
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        #self.bmspoll.emit(1) # May not be needed
        # todo: copy EEPROM to this cfg for easier ui?
        # todo: Figure out how to inherit parent data here, or give up and implement ui setup in main.
        # Emulate main.py and create another QThreader to handle BMS serial.
        self.ui.ExitBtn.clicked.connect(lambda: self.hide())
        self.ui.ChargeLevelSlider.valueChanged.connect(lambda: self.bmscutoff(self.ui.ChargeLevelSlider.value()))
        self.ui.BalanceLevelSlider.valueChanged.connect(lambda: self.bmsbalance(self.ui.BalanceLevelSlider.value()))
        #self.ui.DisplayInvertBtn.toggled.connect(lambda: self.displayInvert(self.ui.DisplayInvertBtn.isChecked()))
        #self.ui.DisplayInvertBtn.setChecked(self.displayinvert_bool)
        #self.ui.DisplaySlider.valueChanged.connect(self.displayBacklight)
    def close(self):
        #self.bmspoll.emit(0)
        pass
    def bmscutoff(self, val):
        self.ui.ChargeLevelLabel.setText('{:.3f}'.format(val/1000))
    def bmsbalance(self, val):
        self.ui.BalanceVLabel.setText('{:.3f}'.format(val/1000))
    @QtCore.pyqtSlot(object)  # dict of BMS reads.
    def bmsBasicUpdate(self, msg):
        self.basicMsg = msg
        keys = ['cell0_mv', 'cell1_mv', 'cell2_mv', 'cell3_mv', 'cell4_mv', 'cell5_mv', 'cell6_mv', 'cell7_mv',
                'cell8_mv', 'cell9_mv', 'cell10_mv', 'cell11_mv', 'cell12_mv', 'cell13_mv', 'cell14_mv', 'cell15_mv',
                'cell16_mv', 'cell17_mv', 'cell18_mv', 'cell19_mv', 'cell20_mv']
        cellv = []
        for i in keys:
            cellv.append(self.basicMsg[0][i] / 1000)
        cellvmin = min(cellv)
        cellvmax = max(cellv)
        self.ui.VRangeLabel.setText('{:.2f}'.format(cellvmax) + '~' + '{:.2f}'.format(cellvmin)
                                                   + '<sub>V</sub>')
        self.ui.VDiffLabel.setText('{:.3f}'.format(cellvmax - cellvmin) + '<sub>V</sub>')
        # Voltage Bars
        self.ui.C1Bar.setValue(self.basicMsg[0]['cell0_mv'])
        self.ui.C2Bar.setValue(self.basicMsg[0]['cell1_mv'])
        self.ui.C3Bar.setValue(self.basicMsg[0]['cell2_mv'])
        self.ui.C4Bar.setValue(self.basicMsg[0]['cell3_mv'])
        self.ui.C5Bar.setValue(self.basicMsg[0]['cell4_mv'])
        self.ui.C6Bar.setValue(self.basicMsg[0]['cell5_mv'])
        self.ui.C7Bar.setValue(self.basicMsg[0]['cell6_mv'])
        self.ui.C8Bar.setValue(self.basicMsg[0]['cell7_mv'])
        self.ui.C9Bar.setValue(self.basicMsg[0]['cell8_mv'])
        self.ui.C10Bar.setValue(self.basicMsg[0]['cell9_mv'])
        self.ui.C11Bar.setValue(self.basicMsg[0]['cell10_mv'])
        self.ui.C12Bar.setValue(self.basicMsg[0]['cell11_mv'])
        self.ui.C13Bar.setValue(self.basicMsg[0]['cell12_mv'])
        self.ui.C14Bar.setValue(self.basicMsg[0]['cell13_mv'])
        self.ui.C15Bar.setValue(self.basicMsg[0]['cell14_mv'])
        self.ui.C16Bar.setValue(self.basicMsg[0]['cell15_mv'])
        self.ui.C17Bar.setValue(self.basicMsg[0]['cell16_mv'])
        self.ui.C18Bar.setValue(self.basicMsg[0]['cell17_mv'])
        self.ui.C19Bar.setValue(self.basicMsg[0]['cell18_mv'])
        self.ui.C20Bar.setValue(self.basicMsg[0]['cell19_mv'])
        self.ui.C21Bar.setValue(self.basicMsg[0]['cell20_mv'])
        # Balance LED's
        self.ui.C1Balance.setChecked(self.basicMsg[1]['bal0'])
        self.ui.C2Balance.setChecked(self.basicMsg[1]['bal1'])
        self.ui.C3Balance.setChecked(self.basicMsg[1]['bal2'])
        self.ui.C4Balance.setChecked(self.basicMsg[1]['bal3'])
        self.ui.C5Balance.setChecked(self.basicMsg[1]['bal4'])
        self.ui.C6Balance.setChecked(self.basicMsg[1]['bal5'])
        self.ui.C7Balance.setChecked(self.basicMsg[1]['bal6'])
        self.ui.C8Balance.setChecked(self.basicMsg[1]['bal7'])
        self.ui.C9Balance.setChecked(self.basicMsg[1]['bal8'])
        self.ui.C10Balance.setChecked(self.basicMsg[1]['bal9'])
        self.ui.C11Balance.setChecked(self.basicMsg[1]['bal10'])
        self.ui.C12Balance.setChecked(self.basicMsg[1]['bal11'])
        self.ui.C13Balance.setChecked(self.basicMsg[1]['bal12'])
        self.ui.C14Balance.setChecked(self.basicMsg[1]['bal13'])
        self.ui.C15Balance.setChecked(self.basicMsg[1]['bal14'])
        self.ui.C16Balance.setChecked(self.basicMsg[1]['bal15'])
        self.ui.C17Balance.setChecked(self.basicMsg[1]['bal16'])
        self.ui.C18Balance.setChecked(self.basicMsg[1]['bal17'])
        self.ui.C19Balance.setChecked(self.basicMsg[1]['bal18'])
        self.ui.C20Balance.setChecked(self.basicMsg[1]['bal19'])
        self.ui.C21Balance.setChecked(self.basicMsg[1]['bal20'])
        # Temp, Current, Power
        self.ui.CurrentLabel.setText(
            '{:.2f}'.format(self.basicMsg[1]['pack_ma'] / 1000) + '<sub>A</sub>')
        self.ui.PowerLabel.setText('{:.1f}'.format(((self.basicMsg[1]['pack_ma'] / 1000) *
                                                                   (self.basicMsg[1][
                                                                        'pack_mv'] / 1000))) + '<sub>W</sub>')
        self.ui.T1Bar.setValue(self.basicMsg[1]['ntc0'])
        self.ui.T2Bar.setValue(self.basicMsg[1]['ntc1'])
        self.ui.T3Bar.setValue(self.basicMsg[1]['ntc2'])
        self.ui.T4Bar.setValue(self.basicMsg[1]['ntc3'])
    @QtCore.pyqtSlot(object)
    def bmsEepromUpdate(self, msg):
        self.eepromMsg = msg
        self.ui.ChargeLevelSlider.setValue(self.eepromMsg[0]['covp'])
        self.ui.BalanceLevelSlider.setValue(self.eepromMsg[0]['bal_start'])
        self.ui.BalanceVLabel.setText(
            '{:.2f}'.format(self.eepromMsg[0]['bal_start'] / 1000))
        self.ui.BalanceLevelSlider.setValue(self.eepromMsg[0]['bal_start'])
        self.ui.ChargeLevelSlider.setValue(self.eepromMsg[0]['covp'])
        self.ui.ChargeLevelLabel.setText(
            '{:.2f}'.format(self.eepromMsg[0]['covp'] / 1000))

    #def displayInvert(self, bool):
    #    self.displayinvertmsg.emit(bool)
    #def displayBacklight(self):
    #    level = self.ui.DisplaySlider.value()
    #    self.ui.BacklightLabel.setText('Backlight: ' + str(level))
    #    self.displaybacklightcmd.emit(level)



# Setup PID tuning, range limiter, total power slider...
