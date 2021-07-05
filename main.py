
import pygame
import inputControl
import graphic
import gridtile
import textgraphic
import random
import plant
import RGBColors
import item
import pickle
import session
from pygame.locals import *
from datetime import date


#Known bugs: in loadList Tile number is wrong. It works for single digits but is not able to parse out after that


def main():
	global pygame,loadList, win, count, loadGrid, loadTextList, endTime, tempTime, currency, inventory, currentItem, loadAboveGrid
	global sessionsList
	global ux, uy, speed

	ux = 10
	uy = 115
	speed = 1
	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#Intilizie Inventory
	#inventory = [item.Item(graphic.Graphic('ITEMSeedInv.png',(0,0),True,'ITEM'),plant.Plant(),'ITEM','SEED','Basic Seed') for x in range(9)]
	inventory = [item.BasicSeed(),item.BlueSeed(),item.PinkSeed()]
	InventoryUpdate()
	#inventory = [None, None, None]

	#INVENTORY IS HARDCODED TO SLOT ITEMS NEED TO FIND A BETTER
	#A suggestion would be to

	loadAboveGrid = {}

	#set background
	loadList['Background'] = graphic.Graphic('Background',"Background.png",(0,0),False,'UI')

	#loadList['CountdownFrame'] = graphic.Graphic("FrameTrace.png",(210,10),True)

	loadList['Background'].name = "Background"
	loadList['SELECTOR'] = None

	#Inventory Frame
	loadList['Inventory'] = graphic.Graphic('Inventory',"InventoryFrame.png",(0,411),True,'UI')
	loadList['Plus'] = graphic.Graphic('Plus',"Plus.png",(100,36),True,'UI')
	loadList['Heart'] = graphic.Graphic('Heart',"HeartIcon.png",(100,62),True,'UI')
	loadList['Shell'] = graphic.Graphic('Shell',"Shell.png", (100, 85), True,'UI')

	#Currency
	loadList['CurrencyCoin'] = graphic.Graphic('CurrencyCoin',"Coins.png",(16,368),False,'UI')

	loadGrid = [[None for x in range(10)] for y in range(10)]
	for x in range(10):
		for y in range(10):
			loadGrid[x][y] = gridtile.Gridtile(x,y,'OUTGRID')
			loadGrid[x][y].name += f' x:{x},y:{y}'
			#loadGrid[x][y].plantOn(plant.Plant())

	tempTime = 45*60
	endTime = None
	loadTextList = {'TIMER': textgraphic.Textgraphic('TIMER',f'{tempTime//60:02}:{tempTime%60:02}',100,(135,20),RGBColors.GRAY,'iflash-502.ttf')}
	loadTextList.update({'TIMER1': textgraphic.Textgraphic('TIMER1',f'{tempTime//60:02}:{tempTime%60:02}',100,(135,12),RGBColors.DDG,'iflash-502.ttf')})

	currentItem = None
	currency = 0


	loadTextList['Currency2'] = textgraphic.Textgraphic('Currency2',f"${currency}", 15, (72,375), (0,0,0), 'Pixeled.ttf')
	loadTextList['Currency'] = textgraphic.Textgraphic('Currency',f"${currency}", 15, (70,373), RGBColors.Gold, 'Pixeled.ttf')

	#timeVariable
	count=0

	#Screen
	win = pygame.display.set_mode((500,500))
	pygame.display.set_caption("Focused Squared")
	pygame.mouse.set_visible(True)
	pygame.mouse.set_cursor(*pygame.cursors.tri_left)
	pygame.display.set_icon(pygame.image.load('logo.png') )
	sessionsList = []

	#Load From Savefile
	#saveLoad('L')

#Adds item to global inventory, updates their location information
def InventoryUpdate():
	global inventory
	for i in range(len(inventory)):
		if inventory[i]:
			inventory[i].pic.setBoundaries(inventory[i].pic.picPath,(20 + (51*i), 432))
			inventory[i].invSlot = i

def TextBubble(t='G'):
	global loadTextList, loadList
	if len(t)>1:
		phrase = t
	else:
		files = {'G':'GenericLines.txt','F':'FailLines.txt','S':'SuccessLines.txt'}
		txt = open(files[t],'r') if t in files else open(files['G'],'r')
		txtList = txt.readlines()
		phrase = txtList[random.randint(0,len(txtList)-1)].strip()
		txt.close()

	loadList['Text'] = graphic.Graphic('Text',"SmallerTextBox.png", (153, 133), False, 'UI',50)
	loadTextList['Text'] = textgraphic.Textgraphic(phrase[0:40], 10, (163, 140), (0, 0, 0), 'iflash-502.ttf',50)
	if len(phrase)>39: loadTextList['Text2'] = textgraphic.Textgraphic(phrase[40:78], 10, (163, 152), (0, 0, 0), 'iflash-502.ttf',50)

