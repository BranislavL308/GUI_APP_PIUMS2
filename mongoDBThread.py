from PyQt5.QtCore import QThread, pyqtSignal
from pymongo import MongoClient
from datetime import datetime
import time
import sys





class MyDBThread(QThread):
    def __init__(self):
        super().__init__()
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['database']
        self.collection = self.db.kolekcija
        self.cnt = 0
        self.doc = {'_id':None,'PRESS':None,'TEMP':None,'LIGHT':None,'time':None}



    def run(self):
        while(1):
            time.sleep(10)

    def update_data_base(self, data):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.cnt += 1
        self.doc['_id'] = self.cnt
        self.doc['PRESS'] = data[0]
        self.doc['TEMP'] = data[1]
        self.doc['LIGHT'] = data[2]
        self.doc['time'] = current_time

        try:
            self.collection.insert_one(self.doc)
        except:
            e = sys.exc_info()[0] #Greske priliko konekcije, upisa itd u bazu
            print(e)



    def exit(self):
        self.terminate()
