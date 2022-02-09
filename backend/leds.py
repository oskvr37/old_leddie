import board
import neopixel

from modes import hue_rgb


PIN = board.D18
LED_COUNT = 86


class Pixel:
    def __init__(self) -> None:
        self.pixel = neopixel.NeoPixel(board.D18, 86, auto_write=False)
        self.startup()

    def startup(self):
        for hue in range(0, 361):
            self.fill(hue_rgb(hue))
        self.fill((0, 0, 0))

    def fill(self, rgb):
        self.color = rgb
        self.pixel.fill(rgb)
        self.pixel.write()
