import board
import neopixel

PIN = board.D18
LED_COUNT = 86

pixel = neopixel.NeoPixel(board.D18, 86)

COLORS = {'red': (255, 0, 0), 'blue': (0, 0, 255), 'green': (0, 255, 0), 'magenta': (255, 0, 255)}
