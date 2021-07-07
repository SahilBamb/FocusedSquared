import random
import graphic
import item

from item import Item

class Booster(Item):
    def __init__(self,pic=None,name='NABooster',cost=1,descrList=[''],posItems=[],numItems=0):
        self.name = name
        self.name = name
        self.posItems = posItems
        self.numItems = numItems
        super().__init__(pic,'BOOSTER',name,cost,descrList)

    def open(self):
        #return [self.posItems[0]]
        return [self.posItems[random.randint(0,len(self.posItems)-1)]]


class BasicBooster(Booster):
    def __init__(self):
        descrList = ['A basic booster pack','Includes: 1-2 Cards', 'Rarities: Commons']
        posItems = [item.BasicSeed(), item.BlueSeed(), item.PinkSeed()]
        numItems = random.randint(1,2)
        pic = graphic.Graphic('BasicPack','BasicPack.png',(0,0),True,'ITEM')
        super().__init__(pic,'Basic Booster', 3, descrList,posItems,numItems)