def update():
	global pygame, count, win, loadList, loadGrid, endTime, tempTime, inventory, sessionsList
	global ux, uy

	#loadList['Test'].coord = (ux, uy)
	#loadTextList['Test'].coord = (ux, uy)

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList, loadGrid, loadTextList, loadAboveGrid, inventory)

	weatherMangement(loadAboveGrid)

	if endTime:
		if ((endTime-pygame.time.get_ticks()) % 60000 ) < 100:
			if 'Weather' in loadAboveGrid: growTiles(loadGrid,4)
			else: growTiles(loadGrid,1)
		if setTime(0,0,'UPDAT'):
			saveSession(tempTime//60)
			getItems()
			InventoryUpdate()
			if not random.randint(0,10): TextBubble('S')
			tempTime = 0
			endTime = None

	#time delay
	pygame.time.delay(50)

	#update the screen
	pygame.display.update()


#lol shouldn't exist please delete
def getItems():
	global inventory
	print('got some items')
	for index in range(len(inventory)):
		if not inventory[index]:
			inventory[index] = [item.BasicSeed(),item.BlueSeed(),item.PinkSeed()][random.randint(0,2)]
			return
	print("No room in inventory")

def saveSession(t):
	global sessionsList
	if t>0:
		today = str(date.today())
		sessionsList.append(session.Session(today,t,'N/A'))

#Would appreciate this being outsourced to a seperate file or something
def weatherMangement(loadAboveGrid):
	if 'Weather' not in loadAboveGrid:
		if not random.randint(0,2000):
			duration = random.randint(100,1000)
			loadAboveGrid['Weather'] = graphic.Graphic('Weather',['Rain1.png', 'Rain2.png', 'Rain3.png'], (0, 0), False, 'UI',duration)
			TextBubble("it started raining!")
		elif not random.randint(0, 10000):
			duration = random.randint(100, 1000)
			loadAboveGrid['Weather'] = graphic.Graphic('Weather',['Snow1.png', 'Snow2.png', 'Snow3.png'], (0, 0), False, 'UI',duration)
			TextBubble("it started snowing!")

def growTiles(loadGrid,timePassed):
	for row in loadGrid:
		for tile in row:
			if tile: tile.grow(timePassed)

#Needs Fixing... a lot of fixing...
def inputCheck(i='None'):
	global pygame, win,count, loadList, endTime, loadGrid, loadTextList, currentItem, inventory, tempTime, currency
	global ux, uy, speed

	if i.upper()=='A':
		return
	else:
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		clickCheck(x,y)
		#print(f'x is {x} and y ix {y}')

		for event in pygame.event.get():
			if event.type==pygame.QUIT: count=1001

			elif event.type== MOUSEBUTTONDOWN:

				clickingOn = clickCheck(x,y)
				if clickingOn:
					if clickingOn.toI == 'UI':
						if not endTime:
							if clickingOn.name=='Heart': setTime(0, 0, 'INIT')
							elif clickingOn.name == 'Shell': setTime(0, 0, 'SET')
							elif clickingOn.name == 'Plus': setTime(15, 0, 'INCR')

					elif clickingOn.toI=='TILE':
						Gridx = clickingOn.Gridx
						Gridy = clickingOn.Gridy

						#If I'm holding a seed and clicking a tile
						if currentItem and currentItem.itemType=='SEED':
							if not loadGrid[Gridx][Gridy].plant:
								print(f"Going to plant on {Gridx}, {Gridy}")
								loadGrid[Gridx][Gridy].plantOn(currentItem.plant)
								loadList.pop('InvCursor')
								inventory[currentItem.invSlot] = None
								currentItem = None
							else:
								print("That location is already planted")

						# If I'm clicking a harvestable tile
						elif loadGrid[Gridx][Gridy].plant and loadGrid[Gridx][Gridy].plant.ReadytoHarvest:
							moneyGain(loadGrid[Gridx][Gridy].harvest())

					elif clickingOn.toI=='ITEM':
						# #Will pickup Seed and put it in currentItem
						if clickingOn.itemType=='SEED':
							if currentItem:
								print(f'De-selecting {currentItem}')
								currentItem = None
								loadList.pop('InvCursor')
						# Will pickup Seed and put it in currentItem
							else:
								currentItem = clickingOn
								ix = currentItem.pic.x
								iy = currentItem.pic.y
								loadList['InvCursor'] = graphic.Graphic('InvCursor',"InvCursor.png", (ix, iy), False, 'UI')
								print(f'Selecting {currentItem}')

			if event.type==pygame.KEYDOWN:
				KeyInputCheck(event.key)

def moneyGain(m,x,y):
	global loadTextList, currency
	currency += m
	loadTextList['Currency2'] = textgraphic.Textgraphic('Currency2',f"${currency}", 15, (72, 375), (0, 0, 0), 'Pixeled.ttf')
	loadTextList['Currency'] = textgraphic.Textgraphic('Currency',f"${currency}", 15, (70, 373), RGBColors.Gold, 'Pixeled.ttf')
	loadTextList['Money'] = textgraphic.Textgraphic('Money',f'+{m}', 8, (x - 5, y - 5), RGBColors.getRandomColor(),'Pixeled.ttf', -10)
	loadTextList['Money'].moving = [0, -5]

def KeyInputCheck(i):
	if i == pygame.K_RIGHT: pass
	elif i == pygame.K_LEFT: pass
	elif i == pygame.K_ESCAPE: setTime(0,0,'SET')
	elif i == pygame.K_LSHIFT: pass
	elif not endTime:
		if i == pygame.K_UP: setTime(0,3,'INCR')
		elif i == pygame.K_DOWN: setTime(-1,0,'INCR')
		elif i == K_0: setTime(0,0,'SET')
		elif i == K_1: setTime(15,0,'INCR')
		elif i == pygame.K_SPACE: setTime(0, 0, 'INIT')

def loadAll(l):
	global pygame,win
	r = []
	printToScreen = lambda pic, coord : win.blit(pygame.image.load(pic),(coord))
	for p in l:
		if type(l)==dict: p = l[p]
		if p:
			if p.toI=='TEXT': drawText(p.text,p.size,p.coord,p.color,p.font)
			else: printToScreen(p.getPicPath(), p.getCoord())
			if not p.iterate(): r.append(p)
			for o in p.getOnTop(): printToScreen(o.picPath,(p.coord[0],p.coord[1]-10))
	for p in r:
		l.pop(p.name)
	#I DON'T THINK THIS WORKS FOR LISTS (You can make it work by using enumerate and then appending indexes to r instead of keys
	return l

def loadGraphics(loadList, loadGrid, loadTextList, loadAboveGrid, inventory):
	global pygame, win, count

	loadList = loadAll(loadList)
	inventory = loadAll(inventory)
	for row in loadGrid: loadAll(row) #Doesn't return an updated grid (for removing through timeline)
	loadAboveGrid = loadAll(loadAboveGrid)
	loadTextList = loadAll(loadTextList)

def clickCheckAll(l,x,y,onTop=[]):
	c = list(l.keys())[::-1] if type(l)==dict else l[::-1]
	for p in c:
		p = l[p] if type(l)==dict else p
		if p and p.clicked(x,y): return p
	return None

def clickCheck(x,y):
	global loadList, loadGrid, inventory, count, currentItem, loadTextList

	for row in loadGrid:
		a = clickCheckAll(row,x,y)
		if a:
			loadAboveGrid['SELECTOR'] = graphic.Graphic('SELECTOR','Selector.png', (a.x, a.y), False,'UI',1)
			return a

	for l in [loadAboveGrid,inventory,loadList]:
		l = clickCheckAll(l,x,y)
		if l: return l

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
		loadTextList['TIMER'].text = loadTextList['TIMER1'].text = f'{minutes:02}:{seconds:02}'
		#loadTextList['TIMER1'].text = f'{minutes:02}:{seconds:02}'
		return False
	else: return False
	tempTime = min((99*60)+59,tempTime)
	loadTextList['TIMER'].text = loadTextList['TIMER1'].text = f'{tempTime//60:02}:{tempTime%60:02}'
	#loadTextList['TIMER1'].text = f'{tempTime//60:02}:{tempTime%60:02}'

def drawText(text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf'):
	global pygame, win
	win.blit(pygame.font.Font(font, size).render(text, True, color),coord)

def saveLoad(t='S'):
	global currency, inventory, loadGrid, sessionsList
	if t=='S':
		print('Saving...')
		with open("savegame", "wb") as f:
			allVariables = [currency,inventory,loadGrid,sessionsList]
			pickle.dump(allVariables, f)
	if t=='L':
		print("Loading...")
		with open("savegame", "rb") as f:
			allVariables = pickle.load(f)
			currency = allVariables[0]
			inventory = allVariables[1]
			loadGrid = allVariables[2]
			sessionsList = allVariables[3]

main()

while count<1000:
	update()

saveLoad('S')
