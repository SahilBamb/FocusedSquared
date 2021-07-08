import random
import graphic
import item
import powerup

from item import Item

class Booster(Item):
    def __init__(self,pic=None,name='NABooster',cost=1,descrList=[''],posItems=[],numItems=0):
        self.name = name
        self.posItems = posItems
        self.numItems = numItems
        super().__init__(pic,'BOOSTER',name,cost,descrList)

    def open(self):
        return [self.posItems[random.randint(0,len(self.posItems)-1)]]


class BasicBooster(Booster):
    def __init__(self):
        descrList = ['A basic booster pack','Includes: 1-2 Cards', 'Rarities: Commons']
        posItems = [item.BasicSeed(), item.BlueSeed(), item.PinkSeed(), item.YellowSeed(), item.GoldSeed(),powerup.TileExpand()]
        posItems = [self.setLoot()]
        numItems = random.randint(1,2)
        pic = graphic.Graphic('BasicPack','BasicPack.png',(0,0),True,'ITEM')
        super().__init__(pic,'Basic Booster', 10, descrList,posItems,numItems)


    def setLoot(self):
        rng = random.randint(1,100)
        if 1<=rng<=50: i = item.BasicSeed()
        elif 51 <= rng <= 70: i = item.BlueSeed()
        elif 71 <= rng <= 80: i = item.YellowSeed()
        elif 81 <= rng <= 90: i = item.PinkSeed()
        elif 91 <= rng <= 99: i = powerup.TileExpand()
        elif 100 <= rng <= 100: i = item.GoldSeed()
        else:
            print(f'rng is out of range {rng}')
            i = item.BasicSeed()
        return i


class GuacBooster(Booster):
    def __init__(self):
        descrList = ['ooh extra guac pack','Includes: 1-2 Cards', 'Rarities: Rares']
        posItems = [powerup.TileExpand()]
        numItems = random.randint(1,2)
        pic = graphic.Graphic('GuacBooster','GuacPack.png',(0,0),True,'ITEM')
        super().__init__(pic,'Basic Booster', 50, descrList,posItems,numItems)


    def setLoot(self):
        pass

