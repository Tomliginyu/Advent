#--- Day 7: Bridge Repair ---
import sys
import re

def solveEQ(rpt):
    #something
    symbols = ['+','*']
    nums = re.findall('\d+',rpt)
    value = int(nums[0])
    factors = []
    for i in range(1,len(nums)):
        factors.append(nums[i])
        
    options = 2 ** (len(factors)-1)
    for j in range(0,options):
        tmp = 0
        bins = (bin(j)[2:]).zfill(16)
        binStId = len(bins)-1
        tmp += int(factors[0])
        eqMont = str(value) + " = " + factors[0]
        for f in range(1,len(factors)):
            match symbols[int(bins[binStId])]:
                case '+':
                    eqMont += " + " + factors[f]
                    tmp = tmp + int(factors[f])
                case '*':
                    eqMont += " * " +factors[f]                  
                    tmp = tmp * int(factors[f])
            binStId += -1
        # print(eqMont,"actual",tmp)
        if tmp == value:
            # print("Good",eqMont)
            return value
        
    # specialPrint(nums)
    return 0
    
def specialPrint(rpt):
    print(rpt[0]+": "+' '.join(str(x) for x in rpt[1:]))
    
if __name__ == "__main__":
    #Setup Arrays/Values
    sum = 0
    equations = []
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            equations.append(line.replace('\n',""))
    
    for eq in equations:
        sum += solveEQ(eq)
        
    print(sum)
    
    #2498720468365 too low
    #2501605301465
    