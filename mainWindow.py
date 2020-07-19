from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mainWindowUI import *
from settingsDialog import *
from communicationThread import *
from mongoDBThread import *
from graphThread import *
from serial import Serial

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.returnValue = None

      
        
        #tastera (UART/Settings/Stat/Open)
        self.ui.actionStart.setEnabled(False)
        self.ui.actionStop.setEnabled(False)

        self.ui.actionSettings.triggered.connect(self.config)



        #Startovanje komunikacije
        self.ui.actionStart.triggered.connect(self.open_com)
        #Prekidanje komunikacije
        self.ui.actionStop.triggered.connect(self.close_com)

        #Kada pritisnemo na settings file pokrecemo prozor dialogUI (Intanciramo objekat klase SettingsWindow)
    def config(self):
        self.ui.actionStart.setEnabled(False)
        self.ui.actionStop.setEnabled(False)
        self.settingsDialog = SettingsDialog()
        #self.settingsDialog.exec_() #funkcija .exec_ pokrece nas prozor

        response = self.settingsDialog.exec_() #funkcija .exec_ pokrece nas prozor
        #Ako pritisnemo x dobijemo 0
        #Ako pritisnemo OK dobijemo 1

        #Ako je korisnik odgovorio sa response onda pozivamo metodu
        if(response):
            self.returnValue = self.settingsDialog.get_data()
            self.ui.actionStart.setEnabled(True)
            self.ui.actionStop.setEnabled(False)

        else:
            self.returnValue = None

        print(self.returnValue['com_port'])


        #Funkcija za otravarnje komunikacije
    def open_com(self):
        self.ui.actionSettings.setEnabled(False)
        self.ui.actionStart.setEnabled(False)
        self.ui.actionStop.setEnabled(True)
        self.db_thread = MyDBThread()
        self.com_thread = MyThread(self.returnValue)
        self.gT = MyGraphThread(self.ui.tabPlot)
        self.com_thread.error.connect(self.error_handling)
        self.com_thread.change_value.connect(self.print_data)
        

        self.com_thread.change_value.connect(self.db_thread.update_data_base)
        self.com_thread.change_value.connect(self.gT.up_graph)

        self.ui.pushButtonON.clicked.connect(self.com_thread.led_ON)
        self.ui.pushButtonOFF.clicked.connect(self.com_thread.led_OFF)
        
        self.com_thread.start()
        self.db_thread.start()
        self.gT.start()


    def print_data(self,data):
        for x in range(len(data)):
            self.ui.textEdit.append(data[x])

    def error_handling(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Greska")
        msg.setInformativeText('Problem pri otvaranju komunikacije!')
        msg.setWindowTitle('Greska')
        msg.exec_()
        self.ui.actionStart.setEnabled(True)
        self.ui.actionStop.setEnabled(False)
        self.ui.actionSettings.setEnabled(True)

    #Funckija za Zatvaranje komunikacije
    def close_com(self):
        self.ui.actionSettings.setEnabled(True)
        self.ui.actionStart.setEnabled(True)
        self.ui.actionStop.setEnabled(False)
        self.com_thread.exit()
        self.gT.exit()
    