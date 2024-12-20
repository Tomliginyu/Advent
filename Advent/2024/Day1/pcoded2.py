#--- Day 1: Historian Hysteria ---
import sys

def simulCalc(lfa, rta):
    #something
    occuran = {}
    sum = 0
    for i in range(len(rta)):
        if rta[i] in occuran.keys():
            occuran[rta[i]] += 1
        else:
            occuran[rta[i]] = 1;
        
    for y in range(len(lfa)):
        if lfa[y] in occuran.keys():
            sum += int(lfa[y]) * occuran[lfa[y]]
    
    print(sum)
    
if __name__ == "__main__":
    #Setup Arrays
    array1 = []
    array2 = []

    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            numbers = line.split()
            array1.append(numbers[0])
            array2.append(numbers[1])
            
    array1.sort()
    array2.sort()
    simulCalc(array1, array2)