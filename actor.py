import graphic
import random
import os

class Actor:

	def __init__(self,x,y,img,item,speed=5):
		self.name = item.name
		self.item = item
		self.facingRight = True
		self.toI = 'ACTOR'
		self.speed = speed
		#picPath = [f'{img}{_}.png' for _ in range(1,4)]
		picPath = [f'{img}{_}.png' for _ in range(1,10) if os.path.exists(f'{img}{_}.png')]

		#if len(picPath)==1: picPath = picPath[0]
		self.image = graphic.Graphic('Actor',picPath,(x,y),True)
		self.route = None
		self.minX = 50
		self.maxX = 400
		self.minY = 50
		self.maxY = 100
		self.wait = 0

	def getPicPath(self,):
		return self.image.getPicPath(False)

	def getCoord(self,):
		return self.image.getCoord()

	def iterate(self,GridBounds):
		if self.wait:
			self.wait-=1
		elif not random.randint(0,100):
			self.wait = random.randint(0,40)
			if random.randint(0,1): self.facingRight = False if self.facingRight else False
		else:
			self.setBackNForth(GridBounds)
			return self.image.iterate()
		return self.image

	def setBackNForth(self,GridBounds):
		oldx, oldy = self.image.x, self.image.y
		steps = self.speed
		if self.facingRight and self.image.x<self.maxX: 
			oldx+=steps
		elif self.image.x>=self.maxX: 
			oldx-=steps
			self.facingRight=False
		elif not self.facingRight and self.minX<self.image.x: 
			oldx-=steps
		else: 
			oldx+=steps
			self.facingRight=True
		if oldx<GridBounds['minX'] or GridBounds['maxX']<oldx or oldy<GridBounds['minY'] or GridBounds['maxY']<oldy:
			print('oof out of bounds')
			self.facingRight = False if self.facingRight else True
			self.wait = 0
			return
		self.image.x = oldx
		self.image.y = oldy

	def setRandomWalk(self,):
		if random.randint(0,1) and self.image.x<self.maxX: 
			self.image.x+=1
			self.facingRight = True
		elif random.randint(0,1) and self.minX<self.image.x: 
			self.image.x-=1
			self.facingRight = False
		elif random.randint(0,1) and self.image.y<self.maxY: 
			self.image.y+=1
		elif random.randint(0,1) and self.minY<self.image.y:
		 	self.image.y-=1

	def clicked(self,x,y):
		return self.image.clicked(x,y, False)
		#hard coded might need to be changed

	def getOnTop(self):
		return []
		
		
