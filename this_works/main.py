import touchio
#import digitalio
#import analogio
#import neopixel
import board
import time
#import servo
#import busio

print("hi")
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

touchBtn = touchio.TouchIn(board.A0)
touchToggle = touchio.TouchIn(board.A1)
lastTouch = False
lastToggle = False
up = True
touchCount = 0

lcd.print("Touches | Up/Dn")
lcd.set_cursor_pos(1, 0)
lcd.print("0       | Up")

while True:
    if touchBtn.value and not lastTouch:
        touchCount = touchCount + 1 if up else touchCount - 1
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(touchCount)+"   ")
    if touchToggle.value and not lastToggle:
        up = not up
        lcd.set_cursor_pos(1, 8)
        msg = "| Up" if up else "| Dn"
        lcd.print(msg)
    lastTouch = touchBtn.value
    lastToggle = touchToggle.value
    time.sleep(0.05)