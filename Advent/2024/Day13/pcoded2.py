#--- Day 13: Claw Contraption ---
import sys
from sympy import *
import re

A=3
B=1
ERROR = 10000000000000


def calcMachine(rpt):
    buttonA = int(rpt[0][0]),int(rpt[0][1])
    buttonB = int(rpt[1][0]),int(rpt[1][1])
    goal = int(rpt[2][0])+ERROR,int(rpt[2][1])+ERROR
    
    a, b = symbols('a b')
    expr1 = buttonA[0]*a + buttonB[0]*b
    expr2 = buttonA[1]*a + buttonB[1]*b
    
    sol = linsolve([Eq(expr1,goal[0]),Eq(expr2,goal[1])], (a, b))
    
    # print(sol)
    ret = (list(sol))[0]
    if ret[0].is_integer and ret[1].is_integer:
        return ret[0]*A + ret[1]*B
    else:
        return 0
    
    
      

if __name__ == "__main__":
    #Setup Arrays/Values
    content = ""
    machines = []
    sum = 0
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            for char in line:
                content += char
    
    test = re.split('\n',content)
    # print(test)
    for i in range(0,len(test),4):
        #Should be tuple, tuple, tuple
        tuple(re.findall('\d\d+',test[i]))
        machines.append([(tuple(re.findall('\d\d+',test[i])),tuple(re.findall('\d\d+',test[i+1])),tuple(re.findall('\d\d+',test[i+2])))])
        
    for machine in machines:
        tmp = calcMachine(machine[0])
        print(machine[0],tmp)
        sum += tmp
    print(sum)
