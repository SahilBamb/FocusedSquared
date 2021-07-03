from graphic import Graphic
import random
class Plant(Graphic):

	def __init__(self,picPath='BasicPlant0.png',variety='NAPlant',stage=0,TimeToHarvest=5,harvest=1, Stages=[""]):
		self.TimeToHarvest = TimeToHarvest
		self.harvest = harvest
		self.ReadytoHarvest = False
		self.Stages = Stages
		self.timeBetweenStages = TimeToHarvest // len(self.Stages)
		self.stage = stage
		self.variety = variety
		picPath = picPath
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

class BasicPlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'BasicPlant0', 'BasicPlant1', 'BasicPlant2', 'BasicPlant3', 'BasicPlant4'
		variety = 'BasicPlant'
		stage = 0
		super().__init__(f'{variety}{stage}.png', variety, stage, TimeToHarvest, harvest, Stages)

class BluePlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'BluePlant0', 'BluePlant1', 'BluePlant2', 'BluePlant3', 'BluePlant4'
		variety = 'BluePlant'
		stage = 0
		super().__init__(f'{variety}{stage}.png', variety, stage, TimeToHarvest, harvest, Stages)

class PinkPlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'PinkPlant0', 'PinkPlant1', 'PinkPlant2', 'PinkPlant3', 'PinkPlant4'
		variety = 'PinkPlant'
		stage = 0
		super().__init__(f'{variety}{stage}.png', variety, stage, TimeToHarvest, harvest, Stages)