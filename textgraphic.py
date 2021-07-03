from graphic import Graphic

class Textgraphic(Graphic):

	def __init__(self,text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf',time=-1):
		self.text = text
		self.size = size
		self.coord = coord
		self.color = color
		self.font = font
		self.ff = False
		self.life = 10
		self.time = time
		#super().__init__('N/A',coord)
		


	def floatFade(self):
		self.life-=1
		self.coord = (self.coord[0],self.coord[1]-3)
		if self.life<=0: return True
		
