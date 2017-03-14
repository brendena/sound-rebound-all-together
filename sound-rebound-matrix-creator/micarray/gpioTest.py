import RPi.GPIO as GPIO
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script");
    
#33 - 13
#29 - 5
def start():
	gpio5 = 29
	gpio13 = 13


	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(gpio5, GPIO.IN)
	GPIO.setup(gpio13, GPIO.IN)

	print("Here we go! Press CTRL+C to exit")

	output = False;
	number = 0;

	try:
		while 1:
			if GPIO.input(gpio5): # button is released
				if output != False:
					print("wen't through")
					output = True;
					GPIO.cleanup()
					break;
				number += 1
			number += 1
			
	except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
		GPIO.cleanup() # cleanup all GPIO
	
	

print "This is a MATRIX Creator demo - not ready for production"  
start()
