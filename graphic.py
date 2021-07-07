import pygame

class Graphic:

	def __init__(self,name,picPath="ErrorIcon.png",coord=(0,0),clickable=False,toI='N/A',time=-1, frame = 0):
		self.toI = toI
		self.name = name
		self.moving = False
		self.frame = frame
		self.frames = [picPath] if type(picPath)==str else picPath
		picPath = self.frames[0]

		self.setBoundaries(picPath, coord)

		self.onTop = []

		self.time = time
		self.clickable = clickable

	def __str__(self):
		return self.name if len(self.name)>0 else f"Name N/A - Picture Path: {self.picPath}"

	def clicked(self,x,y):
		return (self.clickable and self.y+5 < y < self.bottomMost-10 and self.x+5 < x < self.rightMost-10)
		#hard coded might need to be changed

	def getPicPath(self):
		self.iterate()
		return self.picPath

	def getCoord(self):
		return self.coord

	def setBoundaries(self,picPath,coord):
		self.picPath = picPath
		self.coord = coord
		self.x = x = coord[0]
		self.y = y = coord[1]
		try:
			surface = pygame.image.load(picPath)
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

	def moveGraphic(self,x,y):
		self.x = x
		self.y = y
		self.coord = (x,y)

	#True if it still exists, false if it doesn't
	def iterate(self):
		if self.time>0: self.time-=1
		if self.moving:
			self.moveGraphic(self.x+self.moving[0],self.y+self.moving[1])
		if 'TEXT' not in self.toI:
			self.frame = self.frame+1 if self.frame<len(self.frames)-1 else 0
			if len(self.frames)>1: self.picPath=self.frames[self.frame]
		return False if self.time==0 else True

	def getOnTop(self):
		return []

	def changeTOI(self,toI):
		self.toI = toI
		return self



		

