#--- Day 12: Garden Groups ---
import sys

MOVE = [(0,1),(0,-1),(1,0),(-1,0)]

class RegionLock:
    def __init__(self, symbol, num):
        self.symbol = symbol
        self.design = num
        self.plots = []

    def add_plot(self, plot):
        self.plots.append(plot)

def calcRegions():
    global crops,mapS,regions
    for key in crops.keys():
        #Make New Region
        region = 0
        reg = RegionLock(key,region)
        regions[key] = [reg]
        for spot in crops[key]:
            #Pick Region
            if len(reg.plots) == 0:
                reg.add_plot(spot)
                continue
            #Add check if multiple regions
            for i in range(0,len(regions[key])):
                status = False
                if isAdjacentNode(spot,regions[key][i].plots):
                    regions[key][i].add_plot(spot)
                    status = True
                    break
            if status:
                continue
            #It's not adjacent
            region += 1
            reg = RegionLock(key,region)
            reg.add_plot(spot)
            regions[key].append(reg)

def cleanUpRegions():
    global crops,mapS,regions
    for key in regions.keys():
        reg = regions[key]
        if len(reg)> 1:
            #checkifregionsareadjacvent
            for i in range(0,len(reg)):
                tmp = list(range(0,len(reg)))
                tmp.remove(i)
                for oth in tmp:
                    for node in reg[oth].plots:
                        if isAdjacentNode(node,reg[i].plots):
                            for y in reg[oth].plots:
                                reg[i].add_plot(y)
                            index = oth
                            reg[index].design = 'X'
                            reg[index].plots = []
                            break
                
                
    for key in regions.keys():
        tmp = regions[key].copy()
        for t in tmp:
            if t.design == 'X':
                regions[key].remove(t)
                
def updateMap():
    global regions,mapS
    for key in regions.keys():
        region = regions[key]
        for reg in region:
            for spot in reg.plots:
                mapS[spot] = reg.symbol + str(reg.design).rjust(2, '0')
                
                

def calcCost():
    global regions
    sum = 0
    for key in regions.keys():
        for reg in regions[key]:
            sum += calcArea(reg.plots) * calcPer(reg.plots)
            
    print("Cost:",sum)
            
def calcArea(rpt):
    # print("RPT",rpt)
    return len(rpt)
    
def calcPer(reg):
    global mapS
    perm = 0
    for spot in reg:
        for i in range(0,4):
            tmp = (spot[0] + MOVE[i][0], spot[1] + MOVE[i][1])
            if not isValid(tmp):
                perm += 1
                continue
            if mapS[spot] != mapS[tmp]:
                perm += 1
                continue
    return perm
            
def isValid(node):
    global length
    if (node[0] == -1 or node[0] == length) or (node[1] == -1 or node[1] == length):
        return False
    return True
    
def isAdjacent(node, nodes):
    global length, mapS
    chk = mapS[node]
    for i in range(0,4):
            tmp = (node[0] + MOVE[i][0], node[1] + MOVE[i][1])
            if not isValid(tmp):
                continue
            if chk == mapS[tmp]:# or tmp in nodes:
                return True
    return False
    
def isAdjacentNode(node, nodes):
    global length, mapS
    chk = mapS[node]
    for i in range(0,4):
            tmp = (node[0] + MOVE[i][0], node[1] + MOVE[i][1])
            if not isValid(tmp):
                continue
            if tmp in nodes:# or tmp in nodes:
                return True
    return False
    
def printArray(rpt,length,debug):
    if debug:
        for i in range(0,length):
            for j in range(0,length):
                print(rpt[(i,j)],end=" ")
            print()
        # input()
        print()

def printRegions():
    global regions
    for key in regions.keys():
        for reg in regions[key]:
            print(reg.symbol,"Region:",reg.design,"Plots:",len(reg.plots),reg.plots)        

if __name__ == "__main__":
    #Setup Arrays/Values
    global mapS,crops,length,regions
    content = []
    regions = {}
    crops = {}
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            content += (line.replace('\n',""))
    
    sum = 0
    length = int(len(content) ** 0.5)
    mapS = {}
    sP = set()
    for i in range(0,length):
        for j in range(0,length):
            mapS[(i,j)] = content[i*length + j]
            if content[i*length + j] in crops.keys():
                crops[str(content[i*length + j])].append((i,j))
            else:
                crops[str(content[i*length + j])] = [(i,j)]
            

    # printArray(mapS,length,True)
    calcRegions()
    cleanUpRegions()
    cleanUpRegions()
    cleanUpRegions()

    updateMap()
    # printArray(mapS,length,True)
    printRegions()
    
    calcCost()
    
    #1487204 too low
    # 1487382 too low
    #1494342