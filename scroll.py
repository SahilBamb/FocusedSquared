import pygame, item
import random
import graphic
import item
import actor

from item import Item

class Scroll(Item):
	def __init__(self,pic=None,name='Scroll',cost=100,descrList=['']):
		super().__init__(pic,'Scroll',name,cost,descrList,'Rare')


class StoreScroll(Scroll):
	def __init__(self,pic,name,cost,descrList):
		super().__init__(pic,name, cost, descrList)

	def getScroll(self):
		self.uses-=1
		self.descrList[1] = f'Good for {self.uses} uses'
		return self.StoreAddress

class StoreOneScroll(StoreScroll):
	def __init__(self):
		self.uses = random.randint(1,7)
		descrList = ['A Store Scroll','Find an exotic store',f'Good for {self.uses} uses']
		self.StoreAddress = 'Asian Girl Store'
		pic = graphic.Graphic('Store Scroll','StoreScroll1.png',(0,0),True,'ITEM')
		super().__init__(pic,'Asian Store Scroll', 1, descrList)

class StoreTwoScroll(StoreScroll):
	def __init__(self):
		self.uses = random.randint(1,5)
		descrList = ['A Store Scroll','Find an Aussie Store',f'Good for {self.uses} uses']
		self.StoreAddress = 'Camo Girl Store'
		pic = graphic.Graphic('Store Scroll','StoreScroll4.png',(0,0),True,'ITEM')
		super().__init__(pic,'Camo Store Scroll', 1, descrList)

