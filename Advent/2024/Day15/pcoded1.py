#--- Day 15: Warehouse Woes ---
import sys
import re

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
TALL = 0
WIDE = 0
RB = (0,0)

def add(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def calcScore():
    global mapS
    score = 0
    #SwapCommands
    for key in mapS.keys():
        if mapS[key] == 'O':
            score = score + 100 * key[0] + key[1]
            
    print(score)

def tCommands(rpt):
    #SwapCommands
    tComm = []
    for comm in rpt:
        match comm:
            case '^':
                tComm.append(UP)
            case '>':
                tComm.append(RIGHT)
            case '<':
                tComm.append(LEFT)
            case 'v':
                tComm.append(DOWN)
                
    runCommands(tComm)
    
def runCommands(rpt):
    global mapS, RB
    for comm in rpt:
        # print(comm)
        # printArray(mapS,{},True)
        # input()
        next = add(RB,comm)
        #Wall
        if mapS[next] == '#':
            continue
        #FreeSpace
        if mapS[next] == '.':
            RB = next
            continue
        #Crate
        if mapS[next] == 'O':
            toMove = []
            tmp = next
            while True:
                tmp = add(tmp,comm)
                #Push Block, Move Guard
                if mapS[tmp] == '.':
                    toMove.append(tmp)
                    RB = next
                    for b in toMove:
                        mapS[b] = 'O'
                    mapS[next] = '.'
                    break
                #AnotherBlocktoPush
                if mapS[tmp] == 'O':
                    toMove.append(tmp)
                #Wall
                if mapS[tmp] == '#':
                    break
                

            

def printArray(rpt,icons,debug):
    global mapS
    if debug:
        for i in range(0,TALL):
            for j in range(0,WIDE):
                if (i,j) == RB:
                    print('@',end=" ")
                else:
                    print(mapS[(i,j)],end=" ")
            print()
        print()     

if __name__ == "__main__":
    #Setup Arrays/Values
    global mapS
    content = ""
    machines = []
    sum = 0
    map = []
    mapS = {}
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            map.append(line.replace('\n',""))
            
    WIDE = len(line)
    TALL = len(map[0])
    for i in range(0,TALL):
        for j in range(0,WIDE):
            mapS[(i,j)] = map[i][j]
            if map[i][j] == '@':
                RB = (i,j)
                mapS[(i,j)] = '.'
            
    # printArray(mapS,{},True)
    with open("data11.txt", "r") as file:
        for line in file:
            for char in line:
                content += char
    
    commands = content.replace('\n',"")
    tCommands(commands)
    printArray(mapS,{},True)
    calcScore()
    
    
