#--- Day 6: Guard Gallivant ---
import sys
import re

def guardPat(rpt,length):
    #something
    guard = rpt.index('^')
    guardSym = '^'
    while rpt.index(guardSym) > 0:
        #print()
        #printArray(rpt)
        #print()
        #input()
        match guardSym:
                case '^':
                    if rpt.index('^') < length:
                        return rpt.count('X') + 1
                case '>':
                    if (rpt.index('>') + 1) % 130 == 0:
                        return rpt.count('X') + 1
                case '<':
                    if rpt.index('<') % 130 == 0:
                        return rpt.count('X') + 1
                case 'v':
                    if rpt.index('v') > len(rpt) - 130:
                        return rpt.count('X') + 1
        #is object in front
        try:
            match guardSym:
                case '^':
                    if rpt[guard - length] == '#':
                        guardSym = '>'
                        rpt[guard] = guardSym
                        printArray(rpt)
                        continue
                case '>':
                    if rpt[guard + 1] == '#':
                        guardSym = 'v'
                        rpt[guard] = guardSym
                        printArray(rpt)
                        continue
                case '<':
                    if rpt[guard - 1] == '#':
                        guardSym = '^'
                        rpt[guard] = guardSym
                        printArray(rpt)
                        continue
                case 'v':
                    if rpt[guard + length] == '#':
                        guardSym = '<'
                        rpt[guard] = guardSym
                        printArray(rpt)
                        continue
            #start patrol
            match guardSym:
                case '^':
                    rpt[guard] = 'X'
                    rpt[guard-length] = '^'
                    guard = rpt.index('^')
                case '>':
                    rpt[guard] = 'X'
                    rpt[guard+1] = '>'
                    guard = rpt.index('>')
                case '<':
                    rpt[guard] = 'X'
                    rpt[guard-1] = '<'
                    guard = rpt.index('<')
                case 'v':
                    rpt[guard] = 'X'
                    rpt[guard+length] = 'v'
                    guard = rpt.index('v')
        except IndexError:
            return rpt.count('X') + 1

def printArray(rpt):
    if False:
        for i in range(0,len(rpt)):
            if i % length == 0 and not (i == 0):
                print()
            print(rpt[i],end=" ")
        input()
        print()
    
if __name__ == "__main__":
    #Setup Arrays/Values
    map = []
    length = 130
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            map += line.replace('\n',"")
            
    print(guardPat(map,length))

#5337
#5191 too high
#5131
    