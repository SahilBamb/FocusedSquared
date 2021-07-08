import pygame
from pygame.locals import *

def universal(event):
	if event.type==pygame.QUIT: exit()
	
	elif event.type== MOUSEBUTTONDOWN: 
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
	
	if event.type==pygame.KEYDOWN:

		if event.key == pygame.K_RIGHT: pass

		elif event.key == pygame.K_LEFT: pass

		if event.key == pygame.K_ESCAPE: pass