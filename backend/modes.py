def hue_rgb(hue):
	step = 4.25
	hue %= 360
 
	if hue <= 60:
		r, g, b = 255, hue * 255 / 60, 0
	elif hue <= 120:
		hue -= 60
		r, g, b = 255 - hue * step, 255, 0
	elif hue <= 180:
		hue -= 120
		r, g, b = 0, 255, hue * step
	elif hue <= 240:
		hue -= 180
		r, g, b = 0, 255 - hue * step, 255
	elif hue <= 300:
		hue -= 240
		r, g, b = hue * step, 0, 255
	elif hue <= 360:
		hue -= 300
		r, g, b = 255, 0, 255 - hue * step
	else:
		print('unexpected hue: ', hue)
		return 255, 255, 255
	return int(r), int(g), int(b)


def smooth_rgb(rgb_1, rgb_2, smoothness=20):
	def fade(one, two):
		lower, reverse = one, False
		if one > two: lower, reverse = two, True
		step = abs(one - two) / smoothness
		arr = [int(round(s * step + lower, 0)) for s in range(1, smoothness)]
		if reverse:
			return arr[::-1] + [lower]
		return arr + [two]

	r1, g1, b1 = rgb_1
	r2, g2, b2 = rgb_2
	r, g, b = fade(r1, r2), fade(g1, g2), fade(b1, b2)
	rgb_list = list(zip(r, g, b))
	return rgb_list
