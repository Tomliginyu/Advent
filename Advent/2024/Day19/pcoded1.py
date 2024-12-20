#--- Day 17: Chronospatial Computer ---
import sys
import re
from functools import cache

def patternAnalysis():
    global patterns
    newPatterns = []
    for p in patterns:
        if 'w' in p or len(p) == 1:    
            newPatterns.append(p)
            
    return newPatterns

@cache
def patternRec(n):
    global patterns
    if n == "":
        return 1
    else:
        sum = 0
        for p in patterns:
            if n.startswith(p):
                # print(p,n,n[len(p):])
                sum += patternRec(n[len(p):])
    # print("Could not find match for:",n)
    return sum

def patternRecFP(n,altList):
    status = True
    # print("Trying to Match:",n)
    if len(n) == 0:
        return True
    if len(n) == 1:
        for pat in altList:
            if pat in n:
                return True
        return False
    # tmpR = n
    # tmpS = ''.join(tmpR)
    tmpS = n
    for p in altList:
        if p in tmpS:
            # print(p,"in",tmpS)
            tmpA = tmpS.split(p)
            for des in tmpA:
                if len(des) == 0:
                    continue
                # print("checking:",des,"in",tmpA)
                # input()
                status = status and patternRecFP(des,altList)
            if status:
                # print("Matched:",tmpS)
                return True
    
    if status:
        return True
    # print("Could not find match for:",n)
    return False      
        

if __name__ == "__main__":
    #Setup Arrays/Values
    global patterns, designs
    content = []
    finalSet = set()
    failedSet = set()
    testset1 = []
    testset2 = []
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            content.append(line.replace('\n',""))
    
      
    sum = 0
    total = 0
    patterns = content[0].split(', ')
    patterns.sort(key=len)
    patterns.reverse()
    designs = content[1:]
    
    #Trim Patterns
    # patterns = patternAnalysis()
    for d in designs:
        st = patternRec(d)
        if st:
            sum += 1
            total += st
        
    print("Possible:",sum,"of",len(designs))
    print(total,"designs possible")
        
    # 191 too low
    # 227 too low
    # 258
    # 283