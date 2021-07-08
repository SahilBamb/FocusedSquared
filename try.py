#with open('allPlants.txt') as fin, open('output.txt', 'a') as fout:
#    for line in fin:
#       print(line, end='', file=fout)
import random

def importPlant(name):
    with open('allPlants.txt') as fin:
        for line in fin:
            allAtrib = line.split()
            if '#' in line: continue
            if name!=allAtrib[3]: continue 
            harvest = random.randint(0, int(allAtrib[0].strip('r'))) if 'r' in allAtrib[0] else allAtrib[0]
            TimeToHarvest = allAtrib[1]
            name = allAtrib[3]
            Stages = int(allAtrib[2])
            Stages = [f'{name}{x}.png' for x in range(Stages)]

            print(f'Name: {name}')
            print(f'Stages: {Stages}')
            print(f'stage:{0}')
            print(f'TimeToHarvest:{TimeToHarvest}')
            print(f'harvest:{harvest}')


a = [[1,2],[2,3],[4,5]]

for x,y in a:
    print(f'x is {x} y is {y}')

random.shuffle(a)
print(a)