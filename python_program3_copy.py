# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:19:06 2020

@author: Kam Look
"""
import time
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
    seen=[v_start] #archive layer in flowchart
    #initialize a list of lists
    parent=[[] for i in range(len(AdjTable))]
    #soring layer number so only nodes from the directly previous layer are added to the parent
    prev_layer=[]
    working_layer=[v_start]
    parent[v_start]=[v_start]
    #Boolean to decide whether we are done working on the current layer
    
    while len(seen) != len(AdjTable):
        for workingNode in working_layer:
            print('Working Node: ', workingNode)
            for adjWorkingNode in range(len(AdjTable[workingNode])):
                print('adjWorkingNode: ', adjWorkingNode)
                print('seen: ', seen)
                newNode=AdjTable[workingNode][adjWorkingNode]
                time.sleep(5)
                for newAdj in AdjTable[newNode]:
                    if newAdj in seen and newAdj not in parent[newNode]:
                        parent[newNode].append(newAdj)
                        print('parent: ', parent)
        #done with current working nodes, now update the working layer
        for updateWorkingLayer in 
                    #return print('reached parent loop')
        #done with working nodes redefine working layer and update seen list
        

    
    '''
    #AdjTable is a list of lists describing the array
    #v_start is the starting vertex
    #parent is output vector 
    queue=[]
    seen=[] #archive layer in flowchart
    #initialize a list of lists
    parent=[[] for i in range(len(AdjTable))]
    #soring layer number so only nodes from the directly previous layer are added to the parent
    prev_layer=[]
    working_layer=[v_start]
    parent[v_start]=[v_start]
    #Boolean to decide whether we are done working on the current layer
    workingMapped=True
    #ensure starting is the lowest layer
    while len(seen) != len(AdjTable):
        if prev_layer == [] or workingMapped:
            prev_layer = working_layer
            for archiving in prev_layer:
                #print('Seen: ', seen)
                if archiving not in seen:
                    seen.append(archiving)
            working_layer =[]
            workingMapped = False
            for adjChecks in prev_layer:
                #print('prev layer check: ', prev_layer)
                for adjScrub in AdjTable[adjChecks]:
                    if AdjTable[adjScrub] not in seen and AdjTable[adjScrub] not in working_layer:
                        working_layer.append(adjScrub)
            #now we should finally have a working layer ready and can begin finding their parents
            #print('Working layer is: ', working_layer)
        
        for child in working_layer:
            print('\n Working Child: ', child)
            for parentBuilding in AdjTable[child]:
                print('AdjTable[child]: ', AdjTable[child])
                print('parentBuilding: ', parentBuilding)
                print('In parent building loop: ',AdjTable[parentBuilding])
                if AdjTable[parentBuilding] in prev_layer and AdjTable[parentBuilding] not in seen and AdjTable[parentBuilding] not in parent:
                    parent[child].append[AdjTable[parentBuilding]]
                    print('Parent: ', parent)
        workingMapped= True
    return parent
'''
    

#pratice table adjTable
ezAdjTable= [[1],[0,2,4],[1,3],[2],[1]]
AdjTable= [[1, 2, 3, 4],[0,2,6],[0,1,3],[0,2,4,7],[0,3,5,7],[4,6,7],[1,5],[3,5]]
#AdjTable= [[1, 2, 3, 4, 5],[1,3,7],[2,4],[1,3,5,8],[1,4,6,8],[5,7,8],[2,6],[4,6]]
