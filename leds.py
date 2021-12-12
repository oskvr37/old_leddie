import board
import neopixel

PIN = board.D18
COUNT = 86

Leds = neopixel.NeoPixel(PIN, COUNT, auto_write=False)
