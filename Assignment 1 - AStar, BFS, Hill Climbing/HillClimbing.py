# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:42:31 2019

@author: Aditya Mahajan
"""
class Node:
    
    def __init__(self, index, h, parent=None):
        self.index = index
        self.parent = parent
        self.h = h
    
    def __eq__(self, other):
        return self.index == other.index
    
    
def HillClimbing(adj_matrix, heuristic_values, start, end):
    
    #Create Start Node and End node
    start_node = Node(start, heuristic_values[start], None)
    end_node = Node(end, heuristic_values[end], None)
    
    #Set Current node as start node
    current_node = start_node
    
    while True:
        
        #If current node is end node, return path
        if current_node == end_node:
            print("\n***** End node reached *****")
            
            path = []
            
            current = current_node
            
            while current is not None:
                path.append(current.index)
                current = current.parent
                
            return path[::-1]
        
        #Generate Children of current node
        children = []
        
        for index, i in enumerate(adj_matrix[current_node.index]):
            if i == 1:
                child = Node(index, heuristic_values[index], current_node)
                children.append(child)
               
        
        #Select the first child with h value lower than current node, assign it as current node
        flag = False
        for child in children:
            if child.h < current_node.h:
                current_node = child
                flag = True
                break
            
        #If children = [] or no better state found then return
        if flag == False:
            print("\n***** Hill Climbing Failed *****")
            path = []
            
            current = current_node
            
            while current is not None:
                path.append(current.index)
                current = current.parent
                
            return path[::-1]
                
            
def main():
    num_nodes = int(input("Enter number of nodes:- "))
    
    
    print("\n***** Enter adjacency matrix:- *****")
    adj_matrix = []
    
    for i in range(0, num_nodes):
        inner_list = []
        
        for j in range(0, num_nodes):
            inner_list.append(int(input("Enter "+str(i)+","+str(j)+": ")))
        
        adj_matrix.append(inner_list)

    print("\nAdjacency Matrix entered:- \n"+str(adj_matrix))

    print("\n***** Enter heuristic values *****")
    heuristic_values = []
    
    for i in range(0, num_nodes):
        heuristic_values.append(int(input("Enter h value of node "+str(i)+":- ")))
    
    start = int(input("\nEnter start node index:- "))
    end = int(input("\nEnter end node index:- "))
    
    
    path = HillClimbing(adj_matrix, heuristic_values, start, end)
    
    print("\nPath given by Hill Climbing:- "+str(path))                


if __name__ == "__main__":
    main()
