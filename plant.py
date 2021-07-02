from graphic import Graphic
import random
class Plant(Graphic):

	def __init__(self,picPath=None,variety='BasicPlant',stage=0,TimeToHarvest=5):
		self.TimeToHarvest = TimeToHarvest
		self.harvest = random.randint(1,10)
		self.ReadytoHarvest = False
		self.Stages = 'BasicPlant0', 'BasicPlant1', 'BasicPlant2', 'BasicPlant3', 'BasicPlant4'
		self.timeBetweenStages = TimeToHarvest // len(self.Stages)
		self.stage = stage
		self.variety = variety
		picPath = f'{variety}{stage}.png'
		super().__init__(picPath,(0,0))


	def grow(self,time=0):
		if self.stage==len(self.Stages)-1:
			self.ReadytoHarvest = True
			return True
		self.timeBetweenStages -= time
		if self.timeBetweenStages<=0:
			self.timeBetweenStages = self.TimeToHarvest // len(self.Stages)
			self.stage = min(self.stage+1,4)
			self.picPath = f'{self.variety}{self.stage}.png'

