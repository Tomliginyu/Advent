#--- Day 4: Ceres Search ---
import sys
import re

def wordCounter(rpt):
    #something
    sum = 0
    for x in range(0,len(rpt)):
        for y in range(0,len(rpt[x])):
            if rpt[x][y] == 'A':
                sum += evalWord(rpt,x,y)
                
    print(sum)
    
def evalWord(rpt,rw,cl):
    wkstring = ""
    check1 = False
    check2 = False
    #horiz
    #diagrightdown
    if len(rpt[rw]) - 1 > cl and len(rpt) - 1 > rw and rw > 0:
        for i in range(-1,2):
            wkstring += rpt[rw+i][cl+i]
    if wkstring == "SAM" or wkstring == "MAS":
        check1 = True
    wkstring = ""
    #diagrightup
    if (rw > 0 and rw < len(rpt) - 1) and len(rpt[rw]) - 1 > cl:
        for i in range(-1,2):
            wkstring += rpt[rw-i][cl+i]
    
    if wkstring == "SAM" or wkstring == "MAS":
        check2 = True
    wkstring = ""

    if check1 and check2:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    #Setup Arrays/Values
    wordsearch = []
    row = []
    
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            for char in line:
                row.append(char)
            wordsearch.append(row)
            row = []
            

    wordCounter(wordsearch)
    #1967
    