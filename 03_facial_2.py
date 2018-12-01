''''
Real Time Face Recogition
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


'''
Parte da interface grafica integrada no codigo
'''

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
 Para para acessar o database e o dataset atraves de conversão de valores para listas
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

#Zerar todos os acessos    

conn = sqlite3.connect('/home/pi/Banco_de_dados.db')
print('\nBanco aberto com sucesso...');
print('---------------------------')
        
conn.execute('UPDATE CADASTROS set ACESSOS = 0');
conn.commit()
print('Numero total de colunas atualizadas: ', conn.total_changes)
if conn.total_changes > 0:
    print('Alterado com sucesso...')
else:
    print('Alguma operação deu errado...')

print('\n')
conn.close()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#Contador inicial
id = 0

# Iniciar e começa a video captura de tempo-real
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Definir o tamanho minino do quadrado que será usado para reconhecer o rosto
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#Inicia a interface grafica de acompanhamento

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

#Variaveis de temporalização e confirmação de faces
t = 0
v = 0

#Loop principal da aplicação.
while True:
   
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
        
        #atualização real-time do banco
        id_list = []
        name_list = []
        matricula_list = []
        ru_list = []
        acessos_list = []
        data = []
        conn = sqlite3.connect('/home/pi/Banco_de_dados.db')
       
        cursor = conn.execute("SELECT ID, NOME, MATRICULA, RU, ACESSOS from CADASTROS")
        for row in cursor:
            id_list.append(int(row[0]))
            name_list.append(row[1])
            matricula_list.append(int(row[2]))
            ru_list.append(float(row[3]))
            acessos_list.append(int(row[4]))

        conn.close()   
        
        # Iniciação do retangulo de reconhecimento 
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
	# Sistema de valiação por 10 frames não consecutivos 	
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 32): #confiabilidade de 68% em cada match de imagem
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            
            #conversão de valores do banco para a aplicação
            nome = name_list[id]
            numb_acessos = acessos_list[id]
            credito = ru_list[id]
            matricula = str(matricula_list[id])
            credito_1 = round(credito - 5.20, 2)
            dinheiro = str(credito_1)
            id = matricula_list[id]
            confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id = 'Acesso permitido'
            iniciar = 1
            sem_credito = 0
            numero_acessos = numb_acessos
                             
            ui = Ui_Monitor()
            ui.setupUi(Monitor)
            Monitor.show()
            v = v + 1
            
            #condição em que o usuario terá acesso ao restaurante
            if (t == 8 and credito_1 >= 0.0 and numero_acessos == 0):
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id = 'Acesso permitido'
                iniciar = 1
                sem_credito = 0
                numero_acessos = 0
                ui = Ui_Monitor()
                ui.setupUi(Monitor)
                Monitor.show()
                                
                #Temporalização para travar a tela de monitoramento e abrir o GPIO da placa
                if(v == 10):
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #Verde
                    id = 'Acesso permitido'
                    iniciar = 1
                    sem_credito = 0
                    numero_acessos = 0
                    ui = Ui_Monitor()
                    ui.setupUi(Monitor)
                    Monitor.show()
                    
                    #Printar no console as informações que serão gravas como logs
                    print('Bem Vindo ', nome)
                    print('Matricula: ', matricula)
                    print('Creditos restantes: ', credito_1)
                    print('\n')
                    
                    #Atualização do banco de dados
                    conn = sqlite3.connect('/home/pi/Banco_de_dados.db')
                    conn.execute("UPDATE CADASTROS set RU = " +str(round(credito_1, 2))+ " WHERE  MATRICULA = "+ str(matricula));
                    conn.execute('UPDATE CADASTROS set ACESSOS = ACESSOS+1 WHERE  MATRICULA='+str(matricula));
                    conn.commit()
                    print('\nNumero total de colunas atualizadas: ', conn.total_changes)
                    if conn.total_changes > 0:
                            print('Alterado com sucesso...')
                    else:
                            print('Alguma operação deu errado...')

                    print('\n')
                    conn.close()
                    
                    #Criando o arquivo de logs
                    now = datetime.now()
                    arq = open('/home/pi/Arquivos/Logs/acessos.txt', 'a')
                    data = []
                    data.append('\n-------------------------\n')
                    data.append("Data: ")
                    data.append(str(now.year))
                    data.append(':')
                    data.append(str(now.month))
                    data.append(':')
                    data.append(str(now.day))
                    data.append(':')
                    data.append(str(now.hour))
                    data.append(':')
                    data.append(str(now.minute))
                    data.append(':')
                    data.append(str(now.second))
                    data.append(str('\nBem vindo: '+nome))
                    data.append(str('\nMatricula: '+matricula))
                    data.append('\nCreditos restantes: '+str(credito_1))
                    data.append('\nCreditos antes: '+str(credito))
                    data.append('\n------------------------\n')
                    arq.writelines(data)
                    arq.close()

                                      
                    
                    #Abertura do rele
                    #time.sleep(5)
                    os.system("sudo ./gpio")
                    t = 0
                    v = 0
            
            #Condição em que o usuario não terá creditos suficientes para acessar o restaurante.
            elif(t == 8 and credito_1 < 0.0):
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2) #Vermelho
                id = 'Sem creditos...'
                iniciar = 1
                sem_credito = 1
                numero_acessos = 0
                dinheiro_flt = float(credito_1)
                ui = Ui_Monitor()
                ui.setupUi(Monitor)
                Monitor.show()
                
                #Temporalização para travar a tela de monitoramento
                if(v == 10):
                    
                    #Printar no console as informações que serão gravas como logs
                    print('Sem saldo ', nome)
                    print('Matricula: ', matricula)
                    print('Creditos restantes: ', credito_1)
                    print('Creditos: ', credito)
                    print('\n')
                    
                    #Criando o arquivo de logs
                    now = datetime.now()
                    arq = open('/home/pi/Arquivos/Logs/acessos.txt', 'a')
                    data = []
                    data.append('\n-------------------------\n')
                    data.append("Data: ")
                    data.append(str(now.year))
                    data.append(':')
                    data.append(str(now.month))
                    data.append(':')
                    data.append(str(now.day))
                    data.append(':')
                    data.append(str(now.hour))
                    data.append(':')
                    data.append(str(now.minute))
                    data.append(':')
                    data.append(str(now.second))
                    data.append(str('\nBem vindo: '+nome))
                    data.append(str('\nMatricula: '+matricula))
                    data.append('\nCreditos restantes: '+str(credito_1))
                    data.append('\nCreditos antes: '+str(credito))
                    data.append('\n------------------------\n')
                    arq.writelines(data)
                    arq.close()
                    
                    #tempo de permanencia da tela de monitoramento 
                    time.sleep(5)
                    t = 0
                    v = 0
            
            #Condição em que o usuario tentou acessar mais vezes que o permitido no restaurante.
            elif(t == 10 and numero_acessos != 0):
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,165,255), 2) #laranjado
                id = 'Numeros de acessos expirados..'
                iniciar = 1
                sem_credito = 0
                numero_acessos = 1
                dinheiro_flt = float(credito_1)
                ui = Ui_Monitor()
                ui.setupUi(Monitor)
                Monitor.show()
                
                #Temporalização para travar a tela de monitoramento
                if(v == 8):
                    
                    #Printar no console as informações que serão gravas como logs
                    print('Numeros de acessos expirados... ', nome)
                    print('Matricula: ', matricula)
                    print('\n')
                    
                    #Criando o arquivo de logs
                    now = datetime.now()
                    arq = open('/home/pi/Arquivos/Logs/acessos.txt', 'a')
                    data = []
                    data.append('\n-------------------------\n')
                    data.append("Data: ")
                    data.append(str(now.year))
                    data.append(':')
                    data.append(str(now.month))
                    data.append(':')
                    data.append(str(now.day))
                    data.append(':')
                    data.append(str(now.hour))
                    data.append(':')
                    data.append(str(now.minute))
                    data.append(':')
                    data.append(str(now.second))
                    data.append(str('\nBem vindo: '+nome))
                    data.append(str('\nMatricula: '+matricula))
                    data.append('\nCreditos restantes: '+str(credito_1))
                    data.append('\nCreditos antes: '+str(credito))
                    data.append('\n------------------------\n')
                    arq.writelines(data)
                    arq.close()
                    
                    #tempo de permanencia da tela de monitoramento 
                    time.sleep(5)
                    t = 0
                    v = 0
                    
            #Condição de incremento de identificação        
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
                t = t + 1
                
        #confiabilidade menor do que 68% em cada match de imagem       
        elif (confidence < 68):
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id = 'Desconhecido'
            confidence = "  {0}%".format(round(100 - confidence))
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
            #t = 0
            #v = 0
        
        #error de frame e resete da interface de monitoramento.
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id = 'Erro de captura'
            confidence = "  {0}%".format(round(100 - confidence))
            t = 0
            v = 0
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Limpar as telas quando sair

cam.release()
cv2.destroyAllWindows()
sys.exit(app.exec_())

