#--- Day 10: Hoof It ---
import sys

MOVE = [(0,1),(0,-1),(1,0),(-1,0)]

class TreeNode:
    def __init__(self, data, loc, loc2):
        self.data = data
        self.location = loc
        self.children = []
        self.root = loc2

    def add_child(self, child):
        self.children.append(child)
    
    def info(self):
        print(self.location,"val:",self.data)
        
    def find_child(self,rpt):
        global length, sum
        if self.data == 9:
            if self.root in peaks.keys():
                peaks[self.root].append(self.location)
            else:
                peaks[self.root] = [self.location]
            return True
        tar = self.data + 1
        keepG = False
        for m in MOVE:
            newNode = (self.location[0] + m[0],self.location[1] + m[1])
            if not isValid(newNode):
                continue
            if rpt[newNode] == tar:
                keepG = True
                node = TreeNode(tar,newNode,self.root)
                self.add_child(node)

        
        if not keepG:
            return False
        
        # self.print_tree()
        self.info()
        self.print_children()  
        for node in self.children:
            print("Looking for:",node.location,node.data)
            res = node.find_child(rpt)
        return
        
    def remove_child(self,node):
        self.children.remove(node)
        
        
    def print_tree(self):
        self.info()
        for child in self.children:
            child.print_tree()
        print()
        
    def print_children(self):
        print("Has children")
        for item in self.children:
            print(item.location,"val:",item.data)
        

def isValid(node):
    global length
    if (node[0] == -1 or node[0] == length) or (node[1] == -1 or node[1] == length):
        return False
    return True

def evalMap(rpt,startPoints):
    roots = []
    for zer in startPoints:
        #Roots
        root = TreeNode(rpt[zer],zer,zer)
        roots.append(root)
    
    for root in roots:
        val = root.find_child(rpt)
        root.print_tree()
        
                
def printArray(rpt,length,debug):
    if debug:
        for i in range(0,length):
            for j in range(0,length):
                print(rpt[(i,j)],end=" ")
            print()
        # input()
        print()   
    

if __name__ == "__main__":
    #Setup Arrays/Values
    content = []
    #Read File
    with open("data2.txt", "r") as file:
        for line in file:
            content += (line.replace('\n',""))
    
    global sum, length, peaks
    peaks = {}
    sum = 0
    length = int(len(content) ** 0.5)
    mapS = {}
    sP = set()
    for i in range(0,length):
        for j in range(0,length):
            if content[i*length + j] == '.':
                val = content[i*length + j]
            else:
                val = int(content[i*length + j])
            mapS[(i,j)] = val
            if val == 0:
                sP.add((i,j))
            
    # printArray(mapS,length,True)
    evalMap(mapS,sP)
    
    #calcScore
    for starter in peaks.keys():
        sum += len(peaks[starter])
        print(starter,peaks[starter])
    print(sum)
    
    #644
    