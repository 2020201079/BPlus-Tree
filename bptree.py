import bisect
from queue import Queue

order = 3 # order of bptree hardcoding it
class Node:
    def __init__(self): # always creates a non leaf node
        self.keys = [None]*order
        self.pointers = [None]*(order+1)
        self.isLeaf = False
    def getKeys(self):
        return self.keys
    def getPointers(self):
        return self.pointers
    def hasPlace(self):
        if None in self.keys:
            return True
        return False

def getLeafNodeToInsert(currNode,parent,key): #returns leafNode,parent
    while(True):
        if currNode.isLeaf:
            return currNode,parent
        else:
            for i in range(len(currNode.keys)):
                if key<temp.keys[i]:
                    return getLeafNodeToInsert(temp.pointers[i],currNode,key)
            return getLeafNodeToInsert(temp.pointers[len(currNode.keys)],currNode,key)

def printBP(root:Node,level): # print level order
    if root:
        pass
        #print(root.keys)
    queue = []
    queue.append(root)
    while queue:
        currNode = queue.pop(0)
        if currNode:
            for i in range(len(currNode.keys)):
                if currNode.keys[i]:
                    print(currNode.keys[i],end=" ")
                    if currNode.pointers[i]:
                        queue.append(currNode.pointers[i])
            print()
            if currNode.pointers[len(currNode.keys)]:
                queue.append(currNode.pointers[len(currNode.keys)])

def insert(root,key):
    if(root == None):
        root = Node()
        root.keys[0]=key
        root.isLeaf = True
        return root
    else:
        leafNode,parent = getLeafNodeToInsert(root,None,key)
        if(leafNode.hasPlace()):
            for i in range(len(leafNode.keys)):
                if leafNode.keys[i] is None:
                    leafNode.keys[i] = key
                    break
            leafNode.keys = sorted(leafNode.keys,key=lambda x: (x is None,x))
            return root
        else:
            print("implement case for splitting")

def main():
    root = None
    while True:
        val = input() # INSERT X
        val = val.split(' ')
        command = val[0]
        if(command.upper() == 'INSERT'):
            key = val[1]
            root = insert(root,key)
            printBP(root,0)

if __name__ == "__main__":
    main()