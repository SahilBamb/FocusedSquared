
import pygame
import inputControl
import graphic
import gridtile
import textgraphic
import random
from pygame.locals import *


#Known bugs: in loadList Tile number is wrong. It works for single digits but is not able to parse out after that 


def main():
	global pygame,loadList, win, count, loadGrid, loadTextList, endTime, tempTime

	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0))

	loadList['CountdownFrame'] = graphic.Graphic("TimerFrame.png",(300,10),True)
	loadList['CountdownAdd'] = graphic.Graphic("ADD.png",(395,100),True)
	loadList['CountdownCross'] = graphic.Graphic("CROSS.png",(435,99),True)
	loadList['CountdownStart'] = graphic.Graphic("BATT.png",(320,102),True)
	
	
	loadList['Background'].name = "Background"	
	loadList['SELECTOR'] = None


	loadGrid = [[None for x in range(10)] for y in range(10)]
	for x in range(10):
		for y in range(10):
			loadGrid[x][y] = gridtile.Gridtile(x,y,'OUTGRID')
			loadGrid[x][y].name += f' x:{x},y:{y}'


	tempTime = 45*60
	endTime = None
	loadTextList = {'TIMER': textgraphic.Textgraphic(f'{tempTime//60:02}:{tempTime%60:02}',40,(310,0))}
	
	#timeVariable
	count=0

	#Screen
	win = pygame.display.set_mode((500,500))
	pygame.display.set_caption("Focused Squared")
	pygame.mouse.set_visible(True)
	pygame.mouse.set_cursor(*pygame.cursors.tri_left)
	pygame.display.set_icon(pygame.image.load('logo.png') )


def update(): 
	global pygame, count, win, loadList, loadGrid, endTime, tempTime

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList, loadGrid, loadTextList)

	if endTime:
		if setTime(0,0,'UPDAT'):
			tempTime = 45
			endTime = None

	#time delay
	pygame.time.delay(50)

	#update the screen
	pygame.display.update()


def inputCheck(i='None'):
	global pygame, win,count, loadList, endTime
	if i.upper()=='A':
		return
	else:
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		clickCheck(x,y)

		for event in pygame.event.get():
			if event.type==pygame.QUIT: 
				count=1001
			
			elif event.type== MOUSEBUTTONDOWN: 
				clickingOn = clickCheck(x,y)
				if clickingOn == 'CountdownAdd':
					setTime(15,0,'INCR')
				elif clickingOn == 'CountdownCross':
					setTime(0,0,'SET')
				elif clickingOn == 'CountdownStart':
					setTime(0,0,'INIT')


			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT: pass
				elif event.key == pygame.K_LEFT: pass
				if not endTime: 
					if event.key == pygame.K_UP: setTime(1,0,'INCR')
					elif event.key == pygame.K_DOWN: setTime(-1,0,'INCR')
					elif event.key == K_0: setTime(0,0,'SET')
					elif event.key == K_1: setTime(15,0,'INCR')
				if event.key == pygame.K_SPACE:
					if clickCheck(x,y)=='CountdownFrame':
						setTime(0,0,'INIT')
				

def loadGraphics(loadList,loadGrid, loadTextList):
	global pygame, win
	for image in loadList:
		pictureObj = loadList[image]
		if not pictureObj: continue
		else:
			win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)

	for row in loadGrid:
		for tile in row:
			if tile:
				win.blit(pygame.image.load(tile.picPath),tile.coord)

	if loadList['SELECTOR']: 
		pictureObj = loadList['SELECTOR']
		win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)

	for t in loadTextList:
		t = loadTextList[t]
		drawText(t.text,t.size,t.coord,t.color,t.font)



def clickCheck(x,y):
	global loadList, loadGrid, count
		
	for row in loadGrid:
		for tile in row:
			if tile:
				pictureObj = tile
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					loadList['SELECTOR'] = graphic.Graphic('Selector.png',(pictureObj.x,pictureObj.y))
					return tile

	loadList['SELECTOR'] = None

	reverseKeys = list(loadList.keys())
	reverseKeys.reverse()
	for image in reverseKeys:
		pictureObj = loadList[image]
		if not pictureObj: continue
		else:
			if pictureObj.clickable: 
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					if 'Countdown' in image:
						loadList['SELECTOR'] = graphic.Graphic('TimerFrameSelector.png',(loadList['CountdownFrame'].x,loadList['CountdownFrame'].y))
					else: loadList['SELECTOR'] = None
					#print(f'Clicking on {pictureObj}')
					return image

	loadList['SELECTOR'] = None
	return None

def setTime(minutes=0,seconds=0, m='SET'):
	global tempTime, loadTextList, endTime
	if m == 'INIT': endTime = pygame.time.get_ticks()+int((1000*tempTime))
	elif m == 'INCR': tempTime += (minutes*60)+seconds
	elif m == 'SET' : tempTime = (minutes*60)+seconds
	elif m == 'UPDAT':
		milliseconds = endTime-pygame.time.get_ticks()
		minutes = milliseconds//60000
		seconds = (milliseconds%60000) //1000
		if milliseconds<=0: return True
		loadTextList['TIMER'].text = f'{minutes:02}:{seconds:02}'
		return False
	else: return False
	tempTime = min((99*60)+59,tempTime)
	loadTextList['TIMER'].text = f'{tempTime//60:02}:{tempTime%60:02}'


def drawText(text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf'):
	global pygame, win
	win.blit(pygame.font.Font(font, size).render(text, True, color),coord)

main()

while count<1000:
	update()
	