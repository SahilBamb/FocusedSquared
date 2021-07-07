from graphic import Graphic
import pygame

class Textgraphic(Graphic):

	def __init__(self,name,text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf',time=-1,clickable=False):
		self.toI = 'TEXT'
		self.clickable = clickable
		self.name = name
		self.text = text
		self.size = size
		self.coord = coord
		self.color = color
		self.font = font
		self.time = time
		#super().__init__('N/A',coord)
		self.moving = False
		self.setBoundaries(size,coord)

	def clicked(self,x,y):
		if not self.clickable: return False
		if self.y < y < self.bottomMost and self.x < x < self.rightMost:
			if '>' not in self.text: self.text = f'>{self.text}'
			return True
		else:
			self.text = self.text.strip('>')

	def floatFade(self):
		self.life-=1
		self.coord = (self.coord[0],self.coord[1]-3)
		if self.life<=0: return True

	def setBoundaries(self,size,coord):
		self.coord = coord
		self.x = x = coord[0]
		self.y = y = coord[1]
		width = size
		height = size
		#I don't think it accurately captures the height
		try:
			surface = pygame.font.Font(self.font, self.size).render(self.text, True, self.color)
			width = surface.get_width()
			height = surface.get_height()
		except:
			width = 0
			height = 0
		topLeft = coord
		topRight = (x+width,y)
		botLeft = (x,y+height)
		botRight = (x+width,y+height)
		self.rightMost = x+width
		self.bottomMost = y+height
		return (topLeft,topRight,botLeft,botRight)