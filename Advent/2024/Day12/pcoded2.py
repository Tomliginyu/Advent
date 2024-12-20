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
                
def cleanUpEdgeSets(edgeSet):
    global crops,mapS,regions
    for key in edgeSet.keys():
        if len(edgeSet[key]) > 1:
            #checkifregionsareadjacvent
            for i in range(0,len(edgeSet[key])):
                tmp = list(range(0,len(edgeSet[key])))
                tmp.remove(i)
                for oth in tmp:
                    for node in edgeSet[key][oth]:
                        if isAdjacentNode(node,edgeSet[key][i]):
                            edgeSet[key][i].extend(edgeSet[key][oth])
                            edgeSet[key][oth] = []
                            break
                
                
    for key in edgeSet.keys():
        tmp = edgeSet[key].copy()
        for t in tmp:
            if len(t) == 0:
                edgeSet[key].remove(t)
                
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
            tmp = calcSides(reg.plots,reg.symbol+str(reg.design))
            print(reg.symbol+str(reg.design),calcArea(reg.plots),tmp)
            sum += calcArea(reg.plots) * tmp
            
    print("Cost:",sum)
            
def calcArea(rpt):
    # print("RPT",rpt)
    return len(rpt)
    
def calcSides(reg,debug):
    global mapS, usedSet
    sides = 0
    edges = {"^":[],"<":[],">":[],"v":[]}
    for spot in reg:
        shp = mapS[spot]
        chkS = 0
        abs = 0 
        tmpE = (spot[0] + MOVE[0][0], spot[1] + MOVE[0][1])
        tmpN = (spot[0] + MOVE[3][0], spot[1] + MOVE[3][1])
        tmpS = (spot[0] + MOVE[2][0], spot[1] + MOVE[2][1])
        tmpW = (spot[0] + MOVE[1][0], spot[1] + MOVE[1][1])
        #Check Edges
        if isEdge(tmpW,shp):
            edges['<'].append(spot)
        if isEdge(tmpE,shp):
            edges['>'].append(spot)
        if isEdge(tmpN,shp):
            edges['^'].append(spot)
        if isEdge(tmpS,shp):
            edges['v'].append(spot)
    
    edgeSet = {}
    for keys in edges.keys():
        edgeSet[keys] = []
        for spot in edges[keys]:
            status = False
            for edg in edgeSet[keys]:
                if len(edg) == 0:
                    edgeSet[keys].append(spot)
                    status = True
                    break
                if isAdjacentNode(spot,edg):
                    edg.append(spot)
                    status = True
                    break
            if status:
                continue
            
            edgeSet[keys].append([spot])
    
    # if "V8" in debug or "E8" in debug:
        # print(edgeSet)
    
    for i in range(0,5):
        cleanUpEdgeSets(edgeSet)
    
    # if "V8" in debug or "E8" in debug:
        # print(edgeSet)
    
    # for key in edgeSet.keys():
        # for arr in edgeSet[key]:
            # for item in arr:
                # tmp = (item,key)
                # if tmp in usedSet:
                    # print("Double Booked",tmp,chk)
                # else:
                    # usedSet.add(tmp)
    
    for key in edgeSet.keys():
        sides += len(edgeSet[key])
    return sides
                
def isEdge(node,shp):
    global mapS
    if not isValid(node):
        return True
    if mapS[node] != shp:
        return True
    return False
            
def isValid(node):
    global length
    if (node[0] == -1 or node[0] == length) or (node[1] == -1 or node[1] == length):
        return False
    return True
    
def isInterior(node):
    global length, mapS
    chk = mapS[node]
    chkS = 0
    for i in range(0,4):
            tmp = (node[0] + MOVE[i][0], node[1] + MOVE[i][1])
            if not isValid(tmp):
                continue
            if chk == mapS[tmp]:# or tmp in nodes:
                chkS += 1
    if chkS == 4:
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
            print(str(i).rjust(3, '0'),end=" ")
        print()
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
    global mapS,crops,length,regions,usedSet
    content = []
    regions = {}
    crops = {}
    usedSet = set()
    #Read File
    with open("data2.txt", "r") as file:
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

    # removeInteriors()
    updateMap()
    # printArray(mapS,length,True)
    #
    
    # printRegions()
    
    calcCost()
    # print(usedSet)

    
    #1487204 too low
    # 1487382 too low