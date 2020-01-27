# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:18:30 2020

@author: Kam Look, A13798549

E 2.9
"""

def classifyVerts(workspace, obstacles): 
    #obstacles is a list of obstacles, each one a list of vertices.
    #each point in the obstacle in a list of length 2, [x,y]
    vTypeArray=[None]*size(obstacles)
    for o in range(0,obstacles):
        polygon=obstacles(o)
        vTypeArray[o]=[None]*len(polygon)
        for v in range(0,polygon):
            if v==1:
                pre=polygon[-1]
                testing=polygon[0]
                post=polygon[1]
            elif v==len(polygon):
                pre=polygon[v-1]
                testing=polygon[v]
                post=polygon[0]
            else:
                pre=polygon[v-1]
                testing=polygon[v]
                post=polygon[v+1]
            determineEndpointType(pre,testing,post)
            vTypeArray[o][v]=determineConvexity(pre,testing,post,case)
            return vTypeArray
            
            


def determineEndpointType(pre,testing,post):
    preX=pre[0]
    testingX=testing[0]
    postX=post[0]
    case=''
    if preX < testingX and postX < testingX:
        case='LL'
        return case
    elif preX > testingX and postX > testingX:
        case = 'RR'
        return
    elif preX > testingX and postX < testingX or preX < testingX and postX > testingX:
        case = 'LR'
        return
    else:
        return 0, print('Error: no valid cases met')

def determineConvexity(pre,testing,post,case):
    vector1= [pre[0]-testing[0],pre[1]-testing[1]]
    vector2= [post[0]-testing[0],post[1]-testing[1]]
    acuteAngle= acos(dot(vector1,vector2)/dot(abs(vector1),abs(vector2)))
    intAngle=0
    if post[1] > pre[1]:
        intAngle=acuteAngle
    else:
        intAngle=2*pi-acuteAngle
    
    if case == 'LL':
        if intAngle =< pi:
            return 1
        else:
            return 2
    elif case == 'RR':
        if intAngle =< pi:
            return 3
        else:
            return 4
    elif case == 'LR':
        if intAngle =< pi:
            return 5
        else:
            return 6
        
    
    
    
    
    