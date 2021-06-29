from graphic import Graphic

class Textgraphic(Graphic):

	def __init__(self,text='Sample Text',size=40,coord=(230,200),color=(82,123,219),font='Pixeled.ttf'):
		self.text = text
		self.size = size
		self.coord = coord
		self.color = color
		self.font = font
		#super().__init__('N/A',coord)
		


