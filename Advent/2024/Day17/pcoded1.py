#--- Day 17: Chronospatial Computer ---
import sys
import re

#Function to Create Ternary Numbers by Poke
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))
    
def ternaryS (n):
    n.reverse()
    result = 0
    power = 1
    for d in n:
        result += int(d) * power
        power *= 3
    return result

def bwXOR(v1,v2):
    return v1 ^ v2
    
def readCommands(comm):
    global A,B,C
    score = 0
    output = ""
    i = 0
    while i < len(comm):
        opCode = int(comm[i])
        # print(A,B,C,output)
        # print(opCode,comm[i+1])
        # input()
        #pullthefirst 4 numbers
        match opCode:
            case 0:
            # Division RA / 2*
                A = int(A / (2 ** combo(int(comm[i+1]))))
                i += 2
            case 1:
            # bitwise XOR
                B = bwXOR(B,int(comm[i+1]))
                i += 2
            case 2:
            # modulo 8
                B = combo(int(comm[i+1])) % 8
                i += 2
            case 3:
            # jnz
                if A != 0:
                    i = int(comm[i+1])
                else:
                    i += 2
            case 4:
            # bitwise XOR
                B = bwXOR(B,C)
                i += 2
            case 5:
            # out
                tmp = combo(int(comm[i+1])) % 8
                if len(output) > 0:
                    output += ',' + str(tmp)
                else:
                    output += str(tmp)
                i += 2
            case 6:
            # Division
                B = int(A / (2 ** combo(int(comm[i+1]))))
                i += 2
            case 7:
            # Division
                C = int(A / (2 ** combo(int(comm[i+1]))))
                i += 2
                
        # print(output)
                
    return output
       
def combo(val):
    global A,B,C
    match val:
        case 0|1|2|3:
            return val
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            print("This isn't supposed to be here")
            
def switch(val):
    match val:
        case 0:
            return val
        case 1:
            return 3
        case 2:
            return 5
        case 3:
            return 3
        case 4:
            return 5
        case 5:
            return 4
        case 6:
            return 7
        case 7:
            return 6
        

if __name__ == "__main__":
    #Setup Arrays/Values
    global A,B,C
    content = []
    #Read File
    with open("data1.txt", "r") as file:
        for line in file:
            content.append(line.replace('\n',""))
            
    A = int(content[0])
    B = int(content[1])
    C = int(content[2])
    comm = content[3].split(',')
    output = readCommands(comm)
    # output = ""
    # print(comm,output)
    # A = 281474976710657
    # A = 35184372088832
    #Final = comm 2412751344550330
    # output = readCommands(comm)
    # A = 281474976710657
    # A = 37222273957364
    # A = 35184372088833 + (3*(8 ** 13)) + (1*(8 ** 12)) + (1*(8 ** 11)) + (1*(8 ** 10)) + (1*(8 ** 9)) + (1*(8 ** 8)) + (1*(8 ** 7)) + (1*(8 ** 6)) + (1*(8 ** 7)) + (1*(8 ** 5)) + + (1*(8 ** 4)) + (1*(8 ** 3)) + (1*(8 ** 10))
    # A = 37222273957312
    A = 0
    tmp = A
    while True:
        output = readCommands(comm)
        output = output.split(',')
        print(tmp,"".join(output))
        tmp1 = comm.copy()
        tmp1.reverse()
        tmpS = output.copy()
        tmpS.reverse()
        print(tmp1)
        print(tmpS)
        match = True
        if tmp1 == tmpS:
            print("We did it",tmp)
            break
        for y in range(0,len(tmpS)):
            if tmpS[y] != tmp1[y]:
                match = False
        if match:
            print(tmp1,tmpS)
            tmp = tmp*8
        else:
            var = 1
            tmp += var
        A = tmp
        
    # sum = 0
    # for i in range(0,len(comm)):
        # tmp = int(comm[i])
        # sum += tmp * (8 ** i)

    # print(sum)
    
    

    # print("A:",A,"B:",B,"C:",C)
    # print("Output:",output)
    
    #715240761
    #37222273957364
