#--- Day 8: Resonant Collinearity ---
import sys
import re

def calcRadio(rpt,radios,length):
    #something
    #need
    locations = {}
    antiNodeLoc = {}
    for key,value in rpt.items():
        if value in radios:
            if value in locations.keys():
                locations[value].append(key)
            else:
                locations[value] = [key]
                
    
    # needAntis
    for key in locations.keys():
        for loc in locations[key]:
            tmp = locations[key].copy()
            tmp.remove(loc)
            for other in tmp:
                tmpV = (loc[0]-(loc[0] - other[0])*2,loc[1]-(loc[1] - other[1])*2)               
                if (tmpV[0] >= 0 and tmpV[1] >= 0) and (tmpV[0] < length and tmpV[1] < length):
                    if key in antiNodeLoc.keys():
                        antiNodeLoc[key] += [tmpV]
                    else:
                        antiNodeLoc[key] = [tmpV]
                    
    print(antiNodeLoc)
    alterMap(rpt,antiNodeLoc,'#')
    
    printArray(rpt,length,True)
    matches = [i for i, x in enumerate(rpt.values()) if '#' in x ]
    print(len(matches))
           
def alterMap(rpt,points,symbol):
    for key in points.keys():
        for val in points[key]:
            # print(val)
            current = rpt[val]
            if current == '.':
                rpt[val] = symbol+key
            else:
                rpt[val] += symbol+key     
    
def printArray(rpt,length,debug):
    if debug:
        for i in range(0,length):
            for j in range(0,length):
                print(rpt[(i,j)],end=" ")
            print()
        # input()
        print() 
    
if __name__ == "__main__":
    #Setup Arrays/Values
    content = []
    symbols = set()
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            content += (line.replace('\n',""))
    
    length = int(len(content) ** 0.5)
    mapS = {}
    for i in range(0,length):
        for j in range(0,length):
            mapS[(i,j)] = content[i*length + j]
    
    for key in mapS.keys():
        symbols.add(mapS[key])
    symbols.remove('.')
    
    # printArray(mapS,length,True)
    calcRadio(mapS,symbols,length)
    
    #240 too high
    #228
    