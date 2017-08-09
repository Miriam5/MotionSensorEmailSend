from gpiozero import MotionSensor
from time import sleep
import smtplib

m = MotionSensor(4)

def emailSend():
  senderEmail = "yourEmail@gmail.com"
  password = "yourPassword"
  receiver = "girlsandtechbook@gmail.com"
  message = "Subject: Someone's in your room!"
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.ehlo()
  server.login(senderEmail, password)
  print("Email sent")
  
while True:
  if m.motion_detected: 
    emailSend()
    print("Who goes there?")
    sleep(2)
  else: 
    print("All quiet")
    sleep(2)
    
    
    
