#--- Day 3: Mull It Over ---
import sys
import re

def mulCheck(rpt):
    #something
    sum = 0
    values = re.findall("mul\(\d+,\d+\)",rpt)
    for mul in values:
        ints = re.findall("\d+,\d+",mul)
        for val in ints:
            tmp = val.split(',')
            sum += int(tmp[0]) * int(tmp[1])
            
    return sum
    
    
if __name__ == "__main__":
    #Setup Arrays/Values
    sum = 0
    
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            sum += mulCheck(line)
            

    print(sum)
    
    
#24587096