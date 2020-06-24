"""
Created on Sat Oct 26 03:47:03 2019

@author: Aditya Mahajan
"""

class Node: #Node class 
    
    g = 0
    f = 0
    
    def __init__(self, index, h, parent=None):
        self.index = index
        self.parent = parent
        
        self.h = h
    
    def __eq__(self, other):
        return self.index == other.index
    


def astar(adj_matrix, path_costs,heuristic_values, start, end):
    
    #Create Start Node and End Node
    start_node = Node(start, heuristic_values[start], None)
    start_node.f = start_node.g + start_node.h
    
    end_node = Node(end, heuristic_values[end], None)
    
    #Initialize open and closed list
    open_list = []
    closed_list = []
    
    #Add start node to open list
    open_list.append(start_node)
    
    #Loop until you find end
    while len(open_list) > 0:
        
        #Get current node which is the node with smallest f value in open list
        current_node = open_list[0]
        current_index = 0
                
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index
      
        #Remove that node from the open list and add it closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        #Check if current node is end node, if yes return path by back tracking
        if current_node == end_node:
            print("\n**** End node reached*****")
            
            
            path = []
            
            current = current_node
            while current is not None:
                path.append(current.index)
                current = current.parent
            
            return path[::-1]  #return reverse of path
        
        #Generate Children
        children = []
        
        for index, i in enumerate(adj_matrix[current_node.index]):
            if i == 1:
                child = Node(index, heuristic_values[index], current_node)
                children.append(child)
            
        #Loop through children
        for child in children:
            
            #if child is already in closed list, ignore
            flag = False
            
            for closed_node in closed_list:
                if child == closed_node:
                    flag = True
                    break
            
            if flag == True:
                continue
            
            #Calculate g and f values for child
            child.g = current_node.g + path_costs[current_node.index][child.index]
            child.f = child.g + child.h
            
            #if child is in open list and has higer f value, ignore
            flag = False
            
            for open_node in open_list:
                if child == open_node and child.f > open_node.f:
                    flag = True
                    break
                
            if flag == True:
                continue
            
            #Append the child to open list
            open_list.append(child)
            

def main():
    
    num_nodes = int(input("Enter number of nodes:- "))
    
    adj_matrix = []
    path_costs = []
    heuristic_values = []
    
    print("\n***** Enter Adjacency Matrix:- *******")
    for i in range(0,num_nodes):
        inner_list = []
        
        for j in range(0,num_nodes):
            inner_list.append(int(input("Enter "+str(i)+","+str(j)+": ")))
        
        adj_matrix.append(inner_list)
        
    print("\nAdjacency Matrix:- \n"+str(adj_matrix))
        
    print("\n***** Enter path costs:- *****")
    for i in range(0,num_nodes):
        inner_list = []
        
        for j in range(0, num_nodes):
            if adj_matrix[i][j] == 1:
                cost = int(input("Enter cost of path from "+str(i)+" to "+str(j)+":- "))
            else:
                cost = 9999
                
            inner_list.append(cost)
        
        path_costs.append(inner_list)
        
    print("\n***** Enter heuristic values:- *****")
    for i in range(0,num_nodes):
        heuristic_values.append(int(input("Enter value for node "+str(i)+":- ")))
            
    
    start = int(input("\nEnter start node index:- "))
    end = int(input("\nEnter end node index:- "))
    
    
    path = astar(adj_matrix, path_costs,heuristic_values, start, end)
    
    
    print("\nPath given by A*:- "+str(path))
    
        
if __name__ == "__main__":
    main()
        