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
    if type(adj_table) != list:return print('Error: first input must be an adjacency table (list)')
    if type(starting_val) != int: return print('Error: starting node must be defined as an interger')
    
    
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
                parent[right_val] = append_list
        #move layers along the list
        left_pointer+=1
        right_pointer+=1
    return parent


def computeBFSpath(adj_table,starting_val,goal_val):
    #path goes from goal to start
    path=[goal_val]
    #build connection betwee parents
    parent_list=computeBFSTree(adj_table,starting_val)
    while path[-1] != starting_val:
        furthest_node=path[-1]
        #take first parent, since any path will be sufficient as an output
        path.append(parent_list[furthest_node][0])
    return path


adj_table = [[1,2,3,4],[0,2,6],[0,1,3],[0,2,4,7],[0,3,5,7],[4,6,7],[1,5],[3,5]]
starting_node = 0
print(computeBFSTree(adj_table, starting_node))

goal_node = 7
print(computeBFSpath(adj_table,starting_node,goal_node))
