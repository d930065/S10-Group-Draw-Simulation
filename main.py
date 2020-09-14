import itertools

class team():
    def __init__(self, name, region):
        self.name = name
        self.region = region
        
TES, JDG, SN, LGD = team("TES","CN"), team("JDG","CN"), team("SN ","CN"), team("LGD","CN")
G2, FNC, RGE, MAD = team("G2 ","EU"), team("FNC","EU"), team("RGE","EU"), team("MAD","EU")
DWG, DRX, GEN = team("DWG","KR"), team("DRX","KR"), team("GEN","KR")
TSM, FLY, TL = team("TSM","NA"), team("FLY","NA"), team("TL ","NA")
MCX, PSG = team("MCX","PCS"), team("PSG","PCS")

def search_pool2(pool, a, error):
    if error == 1:
        temp[last[a]-1]=0       
    for i in range(last[a] if error == 1 else 0,4):
        if temp[i] == 0 and groups[i][0].region != pool[a].region:
            temp[i] = pool[a]
            last[a] = i+1
            if a < 3:
                search_pool2(pool, a+1, 0)
            return
    search_pool2(pool, a-1, 1)
    
def search_pool3(pool, a, error):
    if error == 1:
        temp[last[a]-1]=0       
    for i in range(last[a] if error == 1 else 0,4):
        if temp[i] == 0 and groups[i][0].region != pool[a].region and groups[i][1].region != pool[a].region:
            temp[i] = pool[a]
            last[a] = i+1
            if a < 3:
                search_pool3(pool, a+1, 0)
            return
    search_pool3(pool, a-1, 1)   
    
def search_pool4(pool, a, error):
    if error == 1:
        temp[last[a]-1]=0       
    for i in range(last[a] if error == 1 else 0,4):
        if temp[i] == 0 and groups[i][0].region != pool[a].region and groups[i][1].region != pool[a].region and groups[i][2].region != pool[a].region:
            temp[i] = pool[a]
            last[a] = i+1
            if a < 3:
                search_pool4(pool, a+1, 0)
            return
    search_pool4(pool, a-1, 1)
    
count = 0

pool_1_iter = list(itertools.permutations([TES,DWG,G2,TSM]))
pool_2_iter = list(itertools.permutations([FNC,JDG,SN,DRX]))
pool_3_iter = list(itertools.permutations([GEN,RGE,FLY,MCX]))
pool_4_iter = list(itertools.permutations([LGD,MAD,TL,PSG]))   
     
for i in pool_1_iter:
    for j in pool_2_iter:
        for k in pool_3_iter:
            for l in pool_4_iter:
                
                pool_1 = list(i)        
                pool_2 = list(j)
                pool_3 = list(k)
                pool_4 = list(l)
                pools = [pool_1,pool_2,pool_3,pool_4]
                
                group_A = [pool_1.pop(0)]
                group_B = [pool_1.pop(0)]
                group_C = [pool_1.pop(0)]
                group_D = [pool_1.pop(0)]
                groups = [group_A,group_B,group_C,group_D]
                
                temp = [0]*4
                last = [0]*4
                search_pool2(pool_2,0,0)
                for _ in groups:
                    _.append(temp.pop(0))
                    
                temp = [0]*4
                last = [0]*4
                start = 0
                for _ in range(4):
                    if groups[_][0] == TSM  and groups[_][1] == DRX:
                        pool_3.remove(RGE)
                        pool_3.insert(0,RGE)
                        temp[_] = RGE
                        last[0] = _
                        start = 1
                search_pool3(pool_3,start,0)
                for _ in groups:
                    _.append(temp.pop(0))
                
                temp = [0]*4
                last = [0]*4
                search_pool4(pool_4,0,0)
                for _ in groups:
                    _.append(temp.pop(0))
                    
                for _ in range(4):
                    if groups[_][0] == TES:
                        if groups[_][1] == FNC:
                            count+=1
print(count)
