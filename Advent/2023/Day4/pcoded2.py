#--- Day 3: Gear Ratios ---
import sys
    
                      
def scratchCards(dict, numbs):
    sortArr = numbs.keys()
    
    for game in sortArr:
        numbs = dict[game].split('|')
        winns = len(intersection(numbs[0].split(),numbs[1].split()))
        #UpdateCounter
        for j in range(0,cardNumb[game]):
            for i in range(int(game)+1,int(game) + winns + 1):
                cardNumb[str(i)] += 1
                
    sum = 0
    for ticket in cardNumb:
        sum += cardNumb[ticket]
    print(sum)
                
        
    
    
def intersection(list_a, list_b):
    return [ e for e in list_a if e in list_b ]
    
if __name__ == "__main__":
    #Setup Arrays
    sum = 0
    
    cardDict = {}
    cardNumb = {}
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            num = line[5:line.index(':')]
            numbers = line[line.index(':')+1:].replace('\n',"")
            cardDict[num.strip()] = numbers
            cardNumb[num.strip()] = 1
    
    scratchCards(cardDict, cardNumb)