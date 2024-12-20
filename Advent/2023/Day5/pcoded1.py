#--- Day 3: Gear Ratios ---
import sys
import re
    
                      
def translate(rpt):
    print()
    
    
if __name__ == "__main__":
    #Setup Arrays
    counter = -1
    res = []
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            res.append(re.search('^[\d+\s]+\n?',line))
            
     
    for line in res:
        if line is None:
            counter += 1
            continue
        if line.match() == '\n':
            continue
        match counter:
            case 0:
                line.replace('\n',"")
                line
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
