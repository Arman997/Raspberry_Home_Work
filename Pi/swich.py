import RPi.GPIO as GPIO
import time
ledPin = 4 
buttonPin = 17

def setup():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    x = False
    while True:
        if (GPIO.input(buttonPin)==1):
            print ( 'OFF' if  x else  'ON')    
            x = not x
            time.sleep(0.7)
            continue
        else :

            if x:
                GPIO.output(ledPin,GPIO.HIGH)
            else:
                GPIO.output(ledPin,GPIO.LOW)


def destroy():
    GPIO.output(ledPin, GPIO.LOW)     
    GPIO.cleanup()                    

if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()
