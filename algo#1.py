import random
from shapely.geometry import Polygon
import sys

sys.setrecursionlimit(10**9)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def swap(p,q):
    p.x,q.x = q.x,p.x
    p.y,q.y = q.y,p.y

def dist(p1,p2):
    return (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y)

def orientation(p,q,r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def compare(a,b,p0):
    
    o= orientation(p0,a,b)
    if (o==0):
        if (dist(p0, b) >= dist(p0, a)):
            return -1
        else:
            return 1

    if(o==2):
        return -1
    else:
        return 1


def distribute(bins,L,fn):
      for item in L:
          
          bins[fn(item)].append(item)

def qsort(L, p0):
    if len(L)<2: return L
    p = random.choice(L)
    bins = {-1:[],1:[]}
    distribute(bins,L, lambda x: compare(x,p,p0) )
    return qsort(bins[-1],p0)+qsort(bins[1],p0)

# def qsort(myList,p0):
#     if len(myList) < 2:
#         return myList
#     else:
        
#         p = random.choice(myList)
#         lesser = qsort([x for x in myList[1:] if compare(x,p,p0)==-1],p0)
#         greater = qsort([x for x in myList[1:] if compare(x,p,p0)==1],p0)
#         myList = lesser + greater
#         return myList

def printClosedPath(points,n):
    ymin = points[0].y
    min = 0

    for i in range(1,n):
        y = points[i].y

        if (y < ymin) or (ymin == y and (points[i].x < points[min].x)):
            ymin = points[i].y
            min = i

    swap(points[0],points[min])
    p0 = points[0]
    
    xyz = qsort(points[1:],p0)

    a.append((p0.x,p0.y))
    

    for i in range(len(xyz)):
        a.append((xyz[i].x,xyz[i].y))

    return a



a=[]
points = []
# points.append(Point(12, 29))
# points.append(Point(23, 29))
# points.append(Point(19, 36))
# points.append(Point(18, 29))
# points.append(Point(13, 35))
# points.append(Point(7, 27))

trial = []
for i in range (40):
    # if i == 0:
    #     x=random.randint(-10, 1090)
    #     y=random.randint(-10, 1070)
    #     trial.append((x, y))
    #     points.append(Point(x, y))
    # else:
    x = random.randint(-10, 1990)
    y = random.randint(-10, 1090)
    trial.append((x, y))
    points.append(Point(x, y))
    
#print("trial ", trial)
# points.append(Point(19, 28))
# points.append(Point(17, 34))
# points.append(Point(10, 33))
# points.append(Point(8, 28))
# points.append(Point(14, 28))


xxx = printClosedPath(points,len(points))

pa = Polygon(xxx)
print(pa.wkt)

#%%
def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m


slop = slope(780, 1036, 760, 582)
print(slop)

# 715 328, 1045 1036, 760 582

