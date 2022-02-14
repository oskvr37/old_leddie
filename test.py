latest = []
favs = [1, 2, 3, 4, 5]

def changeColor(color):
	if color not in latest:
		if len(latest) > 9:
			latest.insert(0, color)
			latest.pop()


def addFav(color):
	if color not in favs:
		if len(favs) > 4:
			favs.insert(0, color)
			favs.pop()


addFav(1)
addFav(5)
addFav(3)
addFav(8)
addFav(9)
