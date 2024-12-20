#--- Day 5: Print Queue ---
import sys
import re

def orderCheck(rpt):
    #something
    printed = []
    depends = []
    for item in rpt:
        if item in rules.keys():
            depends = rules[item]
            for dep in depends:
                if dep in printed:
                    print(rpt,"failed:",dep)
                    return 0
            printed.append(item)
        else:
            printed.append(item)
        
    return int(rpt[int(len(rpt)/2)])
    
def orderFixer(rpt):
    printed = []
    fixes = []
    depends = []
    print(rpt)
    for item in rpt:
        if item in rules.keys():
            depends = rules[item]
            for dep in depends:
                if dep in printed:
                    print(item,dep, "in",printed)
                    fixes.append(dep)
            if len(fixes) > 0:
                #find lowest index
                lowest = len(printed)
                for val in fixes:
                    lowest = min(lowest,printed.index(val))
                printed.insert(lowest,item)
            fixes = []
            if not (item in printed):
                printed.append(item)
        else:
            printed.append(item)
    
    #return 0
    return int(printed[int(len(printed)/2)])

    
    
if __name__ == "__main__":
    #Setup Arrays/Values
    rules = {}
    order = []
    
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            nums = line.split('|')
            if nums[0] in rules.keys():
                rules[nums[0]].append(nums[1].replace('\n',""))
            else:
                rules[nums[0]] = [nums[1].replace('\n',"")]
                
    with open("data22.txt", "r") as file:
        for line in file:
            sec = line.replace('\n',"")
            order.append(sec.split(','))
                
    sum = 0
    #print(rules)
    #print(order)
    for row in order:
        value = orderCheck(row)
        if value == 0:
            sum += orderFixer(row)
        
    print(sum)
    
    #4944