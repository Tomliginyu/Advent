#--- Day 2: Red-Nosed Reports ---
import sys

def safeChk(rpt, retStatus):
    #something
    work = int(rpt[0])
    status = ""
    sign = ""
    for i in range(1,len(rpt)):
        res = work - int(rpt[i])
        if abs(res) > 3:
            status = "Unsafe"
            break
        if res == 0:
            status = "Unsafe"
            break

        if res > 0 and sign == "":
            sign = "dwn"
            work = int(rpt[i])
            continue
            
        if res < 0 and sign == "":
            sign = "up"
            work = int(rpt[i])
            continue
            
        if res > 0 and sign == "up":
            status = "Unsafe"
            break
            
        if res < 0 and sign == "dwn":
            status = "Unsafe"
            break
            
        work = int(rpt[i])
     
    if status == "Unsafe" and retStatus == "Unsafe":
        return "Unsafe"
        
    #Run on Two different arrays
    if status == "Unsafe" and retStatus == "":
        for y in range(len(rpt)):
            arr1 = rpt.copy()
            arr1.pop(y)
            if safeChk(arr1,"Unsafe") == "Safe":
                return "Safe"
        return "Unsafe"
    
    return "Safe"
    
    
if __name__ == "__main__":
    #Setup Arrays
    array = []
    
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            array.append(safeChk(line.split(),""))
            

    #print(array)
    print(array.count("Safe"))