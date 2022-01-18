#CODE FOR READING ALL LOG FILES AND PLACING DATA IN A SINGLE FILE
from os.path import *
import os
from shutil import *
src_path=input('src directory of log files path: ')
pth=input('destination path to store log file data: ')
src=os.listdir(src_path)
data=src[:len(src)-2]
data.sort(key=lambda x:int(x.split('.')[0]))
file_data=[]
s=0
for i in data:
    file_data.append(open(pth).read())
final_data="\n".join(file_data)
with open('ALL_LOGS.txt','w') as file:
    file.write(final_data)
