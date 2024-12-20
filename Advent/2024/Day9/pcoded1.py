#--- Day 9: Disk Fragmenter ---
import sys
import numpy as np

def createDisk(rpt):
    counter = 0
    newDisk = []
    for i in range(0,len(rpt)):
        if i % 2 == 0:
            newDisk.extend([counter]*int(rpt[i]))
            counter += 1
        else:
            newDisk.extend(['.']*int(rpt[i]))
    
    return newDisk
    
def crackDisk(rpt):
    val = 0
    space = rpt.count('.')
    files = len(rpt)-space
    while '.' in rpt:
        switch = rpt.pop()
        rpt[rpt.index('.')] = switch
    # rpt.extend(['.']*space)
    
    for i in range(0,len(rpt)):
        val += rpt[i]*i
    
    return val
    
    

if __name__ == "__main__":
    #Setup Arrays/Values
    array = []
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            array += line
  
    ops = createDisk(array)
    print(crackDisk(ops))