#Kam Look, A13798549
'''Homework 1'''

#create functions. Example computations carried out at the end of the script
def computeLineThroughTwoPoints(p1,p2):
    '''
    How to implement function:
    First we check for cases to make sure arguments are in the  right format
    and are not exceptions.
    
    Then we solve for slope anf the y intercept and move it into the desired form 
    of ax+by+c=0
    
    Lastly, we normalize the values by dividing by the squareroot of the sum of 
    a and b so a^2 + b^2 = 1
    '''
    if type(p1)!= list or type(p2) != list: return print("Invalid type: Arguments must be lists")
    if len(p1) !=2 or len(p2) !=2:return print ('Invalid argument length; each argument must have 2 values')
    if p1==p2: return print('Infinite possible solutions')
    if p1[0]==p2[0]: return print('Vertical line with a slope of infinity. x -',p1[0],'= 0')
    
    slope=(p2[1]-p1[1])/(p2[0]-p1[0]) #solve for the slope of the line 
    yInt= p1[1] - slope*p1[0] #solve for y intercept
    coeff = [-slope, 1, -yInt] #rearrange values from slope intercept form in 
    #desired format for the project 
    divNorm = (coeff[0]**2 + coeff[1]**2)**0.5
    a = coeff[0]/divNorm
    b = coeff[1]/divNorm
    c= coeff[2]/divNorm
    return a, b, c


def computeDistancePointToLine(q,p1,p2):
    '''
    How to implement function:
    First we check for cases to make sure arguments are in the  right format
    and are not exceptions.
    
    Then we solve for slope anf the y intercept of line containing p1 and p2.
    Next we solve for a line with a perpendicular slope to the line with p1 and p2
    that also contains point q
    
    Lastly, we solve for the distance from the intersection of these two lines and q
    by using the pythagorean theorem
    '''
    if type(p1)!= list or type(p2) != list or type(q) != list: return print("Invalid type: Arguments must be lists")
    if len(p1) !=2 or len(p2) !=2 or len(q)!=2:return print ('Invalid argument length; each argument must have 2 values')
    if p1==p2: return print('Infinite possible solutions')
    if p1[0]==p2[0]: 
        distance=abs(p1[0]-q[0])
        return distance
    
    
    slope=(p2[1]-p1[1])/(p2[0]-p1[0]) #solve for the slope of the line 
    yInt= p1[1] - slope*p1[0] #solve for y intercept
    qSlope= -1/slope
    qYInt= q[1] - qSlope *q[0]
    
    xShared= (qYInt - yInt)/(slope - qSlope)
    yShared= slope*xShared + yInt
    
    distance=((xShared - q[0])**2 + (yShared - q[1])**2)**0.5
    
    return distance

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
        return distance
    
    
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
         

p1=[1,1]
p2 = [2,2]
q=[3,4]
print('p1: ', p1)
print('p2: ', p2)
print('q: ', q)
a,b,c=computeLineThroughTwoPoints(p1,p2)
print('a: ', a ,', b: ', b , ', c: ', c)
distance= computeDistancePointToLine(q,p1,p2)
print('distance: ', distance)
d,w= computeDistancePointToSegment(q,p1,p2)
print('distance:', d, ' w= ',w)



