
import pygame
import inputControl
import graphic
import gridtile
import random
from pygame.locals import *


#Known bugs: in loadList Tile number is wrong. It works for single digits but is not able to parse out after that 


def main():
	global pygame,loadList, win, count, LatestTile, TakenGrid, loadGrid

	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0))

	#@loadList['Tile1'] = graphic.Graphic("DirtTile.png",(250,250),True)
	loadList['Background'].name = "Background"	

	loadGrid = [[None for x in range(10)] for y in range(10)]
	for x in range(10):
		for y in range(10):
			loadGrid[x][y] = gridtile.Gridtile(x,y)

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
	#pygame.display.set_icon(pygame.image.load('logo.png') )


def update(): 
	global pygame, count, win, loadList, loadGrid

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList, loadGrid)

	#time delay
	pygame.time.delay(100)

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


'''
	if Overlap:
		loadList.pop(prevTileName)
		loadList[prevTileName] = prevTile
'''

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
	global pygame, win,count, LatestTile, loadList
	if i.upper()=='A':
		return
	else:	
		for event in pygame.event.get():
			if event.type==pygame.QUIT: 
				count=1001
				print("Quitting")
			
			elif event.type== MOUSEBUTTONDOWN: 
				x = pygame.mouse.get_pos()[0]
				y = pygame.mouse.get_pos()[1]
				hold = clickCheck(x,y)
				if hold: loadList[hold].picPath='GrassTile.png'

			
			if event.type==pygame.KEYDOWN:

				if event.key == pygame.K_RIGHT:
					updateGraphic(LatestTile,1,0,"INCR")

				elif event.key == pygame.K_LEFT:
					updateGraphic(LatestTile,-1,0,"INCR")

				elif event.key == pygame.K_UP: 
					updateGraphic(LatestTile,0,-1,"INCR")

				elif event.key == pygame.K_DOWN:
					updateGraphic(LatestTile,0,1,"INCR") 

				if event.key == pygame.K_ESCAPE: pass

				if event.key == pygame.K_SPACE:
					AddTile()

def loadGraphics(loadList,loadGrid):
	global pygame,win
	for graphic in loadList:
		pictureObj = loadList[graphic]
		if type(pictureObj)==str:
			win.blit(pygame.image.load(pictureObj),(0,0))
		else:
			win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)

	for row in loadGrid:
		for tile in row:
			if tile:
				win.blit(pygame.image.load(tile.picPath),tile.coord)



def clickCheck(x,y):
	global loadList
	for row in loadGrid:
		for tile in row:
			if tile:
				pictureObj = tile
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					print(f'Clicking on {pictureObj}')



	for graphic in loadList:
		pictureObj = loadList[graphic]
		if type(pictureObj)==str:
			continue
		else:
			if pictureObj.clickable: #Equally horrible peice of code that restricts clicking based on precision (hard coded so not adjusted to size like it should be)
				if pictureObj.y+5<y<pictureObj.bottomMost-10 and pictureObj.x+5<x<pictureObj.rightMost-10:
					print(f'Clicking on {pictureObj}')
					if 'Grass' not in pictureObj.picPath: return graphic
					#Horrible piece of code that makes this link dependent on not being 'Grass'

	return None


main()


while count<1000:
	update()
	#AddTile()




	




