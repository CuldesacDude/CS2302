# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:32:33 2019

@author: kevin
"""
import time
import numpy as np
import matplotlib.pyplot as plt
import math

class BTree(object):
    # Constructor
    def __init__(self, data, child=[], isLeaf=True, max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
        
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)  
        
def IsFull(T):
    return len(T.data) >= T.max_data

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k < T.data[i]:
            return i
    return len(T.data)

def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.data.append(i)  
    T.data.sort()
    
def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
def readTXT(T, filename):
    with open(filename) as f:
        for line in f:
            line = line.split()
            Insert(T, line)
            
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])
    
def Print(T):
    # Prints data in tree in ascending order
    if T.isLeaf:
        for t in T.data:
            print(t,end=' ')
    else:
        for i in range(len(T.data)):
            Print(T.child[i])
            print(T.data[i],end=' ')
        Print(T.child[len(T.data)])
        
def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i][0])
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i][0])
            PrintD(T.child[i],space+'   ')

class Node:
    def __init__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None
        
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild=Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True
            
    def find (self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False
            
    def preorder(self):
        if self:
            print(str(self.value[0]))
            if self.leftchild:
                self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()
                
    def getHeight(self):
        if self.leftchild and self.rightchild:
            return 1 + max(self.leftchild.getHeight(), self.rightchild.getHeight())
        elif self.leftchild:
           return 1 + self.leftchild.getHeight()
        elif self.rightchild:
           return 1 + self.rightchild.getHeight()
        else:
           return 1
                
class Tree:
    def __init__(self):
        self.root = None
        
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0
        
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
        
    def find (self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
        
    def preOrder(self):
        print("preOrder")
        self.root.preorder()

    def readTxtInsert(self, filename):
     with open(filename) as f:
        for line in f:
            line = line.split()
            content = line
            self.insert(content)
 

def compareWords(filename):
    with open(filename)as f:
        for line in f:
            line = line.split()

"""
the 0.418 0.24968

he -0.20092 -0.060271
"""


n1 = np.dot(0.418,  0.24968) * np.dot(-0.20092,  -0.060271)
n2 = np.linalg.norm(0.24968) * np.linalg.norm(-0.060271)

n3 = n1//n2

print(n3)
"""
bst = Tree()

Start_Time = time.time()
bst.readTxtInsert("glove.6B.50d (2).txt")
End_Time = time.time()
print("TIME:",End_Time - Start_Time)

print(bst.getHeight())
#bst.preOrder()


C = BTree([], max_data=5)
filename = "glove.6B.50d (2).txt"

Start_Time = time.time()
readTXT(C, filename)
End_Time = time.time()
print("TIME:",End_Time - Start_Time)

print(Height(C))

"""