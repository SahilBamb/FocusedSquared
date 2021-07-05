from graphic import Graphic

class Textgraphic(Graphic):

	def __init__(self,name,text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf',time=-1):
		self.toI = 'TEXT'
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
		topLeft = coord
		topRight = (x+width,y)
		botLeft = (x,y+height)
		botRight = (x+width,y+height)
		self.rightMost = x+width
		self.bottomMost = y+height
		return (topLeft,topRight,botLeft,botRight)