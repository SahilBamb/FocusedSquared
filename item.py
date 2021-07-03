import graphic
import plant

class Item:

	def __init__(self, pic=None, planite=None, toI = 'NA', itemType='NA',itemName='NA'):
		self.pic = pic
		self.plant = planite
		self.toI = toI
		self.itemType = itemType
		self.name = itemName
		self.descrList = [x[:20] for x in [f'ItemType: {itemType}','A lil\' ol\' seed', 'Rarity: Common', 'Harvest: $1-5','Harvest Time: 30']]
'''
class BasicSeed(Item):
	pic = graphic.Graphic('ITEMSeedInv.png',(20+(51*x),432),True,'ITEM')
	super().__init__('ITEMSeedInv.png')
'''