#--- Day 14: Restroom Redoubt ---
import sys
import math
import re

WIDE = 101
TALL = 103
TIME = 0

def calcLocation():
    #FindLocationAtTime
    global pos,vec
    posT = {}
    for key in pos.keys():
        loc = pos[key]
        vel = vec[str(key[1])]
        velt = tuple([TIME*x for x in vel])
        loct = (loc[0]+velt[1],loc[1]+velt[0])
        x1,x2 = divmod(loct[0],TALL)
        y1,y2 = divmod(loct[1],WIDE)
        loct = (x2,y2)
        posT[(TIME,key[1])] = loct
        
    return posT
    #0p=04,2 v=2,-3
    #1p=01,4
    #2p=-2,6 = 5,6
    #3p=-5,8 = 2,8
    #4p=-8,10 = 6,10
    #5p=-11,12 = 3,1
    
def calcSafety(pos):
    #Quads 1,2,3,4
    #Q1, 0,5 and 0,3
    q1=q2=q3=q4=0
    for key in pos.keys():
        #Heights 0,7/2, 7/2+1, 
        x,y = pos[key]
        #Q1
        if x<int(TALL/2) and y<int(WIDE/2):
            q1 += 1
            continue
        #Q3
        if x>int(TALL/2) and y<int(WIDE/2):
            q3 += 1
            continue
        #Q2
        if x<int(TALL/2) and y>int(WIDE/2):
            q2 += 1
            continue
        #Q4
        if x>int(TALL/2) and y>int(WIDE/2):
            q4 += 1
            continue
            
    return q1,q2,q3,q4,q1*q2*q3*q4
    
    
def printArray(rpt,icons,debug):
    if debug:
        for i in range(0,TALL):
            for j in range(0,WIDE):
                # if i == int(TALL/2):
                    # print("|",end=" ")
                    # continue
                # if j == int(WIDE/2):
                    # print("_",end=" ")
                    # continue
                if (i,j) in icons.values():
                    print("X",end=" ")
                else:
                    print(" ",end=" ")
            print()
        # input()
        print()      

if __name__ == "__main__":
    #Setup Arrays/Values
    global pos,vec,posT
    content = ""
    mapS = {}
    pos = {}
    vec = {}
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            for char in line:
                content += char
    
    vals = re.findall('(\d+,\d+) v=(-?\d+,-?\d+)',content)
    counter = 0
    # print(vals)
    for v in vals:
        tmp1 = v[0].split(',')
        tmp2 = v[1].split(',')
        pos[(0,counter)] = (int(tmp1[1]),(int(tmp1[0])))
        vec[str(counter)] = (int(tmp2[0]),int(tmp2[1]))
        counter += 1
    
    # print(vals)
    posT = calcLocation()
    #print(calcSafety(posT))
    
    for i in range(0,TALL):
        for j in range(0,WIDE):
            mapS[(i,j)] = '.'
    
    testSet = set(posT.values())
    print(testSet)
    for i in range(86,100000,101):
        TIME = i
        posT = calcLocation()
        testSet = set(posT.values())
        print(i,len(testSet))
        printArray(mapS,posT,True)
        if len(testSet) == 500:
            input()
        
    # 189655128 too low
    # 211451280 too low
    # 218619120
    # 7055,17458,27861
