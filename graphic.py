import pygame

class Graphic:

	def __init__(self,picPath="ErrorIcon.png",coord=(0,0),clickable=False,toI='N/A',time=-1, frame = 0):
		self.frame = frame
		self.frames = [picPath] if type(picPath)==str else picPath
		try: 
			#self.img = pygame.image.load(picPath)
			self.picPath = self.frames[0]
		except: 
			self.picPath = "ErrorIcon.png"

		self.time = time
		self.toI = toI
		self.coord = coord
		self.setBoundaries(self.picPath, coord)
		self.clickable = clickable

		try: self.name
		except: self.name = ""

	def __str__(self):
		return self.name if len(self.name)>0 else f"Name N/A - Picture Path: {self.picPath}"

	def setBoundaries(self,picPath,coord):
		self.x = x = coord[0]
		self.y = y = coord[1]
		try: surface = pygame.image.load(picPath)
		except: print(picPath)
		width = surface.get_width()
		height = surface.get_height()
		topLeft = coord
		topRight = (x+width,y)
		botLeft = (x,y+height)
		botRight = (x+width,y+height)
		self.rightMost = x+width
		self.bottomMost = y+height
		self.bouncing = False
		return (topLeft,topRight,botLeft,botRight)

	def moveGraphic(self,x,y):
		self.x = x
		self.y = y
		self.coord = (x,y)

	def isTile(self):
		return 'TILE' in self.name.upper()

	def isItem(self):
		return 'ITEM' in self.name.upper()

	def iterate(self):
		self.time-=1
		self.frame = self.frame+1 if self.frame<len(self.frames)-1 else 0
		if len(self.frames)>1:
			self.picPath=self.frames[self.frame]



		

