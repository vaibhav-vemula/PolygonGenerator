import math, random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pandas as pd
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def genPolygon( X, Y, radius, irregular, spike, n) :

    irregular = irregular* 2*math.pi / n
    spike = spike * radius

    # generate n angle between the random limits
    angles = []
    low = (2*math.pi / n) - irregular
    high = (2*math.pi / n) + irregular

    for i in range(n) :
        temp = random.uniform(low, high)
        angles.append( temp )

    #adding first vertice to end of list to make a closed polygon.
    angles.append(angles[0])
    
    #generating points
    points = []
    angle = random.uniform(0, 2 * math.pi)
    for i in range(n) :
        r_i = random.gauss(radius, spike)
        x =  X + r_i*math.cos(angle)
        y = Y + r_i*math.sin(angle)
        points.append((x,y))
        angle = angle + angles[i]

    return points

verts = genPolygon( X=50, Y=100, radius=400, irregular=0.2, spike=0.03, n=100 )
pa = Polygon(verts)
print(pa.wkt)
