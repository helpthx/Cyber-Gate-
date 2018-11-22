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
            matricula = matricula_list[id]
            credito_1 = credito - 5.20
            id = matricula_list[id]
            confidence = "  {0}%".format(round(100 - confidence))
            #t = t + 1
            if (t == 10 and credito_1 >= 0.0):
                time.sleep(3)
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id = 'Acesso permitido'
                #time.sleep(2)
                
                print('Bem Vindo ', nome)
                print('Matricula: ', matricula)
                print('Creditos restantes: ', credito_1)
                print('\n')
                time.sleep(3)
                #os.system("sudo ./gpio")
                t = 0
            elif(t == 10 and credito_1 < 0.0):
                #time.sleep(1)
                cv2.rectangle(img, (x,y), (x+w,y+h), (144,255,0), 2)
                #time.sleep(3)
                id = 'Sem creditos...'
                print('Creditos: ', credito)
                print('\n')
                #time.sleep(3)
                #time.sleep(1)
                t = 0
            else:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255), 2) #Amarelo
                id = 'Identificando rosto...'
                #confidence = "  {0}%".format(round(100 - confidence))
                t = t + 1
                
                
        elif (confidence < 65):
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id = 'Desconhecido'
            confidence = "  {0}%".format(round(100 - confidence))
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