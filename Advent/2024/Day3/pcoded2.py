#--- Day 3: Mull It Over ---
import sys
import re

def mulCheck(rpt):
    #something
    sum = 0
    global active
    values = re.findall("do\(\)|don't\(\)|mul\(\d+,\d+\)",rpt)
    for op in values:
        print(op)
        if "do()" in op:
            active = 0
            continue
        if "don't()" in op:
            active = -1
            continue
            
        if active == 0:
            ints = re.findall("\d+,\d+",op)
            for val in ints:
                tmp = val.split(',')
                sum += int(tmp[0]) * int(tmp[1])
                print(sum,"Add:",int(tmp[0]) * int(tmp[1]))
            
    return sum
    
    
if __name__ == "__main__":
    #Setup Arrays/Values
    sum = 0
    global active
    active = 0
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            sum += mulCheck(line)
            

    print(sum)
    
    
#79967531 too high
#72948684