def hue_rgb(hue) -> tuple[int, int, int]:
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
