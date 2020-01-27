#Kam Look, A13798549
'''Homework 2'''

#create functions. Example computations carried out at the end of the script

from matplotlib.path import Path

def computeDistancePointToSegment(q,p1,p2):
    '''
    How to implement function:
        
    First we do everthing we did before in computeDistancePointToLine(q,p1,p2)
    Then we compute distances from q to p1 and q to p2
    
    Lastly we perform checks to see if the intersect of the q line and the line 
    containing p1 and p2 is on the segment, closer to p1, or closer to p2. 
    '''
    if type(p1)!= list or type(p2) != list or type(q) != list: return print("Invalid type: Arguments must be lists")
    if len(p1) !=2 or len(p2) !=2 or len(q)!=2:return print ('Invalid argument length; each argument must have 2 values')
    if p1==p2: return print('Infinite possible solutions')
    if p1[0]==p2[0]: 
        distance=abs(p1[0]-q[0])
        print('Segment is a vertical line')
        print('Distance Approximate')
        w=None
        return distance,w
    if p1[1]==p2[1]:
        distance = abs(p1[1]-q[1])
        print('Segment is a horizontal line')
        print('Distance Approximate')
        w=None
        return distance,w
    
    
    slope=(p2[1]-p1[1])/(p2[0]-p1[0]) #solve for the slope of the line 
    yInt= p1[1] - slope*p1[0] #solve for y intercept
    qSlope= -1/slope
    qYInt= q[1] - qSlope *q[1]
    
    xShared= (qYInt - yInt)/(slope - qSlope)
    yShared= slope*xShared + yInt
    
    distance=((xShared - q[0])**2 + (yShared - q[1])**2)**0.5
    dToP1 =((p1[0]-q[0])**2 + (p1[1]-q[1])**2)**0.5 
    dToP2= ((p2[0]-q[0])**2 + (p2[1]-q[1])**2)**0.5 
    
    if xShared>p1[0] and xShared<p2[0] or xShared<p1[0] and xShared>p2[0]:
        d=distance
        w=0
        return d,w
    elif dToP1 > dToP2:
        d = dToP2
        w = 2
        return d,w
    else:
        d =dToP1
        w=1
        return d,w
################## NEW PROGRAM ############################         
def computeDistancePointToPolygon(P,q):
    '''
    How to use function:
        Iterate the computeDistancePointToSegment function from before over
        every vertex in the polygon to find all the distances to each segment.
        
        Update the distance value as shorter distances are measured.
    '''
    if type(P) != list or type(q) != list: return print("Invalid type: Arguments must be lists")
    dist = float('inf')
    for vert in range(0,len(P)):
        d,w=computeDistancePointToSegment(q,P[vert-1],P[vert])
        if d < dist:
            dist=d
    return dist

def computeTangentVectorToPolygon(P,q):
    '''
    How to implement fucntion:
        
        First use matplotlib library to check if the point exists within the polygon.
        
        Next we use a mehtod similar to that in computeDistancePointToPolygon,
        we iterate the computeDistancePointToSegment to find the shortest distance and 
        also save the w case of the shortest distance found. 
        
        Lastly we then find the vector parallel to the line segment if the closest 
        piece of the polygon is a line segment and a vector perpendicular to the
        vector from q to polygonVerex if the closest point is a vertex.
    '''
    dist=float('inf')
    path=Path(P)
    wShort=9 #initializing value to be replaced
    inside=path.contains_point(q)
    if inside:
        return print('Cannot find tangent line, point is inside the polygon')
    else:
        for vert in range(0,len(P)):
            d,w=computeDistancePointToSegment(q,P[vert-1], P[vert])
            if d < dist:
                dist = d
                wShort=w
                p1=P[vert-1]
                p2=P[vert]
        if wShort == 0:
            #get equation for vector parallel to
            u = [p2[0]-p1[0],p2[1]-p1[1]]
            u = [u[0]/(u[0]**2+u[1]**2)**0.5, u[1]/(u[0]**2+u[1]**2)**0.5]
            return u
        elif wShort == 1:
            circleRad = [q[0]-p2[0],q[1]-p2[1]]
            y= -circleRad[0]/circleRad[1]
            u=[1,y]
            u = [u[0]/(u[0]**2+u[1]**2)**0.5, u[1]/(u[0]**2+u[1]**2)**0.5]
            return u
        elif wShort == 2:
            circleRad = [q[0]-p1[0],q[1]-p1[1]]
            y= -circleRad[0]/circleRad[1]
            u=[1,y]
            u=[u[0]/(u[0]**2+u[1]**2)**0.5, u[1]/(u[0]**2+u[1]**2)**0.5]
            return u 
        else:
            print('Error: No valid case met')
            
#Test Cases
P=[[1,1],[2,2],[1,3],[0,2]]
q=[6,6]
qInner=[1,2]

distance=computeDistancePointToPolygon(P,q)
print('distance:', distance)
u=computeTangentVectorToPolygon(P,q)
print('u:',u)
computeTangentVectorToPolygon(P,qInner)




