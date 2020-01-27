# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:19:06 2020

@author: Kam Look
"""
def computeBFStree(AdjTable, v_start):
    '''
    nodes must be numbered the same way it is indexed (i.e has node labeled 0)
    
    CURRENT BUGS:
        Adding all seen adjacent nodes to the parent, not just ones from the direct previous layer
        Not reading proper nodes on later nodes 
            (like 7, some thing about order of seeing a node and not processing it 
            it is only seeing 3 and not 5?)
    '''
    #AdjTable is a list of lists describing the array
    #v_start is the starting vertex
    #parent is output vector 
    queue=[]
    seen=[]
    #initialize a list of lists
    parent=[[] for i in range(len(AdjTable))]
    #soring layer number so only nodes from the directly previous layer are added to the parent
    layer_number=[0]*len(AdjTable)
    parent[v_start]=[v_start]
    #ensure starting is the lowest layer
    layer_number[v_start]=-1
    queue.append(v_start)
    while queue != []:
        current=queue.pop(0)
        print('queue is: ', queue)
        #begin checking if node in queue has been discovered before
        if current not in seen:
            seen.append(current)
            print('WORKING ON NODE: ',current, '     seen is: ', seen)
            #node is not seen before, so lets buils a parent for it 
            #parent can only contain modes we have already scene
            for adjacent in AdjTable[current]:
                if adjacent in seen:
                    #some how check for prev layer only?
                    #if adjacent in seen and adjacent in prev_layer:
                    print('Adjacent to current: ', AdjTable[current])
                    parent[current].append([adjacent])
                    print('adding adj: ', adjacent, '      to parent: ', parent[current], '\n')
            #add adjacents of the current into the queue
            for unseen in AdjTable[current]:
                if unseen not in seen:
                    queue.append(unseen)
    return parent


#pratice table adjTable
ezAdjTable= [[1],[0,2,4],[1,3],[2],[1]]
AdjTable= [[1, 2, 3, 4],[0,2,6],[0,1,3],[0,2,4,7],[0,3,5,7],[4,6,7],[1,5],[3,5]]
#AdjTable= [[1, 2, 3, 4, 5],[1,3,7],[2,4],[1,3,5,8],[1,4,6,8],[5,7,8],[2,6],[4,6]]
