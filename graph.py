import pygame

class Graph:

    def __init__(self,pic,coord):
        self.setBoundaries(self,pic,coord)
        self.picPath = pic

    def setBoundaries(self,picPath,coord):
        self.picPath = picPath
        self.coord = coord
        self.x = x = coord[0]
        self.y = y = coord[1]
        try:
            surface = pygame.image.load(picPath)
            width = surface.get_width()
            height = surface.get_height()
        except:
            width = 0
            height = 0
        topLeft = coord
        topRight = (x+width,y)
        botLeft = (x,y+height)
        botRight = (x+width,y+height)
        self.rightMost = x+width
        self.bottomMost = y+height
        return (topLeft,topRight,botLeft,botRight)