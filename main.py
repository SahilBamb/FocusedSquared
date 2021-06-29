
import pygame
import inputControl
import graphic
import gridtile
import textgraphic
import random
from pygame.locals import *


#Known bugs: in loadList Tile number is wrong. It works for single digits but is not able to parse out after that 


def main():
	global pygame,loadList, win, count, LatestTile, TakenGrid, loadGrid, loadTextList, endTime, tempTime, UIList

	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0))



	UIList = {}
	UIList['CountdownAdd'] = graphic.Graphic("ADD.png",(395,100),True)
	UIList['CountdownCross'] = graphic.Graphic("CROSS.png",(435,99),True)
	UIList['CountdownStart'] = graphic.Graphic("BATT.png",(320,102),True)

	loadList['CountdownFrame'] = graphic.Graphic("TimerFrame.png",(300,10),True)
	
	

	loadList['Background'].name = "Background"	
	loadList['SELECTOR'] = None



	loadGrid = [[None for x in range(10)] for y in range(10)]
	for x in range(10):
		for y in range(10):
			loadGrid[x][y] = gridtile.Gridtile(x,y,'OUTGRID')


	tempTime = 45*60
	loadTextList = {'TIMER': textgraphic.Textgraphic(f'{tempTime//60:02}:{tempTime%60:02}',40,(310,0))}
	endTime = None

	#timeVariable
	count=0
	
	#LatestTile
	LatestTile = "Tile1"


	#What grid spots are tken
	TakenGrid = []

	#Screen
	win = pygame.display.set_mode((500,500))
	pygame.display.set_caption("Focused Squared")
	pygame.mouse.set_visible(True)
	pygame.mouse.set_cursor(*pygame.cursors.tri_left)
	pygame.display.set_icon(pygame.image.load('logo.png') )


def update(): 
	global pygame, count, win, loadList, loadGrid, UIList, endTime, tempTime

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList, loadGrid, loadTextList, UIList)

	if endTime:
		if updateTime():
			tempTime = 45
			endTime = None

	#time delay
	pygame.time.delay(50)

	#update the screen
	pygame.display.update()


def AddTile():
	global pygame, count, win, loadList, LatestTile, TakenGrid
	prevTile = loadList[LatestTile]
	prevTileName = LatestTile

	Overlap = False
	loc = random.randint(0, 3)


	if loc == 0:
		x = prevTile.x+16
		y = prevTile.y+8
	elif loc == 1:
		x = prevTile.x-16
		y = prevTile.y+8
	elif loc == 2:
		x = prevTile.x-16
		y = prevTile.y-8
		Overlap = True
	elif loc == 3:
		x = prevTile.x+16
		y = prevTile.y-8 
		Overlap = True


	if (x,y) not in TakenGrid: 
		TileNum = str(int(LatestTile[-1])+1)
		LatestTile = LatestTile[:-1]+TileNum 
		loadList[LatestTile] = graphic.Graphic("DirtTile.png",(x,y),True)
		loadList[LatestTile].name = LatestTile[:-1]+TileNum 
		TakenGrid.append((x,y))

		allKeys = list(loadList.keys())
		index = 0
		while (index<len(allKeys)):
			g = allKeys[index]
			if loadList[g].y > y or (loadList[g].y == y and loadList[g].x < x):
				loadList[g] = loadList.pop(g)
				#print(f'Moved tile back')
			index+=1


def updateGraphic(name,x=0,y=0,m="SET"):
	global loadList
	if name in loadList:
		pictureObj = loadList[name]
	else:
		print("No graphic exists")
		return
	if m=="SET":
		pictureObj.moveGraphic(x,y)
		print(f'Set to {x} and {y}')
	if m=="INCR":
		pictureObj.moveGraphic(pictureObj.x+x,pictureObj.y+y)
		print(f'Moved to {pictureObj.x+x} and {pictureObj.y+y}')
	loadList[name] = pictureObj

		

def inputCheck(i='None'):
	global pygame, win,count, LatestTile, loadList, endTime
	if i.upper()=='A':
		return
	else:
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		clickCheck(x,y)

		for event in pygame.event.get():
			if event.type==pygame.QUIT: 
				count=1001
				print("Quitting")
			
			elif event.type== MOUSEBUTTONDOWN: 
				clickingOn = clickCheck(x,y)
				if clickingOn == 'CountdownAdd':
					setTime(15,0,'INCR')
				elif clickingOn == 'CountdownCross':
					setTime(0,0,'SET')
				if clickingOn == 'CountdownStart':
					timeStart()


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
						timeStart()
				

def loadGraphics(loadList,loadGrid, loadTextList, UIList):
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


	for u in UIList:
		pictureObj = UIList[u]
		win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)

	for t in loadTextList:
		t = loadTextList[t]
		drawText(t.text,t.size,t.coord,t.color,t.font)



def clickCheck(x,y):
	global loadList, loadGrid, count, UIList


	for u in UIList:
		pictureObj = UIList[u]
		if pictureObj.clickable: 
			if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
				return u
					

	for row in loadGrid:
		for tile in row:
			if tile:
				pictureObj = tile
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					loadList['SELECTOR'] = graphic.Graphic('Selector.png',(pictureObj.x,pictureObj.y))
					#if count%3==0: 
					return tile

	loadList['SELECTOR'] = None

	for image in loadList:
		pictureObj = loadList[image]
		if not pictureObj: continue
		else:
			if pictureObj.clickable: 
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					if image=='CountdownFrame':
						loadList['SELECTOR'] = graphic.Graphic('TimerFrameSelector.png',(pictureObj.x,pictureObj.y))
					else: loadList['SELECTOR'] = None
					print(f'Clicking on {pictureObj}')
					return image

	loadList['SELECTOR'] = None
	return None


def setTime(minutes=0,seconds=0, m='SET'):
	global tempTime, loadTextList
	if m == 'INCR': tempTime += (minutes*60)+seconds
	elif m == 'SET' : tempTime = (minutes*60)+seconds
	else: return False
	tempTime = min((99*60)+59,tempTime)
	loadTextList['TIMER'].text = f'{tempTime//60:02}:{tempTime%60:02}'


def timeStart():
	global endTime, tempTime
	endTime = pygame.time.get_ticks()+int((1000*tempTime))

def updateTime():
	global endTime, loadTextList
	milliseconds = endTime-pygame.time.get_ticks()
	minutes = milliseconds//60000
	seconds = (milliseconds%60000) //1000
	if milliseconds<=0: return True
	loadTextList['TIMER'].text = f'{minutes:02}:{seconds:02}'
	return False


	minutes, seconds = divmod(timeSeconds, 60)
	while timeLeft:
		
		timeText = '{:02d}:{:02d}'.format(minutes, seconds)
		print(timeText)
		time.sleep(1)
		timeSeconds -= 1

def drawText(text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf'):
	global pygame, win
	win.blit(pygame.font.Font(font, size).render(text, True, color),coord)

main()


while count<1000:
	update()
	#AddTile()




	




