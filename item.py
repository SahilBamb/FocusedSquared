import random
import graphic
import plant

class Item:

	def __init__(self, pic=None,itemType='NA',name='NA',cost=1,descrList=[''],rarity='COMMON'):
		self.toI = 'ITEM'
		self.pic = pic
		self.cost = cost
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
		return [f'{self.name}',f'cost: {self.cost}',descrList[0], f'Rarity: {self.rarity}', descrList[1] ,descrList[2] ]
		#return [f'{self.name}', f'ItemType: {self.itemType}', descrList[0], f'Rarity: {self.rarity}', descrList[1],descrList[2], f'cost: {self.cost}']

class BasicSeed(Item):
# medium risk / medium reward seed
	def __init__(self):
		pic = graphic.Graphic('BasicSeed','GreenSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.BasicPlant(30,random.randint(2,4))
		descrList = ['A lil\' ol\' seed','Harvest: $2-4','Grow Time: 30 mins']
		super().__init__(pic,'SEED','Basic Seed',2,descrList,'COMMON')

class BlueSeed(Item):
# Low risk / low reward seed
	def __init__(self):
		pic = graphic.Graphic('BlueSeed','BlueSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.BluePlant(30,3)
		descrList = ['Daba dee daba die', 'Harvest: $3','Grow Time: 30 mins']
		super().__init__(pic,'SEED','Blue Seed',2,descrList,'COMMON')

class PinkSeed(Item):
# High risk / high reward seed
	def __init__(self):
		pic = graphic.Graphic('PinkSeed','PinkSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.PinkPlant(45,[1,2,3,10,15][random.randint(0,4)])
		descrList = ['Girly girl-ee pink', 'Harvest: $1-15','Grow Time: 45 mins']
		super().__init__(pic,'SEED','Pink Seed',3,descrList,'COMMON')

class YellowSeed(Item):
# Returns only 1 coin, but 1% chance to produce a gold seed
	def __init__(self):
		pic = graphic.Graphic('YellowSeed','YellowSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.YellowPlant(60,random.randint(1,2))
		descrList = ['eh pee colored seed', 'Harvest: $1-2','Grow Time: 60 mins']
		super().__init__(pic,'SEED','Yellow Seed',1,descrList,'COMMON')

class GoldSeed(Item):
# Sells for 100 coins, 50% chance to be planted for 1000 coins or 1 yellowseed
	def __init__(self):
		pic = graphic.Graphic('GoldSeed','GoldSeed.png',(0,0),True,'ITEM')
		self.plant = plantie = plant.GoldPlant(60,[1,100][random.randint(0,1)])
		descrList = ['This seed is gorgeous...', 'Rarity: Legendary', 'Harvest: ???','Harvest Time: 60 mins']
		super().__init__(pic,'SEED','Gold Seed',100,descrList,'LEGENDARY')

# class BondSeed(Item):
# # Produces 0 return but then +2 for each seed it is next to
# 	def __init__(self):
# 		pic = graphic.Graphic('GoldSeed','GoldSeed.png',(0,0),True,'ITEM')
# 		# -> self.plant = plantie = plant.PinkPlant(45,[1,1,1,10,15][random.randint(0,4)])
# 		descrList = ['ItemType: Seed','This seed is gorgeous...', 'Rarity: Legendary', 'Harvest: ???','Harvest Time: 60 mins']
# 		super().__init__(pic,'SEED','Pink Seed',3,descrList,'COMMON')

# class TimeSeed(Item):
# Produces 0 from 45 to 60 minutes, otherwise time//10
# 	def __init__(self):
# 		pic = graphic.Graphic('GoldSeed','GoldSeed.png',(0,0),True,'ITEM')
# 		# -> self.plant = plantie = plant.PinkPlant(45,[1,1,1,10,15][random.randint(0,4)])
# 		descrList = ['ItemType: Seed','This seed is gorgeous...', 'Rarity: Legendary', 'Harvest: ???','Harvest Time: 60 mins']
# 		super().__init__(pic,'SEED','Pink Seed',3,descrList,'COMMON')

# class DeathSeed(Item):
# kills seeds around it and has a chance of multiplying their output by 3
# 	def __init__(self):
# 		pic = graphic.Graphic('GoldSeed','GoldSeed.png',(0,0),True,'ITEM')
# 		# -> self.plant = plantie = plant.PinkPlant(45,[1,1,1,10,15][random.randint(0,4)])
# 		descrList = ['ItemType: Seed','This seed is gorgeous...', 'Rarity: Legendary', 'Harvest: ???','Harvest Time: 60 mins']
# 		super().__init__(pic,'SEED','Pink Seed',3,descrList,'COMMON')