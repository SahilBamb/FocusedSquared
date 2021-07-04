
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
	global pygame,loadList, win, count, loadGrid, loadTextList, endTime, tempTime, currency, inventory, PlantingOnX, PlantingOnY, currentItem, loadAboveGrid
	global store, storeInventory, sessionsList
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
	#inventory = [item.BasicSeed(),item.BlueSeed(),item.PinkSeed()]
	inventory = [None, None, None]

	#INVENTORY IS HARDCODED TO SLOT ITEMS NEED TO FIND A BETTER
	#A suggestion would be to

	loadAboveGrid = {}

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0),False,'UI')

	#loadList['CountdownFrame'] = graphic.Graphic("FrameTrace.png",(210,10),True)

	loadList['Background'].name = "Background"	
	loadList['SELECTOR'] = None

	#Inventory Frame
	loadList['Inventory'] = graphic.Graphic("InventoryFrame.png",(0,411),True,'UI')
	loadList['Plus'] = graphic.Graphic("Plus.png",(100,36),True,'UI')
	loadList['Plus'].name = 'Plus'
	loadList['Heart'] = graphic.Graphic("HeartIcon.png",(100,62),True,'UI')
	loadList['Heart'].name = 'Heart'
	loadList['Shell'] = graphic.Graphic("Shell.png", (100, 85), True,'UI')
	loadList['Shell'].name = 'Shell'

	#Currency
	loadList['CurrencyCoin'] = graphic.Graphic("Coins.png",(16,368),False,'UI')

	loadGrid = [[None for x in range(10)] for y in range(10)]
	for x in range(10):
		for y in range(10):
			loadGrid[x][y] = gridtile.Gridtile(x,y,'OUTGRID')
			loadGrid[x][y].name += f' x:{x},y:{y}'
			#loadGrid[x][y].plantOn(plant.Plant())

	PlantingOnX = PlantingOnY = None
	tempTime = 45*60
	endTime = None
	loadTextList = {'TIMER': textgraphic.Textgraphic(f'{tempTime//60:02}:{tempTime%60:02}',100,(135,20),RGBColors.GRAY,'iflash-502.ttf')}
	loadTextList.update({'TIMER1': textgraphic.Textgraphic(f'{tempTime//60:02}:{tempTime%60:02}',100,(135,12),RGBColors.DDG,'iflash-502.ttf')})

	currentItem = None
	currency = 0

	store = storeInventory = None

	loadTextList['Currency2'] = textgraphic.Textgraphic(f"${currency}", 15, (72,375), (0,0,0), 'Pixeled.ttf')
	loadTextList['Currency'] = textgraphic.Textgraphic(f"${currency}", 15, (70,373), RGBColors.Gold, 'Pixeled.ttf')

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
	saveLoad('L')



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

	loadList['Text'] = graphic.Graphic("SmallerTextBox.png", (153, 133), False, 'UI',50)
	loadTextList['Text'] = textgraphic.Textgraphic(phrase[0:40], 10, (163, 140), (0, 0, 0), 'iflash-502.ttf',50)
	if len(phrase)>39: loadTextList['Text2'] = textgraphic.Textgraphic(phrase[40:78], 10, (163, 152), (0, 0, 0), 'iflash-502.ttf',50)

