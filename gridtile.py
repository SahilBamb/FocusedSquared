from graphic import Graphic
import plant

class Gridtile(Graphic):

	def __init__(self,x,y,kind='DIRT'):

		self.plant = None

		self.Gridx = x
		self.Gridy = y
		slx = 190
		sly = 250
		
		if y==0:
			y = slx+(y+1)*x*8
			x = sly+x*16

		if y==1:
			y = slx+8+(y)*x*8
			x = sly+(x-1)*16

		if y==2:
			y = slx+16+(y-1)*x*8
			x = sly+(x-2)*16

		if y==3:
			y = slx+24+(y-2)*x*8
			x = sly+(x-3)*16

		if y==4:
			y = slx+32+(y-3)*x*8
			x = sly+(x-4)*16

		if y==5:
			y = slx+40+(y-4)*x*8
			x = sly+(x-5)*16

		if y==6:
			y = slx+48+(y-5)*x*8
			x = sly+(x-6)*16

		if y==7:
			y = slx+56+(y-6)*x*8
			x = sly+(x-7)*16

		if y==8:
			y = slx+64+(y-7)*x*8
			x = sly+(x-8)*16

		if y==9:
			y = slx+72+(y-8)*x*8
			x = sly+(x-9)*16
			
		coord = (x,y)

		super().__init__(f'TILE{x}{y}',self.assignKind(kind),coord,True,'TILE')

	def assignKind(self,kind):
		tileTypes = {'DIRT':'DirtTile.png','GRASS':'GrassTile.png','OUTGRID':'OutlinedDirtBlock.png'}
		if kind in tileTypes:
			self.kind = kind
			self.name = f'{kind} Tile'
			return tileTypes[kind]

	def plantOn(self,plant):
		self.plant = plant

	def grow(self,time=0):
		if self.plant:
			self.plant.grow(time)

	def getOnTop(self):
		allOnTop = []
		if self.plant: allOnTop.append(self.plant)
		return allOnTop

	def harvest(self):
		if self.plant and self.plant.ReadytoHarvest:
			val = self.plant.harvest
			self.plant = None
			return val
		else:
			return False


		


