import random
import graphic
import item

from item import Item

class Tilexpand(Item):
    def __init__(self,pic=None,name='NABooster',cost=1,descrList=[''],posItems=[],numItems=0):
        self.name = name
        self.name = name
        self.posItems = posItems
        self.numItems = numItems
        super().__init__(pic,'BOOSTER',name,cost,descrList)

