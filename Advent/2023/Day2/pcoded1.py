#--- Day 2: Red-Nosed Reports ---
import sys

def gameScore(rpt):
    record = rpt.split(":")
    gameNum = int((record[0].split())[1])
    rounds = record[1].split(";")
    for hand in rounds:
        roll = hand.split(", ")
        for r in roll:
            value = r.strip()
            value = value.split()
            if checks[value[1]] < int(value[0]):
                return 0
    
    
    return gameNum
    
if __name__ == "__main__":
    #Setup Arrays
    sum = 0
    checks = {
        "red":12,
        "blue":14,
        "green":13,
    }
    
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            sum += gameScore(line)
            
    
    print(sum)