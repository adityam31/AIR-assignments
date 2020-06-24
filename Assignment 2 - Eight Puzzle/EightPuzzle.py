# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:06:36 2019

@author: Aditya Mahajan
"""
import copy

size = 3

class Node:
    
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
        self.h = 0
    
    def __eq__(self, other):
        flag = True
        
        for i in range(0, size):
            for j in range(0, size):
                if self.state[i][j] != other.state[i][j]:
                    flag = False
                    break
            if flag == False:
                break
            
        return flag
    
def calculate_heuristic(node, end_node):
    hamming_distance = 0
    
    for i in range(0, size):
            for j in range(0, size):
                if node.state[i][j] != end_node.state[i][j]:
                    hamming_distance = hamming_distance + 1
                    
    return hamming_distance


def generate_children(parent, end_node):
   
    children = []
    
    parent_state = parent.state
    
    #Find the place of blank space (represented by 0)
    found = False
    
    for i in range(0, size):
        for j in range(0, size):
            if parent_state[i][j] == 0:
                row = i
                col = j
                found = True
                break
        
        if found == True:
            break
    
    if (row+1) >= 0 and (row+1) < size:
        
        child_state = copy.deepcopy(parent_state)
        
        temp = child_state[row][col]
        child_state[row][col] = child_state[row+1][col]
        child_state[row+1][col] = temp
        
        child = Node(child_state, parent)
        child.h = calculate_heuristic(child, end_node)
        
        children.append(child)
        
    if (row-1) >= 0 and (row-1) < size:
        
        child_state = copy.deepcopy(parent_state)
        
        temp = child_state[row][col]
        child_state[row][col] = child_state[row-1][col]
        child_state[row-1][col] = temp
        
        child = Node(child_state, parent)
        child.h = calculate_heuristic(child, end_node)
        
         
        children.append(child)
        
        
    if (col+1)>= 0 and (col+1) < size:
        
        child_state = copy.deepcopy(parent_state)
        
        temp = child_state[row][col]
        child_state[row][col] = child_state[row][col+1]
        child_state[row][col+1] = temp
        
        child = Node(child_state, parent)
        child.h = calculate_heuristic(child, end_node)
        
        children.append(child)
        
    if (col-1) >= 0 and (col-1) < size:
        
        child_state = copy.deepcopy(parent_state)
        
        temp = child_state[row][col]
        child_state[row][col] = child_state[row][col-1]
        child_state[row][col-1] = temp
        
        child = Node(child_state, parent)
        child.h = calculate_heuristic(child, end_node)
        
        children.append(child)
             
    return children
    
                
    

def BFS(start, end):
    
    #Create start and end state
    start_node = Node(start, None)
    end_node = Node(end, None)
    
    start_node.h = calculate_heuristic(start_node, end_node)
    
    
    
    #Initialize open and closed list
    open_list = []
    closed_list = []
    
    #Add start node to the open list
    open_list.append(start_node)
    
    
    #Loop until you find end
    while len(open_list) > 0:
        
        #Get current node from open list with minimum value of h
        current_node = open_list[0]
        current_index = 0
        
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
                path.append(current.state)
                current = current.parent
                
            return path[::-1]
        
        #Generate children
        children = generate_children(current_node, end_node)
        
        
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
    
    start = []
    end = []
    
    print("\nEnter start state:- ")
    for i in range(0, size):
        inner_list = []
        for j in range(0, size):
            inner_list.append(int(input("Enter "+str(i)+","+str(j)+":- ")))
        start.append(inner_list)
        
    
    print("\nEnter end state:- ")
    for i in range(0, size):
        inner_list = []
        for j in range(0, size):
            inner_list.append(int(input("Enter "+str(i)+","+str(j)+":- ")))
        end.append(inner_list)
        
    
    path = BFS(start,end)
    
    print("\nPath given by BFS:- ")
    
    if path is not None:
        for state in path:
            for row in state:
                print(str(row))
        
            print("**************\n")
    else:
        print(str(path))
        
    
    
if __name__ == "__main__":
    main()
        
        