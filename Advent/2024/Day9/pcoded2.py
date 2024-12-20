#--- Day 9: Disk Fragmenter ---
import sys
import numpy as np

def createDisk(rpt):
    counter = 0
    newDisk = []
    files = {}
    chunksLeft = [0]*10
    filesLeft = [0]*10
    emptyChunks = []
    for i in range(0,10):
        chunksLeft[i] = 0
    for i in range(0,len(rpt)):
        if i % 2 == 0:
            newDisk.extend([counter]*int(rpt[i]))
            files[str(counter)]=int(rpt[i])
            counter += 1
            if rpt[i] != '0':
                filesLeft[int(rpt[i])] += 1
        else:
            emptyChunks.append([len(newDisk),int(rpt[i])])
            newDisk.extend(['.']*int(rpt[i]))
            if rpt[i] != '0':
                chunksLeft[int(rpt[i])] += 1
    
    return newDisk,files,emptyChunks,chunksLeft,filesLeft
    
def crackDisk(rpt,files,emptyChunks,chunksLeft,filesLeft):
    val = 0
    space = rpt.count('.')
    filesIDs = sorted(files.keys(), key=int,reverse=True)
    min = 0
    sizeChunks = [0] * 10
    for i in range(0,10):
        sizeChunks[i] = i
    prettyPrint(rpt)
    
    # print(filesIDs)
    # print(emptyChunks)
    filesIDs.pop()
    while True:
        swap = False
        if filesLeft[min] == 0:
            min += 1
            emptyChunks = [x for x in emptyChunks if x[1] >= min]
        if chunksLeft[sizeChunks[-1]] == 0:
            tmpA = filesIDs.copy()
            for fi in tmpA:
                if files[fi] >= sizeChunks[-1]:
                    filesLeft[files[fi]] -= 1
                    filesIDs.remove(fi)
            chunksLeft.pop()
            sizeChunks.pop()
            continue
        #nothing left to process
        if len(filesIDs) == 0 or len(emptyChunks) == 0:
            break
        ids = filesIDs[0]
        fileChunk = files[ids]
        fL = rpt.index(int(ids))
        valid = False
        if sizeChunks[-1] >= fileChunk:
            valid = True
        else:
            filesIDs.pop(0)
            continue
        # print(ids,fileChunk)
        # print(filesLeft,chunksLeft)
        # prettyPrint(rpt)
        # input()
        if valid:
            for i in range(0,len(emptyChunks)):
                if emptyChunks[i][1] >= fileChunk and emptyChunks[i][0] < rpt.index(int(ids)):
                    #swap
                    swap = True
                    emV = emptyChunks[i][1]
                    chunksLeft[emV] -= 1
                    index = emptyChunks[i][0]
                    fS = files[ids]
                    emptyChunks[i][1] = emV - fS
                    emptyChunks[i][0] += fS
                    filesLeft[fS] -= 1
                    chunksLeft[emV-fS] += 1
                    for i in range(0,fS):
                        rpt[index+i],rpt[fL+i] = rpt[fL+i],rpt[index+i]
                    break
            #invalidateEmptyChunks
            emptyChunks.reverse()
            for j in emptyChunks:
                if j[0] >= fL:
                    chunksLeft[j[1]] -= 1
                    j[1] = 0
                else:
                    break
            emptyChunks.reverse()
                    
            if swap:
                filesIDs.pop(0)
                continue
        filesIDs.pop()
            
                

    # rpt.extend(['.']*spasce)
    for i in range(0,len(rpt)):
        if rpt[i] == '.':
            continue
        val += int(rpt[i])*i
        
        
    return val
    
    
def prettyPrint(rpt):
    for obj in rpt:
        print(obj,end=" ")
    print()
    # input()

if __name__ == "__main__":
    #Setup Arrays/Values
    array = []
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            array += line
  
    ops,files,spaces,chunksLeft,filesLeft = createDisk(array)
    # prettyPrint(ops)
    print(crackDisk(ops,files,spaces,chunksLeft,filesLeft))
    # prettyPrint(ops)
    
#15087147054931 too high
#15849602591702 too high
#6389911791746