import random

def shuffleString(Word,jumlah):
     BuatList = []
     i = 0
     while i<jumlah:
        RandomAcak =[''.join(random.sample(Word,len(Word)))]
        if(RandomAcak  not in BuatList):
            BuatList += RandomAcak
            i+=1
     print(BuatList)


shuffleString('aku',2)
shuffleString('aku',3)
shuffleString('aku',4)