#--- Day 4: Ceres Search ---
import sys
import re

def wordCounter(rpt):
    #something
    sum = 0
    for x in range(0,len(rpt)):
        for y in range(0,len(rpt[x])):
            if rpt[x][y] == 'X':
                sum += evalWord(rpt,x,y)
                
    print(sum)
    
def evalWord(rpt,rw,cl):
    wkstring = ""
    results = []
    #horiz
    if len(rpt[rw]) - 3 > cl:
        for i in range(0,4):
            wkstring += rpt[rw][cl+i]
    results.append(wkstring)
    wkstring = ""
    #hbk
    if cl > 2:
        for i in range(0,4):
            wkstring += rpt[rw][cl-i]
    results.append(wkstring)
    wkstring = ""
    #vertidw
    if len(rpt) - 3 > rw:
        for i in range(0,4):
            wkstring += rpt[rw+i][cl]
    results.append(wkstring)
    wkstring = ""
    #vertiup
    if rw > 2:
        for i in range(0,4):
            wkstring += rpt[rw-i][cl]
    results.append(wkstring)
    wkstring = ""
    #diagrightdown
    if len(rpt[rw]) - 3 > cl and len(rpt) - 3 > rw:
        for i in range(0,4):
            wkstring += rpt[rw+i][cl+i]
    results.append(wkstring)
    wkstring = ""
    #diagleftup
    if rw > 2 and cl > 2:
        for i in range(0,4):
            wkstring += rpt[rw-i][cl-i]
    results.append(wkstring)
    wkstring = ""
    #diagrightup
    if rw > 2 and len(rpt[rw]) - 3 > cl:
        for i in range(0,4):
            wkstring += rpt[rw-i][cl+i]
    results.append(wkstring)
    wkstring = ""
    #diagleftd
    if cl > 2 and len(rpt) - 3 > rw:
        for i in range(0,4):
            wkstring += rpt[rw+i][cl-i]

    results.append(wkstring)
    wkstring = ""
    print(results)
    return results.count("XMAS")
    
if __name__ == "__main__":
    #Setup Arrays/Values
    wordsearch = []
    row = []
    
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            for char in line:
                row.append(char)
            wordsearch.append(row)
            row = []
            
    #DumbDownArray?

    wordCounter(wordsearch)
    
#2474 too low
#2483 too low
#2488
#2496