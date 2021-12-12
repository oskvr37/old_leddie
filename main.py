from modes import linearFade
from leds import Leds

BLUE = (0, 0, 255)
PINK = (255, 0, 255)
COUNT = 86

fade = linearFade(BLUE, PINK, COUNT)

for f in fade:
    Leds.fill(f)
    Leds.show()
