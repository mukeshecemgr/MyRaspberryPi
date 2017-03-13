#!/usr/bin/python

"""Light sensor LED display, Detects the light intesity and respond as LED blink for light changes"""

from gpiozero import LightSensor, Buzzer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)                                                                                        
GPIO.setwarnings(False)                                                                                       
GPIO.setup(4,GPIO.OUT) #Pin selection for LDR
ldr = LightSensor(18)  #Pin selection for LED
GPIO.output(4,GPIO.LOW)
while True:
	val = ldr.value
	if val > 0.2:
		GPIO.output(4,GPIO.LOW)
	else:
		GPIO.output(4,GPIO.HIGH)
	time.sleep(1)
