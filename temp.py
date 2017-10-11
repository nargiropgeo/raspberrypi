#!/usr/bin/env python
import os
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

# Return CPU temperature as a character string
def getCPUtemperature():
	res = os.popen("vcgencmd measure_temp").readline()
	res = res.replace("temp=", "")
	for i in res:
		res = res[:4]
	return float(res)

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)  # GPIO4

while True:
	temp = getCPUtemperature()
	if temp > 45:
		gpio.output(4, True)  # GPIO4
		while temp > 42:
			time.sleep(300)
			temp = getCPUtemperature()
		else:
			print temp
			gpio.output(4, False)  # GPIO4
	else:
		gpio.output(4, False)  # GPIO4
	time.sleep(300)
