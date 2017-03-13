#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)

if __name__=='__main__':
	while True:
		GPIO.output(4,GPIO.HIGH)
		time.sleep(1.0)
		GPIO.output(4,GPIO.LOW)
		time.sleep(1.0)
