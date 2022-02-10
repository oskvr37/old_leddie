"""LINEAR FADE"""
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


"""hue to rgb"""
def hue_rgb(hue):
    STEP = 4.25
    if hue <= 60:
        r, g, b = 255, hue * 255 / 60, 0
    elif hue <= 120:
        hue -= 60
        r, g, b = 255 - hue * STEP, 255, 0
    elif hue <= 180:
        hue -= 120
        r, g, b = 0, 255, hue * STEP
    elif hue <= 240:
        hue -= 180
        r, g, b = 0, 255 - hue * STEP, 255
    elif hue <= 300:
        hue -= 240
        r, g, b = hue * STEP, 0, 255
    elif hue <= 360:
        hue -= 300
        r, g, b = 255, 0, 255 - hue * STEP
    else:
        return 255, 255, 255
    return int(r), int(g), int(b)


def smooth_rgb(rgb_1, rgb_2):
    SMOOTH_STEP = 10
    def fade(one, two):
        lower, reverse = one, False
        if one > two: lower, reverse = two, True
        step = abs(one - two) / SMOOTH_STEP
        arr = [int(round(s * step + lower, 0)) for s in range(1, 10)]
        if reverse:
            return arr[::-1] + [lower]
        return arr + [two]

    r1, g1, b1 = rgb_1
    r2, g2, b2 = rgb_2
    r, g, b = fade(r1, r2), fade(g1, g2), fade(b1, b2)
    rgb_list = zip(r, g, b)
    return rgb_list
