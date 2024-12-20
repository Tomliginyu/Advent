#--- Day 3: Gear Ratios ---
import sys
import re

def gearRatio(rpt):
    gear_regex = r'\*'
    gears = dict()
    
    for i, line in enumerate(rpt):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []
    
    number_regex = r'\d+'
    for i, line in enumerate(rpt):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))
                        
    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += nums[0] * nums[1]
            
    print(gear_ratio_sum)
    
    
if __name__ == "__main__":
    #Setup Arrays
    arr = []
    
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            length = len(line)-1
            arr.append(line[0:length])
            
    gearRatio(arr)
    #print(arr)