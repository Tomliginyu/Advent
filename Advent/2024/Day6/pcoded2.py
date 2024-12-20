#--- Day 6: Guard Gallivant ---
import sys
import re

def guardPat(rpt,length,guardLoc,debug,newObs):
    #something
    if newObs is None:
        newObs = -1
    moveTracker = set()
    visited = set()
    loopCounter = 0
    guard = guardLoc
    guardSym = '^'
    while True:
        moveTracker.add(guard)
        if (guard,guardSym) in visited:
            return _, True
        else:
            visited.add((guard,guardSym))
        match guardSym:
                case '^':
                    if guard < length:
                        return moveTracker, False
                case '>':
                    if (guard + 1) % length == 0:
                        return moveTracker, False
                case '<':
                    if guard % length == 0:
                        return moveTracker, False
                case 'v':
                    if guard > len(rpt) - length:
                        return moveTracker, False
        #is object in front
        match guardSym:
            case '^':
                if rpt[guard - length] == '#':
                    guardSym = '>'
                    rpt[guard] = '+'
                    printArray(rpt, newObs, debug)
                    moveTracker.add(guard)
                    continue
            case '>':
                if rpt[guard + 1] == '#':
                    guardSym = 'v'
                    rpt[guard] = '+'
                    printArray(rpt, newObs, debug)
                    moveTracker.add(guard)
                    continue
            case '<':
                if rpt[guard - 1] == '#':
                    guardSym = '^'
                    rpt[guard] = '+'
                    printArray(rpt, newObs, debug)
                    moveTracker.add(guard)
                    continue
            case 'v':
                if rpt[guard + length] == '#':
                    guardSym = '<'
                    rpt[guard] = '+'
                    printArray(rpt, newObs, debug)
                    moveTracker.add(guard)
                    continue
        #start patrol
        match guardSym:
            case '^':
                rpt[guard-length] = '^'
                guard += -length
            case '>':
                rpt[guard+1] = '>'
                guard += 1
            case '<':
                rpt[guard-1] = '<'
                guard += -1
            case 'v':
                rpt[guard+length] = 'v'
                guard += length
            case _:
                moveTracker.add(guard)

def printArray(rpt,icon,debug):
    if debug:
        for i in range(0,len(rpt)):
            if i % length == 0 and not (i == 0):
                print()
            if i == icon:
                print('X',end="")
            else:
                print(rpt[i],end="")
        input()
        print()     
        
def printArrayS(rpt):
    if True:
        for i in range(0,len(rpt)):
            if i % length == 0 and not (i == 0):
                print()
            print(rpt[i],end=" ")
        input()
        print()   
    

if __name__ == "__main__":
    #Setup Arrays/Values
    map = []
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            map += line.replace('\n',"")
            
    length = 130
    guard = map.index('^')
    firstMap = map.copy()
    spaces, _ = guardPat(firstMap,length, guard, False, None)
    print(len(spaces))
    spaces.remove(guard)
    obstructions = set()
    for moves in spaces:
        new_map = map.copy()
        new_map[moves] = '#'
        _, loop = guardPat(new_map,length, guard, False, moves)
        if loop:
            obstructions.add(moves)
            
            
    # Single Tester
    # sus = 809
    # new_map = map.copy()
    # new_map[sus] = '#'
    # _, loop = guardPat(new_map,length, guard, True, sus)
    # print(loop)
    # if loop:
        # print("Loop Found")
       
    print(len(obstructions))
    

#1784
    