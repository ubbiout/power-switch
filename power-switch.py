import threading, subprocess, time
import RPi.GPIO as GPIO
def shutdown():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(5, GPIO.IN)
	t.cancel()
	duration = 0
	start = 0
	button_depressed = False
	while True:
		if GPIO.input(5) == GPIO.LOW:
			if button_depressed == False:
				start = time.time()
				button_depressed = True
			delta = time.time() - start
			duration = duration + delta
			if duration > 10:
				subprocess.call('shutdown -h now', shell=True)
				duration = 0
				break
		else:
			if button_depressed == True:
				duration = 0
				button_depressed = False
			time.sleep(1)
def edge_detected(pin):
	t.start()
	GPIO.remove_event_detect(pin)
if __name__ == '__main__':
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(5, GPIO.IN)
		GPIO.add_event_detect(5, GPIO.FALLING, callback=edge_detected, bouncetime=200)
		t = threading.Timer(0.1, shutdown)
		while True:
			pass
	finally:
		GPIO.cleanup()
