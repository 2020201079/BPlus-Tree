import copy
from queue import Queue

order = 2 # order of bptree hardcoding it # number of children
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
    def getLen(self): # returns number of keys
        count = 0
        for k in self.keys:
            if k is not None:
                count += 1
        return count
    def reset(self):
        self.keys = [None]*order
        self.pointers = [None]*(order+1)
        self.isLeaf = False

def getLeafNodeToInsert(currNode,parent,key): #returns leafNode,parent
    while(True):
        if currNode.isLeaf:
            return currNode,parent
        else:
            for i in range(currNode.getLen()):
                if key<currNode.keys[i]:
                    return getLeafNodeToInsert(currNode.pointers[i],currNode,key)
            return getLeafNodeToInsert(currNode.pointers[currNode.getLen()],currNode,key)

def getParent(root:Node,parent:Node):
    if(root == parent):
        return None
    for p in root.pointers:
        if p==parent:
            return root
    else:
        for i in range(root.getLen()):
            if parent.keys[0] < root.keys[i]:
                return getParent(root.pointers[i],parent)
        return getParent(root.pointers[root.getLen()],parent)

def printBP(root:Node): # print level order
    if root:
        pass
        #print(root.keys)
    queue = []
    queue.append(root)
    while queue:
        currNode = queue.pop(0)
        if currNode:
            print(currNode.keys)
            for i in range(len(currNode.pointers)):
                if currNode.pointers[i]:
                    queue.append(currNode.pointers[i])
            print()
def getNewLeafNodes(currList:list): #returns left and right Nodes
    leftNode = Node()
    rightNode = Node()
    leftNode.isLeaf = True
    rightNode.isLeaf = True
    leftNode.keys[0] = currList[0]
    rightNode.keys[0] = currList[1]
    rightNode.keys[1] = currList[2]
    return leftNode,rightNode

def getKeysPointers(parent:Node,leftNode:Node,rightNode:Node,keyToInsert):
    #here parent should already be full otherwise throw error
    keyAns = []
    pointerAns = []
    if keyToInsert < parent.keys[0]:
        keyAns.append(keyToInsert)
        keyAns.append(parent.keys[0])
        keyAns.append(parent.keys[1])
        pointerAns.append(leftNode)
        pointerAns.append(rightNode)
        pointerAns.append(parent.pointers[1])
        pointerAns.append(parent.pointers[2])
        return keyAns,pointerAns
    elif (keyToInsert>parent.keys[0] and keyToInsert<parent.keys[1]):
        keyAns.append(parent.keys[0])
        keyAns.append(keyToInsert)
        keyAns.append(parent.keys[1])
        pointerAns.append(parent.pointers[0])
        pointerAns.append(leftNode)
        pointerAns.append(rightNode)
        pointerAns.append(parent.pointers[2])
        return keyAns,pointerAns
    else:
        keyAns.append(parent.keys[0])
        keyAns.append(parent.keys[1])
        keyAns.append(keyToInsert)
        pointerAns.append(parent.pointers[0])
        pointerAns.append(parent.pointers[1])
        pointerAns.append(leftNode)
        pointerAns.append(rightNode)
        return keyAns,pointerAns

def insertIntermediate(parent:Node,leftNode:Node,rightNode:Node,root:Node,keyToInsert):
    #keep mutating the parent no assignment
    if parent.hasPlace():
        # need to implement rightNode.keys[0] in parent
        if(parent.keys[0] < keyToInsert):
            parent.keys[1] = keyToInsert
            parent.pointers[1] = leftNode
            parent.pointers[2] = rightNode
        else:
            parent.keys[1] = parent.keys[0]
            parent.pointers[2] = parent.pointers[1]
            parent.pointers[1] = parent.pointers[0]
            parent.keys[0] = keyToInsert
            parent.pointers[0] = leftNode
            parent.pointers[1] = rightNode
    else:
        print("Implement parent does not has place case")
        grandParent = getParent(root,parent)
        if grandParent is None:
            print("parent is None")
            #need to set keys and pointers first
            newKeys,newPointers = getKeysPointers(parent,leftNode,rightNode,keyToInsert)
            print("new keys ", newKeys)
            leftIntermediateNode = Node()
            leftIntermediateNode.keys[0] = newKeys[0]
            leftIntermediateNode.pointers[0] = newPointers[0]
            leftIntermediateNode.pointers[1] = newPointers[1]
            rightIntermediateNode = Node()
            rightIntermediateNode.keys[0] = newKeys[2]
            rightIntermediateNode.pointers[0] = newPointers[2]
            rightIntermediateNode.pointers[1] = newPointers[3]
            root.reset()
            root.keys[0] = newKeys[1]
            root.pointers[0] = leftIntermediateNode
            root.pointers[1] = rightIntermediateNode
        else:
            print("parent is ",grandParent.keys)
            newKeys,newPointers = getKeysPointers(parent,leftNode,rightNode,keyToInsert)
            print("new keys ", newKeys)
            leftIntermediateNode = Node()
            leftIntermediateNode.keys[0] = newKeys[0]
            leftIntermediateNode.pointers[0] = newPointers[0]
            leftIntermediateNode.pointers[1] = newPointers[1]
            rightIntermediateNode = Node()
            rightIntermediateNode.keys[0] = newKeys[2]
            rightIntermediateNode.pointers[0] = newPointers[2]
            rightIntermediateNode.pointers[1] = newPointers[3]
            insertIntermediate(grandParent,leftIntermediateNode,rightIntermediateNode,root,newKeys[1])



def insert(root,key):
    print("Inserting : ",key) 
    leafNode,parent = getLeafNodeToInsert(root,None,key)
    if(leafNode.hasPlace()):
        for i in range(len(leafNode.keys)):
            if leafNode.keys[i] is None:
                leafNode.keys[i] = key
                break
        leafNode.keys = sorted(leafNode.keys,key=lambda x: (x is None,x))
        printBP(root)
        print("-"*10)
    else:
        currList = leafNode.keys.copy()
        currList.append(key)
        currList = sorted(currList)
        leftNode,rightNode = getNewLeafNodes(currList)
        if parent is None:
            print("entered parent is None Cond")
            #newParent = Node()
            root.reset()
            root.keys[0] = rightNode.keys[0]
            root.pointers[0] = leftNode
            root.pointers[1] = rightNode
            root.isLeaf = False
            printBP(root)
            print("-"*10)
            #root = newParent
            #return newParent
        else:
            print("Parent is not none condition")
            insertIntermediate(parent,leftNode,rightNode,root,rightNode.keys[0])
            printBP(root)
            print("-"*10)

def main():
    root = Node()
    root.isLeaf = True
    insert(root,20)
    insert(root,10)
    insert(root,5)
    insert(root,1)
    insert(root,2)
    insert(root,15)
    insert(root,60)
    while True:
        val = input() # INSERT X
        val = val.split(' ')
        command = val[0]
        if(command.upper() == 'I'):
            key = int(val[1])
            insert(root,key)
            #printBP(root,0)

if __name__ == "__main__":
    main()