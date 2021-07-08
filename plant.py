from graphic import Graphic
import random
class Plant(Graphic):

	def __init__(self,name,picPath='BasicPlant0.png',stage=0,TimeToHarvest=5,harvest=1, Stages=[""]):
		self.TimeToHarvest = TimeToHarvest
		self.harvest = harvest
		self.ReadytoHarvest = False
		self.Stages = Stages
		self.timeBetweenStages = TimeToHarvest // len(self.Stages)
		self.stage = stage
		self.name = name
		picPath = picPath
		super().__init__(name,picPath,(0,0))


	def grow(self,time=0):
		if self.stage==len(self.Stages)-1:
			self.ReadytoHarvest = True
			return True
		self.timeBetweenStages -= time
		if self.timeBetweenStages<=0:
			self.timeBetweenStages = self.TimeToHarvest // len(self.Stages)
			self.stage = min(self.stage+1,4)
			self.picPath = self.Stages[self.stage]
			#self.picPath = f'{self.variety}{self.stage}.png'

class BasicPlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'BasicPlant0.png', 'BasicPlant1.png', 'BasicPlant2.png', 'BasicPlant3.png', 'BasicPlant4.png'
		name = 'BasicPlant'
		stage = 0
		super().__init__(name, Stages[stage], stage, TimeToHarvest, harvest, Stages)

class BluePlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'BluePlant0.png', 'BluePlant1.png', 'BluePlant2.png', 'BluePlant3.png', 'BluePlant4.png'
		name = 'BluePlant'
		stage = 0
		super().__init__(name, Stages[stage], stage, TimeToHarvest, harvest, Stages)

class PinkPlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'PinkPlant0.png', 'PinkPlant1.png', 'PinkPlant2.png', 'PinkPlant3.png', 'PinkPlant4.png'
		name = 'PinkPlant'
		stage = 0
		super().__init__(name, Stages[stage], stage, TimeToHarvest, harvest, Stages)

class YellowPlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'YellowPlant0.png', 'YellowPlant1.png', 'YellowPlant2.png', 'YellowPlant3.png', 'YellowPlant4.png'
		name = 'YellowPlant'
		stage = 0
		super().__init__(name, Stages[stage], stage, TimeToHarvest, harvest, Stages)

class GoldPlant(Plant):

	def __init__(self,TimeToHarvest,harvest):
		Stages = 'GoldPlant0.png', 'GoldPlant1.png', 'GoldPlant2.png', 'GoldPlant3.png', 'GoldPlant4.png'
		name = 'GoldPlant'
		stage = 0
		super().__init__(name, Stages[stage], stage, TimeToHarvest, harvest, Stages)

class importPlant(Plant):

	def __init__(self,name):
		with open('allPlants.txt') as fin:
			for line in fin:
				allAtrib = line.split()
				if '#' in line: continue
				if name != allAtrib[3]: continue
				harvest = random.randint(0, int(allAtrib[0].strip('r'))) if 'r' in allAtrib[0] else allAtrib[0]
				TimeToHarvest = allAtrib[1]
				name = allAtrib[3]
				Stages = int(allAtrib[2])
				Stages = [f'{name}{x}.png' for x in range(Stages)]
				stage = 0
		super().__init__(name, Stages[stage], stage, TimeToHarvest, harvest, Stages)