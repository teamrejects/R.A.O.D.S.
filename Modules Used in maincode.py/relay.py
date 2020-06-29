





def fuel_flow():
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, GPIO.LOW)
    
    GPIO.cleanup()
     
def fuel_stop():
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, GPIO.HIGH)
    
    



# 