from time import sleep
from pulseio import PWMOut
from random import randint

class FancyLED:

    full = 2**16-1

    def __init__(self, pins):
        self.pwmList = []
        for pin in pins:
            self.pwmList.append(PWMOut(pin, duty_cycle=0,frequency=5000))

    def setVals(self, arr):
        for i, pwm in enumerate(self.pwmList):
            pwm.duty_cycle = int(self.full-arr[i]*self.full)

    def alternate(self):
        for i in range(50):
            arr = (1, 0, 1)
            self.setVals(arr)
            sleep(.1)
            arr = (0, 1, 0)
            self.setVals(arr)
            sleep(.1)

    def blink(self):
        for i in range(50):
            arr = (1, 1, 1)
            self.setVals(arr)
            sleep(.1)
            arr = (0, 0, 0)
            self.setVals(arr)
            sleep(.1)

    def chase(self):
        for i in range(50):
            arr = (1, 0, 0)
            self.setVals(arr)
            sleep(.1)
            arr = (0, 1, 0)
            self.setVals(arr)
            sleep(.1)
            arr = (0, 0, 1)
            self.setVals(arr)
            sleep(.1)

    def sparkle(self):
        for i in range(50):
            arr = (randint(0,1), randint(0,1), randint(0,1))
            self.setVals(arr)
            sleep(.1)
