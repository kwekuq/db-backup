__author__ = 'kwekuq'

import os
import datetime as dt
import time

import smtplib


HOST = '178.62.106.14'
DB = 'redmine'
USER = 'root'
PASSWORD = 'Nqobile0203'
BACKUPNAME = dt.date.today().strftime("%d-%m-%Y") +'-backup.sql'
starttime = time.time()
try:
    os.system('mysqldump -u '+ USER +' -h '+HOST+' -p'+PASSWORD+' '+DB+' > '+BACKUPNAME)
except:
    print ("Unsuccessfully")
endtime = time.time() - starttime
MESSAGE = "Executed in "+ str(endtime) +" seconds"
try:
    fromaddr = 'kwekuraspberry@gmail.com'
    toaddrs  = 'kwekuq@gmail.com'
    msg = 'Portal database backup successful \nDetails as follows: \nBackup directory: {2} \nBackup name: {0} \nComment: {1}'.format(BACKUPNAME, MESSAGE, os.getcwd())

    header = 'Subject: Database Backup\n\n'
    message = header + msg

    # Gmail Login
    username = 'kwekuraspberry'
    password = 'Pa44word1'
    # Sending the mail
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()
    print(msg)
except:
    print("Email not send")