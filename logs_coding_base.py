#Codigo base para criar os logs
import os
from datetime import datetime
now = datetime.now()

arq = open('/home/alunos/logs.txt', 'a')
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
data.append('\n------------------------\n')
arq.writelines(data)
arq.close()


