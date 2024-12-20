#--- Day 2: Red-Nosed Reports ---
import sys

def safeChk(rpt):
    #something
    work = int(rpt[0])
    sign = ""
    for i in range(1,len(rpt)):
        res = work - int(rpt[i])
        if abs(res) > 3:
            return "Unsafe"
        if res == 0:
            return "Unsafe"

        if res > 0 and sign == "":
            sign = "dwn"
            work = int(rpt[i])
            continue
            
        if res < 0 and sign == "":
            sign = "up"
            work = int(rpt[i])
            continue
            
        if res > 0 and sign == "up":
            return "Unsafe"
            
        if res < 0 and sign == "dwn":
            return "Unsafe"
            
        work = int(rpt[i])
            
    return "Safe"
    
    
if __name__ == "__main__":
    #Setup Arrays
    array = []
    
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            array.append(safeChk(line.split()))
            

    print(array.count("Safe"))