import RAFAEL.RAFAEL_v60 as R
import os
import pandas as pd
import cv2
import time
from matplotlib import pyplot as plt
from pyzbar import pyzbar
import sqlite3
from threading import Thread
var_r = '0'
repeticoes = 0
conn = sqlite3.connect('drone.db')
c = conn.cursor()
# c.execute('''CREATE TABLE bar_code(id INTEGER PRIMARY KEY AUTOINCREMENT,code TEXT NOT NULL, datetime DATETIME DEFAULT CURRENT_TIMESTAMP)''')

def salva_cod_barras_excel(codigo):
    global var_r
    global repeticoes
    print('xxx')
    R.DORME(0.25)
    if str(var_r) == str(codigo):
        repeticoes += 1
        print("X: ", repeticoes, ' de ', var_r, ' == ', codigo)
        if repeticoes >= 5:
            repeticoes = 0
            var_r = '0'
            print('SALVA CODIGO ', codigo)
            df = R.CRIA_DF([str(codigo)],['CODIGO'])
            R.CRIA_PASTA_AUXILIAR()
            R.HISTORICO_CRIA_E_ATUALIZA(df,'ARQUIVOS_AUXILIARES\\LEITURAS.xlsx')
            R.DORME(3)
    else:
        print("X: ", repeticoes, ' de ', var_r, ' != ', codigo)
        repeticoes = 0
    var_r = codigo
    return



def save_to_base(code):
    global var_r
    if (var_r == code):
        print("repetido: ", var_r)
        return
    else:
        var_r = code
        print("novo: ", code)
        c.execute('''INSERT INTO bar_code (code) VALUES (?)''', (code,))
        conn.commit()
#         c.execute('''SELECT * FROM bar_code''')
#         results = c.fetchall()
#         print(results)

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        # 3
        #save_to_base(barcode_info)
        salva_cod_barras_excel(barcode_info)
    return frame, barcode_info


class ThreadedCamera(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        # FPS = 1/X
        # X = desired FPS
        self.FPS = 1 / 30
        self.FPS_MS = int(self.FPS * 1000)
        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(self.FPS)
    def show_frame(self):
        try:
            frame, barcode_info = read_barcodes(self.frame)
            print(barcode_info)
        except:
            pass
        cv2.imshow('frame', self.frame)
        cv2.waitKey(self.FPS_MS)


def ABRIR():
    src = 0
    #src = 'rtmp://10.20.4.98:1935/live?.sdp'
    #src = 'C:\\Users\\rafael.garcia\\Videos\\FINAL 1-6000.mp4'
    src = 'http://192.168.1.73:4747/video/'
    threaded_camera = ThreadedCamera(src)
    while True:
        try:
            threaded_camera.show_frame()
        except AttributeError:
            pass

ABRIR()