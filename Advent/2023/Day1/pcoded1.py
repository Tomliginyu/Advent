#--- Day 1: Trebuchet?! ---
import sys
import re

def valueCalc(arr):
    #something
    line = re.findall("\d",arr)

    return line[0] + line[len(line)-1]
    
if __name__ == "__main__":
    #Setup Arrays/Values
    sum = 0

    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            sum += int(valueCalc(line))
            
    print(sum)