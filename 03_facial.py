''''
Real Time Face Recogition
    ==> Each face stored on dataset/ dir, should have a unique numeric integer ID linked with some infos in "Banco_de_dados.db".                       
    ==> LBPH computed model (trained faces) should be on trainer
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    
Developed by João Vitor Rodrigues Baptista  
'''

import cv2
import numpy as np
import os 
import time
from datetime import datetime
import sqlite3
from time import sleep
from PyQt4 import QtCore, QtGui
import time
import sys


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName(_fromUtf8("Monitor"))
        Monitor.resize(620, 700)
        Monitor.setMaximumSize(QtCore.QSize(620, 700))
        self.centralwidget = QtGui.QWidget(Monitor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Nome = QtGui.QTextBrowser(self.centralwidget)
        self.Nome.setGeometry(QtCore.QRect(30, 350, 571, 81))
        self.Nome.setObjectName(_fromUtf8("Nome"))
        self.Matricula = QtGui.QTextBrowser(self.centralwidget)
        self.Matricula.setGeometry(QtCore.QRect(30, 460, 301, 51))
        self.Matricula.setObjectName(_fromUtf8("Matricula"))
        self.Dinheiro = QtGui.QTextBrowser(self.centralwidget)
        self.Dinheiro.setGeometry(QtCore.QRect(340, 460, 261, 51))
        self.Dinheiro.setObjectName(_fromUtf8("Dinheiro"))
        self.Matricula_l = QtGui.QLabel(self.centralwidget)
        self.Matricula_l.setGeometry(QtCore.QRect(30, 440, 71, 17))
        self.Matricula_l.setObjectName(_fromUtf8("Matricula_l"))
        self.DInheiro_l = QtGui.QLabel(self.centralwidget)
        self.DInheiro_l.setGeometry(QtCore.QRect(340, 440, 131, 17))
        self.DInheiro_l.setObjectName(_fromUtf8("DInheiro_l"))
        self.Nome_L = QtGui.QLabel(self.centralwidget)
        self.Nome_L.setGeometry(QtCore.QRect(30, 330, 131, 17))
        self.Nome_L.setObjectName(_fromUtf8("Nome_L"))
        self.Data_e_HOra = QtGui.QDateTimeEdit(self.centralwidget)
        self.Data_e_HOra.setGeometry(QtCore.QRect(410, 530, 194, 27))
        self.Data_e_HOra.setObjectName(_fromUtf8("Data_e_HOra"))
        self.Status = QtGui.QTextBrowser(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(30, 560, 571, 81))
        self.Status.setObjectName(_fromUtf8("Status"))
        self.Status_l = QtGui.QLabel(self.centralwidget)
        self.Status_l.setGeometry(QtCore.QRect(30, 540, 66, 17))
        self.Status_l.setObjectName(_fromUtf8("Status_l"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 10, 275, 320))
        self.textBrowser.setMinimumSize(QtCore.QSize(275, 320))
        self.textBrowser.setMaximumSize(QtCore.QSize(275, 320))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        Monitor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Monitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Monitor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Monitor)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Monitor.setStatusBar(self.statusbar)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        Monitor.setWindowTitle(_translate("Monitor", "Monitor", None))
        self.Nome.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">"+nome+"</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600;\"><br /></p></body></html>", None))
        self.Matricula.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">"+matricula+"</span></p></body></html>", None))
        self.Dinheiro.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">R$ "+dinheiro+"</span></p></body></html>", None))
        self.Matricula_l.setText(_translate("Monitor", "Matrícula: ", None))
        self.DInheiro_l.setText(_translate("Monitor", "Saldo Atual:", None))
        self.Nome_L.setText(_translate("Monitor", "Nome:", None))
        if(numero_acessos != 0 and iniciar == 1):
             self.Status.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#ff5500;\">NUMERO DE ACESSOS EXPIRADOS</span></p>\n"
    "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; color:#00aa00;\"><br /></p></body></html>", None))

        elif(sem_credito == 1 and iniciar == 1):
            self.Status.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">SALDO INSUFICIENTE</span></p>\n"
    "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; color:#00aa00;\"><br /></p></body></html>", None))
        elif(sem_credito == 0 and numero_acessos == 0 and iniciar == 1):
            self.Status.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#00aa00;\">ACESSO PERMITIDO</span></p></body></html>", None))
       
        elif(sem_credito == 0 and iniciar == 1):
            self.Status.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">SALDO INSUFICIENTE</span></p>\n"
    "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; color:#00aa00;\"><br /></p></body></html>", None))
        elif(iniciar == 0):
            self.Status.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#5978c6;\">APROXIME SEU ROSTO</span></p>\n"
    "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; color:#00aa00;\"><br /></p></body></html>", None))

        self.Status_l.setText(_translate("Monitor", "Status:", None))
        self.textBrowser.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"/home/pi/Interface/cortado.png\" /></p></body></html>", None))




