#! /usr/bin/python

# Import the libraries we need
import Rpi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

LED = 21

GPIO.setup(LED,GPIO,OUT)

GPIO.output(LED,True)

time.sleep(5)

GPIO.output(LED,False)



        
        



    
