from graphic import Graphic

class Gridtile(Graphic):

	def __init__(self,x,y,kind='DIRT'):
		
		if y==0:
			y = 100+(y+1)*x*8
			x = 200+x*16

		if y==1:
			y = 108+(y)*x*8
			x = 200+(x-1)*16

		if y==2:
			y = 116+(y-1)*x*8
			x = 200+(x-2)*16

		if y==3:
			y = 124+(y-2)*x*8
			x = 200+(x-3)*16

		if y==4:
			y = 132+(y-3)*x*8
			x = 200+(x-4)*16

		if y==5:
			y = 140+(y-4)*x*8
			x = 200+(x-5)*16

		if y==6:
			y = 148+(y-5)*x*8
			x = 200+(x-6)*16

		if y==7:
			y = 156+(y-6)*x*8
			x = 200+(x-7)*16

		if y==8:
			y = 164+(y-7)*x*8
			x = 200+(x-8)*16

		if y==9:
			y = 172+(y-8)*x*8
			x = 200+(x-9)*16
			
		coord = (x,y)

		super().__init__(self.assignKind(kind),coord)

	def assignKind(self,kind):
		tileTypes = {'DIRT':'DirtTile.png','GRASS':'GrassTile.png'}
		if kind in tileTypes:
			self.kind = kind
			self.name = f'{kind}'
			return tileTypes[kind]
		


