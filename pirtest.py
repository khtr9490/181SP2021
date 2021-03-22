import RPi.GPIO as GPIO

GPIO_trigger = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(GPIO_trigger, GPIO.IN)         #Read output from PIR motion sensor

def Detector():
    i=GPIO.input(GPIO_trigger)
    if i==0:                 #When output from motion sensor is LOW
        alert = "False"
    if i==1:               #When output from motion sensor is HIGH
        alert = "True"
    return alert