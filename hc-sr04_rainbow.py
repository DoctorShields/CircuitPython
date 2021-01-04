import time
import board
import adafruit_hcsr04
import neopixel
from math import sin, pi

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

def cap(n, minn, maxn):
    return round(min(max(n, minn), maxn))

def makeColor():
    d = sonar.distance
    r = cap(260 - sonar.distance/15*255, 0, 255)
    g = cap((sonar.distance-20)/15*255,0, 255)
    b = sin(cap(sonar.distance-5,0,30)/30*pi)*255
    color = (r,g,b)
    print(color)
    dot.fill(color)

print("running!")

while True:
    try:
        makeColor()
    except:
        print("oops")
    # makeColor()
    time.sleep(0.1)