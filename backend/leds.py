import board
import neopixel

import modes


PIN = board.D18
LED_COUNT = 86


class Pixel:
    def __init__(self) -> None:
        self.pixel = neopixel.NeoPixel(board.D18, 86, auto_write=False)
        self.color = (0, 0, 0)
        self.startup()

    def startup(self):
        for hue in range(0, 361):
            self.pixel.fill(modes.hue_rgb(hue))
            self.pixel.write()
        self.fill((0, 0, 0))

    def fill(self, rgb):
        for color in modes.smooth_rgb(self.color, rgb):
            self.pixel.fill(color)
            self.pixel.write()
        self.color = color
