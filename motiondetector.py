from gpiozero import MotionSensor
from time import sleep
import datetime

def watch():
	pir = MotionSensor(4)

	while True:
		pir.wait_for_motion()
		print("Motion detected at {}".format(datetime.datetime.now()))
		sleep(10)
