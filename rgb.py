from pulseio import PWMOut
from time import sleep

class RGB:

    full = 2**16-1
    dotB = 50

    def __init__(self, pins, dot):
        self.pwmList = []
        for pin in pins:
            self.pwmList.append(PWMOut(pin, duty_cycle=0,frequency=5000))
            self.dot = dot

    def setVals(self, arr):
        dotArr = [0,0,0]
        for i, pwm in enumerate(self.pwmList):
            pwm.duty_cycle = int(self.full-arr[i]*self.full)
            dotArr[i] = arr[i]*self.dotB
        self.dot.fill((dotArr[0],dotArr[1],dotArr[2]))

    def red(self):
        arr = (1, 0, 0)
        self.setVals(arr)

    def green(self):
        arr = (0, 1, 0)
        self.setVals(arr)

    def blue(self):
        arr = (0, 0, 1)
        self.setVals(arr)

    def magenta(self):
        arr = (1, 0, 1)
        self.setVals(arr)

    def cyan(self):
        arr = (0, 1, 1)
        self.setVals(arr)

    def yellow(self):
        arr = (1, 1, 0)
        self.setVals(arr)

    def white(self):
        arr = (1, 1, 1)
        self.setVals(arr)

    def black(self):
        arr = (0, 0, 0)
        self.setVals(arr)

    def rainbow(self):
        dt = .01
        for i in range(0,100):
            arr = (i/100,0,0)
            self.setVals(arr)
            sleep(dt)
        for i in range(0,100):
            arr = (1,i/100,0)
            self.setVals(arr)
            sleep(dt)
        for i in range(0,100):
            arr = (1-i/100,1,0)
            self.setVals(arr)
            sleep(dt)
        for i in range(0,100):
            arr = (0,1-i/100,i/100)
            self.setVals(arr)
            sleep(dt)
        for i in range(0,100):
            arr = (i/100,0,1)
            self.setVals(arr)
            sleep(dt)