def update(): 
	global pygame, count, win, loadList, loadGrid, endTime, tempTime, inventory, store, sessionsList
	global ux, uy

	#loadList['Test'].coord = (ux, uy)
	#loadTextList['Test'].coord = (ux, uy)

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList, loadGrid, loadTextList, loadAboveGrid, inventory)

	if not store: weatherMangement(loadAboveGrid)

	if endTime:
		if ((endTime-pygame.time.get_ticks()) % 60000 ) < 100:
			if 'Weather' in loadAboveGrid: growTiles(loadGrid,4)
			else: growTiles(loadGrid,1)
		if setTime(0,0,'UPDAT'):
			saveSession(tempTime//60)
			getItems()
			if not random.randint(0,10): TextBubble('S')
			tempTime = 0
			endTime = None

	#time delay
	pygame.time.delay(50)

	#update the screen
	pygame.display.update()

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

def weatherMangement(loadAboveGrid):
	if 'Weather' not in loadAboveGrid:
		if not random.randint(0,1000):
			duration = random.randint(100,1000)
			loadAboveGrid['Weather'] = graphic.Graphic(['Rain1.png', 'Rain2.png', 'Rain3.png'], (0, 0), False, 'UI',duration)
			TextBubble("it started raining!")
		elif not random.randint(0, 10000):
			duration = random.randint(100, 1000)
			loadAboveGrid['Weather'] = graphic.Graphic(['Snow1.png', 'Snow2.png', 'Snow3.png'], (0, 0), False, 'UI',duration)
			TextBubble("it started snowing!")

def growTiles(loadGrid,timePassed):
	for row in loadGrid:
		for tile in row:
			if tile: tile.grow(timePassed)

def loadStore(t='O'):
	global loadAboveGrid, store, storeInventory
	if t=='O':
		store = 'Basic'
		loadAboveGrid['StoreFrame'] = graphic.Graphic("Store.png", (10, 115), True, 'UI')
		allPossibleItems = [item.BasicSeed(), item.BlueSeed(), item.PinkSeed()]
		storeInventory = [allPossibleItems[random.randint(0,2)] for x in range(3)]
		loadAboveGrid['CloseStore'] = graphic.Graphic("Close.png", (211, 123), True, 'ClosedUI')
		loadAboveGrid['StoreOwner'] = graphic.Graphic("MouseStore.png", (200, 200), True, 'ClosedUI')
	elif t=='C':
		store = storeInventory = None
		loadAboveGrid.pop('StoreFrame')
		loadAboveGrid.pop('CloseStore')
		loadAboveGrid.pop('StoreOwner')

def inputCheck(i='None'):
	global pygame, win,count, loadList, endTime, loadGrid, loadTextList, PlantingOnX, PlantingOnY, currentItem, inventory, tempTime, currency
	global store, storeInventory
	global ux, uy, speed

	if i.upper()=='A':
		return
	else:
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		clickCheck(x,y)
		#print(f'x is {x} and y ix {y}')

		for event in pygame.event.get():
			if event.type==pygame.QUIT: 
				count=1001
			
			elif event.type== MOUSEBUTTONDOWN:
				clickingOn = clickCheck(x,y)
				if clickingOn:
					if store:
						if clickingOn.toI == 'ClosedUI':
							loadStore('C')
						elif clickingOn.toI == 'ITEM':
							for index in range(len(inventory)):
								if not inventory[index]:
									inventory[index] = storeInventory[((clickingOn.pic.x-20)//70)]
									storeInventory[((clickingOn.pic.x - 20) // 70)] = None
									if 'ItemLine1' in loadTextList:
										removeList = [p for p in loadTextList if 'Item' in p]
										for p in removeList: loadTextList.pop(p)

					if clickingOn.toI == 'UI':
						if not endTime:
							if clickingOn.name=='Heart':
								setTime(0, 0, 'INIT')
							elif clickingOn.name == 'Shell':
								#loadStore()
								setTime(0, 0, 'SET')
							elif clickingOn.name == 'Plus':
								setTime(15, 0, 'INCR')

					elif clickingOn.toI=='TILE':
						Gridx = clickingOn.Gridx
						PlantingOnX = Gridx
						Gridy = clickingOn.Gridy
						PlantingOny = Gridx
						if currentItem and currentItem.itemType=='SEED':
							if not loadGrid[Gridx][Gridy].plant:
								print(f"Going to plant on {Gridx}, {Gridy}")
								loadGrid[Gridx][Gridy].plantOn(currentItem.plant)
								loadList.pop('InvCursor')
								inventory[(currentItem.pic.x+20) // 51] = None
								currentItem = None
							else:
								print("That location is already planted")
						elif loadGrid[Gridx][Gridy].plant:
							if loadGrid[Gridx][Gridy].plant.ReadytoHarvest:
								h = loadGrid[Gridx][Gridy].harvest()
								currency += h
								loadTextList['Currency2'] = textgraphic.Textgraphic(f"${currency}", 15, (72, 375),(0, 0, 0), 'Pixeled.ttf')
								loadTextList['Currency'] = textgraphic.Textgraphic(f"${currency}", 15, (70, 373),RGBColors.Gold, 'Pixeled.ttf')
								loadTextList['Money'] = textgraphic.Textgraphic(f'+{h}', 8, (x - 5, y - 5),RGBColors.getRandomColor())
								loadTextList['Money'].ff = True

					elif clickingOn.toI=='ITEM':
						if clickingOn.itemType=='SEED':
							if currentItem:
								print(f'De-selecting {currentItem}')
								currentItem = None
								loadList.pop('InvCursor')
							else:
								currentItem = clickingOn
								ix = currentItem.pic.x
								iy = currentItem.pic.y
								loadList['InvCursor'] = graphic.Graphic("InvCursor.png", (ix, iy), False, 'UI')
								print(f'Selecting {currentItem}')
						if clickingOn.itemType == 'TILEEXPAND':
							pass

					print(clickingOn.toI)

			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT: ux+=speed
				elif event.key == pygame.K_LEFT: ux-=speed
				if event.key == pygame.K_ESCAPE:
					setTime(0,0,'SET')
					if endTime and not random.randint(0, 10): TextBubble('F')
					endTime = None
				if not endTime:
					if event.key == pygame.K_UP:
						uy-=speed
						setTime(0,3,'INCR')
					elif event.key == pygame.K_DOWN:
						uy+=speed
						#setTime(-1,0,'INCR')
					elif event.key == K_0: setTime(0,0,'SET')
					elif event.key == K_1: setTime(15,0,'INCR')
					elif event.key == pygame.K_SPACE:
						setTime(0,0,'INIT')
				if event.key == pygame.K_LSHIFT:
					speed-=1
					print(f'Speed is now {speed}')
				elif event.key == pygame.K_RSHIFT:
					speed+=1
					print(f'Speed is now {speed}')
				print(f'{ux} {uy}')
				

def loadGraphics(loadList,loadGrid, loadTextList, loadAboveGrid, inventory):
	global pygame, win, count, store, storeInventory

	removeList = []
	for image in loadList:
		pictureObj = loadList[image]
		if pictureObj:
			pictureObj.iterate()
			if pictureObj.time==0: removeList.append(image)
			win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)
	for image in removeList:
		loadList.pop(image)

	removeList = []
	for index in range(len(inventory)):
		slot = inventory[index]
		win.blit(pygame.image.load('InvSpot.png'), (24 + (51 * index), 433))
		if slot:
			#(20 + (51 * x), 432)
			slot.pic.iterate()
			if slot.pic.time == 0: removeList.append(index)
			win.blit(pygame.image.load(slot.pic.picPath), (20 + (51*index), 432))

	for slot in removeList:
		inventory[index]=None

	removeList = []
	for row in loadGrid:
		for tile in row:
			if tile:
				win.blit(pygame.image.load(tile.picPath),tile.coord)
				if tile.plant:
					win.blit(pygame.image.load(tile.plant.picPath),(tile.coord[0],tile.coord[1]-10))

	if loadList['SELECTOR']: 
		pictureObj = loadList['SELECTOR']
		win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)

	removeList = []
	for image in loadAboveGrid:
		pictureObj = loadAboveGrid[image]
		if pictureObj:
			pictureObj.iterate()
			if pictureObj.time == 0: removeList.append(image)
			win.blit(pygame.image.load(pictureObj.picPath), pictureObj.coord)

	for image in removeList:
		loadAboveGrid.pop(image)


	removeList = []
	for t in loadTextList:
		pictureObj = loadTextList[t]
		pictureObj.iterate()
		if pictureObj.time == 0: removeList.append(t)

		if pictureObj.ff:
			if pictureObj.floatFade():
				removeList.append(t)

		drawText(pictureObj.text,pictureObj.size,pictureObj.coord,pictureObj.color,pictureObj.font)

	for t in removeList:
		loadTextList.pop(t)

	if store:
		removeList = []
		for index in range(len(storeInventory)):
			slot = storeInventory[index]
			if slot:
				slot.pic.iterate()
				if slot.pic.time == 0: removeList.append(index)
				win.blit(pygame.image.load(slot.pic.picPath), (25 + (73 * index), 135))

		for slot in removeList:
			storeInventory[index]=None


def clickCheck(x,y):
	global loadList, loadGrid, inventory, count, currentItem, loadTextList, store, storeInventory

	if store:
		for index in range(len(storeInventory)):
			i = storeInventory[index]
			if i:
				pictureObj = i.pic
				pictureObj.setBoundaries(pictureObj.picPath, (25 + (70 * index), 135))
				if pictureObj.y + 5 < y < pictureObj.bottomMost and pictureObj.x + 5 < x < pictureObj.rightMost:
					loadList['SELECTOR'] = graphic.Graphic('ItemDescr.png', (13, 177),False, 'ItemUI')
					loadTextList['ItemLine1'] = textgraphic.Textgraphic(i.name, 8, (loadList['SELECTOR'].x + 7, loadList['SELECTOR'].y + 10), (0, 0, 0), "iflash-502.ttf")
					for n, line in enumerate(i.descrList):
						loadTextList[f'ItemLineDescr{n}'] = textgraphic.Textgraphic(line, 8, (loadList['SELECTOR'].x + 7, loadList['SELECTOR'].y + 20 + (10 * n)), (0, 0, 0),"iflash-502.ttf")
					return i



	#loadAboveGrid
	reverseKeys = list(loadAboveGrid.keys())
	reverseKeys.reverse()
	for image in reverseKeys:
		pictureObj = loadAboveGrid[image]
		if not pictureObj:
			continue
		else:
			if pictureObj.clickable:
				if pictureObj.y< y < pictureObj.bottomMost and pictureObj.x< x < pictureObj.rightMost:
					return pictureObj

	if 180<=y<=380:
		for row in loadGrid:
			for tile in row:
				if tile:
					pictureObj = tile
					if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
						if currentItem and currentItem.itemType=='SEED':
							loadList['SELECTOR'] = graphic.Graphic('PSelector.png', (pictureObj.x, pictureObj.y), False,'UI')
						elif pictureObj.plant and pictureObj.plant.ReadytoHarvest:
							loadList['SELECTOR'] = graphic.Graphic('HSelector.png', (pictureObj.x, pictureObj.y), False,'UI')
						else:
							loadList['SELECTOR'] = graphic.Graphic('Selector.png', (pictureObj.x, pictureObj.y), False,'UI')
						return tile

	loadList['SELECTOR'] = None
	if 'ItemLine1' in loadTextList and not loadList['SELECTOR']:
		removeList = [p for p in loadTextList if 'Item' in p]
		for p in removeList: loadTextList.pop(p)
	if y>=420:
		for index in range(len(inventory)):
			i = inventory[index]
			if i:
				pictureObj = i.pic
				pictureObj.setBoundaries(pictureObj.picPath,(20+(51*index),432))
				if pictureObj.y + 5 < y < pictureObj.bottomMost and pictureObj.x + 5 < x < pictureObj.rightMost:
					xShift = 50 if x<250 else -50
					loadList['SELECTOR'] = graphic.Graphic('ItemDescr.png', (pictureObj.x+xShift, pictureObj.y), False,'ItemUI')
					loadTextList['ItemLine1'] = textgraphic.Textgraphic(i.name, 8, (loadList['SELECTOR'].x + 7, loadList['SELECTOR'].y + 5), (0, 0, 0), "iflash-502.ttf")
					for n,line in enumerate(i.descrList):
						loadTextList[f'ItemLineDescr{n}'] = textgraphic.Textgraphic(line, 8, (loadList['SELECTOR'].x + 7, loadList['SELECTOR'].y + 20 + (10*n)), (0, 0, 0), "iflash-502.ttf")
					return i

	reverseKeys = list(loadList.keys())
	reverseKeys.reverse()
	for image in reverseKeys:
		pictureObj = loadList[image]
		if not pictureObj: continue
		else:
			if pictureObj.clickable: 
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					return pictureObj

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
		loadTextList['TIMER1'].text = f'{minutes:02}:{seconds:02}'
		return False
	else: return False
	tempTime = min((99*60)+59,tempTime)
	loadTextList['TIMER'].text = f'{tempTime//60:02}:{tempTime%60:02}'
	loadTextList['TIMER1'].text = f'{tempTime//60:02}:{tempTime%60:02}'


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
