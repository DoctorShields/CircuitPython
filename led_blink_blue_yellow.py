import board
import neopixel
import time

# make a neopixel object
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

# this will run forever
while True:
    print("Make it blue!")
    dot.fill((0,0,255))
    time.sleep(.5)
    print("Make it yellow!")
    dot.fill((255,255,0))
    time.sleep(.5)
    # made a change
