#Kam Look, A13798549
#MAE 145, Homework 3

def computeBFSTree(adj_table, starting_val):
    '''
    The function simply takes and in an adjacency table and a starting point.
    the function is broken down into two major sections:
        In the first section, we build an array named 'layers' which describes the
        layers of the graph that are cascading out from the starting point
        
        In the next section, we use a two pointer technique to iterate through
        the array and check whether the nodes in the previous layer are adjacent
        to the nodes in the current layer


    '''
    #type checks for the input
    if type(adj_table) != list:return print('Error: first input must be an adjacency table (list of lists)')
    if type(starting_val) != int: return print('Error: starting node must be defined as an interger')
    for typecheckList in adj_table:
        if type(typecheckList) != list: return print('Error: first input must be an adjacency table (list of lists)')
        for nodeCheck in typecheckList:
            if type(nodeCheck) != int: return print('Error: all nodes must be intergers')
            
            
        
    #First loop just defines the layers for the graph, going out from the starting 
    
    layers = [[starting_val]]
    #{} indicate set, only unique values can be added
    seen_nodes = {starting_val,}
    while len(seen_nodes) != len(adj_table):
        previous_layer = layers[-1]
        #print('previous layer: ', previous_layer)
        current_layer = []
        for layer in previous_layer:
            possible_vals_in_layer = adj_table[layer]
            #.extend concatenates the two lists
            #all nodes adjacent to the previous layer are now part of the current layer
            current_layer.extend(possible_vals_in_layer)
            
        append_list = []
        continue_layering = False
        #check if nodes in this new layer have already wbeen seen before
        #therefore, are they already stored in a subsequent layer
        for node in current_layer:
            #A new node has been found and we add it to the seen nodes as well
            #we also prepare a new list (append_list) that will be added as a layer to layers
            if node not in seen_nodes: 
                append_list.append(node)
                #this is not the last layer, we want to keep searching so reset 
                #the search to True
                continue_layering = True
                seen_nodes.add(node)
        if continue_layering:
            #add layer, then go to the top of the while loop to look for more layers
            layers.append(append_list)
    
    #Begin adding filling the parent list 
    #Two pointer technique, used to iterate through an array 
    parent = [None]*len(adj_table)
    left_pointer = -1
    right_pointer = 0
    while(right_pointer < len(layers)):
        #initialize the parent of the starting point
        if left_pointer < 0:
            for val in layers[right_pointer]:
                parent[val] = layers[right_pointer]
        else:
            for right_val in layers[right_pointer]:
                append_list = []
                for left_val in layers[left_pointer]:
                    #check if prev_layer (left_val) is in adjacent nodes for
                    #the current layer (right_val)
                    if left_val in adj_table[right_val]:
                        #append_list is the parents of the node in the right_val
                        #(aka current) layer
                        append_list.append(left_val)
                mm=parent[right_val] = append_list
        #move layers along the list
        left_pointer+=1
        right_pointer+=1
    return parent


def computeBFSpath(adj_table,starting_val,goal_val):
    '''
    computeBFSpath uses computeBFSTree to list of how parent nodes are connected.
    Then we work backward from the goal to the start to construct a path from 
    node to node, moving from the goal to the starting node rooting 
            the graph.
    '''
    #path goes from goal to start
    path=[goal_val]
    #build connection betwee parents
    parent_list=computeBFSTree(adj_table,starting_val)
    while path[0] != starting_val:
        furthest_node=path[0]
        #take first parent, since any path will be sufficient as an output
        path.insert(0,parent_list[furthest_node][0])
    return path


adj_table = [[1,2,3,4],[0,2,6],[0,1,3],[0,2,4,7],[0,3,5,7],[4,6,7],[1,5],[3,5]]
starting_node = 0
print('Parent test 1: ',computeBFSTree(adj_table, starting_node))

goal_node = 7
print('Path test 1: ', computeBFSpath(adj_table,starting_node,goal_node))

multiple_parents=[[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]

print('Parent test 2: ', computeBFSTree(multiple_parents, starting_node))
goal_node2= 8
print('Path test 2: ', computeBFSpath(multiple_parents,starting_node,goal_node2))

adj_Given = [[1, 5], \
            [0, 2, 6], \
            [1, 3, 7], \
            [2, 4, 8], \
            [3, 9], \
            [0, 6, 10], \
            [1, 5, 7], \
            [2, 6, 8], \
            [3, 7, 9], \
            [4, 8, 11], \
            [5, 12], \
            [9, 13], \
            [10, 14], \
            [11, 16], \
            [12, 15, 17], \
            [14, 18], \
            [13, 19], \
            [14, 18, 20], \
            [15, 17, 21], \
            [16, 24], \
            [17, 21, 25], \
            [18, 20, 22], \
            [21, 23], \
            [22, 24], \
            [19, 23, 26], \
            [20, 27], \
            [24, 31], \
            [25, 28], \
            [27, 29], \
            [28, 30], \
            [29, 31], \
            [26, 30]]

start_given=0
print('Given Parent test: ', computeBFSTree(adj_Given, start_given))
goal_node_given=31
print('Given Path test: ', computeBFSpath(adj_Given,starting_node,goal_node_given))

