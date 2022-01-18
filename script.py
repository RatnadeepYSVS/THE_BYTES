"""
CODE FOR READING ALL LOG FILES AND PLACING DATA IN A SINGLE FILE
# from os.path import *
# import os
# from shutil import *
# src_path='src directory of log files path'
# src=os.listdir(src_path)
# data=src[:len(src)-2]
# data.sort(key=lambda x:int(x.split('.')[0]))
# file_data=[]
# s=0
# for i in data:
#     pth=f'what ever path you want to give'
#     file_data.append(open(pth).read())
# final_data="\n".join(file_data)
# with open('ALL_LOGS.txt','w') as file:
#     file.write(final_data)
"""
#REPORT GENERATION CODE
from re import *
from os import startfile
print("ENTER DATE RANGE TO GET THE REPORT")
print("""
AFTER SUCCESSFUL CALCULATIONS A TEXT FILE IS CREATED CONTAINING DETAILS OF LOGS.
PLEASE GO THROUGH THE FILE TO SEE THE REPORT DETAILS.
""")
start=input("Enter the starting range: ")
end=input("Enter the ending range: ")
file_path=input("Input the path of Log file to analyse the report: ")
try:
    print("READING FILE DATA FROM THE PATH GIVEN...")
    with open(file_path,'r') as log_file:
        data=log_file.readlines()
    print("DATA ANALYZED SUCCESSFULLY...")
    computers={}
    disconnects={}
    drops={}
    avg_limits={}
    for i in data:
        comp=findall(r'ComputerName:[a-zA-Z0-9*-]+',i)
        try:
            date=i.split("|")[1]
            dare_split=date.split('(')[-1].split('/')
            month,date=dare_split[0],dare_split[1].split()[0]
            startdate,startmonth=start.split('/')
            endate,endmonth=end.split('/')
            computer=comp[0].split(':')[1]
            computers.setdefault(computer)
            disconnects.setdefault(computer,0)
            drops.setdefault(computer,0)
            avg_limits.setdefault(computer,0)
            disconnect_check=search(r'Client is disconnected from agent',i)
            drop_check=search(r'Drop count limit',i)
            avg_limit_check= search(r'Average limit',i)
            if (date>=startdate and month>=startmonth) and (date<=endate and month<=endmonth):
                if disconnect_check is not None:
                    disconnects[computer]=disconnects.get(computer)+1
            if drop_check is not None:
                drops[computer]=drops.get(computer)+1
            if avg_limit_check is not None:
                avg_limits[computer]=avg_limits.get(computer)+1
        except Exception as e:
            pass
    print("CALCULATED DISCONNECTS SUCCESSFULLY....")
    print(f"TOTAL NUMBER OF DISCONNECTS from :- {sum(list(disconnects.values()))}")
    print("CALCULATED NUMBER OF DROPS SUCCESSFULLY....")
    print(f"TOTAL NUMBER OF DROPS FROM :- {sum(list(drops.values()))}")
    print("CALCULATED NUMBER OF AVG LIMITS(EXCEEDED) SUCCESSFULLY....")
    print(f"TOTAL NUMBER OF AVG LIMITS FROM :- {sum(list(avg_limits.values()))}")
    print("GENERATING REPORT....")
    with open('report.txt','a') as file:
        file.write('REPORT RANGING FROM {} - {}\n'.format(start,end))
        z,k,l=list(disconnects.items()),list(drops.items()),list(avg_limits.items())
        z.sort(key=lambda x:-x[1])
        k.sort(key=lambda x:-x[1])
        l.sort(key=lambda x:-x[1])
        file.write(f"TOTAL NUMBER OF DISCONNECTS from {start}-{end}:- {sum(list(disconnects.values()))}\n")
        file.write("COMPUTER NAME  DISCONNECTS\n")
        for i,j in z:
            if j!=0:
                file.write(f"{i} has made {j} disconnects.\n")
        file.write(f"TOTAL NUMBER OF DROPS FROM {start}-{end}:- {sum(list(drops.values()))}\n")
        for i,j in k:
            if j!=0:
                file.write(f"{i} has made {j} drops.\n")
        file.write(f"TOTAL NUMBER OF AVG LIMITS FROM {start}-{end}:- {sum(list(avg_limits.values()))}\n")
        for i,j in l:
            if j!=0:
                file.write(f"{i} has mad {j} avg limits.\n")
    print("REPORT GENERATION COMPLETED.")
    print(f"PLEASE GO THROUGH REPORT.txt FILE TO VIEW THE FULL REPORT OF LOG FILE.")
    startfile("C:\\Users\\ratna\\Downloads\\logs\\report.txt")
except FileNotFoundError:
    print("INVALID FILE PATH")
