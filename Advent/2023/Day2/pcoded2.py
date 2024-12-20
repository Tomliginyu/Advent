#--- Day 2: Red-Nosed Reports ---
import sys

def gameScore(rpt):
    checks = {
        "red":0,
        "blue":0,
        "green":0,
    }
    record = rpt.split(":")
    gameNum = int((record[0].split())[1])
    rounds = record[1].split(";")
    for hand in rounds:
        roll = hand.split(", ")
        for r in roll:
            value = r.strip()
            value = value.split()
            if  int(value[0]) > checks[value[1]]:
                checks[value[1]] = int(value[0])
    
    print(checks)
    return checks["red"] * checks["blue"] * checks["green"]
    
if __name__ == "__main__":
    #Setup Arrays
    sum = 0
    
    
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            sum += gameScore(line)
            
    
    print(sum)