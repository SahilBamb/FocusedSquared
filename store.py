class Store:

    def __init__(self,storeName, storeImage, storeText1, storeText2, responseOptions1, responseOptions2, responseOptions3, storeInventory):
        self.storeName = storeName
        self.storeImage = storeImage
        self.storeText1 = storeText1
        self.storeText2 = storeText2
        self.responseOptions1 = responseOptions1
        self.responseOptions2 = responseOptions2
        self.responseOptions3 = responseOptions3
        self.storeInventory = storeInventory

class importStore(Store):

    def __init__(self, name):
        self.working = False
        with open('allStores.txt') as fin:
            for line in fin:
                if '#' in line or len(line)<10: continue
                allAtrib = line.split('-')
                storeName = allAtrib[0]
                storeImage = allAtrib[1]
                storeText1 = allAtrib[2]
                storeText2 = allAtrib[3]
                responseOptions1 = allAtrib[4]
                responseOptions2 = allAtrib[5]
                responseOptions3 = allAtrib[6]
                storeInventory = allAtrib[7:]
                if storeName==name:
                    print(f'we got em for {name}')
                    self.working = True
                    break

        try: super().__init__(storeName, storeImage, storeText1, storeText2, responseOptions1, responseOptions2, responseOptions3, storeInventory)
        except: self.working = False
