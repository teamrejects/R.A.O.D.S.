def alcoholval():
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.IN)


    return GPIO.input(13)
    time.sleep(0.2)
    GPIO.cleanup()
