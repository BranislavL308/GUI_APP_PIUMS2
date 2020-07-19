import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
