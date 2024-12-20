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
        factors.append(int(nums[i]))
    _,status = reCCur(value,factors,len(factors))
    if status:
        # print(value)
        return value
    else:
        return 0
    
def reCCur(val, factors, endGame):
    retVals = []
    status = False
    if len(factors) < 2:
        #subtract
        if val > factors[0]:
            retVals.append(val-factors[0])
        #divide
        if val % factors[0] == 0:
            retVals.append(int(val/factors[0]))
        #strip
        if str(val).endswith(str(factors[0])):
            retVals.append(int((str(val))[:-len(str(factors[0]))]))
            
        return retVals, False
    else:
        recVals,_ = reCCur(val,factors[1:],endGame)
        # print(val,recVals,"Remaining:", factors[:-1])
        if endGame == len(factors) and factors[0] in recVals:
            return _,True
        for i in range(0,len(recVals)):
            #subtract
            if recVals[i] > factors[0]:
                retVals.append(recVals[i]-factors[0])
            #divide
            if recVals[i] % factors[0] == 0:
                retVals.append(int(recVals[i]/factors[0]))
            #strip
            if str(recVals[i]).endswith(str(factors[0])) and recVals[i] != factors[0]:
                retVals.append(int((str(recVals[i]))[:-len(str(factors[0]))]))
    return retVals, False
    
    
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
    