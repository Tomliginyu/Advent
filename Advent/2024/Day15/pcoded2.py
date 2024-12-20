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
        if mapS[key] == '[':
            score = score + 100 * key[0] + key[1]
            
    print(score)
    
def calcScore2():
    global mapS2
    score = 0
    #SwapCommands
    for key in mapS2.keys():
        if mapS2[key] == '[':
            score = score + 100 * key[0] + key[1]
            
    print(score)                    

    
def fixMap():
    global mapS
    for key in mapS.keys():
        if mapS[key] == '[' and not (mapS[(key[0],key[1]+1)] == ']'):
            mapS[key] = '.'
        if mapS[key] == ']' and not (mapS[(key[0],key[1]-1)] == '['):
            mapS[key] = '.'  
           

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
                
    runCommands(tComm,rpt)
    
def runCommands(rpt,unt):
    global mapS, RB
    index = 0
    for comm in rpt:
        # fixMap()
        if index >= 340 and False:
            tmpS = unt[index]
            tmpI = index
            print(unt[index],index)
            printArray(mapS,{},True)
            input()
        index+=1
        next = add(RB,comm)
        #Wall
        if mapS[next] == '#':
            continue
        #FreeSpace
        if mapS[next] == '.':
            RB = next
            continue
        #CrateH
        if comm == LEFT or comm == RIGHT:
            shiftRow(next,comm)
            continue
        #CrateV
        if comm == UP or comm == DOWN:
            shiftCol(next,comm)
            continue
            
        
        
                        

def shiftCol(n,c):
    global mapS,RB
    working = {}
    working[str(RB[0])] = {}
    working[str(n[0])] = {n}
    if mapS[n] == ']':
        working[str(n[0])].add((n[0],n[1]))
        working[str(n[0])].add((n[0],n[1]-1))
    if mapS[n] == '[':
        working[str(n[0])].add((n[0],n[1]))
        working[str(n[0])].add((n[0],n[1]+1))
    temp = n
    size = len(working[str(temp[0])])
    while True:
        fs = 0
        print(working)
        status = True
        for tup in working[str(temp[0])]:
            if mapS[tup] == '.':
                continue
            tmp = add(tup,c)
            if not str(tmp[0]) in working.keys():
                working[str(tmp[0])] = set()
            if mapS[tmp] == '#':
                working.clear()
                return
            if mapS[tmp] == '.':
                working[str(tmp[0])].add(tmp)
                fs += 1
                continue
            if mapS[tmp] == ']':
                status = False
                working[str(tmp[0])].add((tmp[0],tmp[1]))
                working[str(tmp[0])].add((tmp[0],tmp[1]-1))
                continue
            if mapS[tmp] == '[':
                status = False
                working[str(tmp[0])].add((tmp[0],tmp[1]))
                working[str(tmp[0])].add((tmp[0],tmp[1]+1))
                continue
        #Push    
        if status:
            break
        else:
            temp = add(temp,c)
            size = len(working[str(temp[0])])
            continue
            
    #Redistribute
    keys = list(working.keys())
    keys.reverse()
    keys.pop()
    print(working)
    for key in keys:
        arr = working[key]
        tArr = working[str(int(key)-c[0])]
        for t in arr:
            if (t[0]-c[0],t[1]) in tArr:
                mapS[t] = mapS[(t[0]-c[0],t[1])]
            else:
                mapS[t] = '.'
            
    RB = n

    

def shiftRow(n,c):
    global mapS,RB
    mapS[RB] = '.'
    items = []
    items.append(RB)
    items.append(n)
    temp = add(n,c)
    while True:
        #There's Space
        if mapS[temp] == '.':
            items.append(temp)
            break
        #Blocker
        if mapS[temp] == '#':
            items.clear()
            return
        items.append(temp)
        temp = add(temp,c)
        
    items.reverse()
    for i in items:
        if i != RB:
            mapS[i] = mapS[(i[0],i[1]-c[1])]
        else:
            RB = n
    
        
    
    # printArray(mapS,{},True)
            
            
def printArray(rpt,icons,debug):
    global mapS,mapS2
    if debug:
        for i in range(0,TALL):
            for j in range(0,WIDE*2):
                if (i,j) == RB:
                    print('@',end=" ")
                else:
                    print(mapS[(i,j)],end=" ")
            print()
        print()     

if __name__ == "__main__":
    #Setup Arrays/Values
    global mapS,mapS2
    content = ""
    machines = []
    sum = 0
    map = []
    map2 = []
    mapS = {}
    mapS2 = {}
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            map.append(line.replace('\n',""))
            
    WIDE = len(line)
    # with open("data4.txt", "r") as file:
        # for line in file:
            # map2.append(line.replace('\n',""))
    # print(map2)
    TALL = len(map[0])
    # for i in range(0,TALL):
        # for j in range(0,WIDE*2):
            # mapS2[(i,j)] = map2[i][j]
     
    for i in range(0,TALL):
        scalar = 0
        for j in range(0,WIDE):
            match map[i][j]:
                case '@':
                    mapS[(i,scalar)] = '.'
                    mapS[(i,scalar+1)] = '.'
                    RB = (i,scalar)
                case 'O':
                    mapS[(i,scalar)] = '['
                    mapS[(i,scalar+1)] = ']'
                case '.':
                    mapS[(i,scalar)] = '.'
                    mapS[(i,scalar+1)] = '.'
                case '#':
                    mapS[(i,scalar)] = '#'
                    mapS[(i,scalar+1)] = '#'
            scalar += 2
            
    # printArray(mapS,{},True)
    with open("data22.txt", "r") as file:
        for line in file:
            for char in line:
                content += char
    
    # printArray(mapS,{},True)
    commands = content.replace('\n',"")
    tCommands(commands)
    # fixMap()
    printArray(mapS,{},True)
    calcScore()
    # calcScore2()
    #1473004 TooHigh
    #1478475 toohigh
    #1471049
    
