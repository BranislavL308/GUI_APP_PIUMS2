from PyQt5.QtCore import QThread, pyqtSignal
from serial import Serial
#Trebamo uvezati signal change value na nas slot update_graph

#Signali nam sluze za sinhronizovanje sa nasom glavnom programskom niti (osvezava nam mainWindowUI)


class MyThread(QThread):
    change_value = pyqtSignal(list)
    error = pyqtSignal()
    def __init__(self, com_data): #kada napravimo tred
        super().__init__()
        self.com_port = com_data['com_port']
        self.baud = com_data['baud_rate']
        self.data_bits = com_data['data_bits']
        self.parity = com_data['parity']
        self.stop_bit = com_data['stop_bit']

        try:
            self.s = Serial(self.com_port, self.baud, self.data_bits, self.parity, self.stop_bit)
        except:
            self.error.emit()
            return #ako se desi greska izlazimo iz treda


    def run(self):
        
        while(1):
            d = self.s.readline().decode()
            data = list(d.split())
            self.change_value.emit(data)
    def led_ON(self):
        self.s.write(b'T')  
    
    def led_OFF(self):
       
        self.s.write(b'F') 

#Zatvaranje komunikacije (Ubijanje treda)

    def exit(self):
        self.terminate()
        if self.s.is_open:
            self.s.close()
