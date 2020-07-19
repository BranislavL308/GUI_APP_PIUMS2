from PyQt5.QtWidgets import QDialog
from dialogUI import *
import serial
from serial.tools import list_ports


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        #Podesavanje pocetnih vrednosti comboBox-a
        self.dialog.comboBoxBaudRate.setCurrentIndex(2)
        self.dialog.comboBoxDataBits.setCurrentIndex(3)
        #self.dialog.comboBoxParityBit.setCurrentIndex()
        #self.dialog.comboBoxStopBit.setCurrentIndex()

        #Kada kliknemo OK vrati nam 0
        #self.dialog.pushButton.clicked.connect(self.reject)
        #Kada kliknemo OK vrati nam 1
        self.dialog.pushButton.clicked.connect(self.accept)

        availablePorts = list_ports.comports()
        #Prodji kroz svaki objekat i upisi njegov device kod u listu
        for i in availablePorts:
            self.dialog.comboBox.addItem(str(i.device))
        self.returnVal = {} #Prazan recnik


    #Funkcija koja ce nam pokupiti podatke za dialog prozora (PORT,Baud rate, ...)
    def get_data(self):
        self.returnVal['com_port'] = self.dialog.comboBox.currentText()
        self.returnVal['baud_rate'] = int(self.dialog.comboBoxBaudRate.currentText())

        tmp = self.dialog.comboBoxDataBits.currentText()
        if(tmp == '5'):
            self.returnVal['data_bits'] = serial.FIVEBITS
        if(tmp == '6'):
            self.returnVal['data_bits'] = serial.SIXBITS
        if(tmp == '7'):
            self.returnVal['data_bits'] = serial.SEVENBITS
        if(tmp == '8'):
            self.returnVal['data_bits'] = serial.EIGHTBITS

        tmp = self.dialog.comboBoxParityBit.currentText()
        if(tmp == 'None'):
            self.returnVal['parity'] = serial.PARITY_NONE
        if(tmp == 'Even'):
            self.returnVal['parity'] = serial.PARITY_EVEN
        if(tmp == 'Mark'):
            self.returnVal['parity'] = serial.PARITY_MARK
        if(tmp == 'Space'):
            self.returnVal['parity'] = serial.PARITY_SPACE
        if(tmp == 'Odd'):
            self.returnVal['parity'] = serial.PARITY_ODD


        tmp =self.dialog.comboBoxStopBit.currentText()
        if(tmp == '1'):
            self.returnVal['stop_bit'] = serial.STOPBITS_ONE
        if(tmp == '1.5'):
            self.returnVal['stop_bit'] = serial.STOPBITS_ONE_POINT_FIVE
        if(tmp == '2'):
            self.returnVal['stop_bit'] = serial.STOPBITS_TWO

        return self.returnVal
