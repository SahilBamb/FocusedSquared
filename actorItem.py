import random
import graphic
import item
import actor

from item import Item

class Actoritem(Item):
    def __init__(self,pic=None,name='NAActor',cost=100,descrList=['']):
        super().__init__(pic,'ACTORitem',name,cost,descrList,'Secret Rare')


class Mixie(Actoritem):
    def __init__(self):
        descrList = ['A silly girl','Good for nothing', 'Origin: Icelandia']
        pic = graphic.Graphic('Mixie Item','MixieTN.png',(0,0),True,'ITEM')
        super().__init__(pic,'Mixie Item', 100, descrList)

    def getActInstance(self,x,y):
        return actor.Actor(x,y,'mixie',self,6)

class Skunk(Actoritem):
    def __init__(self):
        descrList = ['A stinky skunk','Cute little thing', 'Origin: Bushlandia']
        pic = graphic.Graphic('Skunk Item','SkunkTN.png',(0,0),True,'ITEM')
        super().__init__(pic,'Skunk Item', 100, descrList)

    def getActInstance(self,x,y):
        return actor.Actor(x,y,'skunk',self,3)

class PurpleDragon(Actoritem):
    def __init__(self):
        descrList = ['Smol Purple Dragon','Barney-esque', 'Origin: Far Nest']
        pic = graphic.Graphic('PurpleDragon Item','PurpleDragonTN.png',(0,0),True,'ITEM')
        super().__init__(pic,'PurpleDragon Item', 1000, descrList)

    def getActInstance(self,x,y):
        return actor.Actor(x,y,'PurpleDragon',self,5)

class BabyBlueDragon(Actoritem):
    def __init__(self):
        descrList = ['A babyblue dragon','A magical glint', 'Origin: Far Nest']
        pic = graphic.Graphic('BabyBlueDragon Item','BabyBlueDragonTN.png',(0,0),True,'ITEM')
        super().__init__(pic,'BabyBlueDragon Item', 1000, descrList)

    def getActInstance(self,x,y):
        return actor.Actor(x,y,'BabyBlueDragon',self,6)

class GreenFox(Actoritem):
    def __init__(self):
        descrList = ['A Magical Fox','Woah what is this', 'Origin: Heaven']
        pic = graphic.Graphic('GreenFox Item','GreenFoxTN.png',(0,0),True,'ITEM')
        super().__init__(pic,'GreenFox Item', 500, descrList)

    def getActInstance(self,x,y):
        return actor.Actor(x,y,'GreenFox',self,20)

class PinkGirl(Actoritem):
    def __init__(self):
        descrList = ['A Pink Girl','Def into costplay', 'Origin: Comi-Con']
        pic = graphic.Graphic('PinkGirl Item','PinkGirlTN.png',(0,0),True,'ITEM')
        super().__init__(pic,'PinkGirl Item', 500, descrList)

    def getActInstance(self,x,y):
        return actor.Actor(x,y,'pinkGirl',self,10)