def linear(one, two, count):
    difference = abs(one-two)
    rev, adjust = False, one
    if two < one: rev, adjust = True, two
    step = difference / (count - 1)
    colors = [round(color * step + adjust) for color in range(0, count)]
    if rev: colors.reverse()
    return colors


def linearFade(firstColor, secondColor, count):
    r1, g1, b1 = firstColor
    r2, g2, b2 = secondColor
    return list(zip(linear(r1, r2, count), linear(g1, g2, count), linear(b1, b2, count)))


BLUE = (0, 0, 255)
PINK = (255, 0, 0)
COUNT = 86

print(linearFade(BLUE, PINK, COUNT))
