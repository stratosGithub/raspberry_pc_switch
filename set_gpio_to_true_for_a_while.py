import sys
import os

import time
import RPi.GPIO as GPIO
from argparse import ArgumentParser


parser = ArgumentParser(description='arguments for gpio setting')

parser.add_argument( '--duration', required=False, type=float, default='6', help='dura$

if __name__ == '__main__':

        args = parser.parse_args()

        ## this is all the input we get from cmd arguments
        duration = args.duration

        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        #Set pin 15 (GPIO22) as input pin
        output_pin = 17
        GPIO.setup(output_pin,GPIO.OUT)

        if duration>0:
                GPIO.output(output_pin, True)
                time.sleep(duration)
                GPIO.output(output_pin, False)
        else:
                for i in range(10):
                        GPIO.output(output_pin, True)
                        time.sleep(1)
                        GPIO.output(output_pin, False)
                        time.sleep(1)

        # when your code ends, the last line before the program exits would be...
        GPIO.cleanup()


