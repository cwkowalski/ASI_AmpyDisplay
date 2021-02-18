from PyQt5 import QtCore, QtWidgets
from ampy_bmsconfig import Ui_bmscfg

from jbdMain import JBD

class bmscfgDialog(QtWidgets.QWidget):
    #bmspoll = QtCore.pyqtSignal(int) # jbdcell/jbdbasic for cellv, balance state.
    #bmscut = QtCore.pyqtSignal(int)
    #bmsbal = QtCore.pyqtSignal(int)
    eepromGet = QtCore.pyqtSignal()
    eepromWrite = QtCore.pyqtSignal() # Should this signal be here, or parent?
    def __init__(self, *args, **kwargs):
        super(bmscfgDialog, self).__init__(*args, **kwargs)
        #self.parent = parent
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.eepromMsg = None
        self.ui = Ui_bmscfg()
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        self.initUI()
    def initUI(self):
        self.ui.setupUi(self)
        self.ui.ExitBtn.clicked.connect(lambda: self.hide())
        #todo: Make a shitload of connections
    def close(self):
        #self.bmspoll.emit(0)
        pass
    @QtCore.pyqtSlot(object)
    def eepromReceiver(self, msg):
        self.eeprom = msg
    def eepromGetter(self):
        self.eepromGet.emit()
    def bmscfgGuiUpdate(self, msg):
        self.eepromMsg = msg
        # BMS Functions (Switches)
        self.ui.SwitchBtn.setChecked(self.eepromMsg[0]['switch'])
        self.ui.SCReleaseBtn.setChecked(self.eepromMsg[0]['scrl'])
        self.ui.BalanceEnableBtn.setChecked(self.eepromMsg[0]['balance_en'])
        self.ui.ChargeBalanceBtn.setChecked(self.eepromMsg[0]['chg_balance_en'])
        self.ui.LEDEnableBtn.setChecked(self.eepromMsg[0]['led_en'])
        self.ui.LEDNumberBtn.setChecked(self.eepromMsg[0]['led_num'])
        self.ui.NTC1Btn.setChecked(self.eepromMsg[0]['ntc1'])
        self.ui.NTC2Btn.setChecked(self.eepromMsg[0]['ntc2'])
        self.ui.NTC3Btn.setChecked(self.eepromMsg[0]['ntc3'])
        self.ui.NTC4Btn.setChecked(self.eepromMsg[0]['ntc4'])
        self.ui.NTC5Btn.setChecked(self.eepromMsg[0]['ntc5'])
        self.ui.NTC6Btn.setChecked(self.eepromMsg[0]['ntc6'])
        self.ui.NTC7Btn.setChecked(self.eepromMsg[0]['ntc7'])
        self.ui.NTC8Btn.setChecked(self.eepromMsg[0]['ntc8'])
        # Balance and Misc Configuration
        self.ui.BalanceStartSpin.setValue(self.eepromMsg[0]['bal_start'] / 1000)
        self.ui.BalanceWindowSpin.setValue(self.eepromMsg[0]['bal_window'])
        self.ui.ShuntSpin.setValue(self.eepromMsg[0]['shunt_res'])
        self.ui.CycleCountSpin.setValue(self.eepromMsg[0]['cycle_cnt'])
        self.ui.DesignCapSpin.setValue(self.eepromMsg[0]['design_cap'] / 1000)
        self.ui.CycleCapSpin.setValue(self.eepromMsg[0]['cycle_cap'] / 1000)
        self.ui.SOC100Spin.setValue(self.eepromMsg[0]['cap_100'])
        self.ui.SOC80Spin.setValue(self.eepromMsg[0]['cap_80'])
        self.ui.SOC60Spin.setValue(self.eepromMsg[0]['cap_60'])
        self.ui.SOC40Spin.setValue(self.eepromMsg[0]['cap_40'])
        self.ui.SOC20Spin.setValue(self.eepromMsg[0]['cap_20'])
        self.ui.SOC0Spin.setValue(self.eepromMsg[0]['cap_0'])
        self.ui.SelfDschgSpin.setValue(self.eepromMsg[0]['dsg_rate'])
        self.ui.FETControlSpin.setValue(self.eepromMsg[0]['fet_ctrl'])
        self.ui.LEDTimerSpin.setValue(self.eepromMsg[0]['led_timer'])
        self.ui.CellCntSpin.setValue(self.eepromMsg[0]['cell_cnt'])
        # Protection Configuration
        self.ui.COVPSpin.setValue(self.eepromMsg[0]['covp'] / 1000)
        self.ui.CUVPSpin.setValue(self.eepromMsg[0]['cuvp'] / 1000)
        self.ui.POVPSpin.setValue(self.eepromMsg[0]['povp'] / 1000)
        self.ui.PUVPSpin.setValue(self.eepromMsg[0]['puvp'] / 1000)
        self.ui.CHGOTSpin.setValue(self.eepromMsg[0]['chgot'])
        self.ui.CHGUTSpin.setValue(self.eepromMsg[0]['chgut'])
        self.ui.DSGOTSpin.setValue(self.eepromMsg[0]['dsgot'])
        self.ui.DSGUTSpin.setValue(self.eepromMsg[0]['dsgut'])
        self.ui.CHGOCSpin.setValue(self.eepromMsg[0]['chgoc'] / 1000)
        self.ui.DSCHOCSpin.setValue(self.eepromMsg[0]['dsgoc'] / 1000)
        self.ui.COVPReleaseSpin.setValue(self.eepromMsg[0]['covp_rel'] / 1000)
        self.ui.CUVPReleaseSpin.setValue(self.eepromMsg[0]['cuvp_rel'] / 1000)
        self.ui.POVPReleaseSpin.setValue(self.eepromMsg[0]['povp_rel'] / 1000)
        self.ui.PUVPReleaseSpin.setValue(self.eepromMsg[0]['puvp_rel'] / 1000)
        self.ui.CHGOTReleaseSpin.setValue(self.eepromMsg[0]['chgot_rel'])
        self.ui.CHGUTReleaseSpin.setValue(self.eepromMsg[0]['chgut_rel'])
        self.ui.DSGOTReleaseSpin.setValue(self.eepromMsg[0]['dsgot_rel'])
        self.ui.DSGUTReleaseSpin.setValue(self.eepromMsg[0]['dsgut_rel'])
        self.ui.CHGOCReleaseSpin.setValue(self.eepromMsg[0]['chgoc_rel'])
        self.ui.DSCHOCReleaseSpin.setValue(self.eepromMsg[0]['dsgoc_rel'])
        self.ui.COVPDelaySpin.setValue(self.eepromMsg[0]['covp_delay'])
        self.ui.CUVPDelaySpin.setValue(self.eepromMsg[0]['cuvp_delay'])
        self.ui.POVPDelaySpin.setValue(self.eepromMsg[0]['povp_delay'])
        self.ui.PUVPDelaySpin.setValue(self.eepromMsg[0]['puvp_delay'])
        self.ui.CHGOTDelaySpin.setValue(self.eepromMsg[0]['chgot_delay'])
        self.ui.CHGUTDelaySpin.setValue(self.eepromMsg[0]['chgut_delay'])
        self.ui.DSGOTDelaySpin.setValue(self.eepromMsg[0]['dsgot_delay'])
        self.ui.DSGUTDelaySpin.setValue(self.eepromMsg[0]['dsgut_delay'])
        self.ui.CHGOCDelaySpin.setValue(self.eepromMsg[0]['chgoc_delay'])
        self.ui.DSCHOCDelaySpin.setValue(self.eepromMsg[0]['dsgoc_delay'])