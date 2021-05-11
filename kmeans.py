#%%
"""for states"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

import json
import random

f = open('states.json')
data = json.load(f)

a = data['New Jersey']['Coordinates']
x1=[]
y1 = []
output = []
for i in a:
    output.append((i['lat'], i['lng']))
    x1.append(i['lat'])
    y1.append(i['lng'])
print(output)
plt.scatter(x1,y1, c='b')
plt.show()

#%%
"""for random polygon"""
import math, random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def generatePolygon( ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts ) :

    irregularity = clip( irregularity, 0,1 ) * 2*math.pi / numVerts
    spikeyness = clip( spikeyness, 0,1 ) * aveRadius

    # generate n angle steps
    angleSteps = []
    lower = (2*math.pi / numVerts) - irregularity
    upper = (2*math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts) :
        tmp = random.uniform(lower, upper)
        angleSteps.append( tmp )
        sum = sum + tmp

    # normalize the steps so that point 0 and point n+1 are the same
    k = sum / (2*math.pi)
    for i in range(numVerts) :
        angleSteps[i] = angleSteps[i] / k

    # now generate the points
    points = []
    angle = random.uniform(0, 2*math.pi)
    for i in range(numVerts) :
        r_i = clip( random.gauss(aveRadius, spikeyness), 0, 2*aveRadius )
        x =  ctrX + r_i*math.cos(angle)
        y = ctrY + r_i*math.sin(angle)
        points.append( (int(x),int(y)) )

        angle = angle + angleSteps[i]

    return points

def clip(x, min, max) :
    if( min > max ) :  return x    
    elif( x < min ) :  return min
    elif( x > max ) :  return max
    else :             return x


verts = generatePolygon( ctrX=100, ctrY=100, aveRadius=200, irregularity=1, spikeyness=0.11, numVerts=20 )
output = verts
pa = Polygon(verts)
print(pa.wkt)

# %%
from shapely.geometry import Polygon, Point
def random_points_within(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds

    points = []

    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)

    return points
# %%
p = random_points_within(Polygon(output), 50000)
points=[]
x_point = []
y_point = []
for i in p:
    points.append([i.x, i.y])
    x_point.append(i.x)
    y_point.append(i.y)
points = np.array(points)
# %%
plt.scatter(x_point,y_point, c='b')
plt.show()
# %%
from sklearn.decomposition import PCA
kmeans = KMeans(n_clusters=8, random_state=0).fit(points)
label = kmeans.fit_predict(points)

pca = PCA(2)
df = pca.fit_transform(points)
filtered_label0 = df[label == 0]
filtered_label1 = df[label == 1]
#filter rows of original data
filtered_label2 = df[label == 2]
filtered_label3 = df[label == 3]
filtered_label4 = df[label == 4]
filtered_label5 = df[label == 5]
filtered_label6 = df[label == 6]
filtered_label7 = df[label == 7]
#Plotting the results
plt.scatter(filtered_label0[:,0] , filtered_label0[:,1])
plt.scatter(filtered_label1[:,0] , filtered_label1[:,1] , color = 'brown')
plt.scatter(filtered_label2[:,0] , filtered_label2[:,1] , color = 'green')
plt.scatter(filtered_label3[:,0] , filtered_label3[:,1] , color = 'yellow')
plt.scatter(filtered_label4[:,0] , filtered_label4[:,1] , color = 'pink')
plt.scatter(filtered_label5[:,0] , filtered_label5[:,1] , color = 'blue')
plt.scatter(filtered_label6[:,0] , filtered_label6[:,1] , color = 'orange')
plt.scatter(filtered_label7[:,0] , filtered_label7[:,1] , color = 'gray')
plt.show()
