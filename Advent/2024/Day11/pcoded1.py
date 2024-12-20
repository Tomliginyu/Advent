#--- Day 11: Plutonian Pebbles ---
import sys

def stoneCalc():
    # print("RPT",rpt)
    global counts, mappings
    # print(counts)
    wkCounts = {}
    # print(rpt)
    for key in counts.keys():
        if key in mappings.keys():
            #transform
            trans = mappings[key]
            for tr in trans:
                if tr in wkCounts.keys():
                    wkCounts[tr] += counts[key]
                else:
                    wkCounts[tr] = counts[key]
            continue
        if len(key) % 2 == 0:         
            tmp1 = str(int(key[int(len(key)/2):]))
            tmp2 = key[:int(len(key)/2)]
            mappings[key] = [tmp1,tmp2]
            if tmp1 in wkCounts.keys():
                wkCounts[tmp1] += counts[key]
            else:
                wkCounts[tmp1] = counts[key]
            if tmp2 in wkCounts.keys():
                wkCounts[tmp2] += counts[key]
            else:
                wkCounts[tmp2] = counts[key]
            continue
        val = str(int(key)*2024)
        mappings[key] = [val]
        if val in wkCounts.keys():
            wkCounts[val] += counts[key]
        else:
            wkCounts[val] = counts[key]           
 
        
    #updateCounts
    counts = wkCounts
    
#ShittyBF
def stoneCalc2(rpt,cD,tD):
    # print(rpt)
    j = 0
    # print(rpt,cD)
    while j < len(rpt):
        if rpt[j] == '0':
            rpt[j] = '1'
            j += 1
            continue
        if len(rpt[j]) % 2 == 0:
            item = rpt[j]
            tmp1 = str(int(item[int(len(item)/2):]))
            tmp2 = item[:int(len(item)/2)]
            rpt[j] = tmp2
            j += 1
            rpt.insert(j,str(tmp1))
            j += 1
            continue
        rpt[j] = str(int(rpt[j])*2024)
        j += 1

    sum = 0    
    if (cD == tD):
        return rpt,len(rpt)
    
    for i in range(0,len(rpt)):
        tmp = [rpt[i]]
        tmp3, val = stoneCalc2(tmp,cD+1,tD)
        rpt.extend(tmp3)
        sum += val
        
    return rpt,sum

if __name__ == "__main__":
    #Setup Arrays/Values
    content = ""
    sum = 0
    global mappings, counts
    mappings = {'0':['1'],'2024':['20','24'],'1':['2024']}
    counts = {}
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            content = line
    
   
    content = content.split(' ')
    newC, sum = stoneCalc2(content,1,25)
    sum2 = 0
    for i in range(0,len(newC),2):
        rein = [newC[i],newC[i+1]]
        reinT, tmpV = stoneCalc2(rein,1,25)
        sum2 += tmpV
        
    print(sum2)
    #For Speed
    # for c in content:
        # if c in counts.keys():
            # counts[c] += 1
        # else:
            # counts[c] = 1
    # for i in range(0,75):
        # stoneCalc()
    # for key in counts.keys():
        # sum += counts[key]
    # print(sum)
