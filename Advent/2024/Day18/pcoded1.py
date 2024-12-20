#--- Day 19: Linen Layout ---
import sys
import re

sys.setrecursionlimit(20000)  # Increase recursion limit

class MOVES:
    UP = (-1,0)
    DOWN = (1,0)
    LEFT = (0,-1)
    RIGHT = (0,1)
MOVE = [MOVES.UP,MOVES.DOWN,MOVES.LEFT,MOVES.RIGHT]
TALL = 71
WIDE = 71
START = (0,0)
END = (TALL-1,WIDE-1)

class TreeNode:
    def __init__(self, loc, score=1e7):
        self.location = loc
        self.score = score
        self.dir = "X"
        self.parent = None

    def attach(self, child):
        #direction
        self.score = child.score + 1
        self.parent = child
        
    
    def info(self):
        if self.parent is not None:
            print(self.location,self.score,self.parent.location)
        else:
            print(self.location,self.score,"ROOT")

    def copy(self):
        tmp = TreeNode(self.location)
        tmp.score = self.score
        tmp.parent = self.parent
        return tmp
        
def add(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def diff(t1,t2):
    return (t1[0]-t2[0],t1[1]-t2[1])
    
def diffS(t1):
    return max(t1[0],t1[1])
    
def prioSort(arr):
    global START
    sarr = sorted(arr, key=diffS)
    # print(sarr)
    # sarr.reverse()
    return sarr
    
def isAdjecent(n1):
    global mapS
    arr = []
    for m in MOVE:
        tmp = add(n1,m)
        if mapS[tmp] != '#':
            arr.append(tmp)
    if len(arr) > 0:
        return prioSort(arr)
    return []

def djikS(node):
    global mapS,djik,adjS,low,paths,low
    if node != END and not node == START:
        printPath((djik[node])[0],{},True)
        input()
        # print(low,end=" ")(djik[node])[0].info()
    if node == START:
        tmp = TreeNode(START)
        tmp.attach(djik[node][0])
        paths.append(tmp)
        # printPath((djik[node])[0],{},True)
        print("Found Path",tmp.score)
        input()
        low = min(low,tmp.score)
        # printPath(tmp,{},True)
        # tmp.info()
        return
    if (djik[node])[0].score > low:
        return False
    adj = adjS[node]
    adjC = adj.copy()
    if node != END and (djik[node])[0].parent.location in adj:
        adjC.remove((djik[node])[0].parent.location)
    #buildout
    for a in adjC:
        status = "False"
        tmp = TreeNode(a)
        tmp.attach((djik[node])[0])
        if a in djik.keys():
            tmp1 = djik[a]
            tarr = list()
            for t in tmp1:
                # print("New Route:")
                # t.info()
                if t.score < tmp.score:
                    # print(node,a,adjC,t.score,tmp.score)
                    status = "Return"
                    return False
                if t.score > tmp.score:
                    # print("Dive This",node,a,adjC,t.score,tmp.score)
                    tarr.append(tmp)
                    djik[a] = tarr
                    status = "Eval"
                    break
                if t.score == tmp.score:
                    djik[a].append(tmp)
                    status = "Return"
                    break
            if status == "Return":
                continue
            if status == "Eval":
                st = djikS(a)                  
        else:
            tarr = list()
            tarr.append(tmp)
            djik[a] = tarr
            st = djikS(a)
            if not st:
                del djik[a]
    
    
def printArray(rpt,icons,debug):
    global mapS
    if debug:
        for i in range(-1,TALL+1):
            for j in range(-1,WIDE+1):
                print(mapS[(i,j)],end="")
            print()
        print()

def setArray(n):
    global bestA
    tn = n.copy()
    while tn.parent is not None:
        bestA.add(tn.location)
        tn = tn.parent
        
def printPath(rpt,icons,debug):
    global mapS
    tarr = []
    tn = rpt.copy()
    tl = rpt.location
    while tn.parent is not None:
        tarr.append(tn.location)
        tn = tn.parent
    if debug:
        for i in range(-1,TALL+1):
            for j in range(-1,WIDE+1):
                if (i,j) == tl:
                    print('O',end="")
                    continue
                if (i,j) in tarr:
                    print('X',end="")
                    continue
                print(mapS[(i,j)],end="")
            print()
        print()
        
def printSet(rpt,icons,debug):
    global mapS
    tn = rpt.copy()
    if debug:
        for i in range(0,TALL):
            for j in range(0,WIDE):
                if (i,j) in rpt:
                    print('O',end=" ")
                    continue
                print(mapS[(i,j)],end=" ")
            print()
        print()

def cleanUpMap():
    global mapS
    sum = 0
    for cord in mapS.keys():
        if cord[0] == -1 or cord[0] == TALL or cord[1] == -1 or cord[1] == WIDE:
            continue
        if mapS[cord] == 'S' or mapS[cord] == 'E':
            continue
        possMoves = []
        tmp = cord
        for dir in MOVE:
            tmp = add(cord,dir)
            if mapS[tmp] == '#':
                possMoves.append(tmp)
        if len(possMoves) > 2:
            mapS[cord] = '#'
            sum += 1
            
    return sum
    
if __name__ == "__main__":
    #Setup Arrays/Values
    global mapS,djik,adjS,paths,bestA,low
    low = 300
    TIME = 1024
    content = ""
    paths = []
    # sum = 0
    map = []
    man = []
    mapS = {}
    djik = {}
    adjS = {}
    bestA = set()
    corr = set()
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            map.append(line.replace('\n',""))
            
    with open("data11.txt", "r") as file:
        for line in file:
            man.append(line.replace('\n',""))
    
    counter = 1
    for item in map:
        tmp = item.split(',')
        corr.add((int(tmp[1]),int(tmp[0])))
        if counter == TIME:
            break
        counter += 1
        
    for item in man:
        tmp = item.split(',')
        corr.add((int(tmp[1]),int(tmp[0])))
        
    verts = set()
    for i in range(0,TALL):
        for j in range(0,WIDE):
            if j == 0:
                mapS[(i,j-1)] = '#'
            if j == WIDE-1:
                mapS[(i,WIDE)] = '#'
            if (i,j) in corr:
                mapS[(i,j)] = '#'
                continue
            if (i,j) == START:
                mapS[(i,j)] = 'S'
                continue
            if (i,j) == END:
                mapS[(i,j)] = 'E'
                continue
            mapS[(i,j)] = '.'
            
    for i in range(-1,0):
        for j in range(-1,WIDE+1):
            mapS[(i,j)] = '#'
            mapS[(TALL,j)] = '#'
            
    printArray([],{},True)
    root = TreeNode(END,0)
    tarr = list()
    tarr.append(root)
    djik[END] = tarr
    # printArray(mapS,{},True)
    # input()
    for i in range(0,100):
        cleanUpMap()
    for key in mapS.keys():
        if mapS[key] != '#':
            verts.add(key)
    for v in verts:
        adjS[v] = isAdjecent(v)
    # printArray(mapS,{},True)
    input()
    djikS(END)
    print("Winning:")
    for e in paths:
        low = min(low,e.score)
    for e in paths:
        if e.score == low:
            setArray(e)
            print(e.score-1)
            printPath(e,{},True)
            
    #290 Too High

