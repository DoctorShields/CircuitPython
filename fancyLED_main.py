from fancyLED import FancyLED
import board

pins1 = [board.D1, board.D2, board.D3]
pins2 = [board.D4, board.D5, board.D7]

fancy1 = FancyLED(pins1)
fancy2 = FancyLED(pins2)

print("go")

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()