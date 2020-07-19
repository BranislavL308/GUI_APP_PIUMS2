from PyQt5.QtCore import QThread, pyqtSignal
import sys
from mongoDBThread import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QGridLayout
from communicationThread import *
from mainWindowUI import *

class MplCanvas(FigureCanvas):
    def __init__(self, width = 5, height = 4, dpi = 100):
        figure = Figure(figsize = (width, height), dpi = dpi,  tight_layout = 3.0)

        self.axes = figure.add_subplot(311)
        self.axes1 = figure.add_subplot(312)
        self.axes2 = figure.add_subplot(313)
        self.axes.set_title('Pressure')

        self.axes1.set_title('Temperature')
        self.axes2.set_title('Irradiance')
        
        self.axes2.set_xlabel('Samples')


        self.axes.set_ylabel('mBar', fontsize = 16)
        self.axes1.set_ylabel('°C', fontsize = 16)
        self.axes2.set_ylabel('uW/cm2', fontsize = 16)

        super().__init__(figure)


class MyGraphThread(QThread):
    def __init__(self, tabPlot):
        super().__init__()
        self.canvas = MplCanvas()
        self.mpl = QGridLayout() #Pravimo gridLayout
        self.mpl.addWidget(self.canvas)
        tabPlot.setLayout(self.mpl) #Na tabPlot primeni gore napravljeni tab

        self.ydata = [None]*10 #Lista od 10 elemenata None
        self.ydata1 = [None]*10
        self.ydata2 = [None]*10
        self.xdata = list(range(10))  #Funkija range nam vraca 10 elemenata u ovom slicaju brojeve od 1 do 10 redom
        self.xdata1 = list(range(10))
        self.xdata2 = list(range(10))

    def run(self):
        
        while(1):
            time.sleep(10)
    def up_graph(self, data):
        """self.canvas = MplCanvas()
        self.mpl = QGridLayout() #Pravimo gridLayout
        self.mpl.addWidget(self.canvas)
        self.tabPlot.setLayout(self.mpl) #Na tabPlot primeni gore napravljeni tab
        
        self.ydata = [None]*10 #Lista od 10 elemenata None
        self.ydata1 = [None]*10
        self.ydata2 = [None]*10
        self.xdata = list(range(10))  #Funkija range nam vraca 10 elemenata u ovom slicaju brojeve od 1 do 10 redom
        self.xdata1 = list(range(10))
        self.xdata2 = list(range(10))
        #Uvezujemo signale koji ce se generisati kada kliknemo na bilo koji od
        self.ydata = self.ydata[1:] #Slice liste, popunjavamo listu s leva na desno, poslednji element odbacujemo
        self.ydata1 = self.ydata1[1:]
        self.ydata2 = self.ydata2[1:]"""
        try:
            self.ydata = self.ydata[1:] #Slice liste, popunjavamo listu s leva na desno, poslednji element odbacujemo
            self.ydata1 = self.ydata1[1:]
            self.ydata2 = self.ydata2[1:]
            self.ydata.append(float(data[0])) #Osvezavamo listu kako se pojavi novi element
            self.ydata1.append(float(data[1]))
            self.ydata2.append(float(data[2]))
            
            print(self.ydata)
            print(self.xdata)
        except:
            self.ydata.append(None)
            self.ydata1.append(None)
            self.ydata2.append(None)
            print('Problem u konverziji')

        #Pritisak
        
        self.canvas.axes.cla() #cla funkija koja brise sve podatke sa grafika
        self.canvas.axes.plot(self.xdata, self.ydata, 'r') #sta hocemo da iscrtamo
        #Temperatura
        
        self.canvas.axes1.cla() #cla funkija koja brise sve podatke sa grafika
        self.canvas.axes1.plot(self.xdata1, self.ydata1, 'g') #sta hocemo da iscrtamo
        #Zracenje
        
        self.canvas.axes2.cla() #cla funkija koja brise sve podatke sa grafika
        self.canvas.axes2.plot(self.xdata2, self.ydata2, 'b') #sta hocemo da iscrtamo
        
        self.canvas.axes.set_title('Pressure')
        self.canvas.axes.set_ylabel('mBar', fontsize = 16)
        self.canvas.axes1.set_title('Temperature')
        self.canvas.axes1.set_ylabel('°C', fontsize = 16)
        self.canvas.axes2.set_title('Irradiance')
        self.canvas.axes2.set_ylabel('uW/cm2', fontsize = 16)
        self.canvas.axes2.set_xlabel('Samples')

        self.canvas.draw()  #funkija za crtanje
    
    def exit(self):
        self.terminate()