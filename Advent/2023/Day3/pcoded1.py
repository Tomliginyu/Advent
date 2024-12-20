#--- Day 3: Gear Ratios ---
import sys
import numpy as np

def gearRatio(rpt):
    status = False
    ret = False
    num = ""
    nums = 0
    for i in range(0,len(rpt)):
        for j in range(0,len(rpt[i])):
            if rpt[i][j].isdigit() and not status:
                status = True
                num += rpt[i][j]
                continue
              
            if not rpt[i][j].isdigit() and status:
                if j == 0:
                    ret = checkVal(rpt,num,i,len(rpt[i]))
                else:
                    ret = checkVal(rpt,num,i,j)
                if ret:
                    print(i,nums, "added:", num)
                    nums += int(num)
                num = ""
                status = False
                ret = False
                continue
                
            if rpt[i][j].isdigit():
                num += rpt[i][j]
                
    print(nums)
            
                
def checkVal(rpt, val, rw, cl):
    #Find out if number is valid
    #check row above
    rows = []
    symbols = ['!','@','#','$','%','^','&','*','/','+','-','=']
    ra = [rw - 1, cl - len(val) - 1,cl]
    #check edges
    rs = [rw, cl - len(val) - 1,cl]
    #check row below
    rb = [rw + 1, cl - len(val) - 1,cl]
    rows.append(ra)
    rows.append(rs)
    rows.append(rb)
    
    for arr in rows:
        #print(val,arr)
        for i in range(arr[1],arr[2]+1):
            print(val, i, arr)
            if arr[0] < 0 or arr[0] >= len(rpt):
                break
            if i < 0 or i >= len(rpt[0]):
                continue
            #print(val,i,rpt[arr[0]][i])
            if rpt[arr[0]][i] in symbols:
                return True
                
    return False
    
    
if __name__ == "__main__":
    #Setup Arrays
    arr = []
    
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            length = len(line)-1
            arr.append(line[0:length])
            
    gearRatio(arr)
    #print(arr)