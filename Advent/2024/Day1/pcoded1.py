#--- Day 1: Historian Hysteria ---
import sys

def distanceCalc(lfa, rta):
    #something
    sum = 0
    for i in range(len(lfa)):
        sum += abs(lfa[i] - rta[i])
        
    print(sum)
    
if __name__ == "__main__":
    #Setup Arrays
    array1 = []
    array2 = []

    #Read File
    with open("data.txt", "r") as file:
        for line in file:
            numbers = line.split()
            array1.append(int(numbers[0]))
            array2.append(int(numbers[1]))
            
    array1.sort()
    array2.sort()
    distanceCalc(array1, array2)