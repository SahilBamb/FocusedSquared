import pygame
from pygame.locals import *

pygame.init()
loadList = []
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Productivity MinMaxer")

pygame.mouse.set_visible(True)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
#pygame.display.set_icon(pygame.image.load('logo.png') )

txt = pygame.font.Font('Pixeled.ttf', 8).render('Hello there', True, (0,0,0)),(0,0)
text_width, text_height = txt

count = 0
while (count<1001):
	win.blit(pygame.image.load('Background.png'),(0,0))
	win.blit(txt)

	

	for event in pygame.event.get():
		if event.type==pygame.QUIT: count=1001
		
		elif event.type== MOUSEBUTTONDOWN: 
			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]
			print(f'x: {x} y: {y}')
		
		if event.type==pygame.KEYDOWN:

			if event.key == pygame.K_RIGHT: pass

			elif event.key == pygame.K_LEFT: pass

			if event.key == pygame.K_ESCAPE: pass


	pygame.time.delay(100)

	pygame.display.update()