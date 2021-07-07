import random
import graphic
import plant

class Item:

	def __init__(self, pic=None,itemType='NA',name='NA',cost=1,descrList=[''],rarity='COMMON'):
		self.toI = 'ITEM'
		self.pic = pic
		self.cost = 1
		self.itemType = itemType
		self.name = name
		self.rarity = rarity
		self.descrList = self.SetDescr(descrList)
		self.invSlot = -1

	def clicked(self,x,y):
		return self.pic.clicked(x,y)

	def getPicPath(self,):
		return self.pic.getPicPath()

	def getCoord(self, ):
		return self.pic.getCoord()

	def getCoord(self, ):
		return self.pic.getCoord()

	def iterate(self, ):
		return self.pic.iterate()

	def getOnTop(self, ):
		return self.pic.getOnTop()

	def SetDescr(self,descrList):
		return [f'ItemType: {self.itemType}',descrList[0], f'Rarity: {self.rarity}', descrList[1] ,descrList[2], f'cost: {self.cost}']

class BasicSeed(Item):

	def __init__(self):
		pic = graphic.Graphic('BasicSeed','ITEMSeedInv.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.BasicPlant(30,random.randint(2,5))
		descrList = ['A lil\' ol\' seed','Harvest: $3-4','Harvest Time: 30 mins']
		super().__init__(pic,'SEED','Basic Seed',1,descrList,'COMMON')

class BlueSeed(Item):

	def __init__(self):
		pic = graphic.Graphic('BlueSeed','BlueSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.BluePlant(30,random.randint(1,6))
		descrList = ['Daba dee daba die', 'Harvest: $1-7','Harvest Time: 30 mins']
		super().__init__(pic,'SEED','Blue Seed',3,descrList,'COMMON')

class PinkSeed(Item):

	def __init__(self):
		pic = graphic.Graphic('PinkSeed','PinkSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.PinkPlant(45,[1,3,4,12][random.randint(0,3)])
		descrList = ['ItemType: Seed','Girly girl-ee pink', 'Rarity: Common', 'Harvest: $1,3,4,9,15','Harvest Time: 45 mins']
		super().__init__(pic,'SEED','Pink Seed',3,descrList,'COMMON')