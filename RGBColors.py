import random
Yellow = (237, 188, 55)
Red = (232, 58, 23)
Green = (48, 224, 36)
Teal = (25, 207, 207)
Blue = (24, 96, 204)
Purple = (93, 29, 196)
Pink = (212, 47, 212)
LightBlue = (102, 204, 255)
White = (255, 255, 255)
Mahagoney = (153, 51, 51)

PURP = (102, 0, 204)
LPURP = (102, 0, 255)
MAG = (51, 51, 204)
LBLUE = (102, 153, 255)
SBLUE = (51, 153, 255)
FBLUE = (51, 204, 255)
AQUA = (0, 255, 255)
GBLUE = (0, 255, 204)
DG = (0, 204, 153)
DDG = (51, 153, 102)

GRAY = (90, 99, 93)
DGRAY = (66, 69, 67)

Gold = (255, 204, 0)

DPURP = (51, 51, 153)
LGREEN = (204, 255, 51)

listofColors = [Yellow,Red,Green,Teal,Blue,Purple,Pink,LightBlue,White]

listofColors2 = [PURP,LPURP,MAG,LBLUE,SBLUE,FBLUE,AQUA,GBLUE,DG,DDG,Gold,DPURP,LGREEN]


def getRandomColor():
	global listofColors
	global listofColors2
	listofColors.extend(listofColors2)
	Tlen = len(listofColors)
	return listofColors[random.randint(0,Tlen-1)]
