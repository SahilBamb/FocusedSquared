import pygame

class Graphic:

	def __init__(self,picPath="ErrorIcon.png",coord=(0,0),clickable=False):
		
		try: 
			self.img = pygame.image.load(picPath)
			self.picPath = picPath
		except: 
			self.picPath = "ErrorIcon.png"
		
		self.coord = coord
		self.setBoundaries(picPath, coord)
		self.clickable = clickable
		self.name = ""


	def __str__(self):
		return self.name if len(self.name)>0 else f"Name N/A - Picture Path: {self.picPath}"


	def setBoundaries(self,picPath,coord):
		self.x = x = coord[0]
		self.y = y = coord[1]
		surface = self.img
		width = surface.get_width()
		height = surface.get_height()
		topLeft = coord
		topRight = (x+width,y)
		botLeft = (x,y+height)
		botRight = (x+width,y+height)
		self.rightMost = x+width
		self.bottomMost = y+height
		return (topLeft,topRight,botLeft,botRight) 
		

