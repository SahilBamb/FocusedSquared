import random
import graphic
import item

from item import Item

class Powerup(Item):
    def __init__(self,pic=None,name='NAPowerup',cost=20,descrList=[''],):
        self.name = name
        super().__init__(pic,'Powerup',name,cost,descrList)

class TileExpand(Powerup):
    def __init__(self):
        descrList = ['A mystical item','Randomly expand grid', 'Rarities: Very rare']
        pic = graphic.Graphic('TileExpand','TileExpand.png',(0,0),True,'ITEM')
        super().__init__(pic,'Tile Expand', 20, descrList)