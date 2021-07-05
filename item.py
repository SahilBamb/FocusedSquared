import random
import graphic
import plant

class Item:

	def __init__(self, pic=None, planite=None, toI = 'NA', itemType='NA',itemName='NA',descrList=['']):
		self.pic = pic
		self.cost = 1
		self.plant = planite
		self.toI = toI
		self.itemType = itemType
		self.name = itemName
		self.descrList = [x[:20] for x in descrList]
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
class BasicSeed(Item):

	def __init__(self):
		pic = graphic.Graphic('BasicSeed','ITEMSeedInv.png',(0,0),True,'ITEM')
		plantie = plant.BasicPlant(30,random.randint(2,5))
		descrList = ['ItemType: Seed','A lil\' ol\' seed', 'Rarity: Common', 'Harvest: $3-4','Harvest Time: 30 mins']
		super().__init__(pic,plantie,'ITEM','SEED','Basic Seed',descrList)

class BlueSeed(Item):

	def __init__(self):
		pic = graphic.Graphic('BlueSeed','BlueSeed.png',(0,0),True,'ITEM')
		plantie = plant.BluePlant(30,random.randint(1,6))
		descrList = ['ItemType: Seed','Daba dee daba die', 'Rarity: Common', 'Harvest: $1-7','Harvest Time: 30 mins']
		super().__init__(pic,plantie,'ITEM','SEED','Blue Seed',descrList)

class PinkSeed(Item):

	def __init__(self):
		pic = graphic.Graphic('PinkSeed','PinkSeed.png',(0,0),True,'ITEM')
		plantie = plant.PinkPlant(45,[1,3,4,12][random.randint(0,3)])
		descrList = ['ItemType: Seed','Girly girl-ee pink', 'Rarity: Common', 'Harvest: $1,3,4,9,15','Harvest Time: 45 mins']
		super().__init__(pic,plantie,'ITEM','SEED','Pink Seed',descrList)