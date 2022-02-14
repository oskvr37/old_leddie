import board
import neopixel

import modes


PIN = board.D18
LED_COUNT = 86


class Pixel:
	def __init__(self) -> None:
		self.led_count, self.pin = LED_COUNT, PIN
		self.pixel = neopixel.NeoPixel(self.pin, self.led_count, auto_write=False)
		self.color: tuple = (0, 0, 0)
		self.startup()

	def startup(self):
		for hue in range(0, 360):
			self.pixel.fill(modes.hue_rgb(hue))
			self.pixel.write()
		self.fill((0, 0, 0))

	def fill(self, rgb):
		for color in modes.smooth_rgb(self.color, rgb):
			self.pixel.fill(color)
			self.pixel.write()
		self.color = color

	def fade(self, color_one, color_two):
		index = 0
		colors = modes.smooth_rgb(color_one, color_two, self.led_count)
		for color in colors:
			self.pixel[index] = color
			index += 1
		self.pixel.write()