'''
==> Path to convert the database in lists, cos we need a list's ID to link the database and the dataset.
'''

id_list = []
name_list = []
matricula_list = []
ru_list = []
acessos_list = []
data = []
conn = sqlite3.connect('/home/pi/Banco_de_dados.db')
print ('Banco aberto com sucesso...');

cursor = conn.execute("SELECT ID, NOME, MATRICULA, RU, ACESSOS from CADASTROS")
for row in cursor:
    id_list.append(int(row[0]))
    name_list.append(row[1])
    matricula_list.append(int(row[2]))
    ru_list.append(float(row[3]))
    acessos_list.append(int(row[4]))

print("Operação feita com sucesso...");
conn.close()       

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
#namelist = ['None', 'Mito', 'Paula', 'Ilza', 'Z', 'W'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
t = 0
#import sys
sair = 1 
app = QtGui.QApplication(sys.argv)
Monitor = QtGui.QMainWindow()
nome = "Aluno"
matricula = "Matricula"
dinheiro = "00"
dinheiro_flt = 00.00
numero_acessos = 0
sem_credito = 0
iniciar = 0
ui = Ui_Monitor()
ui.setupUi(Monitor)
Monitor.show()

while True:
   
      
    #time.sleep(1)
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        
        id_list = []
        name_list = []
        matricula_list = []
        ru_list = []
        acessos_list = []
        data = []
        conn = sqlite3.connect('/home/pi/Banco_de_dados.db')
        #print ('Banco aberto com sucesso...');

        cursor = conn.execute("SELECT ID, NOME, MATRICULA, RU, ACESSOS from CADASTROS")
        for row in cursor:
            id_list.append(int(row[0]))
            name_list.append(row[1])
            matricula_list.append(int(row[2]))
            ru_list.append(float(row[3]))
            acessos_list.append(int(row[4]))

        #print("Operação feita com sucesso...");
        conn.close()   

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 35):
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            nome = name_list[id]
            credito = ru_list[id]
            matricula = str(matricula_list[id])
            credito_1 = credito - 5.20
            dinheiro = str(credito_1)
            id = matricula_list[id]
            confidence = "  {0}%".format(round(100 - confidence))
            #t = t + 1
            time.sleep(0.01)
            if (t == 10 and credito_1 >= 0.0):
                time.sleep(0.01)
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id = 'Acesso permitido'
                time.sleep(0.5)
                iniciar = 1
                sem_credito = 0
                #nome = input("Digite um nome para entrar: ")
                #matricula = input("Digite uma matricula para entrar: ")
                #dinheiro = input("Digite uma quantidade de dinheiro: ")
                #sair = input("Deseja sair 1 ou 0 ?")
                numero_acessos = 0
                dinheiro_flt = float(credito_1)
                ui = Ui_Monitor()
                ui.setupUi(Monitor)
                #Monitor.show()
                time.sleep(3)
                print('Bem Vindo ', nome)
                print('Matricula: ', matricula)
                print('Creditos restantes: ', credito_1)
                print('\n')
                
                #time.sleep(0.25)
                os.system("sudo ./gpio")
                t = 0
            elif(t == 10 and credito_1 < 0.0):
                #time.sleep(1)
                cv2.rectangle(img, (x,y), (x+w,y+h), (144,255,0), 2)
                #time.sleep(3)
                id = 'Sem creditos...'
                iniciar = 1
                sem_credito = 1
                numero_acessos = 0
                dinheiro_flt = float(credito_1)
                ui = Ui_Monitor()
                ui.setupUi(Monitor)
                Monitor.show()
                
                print('Sem saldo ', nome)
                print('Matricula: ', matricula)
                print('Creditos restantes: ', credito_1)
                print('Creditos: ', credito)
                print('\n')
                time.sleep(3)
                #time.sleep(1)
                t = 0
            else:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255), 2) #Amarelo
                id = 'Identificando rosto...'
                iniciar = 0
                nome = "Identificando..."
                matricula = "........"
                dinheiro = ".."
                dinheiro_flt = 00.00
                numero_acessos = 0
                sem_credito = 0
                iniciar = 0
                ui = Ui_Monitor()
                ui.setupUi(Monitor)
                Monitor.show()
                #confidence = "  {0}%".format(round(100 - confidence))
                t = t + 1
                
                
        elif (confidence < 65):
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id = 'Desconhecido'
            confidence = "  {0}%".format(round(100 - confidence))
            #iniciar = 0
            nome = "Aluno"
            matricula = "Matricula"
            dinheiro = "00"
            dinheiro_flt = 00.00
            numero_acessos = 0
            sem_credito = 0
            iniciar = 0
            ui = Ui_Monitor()
            ui.setupUi(Monitor)
            Monitor.show()
            
            
            
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id = 'Erro de captura'
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
#print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
sys.exit(app.exec_())