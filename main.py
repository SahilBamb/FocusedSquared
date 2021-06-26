
import pygame
import inputControl
import graphic
import random
from pygame.locals import *





def main():
	global pygame,loadList, win, count, LatestTile, TakenGrid

	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0))

	loadList['Tile1'] = graphic.Graphic("DirtTile.png",(250,250),True)
	loadList['Background'].name = "Background"	

	loadList['Background'].name = "Background"

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
	global pygame, count, win, loadList

	#iterate count
	count = count+1 if count<999 else 0

	#check inputs
	inputCheck()

	#load all images
	loadGraphics(loadList)

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
		TakenGrid.append((x,y))

		allKeys = list(loadList.keys())
		index = 0
		while (index<len(allKeys)):
			g = allKeys[index]
			if loadList[g].y > y or (loadList[g].y == y and loadList[g].x < x):
				loadList[g] = loadList.pop(g)
				print(f'Moved tile back')
			index+=1

	else:	
		print("No space available")

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
	global pygame, win,count, LatestTile
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
				clickCheck(x,y)
			
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

def loadGraphics(loadList):
	global pygame,win
	for graphic in loadList:
		pictureObj = loadList[graphic]
		if type(pictureObj)==str:
			win.blit(pygame.image.load(pictureObj),(0,0))
		else:
			win.blit(pygame.image.load(pictureObj.picPath),pictureObj.coord)

def clickCheck(x,y):
	global loadList
	for graphic in loadList:
		pictureObj = loadList[graphic]
		if type(pictureObj)==str:
			continue
		else:
			if pictureObj.clickable:
				if pictureObj.y<y<pictureObj.bottomMost and pictureObj.x<x<pictureObj.rightMost:
					print(f'Clicking on {pictureObj}')


main()


while count<1000:
	update()




	




