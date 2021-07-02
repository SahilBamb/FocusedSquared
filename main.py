
import pygame
import inputControl
import graphic
import gridtile
import textgraphic
import random
import plant
import RGBColors
import item
from pygame.locals import *


#Known bugs: in loadList Tile number is wrong. It works for single digits but is not able to parse out after that 


def main():
	global pygame,loadList, win, count, loadGrid, loadTextList, endTime, tempTime, currency, inventory, PlantingOnX, PlantingOnY, currentItem
	global ux, uy, speed

	ux = 70
	uy = 373
	speed = 1
	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#Intilizie Inventory
	inventory = [item.Item(graphic.Graphic('ITEMSeedInv.png',(20+(51*x),432),True,'ITEM'),plant.Plant(),'ITEM','SEED') for x in range(1)]

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0),False,'UI')

	#loadList['CountdownFrame'] = graphic.Graphic("FrameTrace.png",(210,10),True)

	loadList['Background'].name = "Background"	
	loadList['SELECTOR'] = None

	#Inventory Frame
	loadList['Inventory'] = graphic.Graphic("InventoryFrame.png",(0,411),True,'UI')

	loadList['Clover'] = graphic.Graphic("Clovercon.png",(100,36),True,'UI')
	loadList['Clover'].name = 'Clover'
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


def update(): 
	global pygame, count, win, loadList, loadGrid, endTime, tempTime, inventory
	global ux, uy

	#loadList['Test'].coord = (ux, uy)

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList, loadGrid, loadTextList, inventory)

	if endTime:
		if ((endTime-pygame.time.get_ticks()) % 60000 ) < 100:
			print("Issa growin!")
			growTiles(loadGrid,1)
		if setTime(0,0,'UPDAT'):
			tempTime = 45
			endTime = None

	#time delay
	pygame.time.delay(50)

	#update the screen
	pygame.display.update()

def growTiles(loadGrid,timePassed):
	for row in loadGrid:
		for tile in row:
			if tile: tile.grow(timePassed)

def inputCheck(i='None'):
	global pygame, win,count, loadList, endTime, loadGrid, loadTextList, PlantingOnX, PlantingOnY, currentItem, inventory, tempTime, currency
	global ux, uy, speed

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
				if clickingOn:
					if clickingOn.toI == 'UI':
						if not endTime:
							if clickingOn.name=='Heart':
								setTime(15, 0, 'INCR')
							elif clickingOn.name == 'Shell':
								setTime(0, 0, 'SET')
							elif clickingOn.name == 'Clover':
								setTime(0, 0, 'INIT')

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
				'''
				clickingOn = clickCheck(x,y)
				if clickingOn:
					if clickingOn.isTile():
						if PlantingOnX and PlantingOny:
							Gridx = clickingOn.Gridx
							PlantingOnX = Gridx
							Gridy = clickingOn.Gridy
							PlantingOny = Gridx
							print(f"Going to plant on {Gridx}, {Gridy}")
						else:
							PlantingOnX = PlantingOny = None

						if clickingOn.plant:
							h = loadGrid[Gridx][Gridy].grow()
							if h: 
								loadTextList['Money'] = textgraphic.Textgraphic(f'+{h}',8,(x-5,y-5),RGBColors.getRandomColor())
								loadTextList['Money'].ff=True
						else:
							loadGrid[Gridx][Gridy].plantOn(plant.Plant)
						'''

			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT: ux+=speed
				elif event.key == pygame.K_LEFT: ux-=speed
				#if event.key == pygame.K_ESCAPE:
					#tempTime = 45
					#endTime = None
				if not endTime:
					if event.key == pygame.K_UP:
						setTime(0,3,'INCR')
						#setTime(1,0,'INCR')
					elif event.key == pygame.K_DOWN: uy+=speed
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
				

def loadGraphics(loadList,loadGrid, loadTextList, inventory):
	global pygame, win
	for image in loadList:
		pictureObj = loadList[image]
		if not pictureObj: continue
		else:
			win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)
	for slot in inventory:
		if slot:
			win.blit(pygame.image.load(slot.pic.picPath), (slot.pic.coord[0],slot.pic.coord[1]))
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
	for t in loadTextList:
		if loadTextList[t].ff: 
			if loadTextList[t].floatFade(): 
				removeList.append(t)
		t = loadTextList[t]
		drawText(t.text,t.size,t.coord,t.color,t.font)

	for t in removeList:
		loadTextList.pop(t)


def clickCheck(x,y):
	global loadList, loadGrid, inventory, count, currentItem
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

	for i in inventory:
		if i:
			pictureObj = i.pic
			if pictureObj.y + 5 < y < pictureObj.bottomMost and pictureObj.x + 5 < x < pictureObj.rightMost:
				return i

	reverseKeys = list(loadList.keys())
	reverseKeys.reverse()
	for image in reverseKeys:
		pictureObj = loadList[image]
		if not pictureObj: continue
		else:
			if pictureObj.clickable: 
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					#if 'Countdown' in image:
					#	loadList['SELECTOR'] = graphic.Graphic('TimerFrameSelector.png',(loadList['CountdownFrame'].x,loadList['CountdownFrame'].y,False,'UI'))
					#else: loadList['SELECTOR'] = None
					#print(f'Clicking on {pictureObj}')
					return pictureObj

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
		loadTextList['TIMER1'].text = f'{minutes:02}:{seconds:02}'
		return False
	else: return False
	tempTime = min((99*60)+59,tempTime)
	loadTextList['TIMER'].text = f'{tempTime//60:02}:{tempTime%60:02}'
	loadTextList['TIMER1'].text = f'{tempTime//60:02}:{tempTime%60:02}'


def drawText(text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf'):
	global pygame, win
	win.blit(pygame.font.Font(font, size).render(text, True, color),coord)

main()

while count<1000:
	update()
	