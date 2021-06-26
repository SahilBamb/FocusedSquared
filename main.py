import pygame
import inputControl
import graphic
from pygame.locals import *





def main():
	global pygame,loadList, win, count

	#Intilize actual game
	pygame.init()

	#loadlist for images
	loadList = {}

	#set background
	loadList['Background'] = graphic.Graphic("Background.png",(0,0))

	loadList['GridTile1'] = graphic.Graphic("DirtTile.png",(250,250),True)
	loadList['Background'].name = "Background"	

	loadList['Background'].name = "Background"

	#timeVariable
	count=0

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


def inputCheck(i='None'):
	global pygame, win,count
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

				if event.key == pygame.K_RIGHT: pass

				elif event.key == pygame.K_LEFT: pass

				if event.key == pygame.K_ESCAPE: pass

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




	




