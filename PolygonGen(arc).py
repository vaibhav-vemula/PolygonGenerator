from functools import reduce
import operator
import math
import random
from shapely.geometry import Polygon
import csv


x=[]
y=[]


coords= []
with open('t1.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row['X'], row['Y'])
        x.append(row['X'])
        y.append(row['Y'])
        coords.append((float(row['X']),float(row['Y'])))
        # temp = '{'+ str(int(float(row['X'])))+','+ str(int(float(row['Y'])))+ '}'
        # coord.append(temp)


# print(coord[1:5])
random.shuffle(coords)
# print(coords)


center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
po = sorted(coords, key=lambda coord: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)

pa = Polygon(po)
print(pa.wkt)

# f = open("demo.txt", "w")
# f.write(pa.wkt)
# f.close()
