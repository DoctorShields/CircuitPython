from time import sleep
import board
from rgb import RGB
import neopixel

pins1 = [board.D1, board.D2, board.D3]
pins2 = [board.D4, board.D5, board.D7]
delay = 1

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
RGBs = [RGB(pins1, dot), RGB(pins2, dot)]

print("go")

while True:
    for i in RGBs: i.red()
    sleep(delay)
    for i in RGBs: i.green()
    sleep(delay)
    for i in RGBs: i.blue()
    sleep(delay)
    for i in RGBs: i.cyan()
    sleep(delay)
    for i in RGBs: i.magenta()
    sleep(delay)
    for i in RGBs: i.yellow()
    sleep(delay)
    for i in RGBs: i.white()
    sleep(delay)
    for i in RGBs: i.black()
    sleep(delay)
    for i in RGBs: i.rainbow()
    sleep(delay)