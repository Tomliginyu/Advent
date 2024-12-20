#--- Day 7: Bridge Repair ---
import sys
import re
import time

#Function to Create Ternary Numbers by Poke
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def solveEQ(rpt):
    #something
    symbols = ['+','*','|']
    nums = re.findall('\d+',rpt)
    value = int(nums[0])
    factors = []
    for i in range(1,len(nums)):
        factors.append(nums[i])
        
    options = 3 ** (len(factors)-1)
    for j in range(0,options):
        tmp = 0
        tern = ternary(j)
        tern = tern.zfill(16)
        ternStId = len(tern)-1
        tmp += int(factors[0])
        eqMont = str(value) + " = " + factors[0]
        for f in range(1,len(factors)):
            match symbols[int(tern[ternStId])]:
                case '+':
                    eqMont += " + " + factors[f]
                    tmp = tmp + int(factors[f])
                case '*':
                    eqMont += " * " +factors[f]                  
                    tmp = tmp * int(factors[f])
                case '|':
                    eqMont += " || " +factors[f]                  
                    tmp = int(str(tmp)+factors[f])
            if tmp > value:
                break
            ternStId += -1
        # print(eqMont,"actual",tmp)
        if tmp == value:
            print(eqMont)
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
    with open("data2.txt", "r") as file:
        for line in file:
            equations.append(line.replace('\n',""))
    
    start = time.time()
    for eq in equations:
        sum += solveEQ(eq)
        
    print(sum)
    end = time.time()
    print("Time:",(end-start),"seconds")
    
    #44841372855953
    