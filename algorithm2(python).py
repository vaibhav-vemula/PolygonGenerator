import math, random
from shapely.geometry import Polygon
f = open("poooo.txt", "w")
f.write('wkt\n')
def generatePolygon( ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts ) :

    irregularity =  irregularity * 2*math.pi / numVerts
    spikeyness = spikeyness * aveRadius

    angleSteps = []
    lower = (2*math.pi / numVerts) - irregularity
    upper = (2*math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts) :
        tmp = random.uniform(lower, upper)
        angleSteps.append( tmp )
        sum = sum + tmp

    k = sum / (2*math.pi)
    for i in range(numVerts) :
        angleSteps[i] = angleSteps[i] / k

    points = []
    angle = random.uniform(0, 2*math.pi)
    for i in range(numVerts) :
        r_i =  random.gauss(aveRadius, spikeyness)
        x =  ctrX + r_i*math.cos(angle)
        y = ctrY + r_i*math.sin(angle)
        # points.append( (int(x),int(y)) )
        points.append( [int(x),int(y)] )

        angle = angle + angleSteps[i]

    return points

for  i  in range(1000):
    
    verts = generatePolygon( ctrX=100, ctrY=100, aveRadius=200, irregularity=1, spikeyness=0.11, numVerts=random.randint(10,500) )
    # print(verts)
    pa = Polygon(verts)
    f.write(pa.wkt)
    f.write('\n')
    
    # print(pa.wkt)
    # print(verts)