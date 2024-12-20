#--- Day 3: Gear Ratios ---
import sys
    
                      
def scratchCards(rpt):
    numbers = rpt.split('|')
    wins = numbers[0].split()
    curr = numbers[1].split()
    winning = intersection(wins,curr)
    print(winning)
    if len(winning) == 0:
        return 0
    else:
        print(2 ** (len(winning) - 1))
        return 2 ** (len(winning) - 1)
    
def intersection(list_a, list_b):
    return [ e for e in list_a if e in list_b ]
    
if __name__ == "__main__":
    #Setup Arrays
    sum = 0
    
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            sum += scratchCards(line[line.index(':') + 1:])
         
    print(sum)