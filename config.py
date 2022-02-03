import board
import neopixel

PIN = board.D18
LED_COUNT = 86

LEDS = neopixel.NeoPixel(PIN, LED_COUNT, auto_write=False)
