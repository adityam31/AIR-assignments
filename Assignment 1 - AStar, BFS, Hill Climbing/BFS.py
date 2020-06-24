# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:13:21 2019

@author: Aditya Mahajan
"""

class Node:
    
    def __init__(self, index, h, parent=None):
        self.index = index
        self.parent = parent
        self.h = h
    
    def __eq__(self, other):
        return self.index == other.index


def BFS(adj_matrix, heuristic_values, start, end):
    
    #Create Start Node and End node
    start_node = Node(start, heuristic_values[start], None)
    end_node = Node(end, heuristic_values[end], None)

    #Initialize open and closed list
    open_list = []
    closed_list = []
    
    #Add start node to open list
    open_list.append(start_node)
    
    
    #Loop until you find end
    while len(open_list) > 0:
        
        #Get current node from open list with minimum value of h
        current_node = open_list[0]
        current_index = 0               #only used to remove appropriate node from open list
        
        for index, node in enumerate(open_list):
            if node.h < current_node.h:
                current_node = node
                current_index = index
        
        #Remove the current node from open list and add it to the closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        
        #Check if the current node is end node, if yes return path by back tracking
        if current_node == end_node:
            print("\n***** End node reached *****")
            
            path = []
            
            current = current_node
            
            while current is not None:
                path.append(current.index)
                current = current.parent
                
            return path[::-1]
        
        #Generate Children
        children = []
        
        for index, i in enumerate(adj_matrix[current_node.index]):
            if i == 1:
                child = Node(index, heuristic_values[index], current_node)
                children.append(child)
        
        #Loop through children
        for child in children:
            
            #If the child is in closed list, ignore
            flag = False
            
            for closed_node in closed_list:
                if child == closed_node:
                    flag = True
                    break
            
            if flag == True:
                continue
            
            #If child is in open list and child has higher h value, then ignore
            flag = False
            
            for open_node in open_list:
                if child == open_node and child.h > open_node.h:
                    flag = True
                    break
            
            if flag == True:
                continue
            
            #Append child to open list
            open_list.append(child)
        

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
    
    
    path = BFS(adj_matrix, heuristic_values, start, end)
    
    print("\nPath given by BFS:- "+str(path))                


if __name__ == "__main__":
    main()