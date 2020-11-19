#!/usr/bin/env python3
# visualization.py

import sys
import matplotlib.pyplot as plt
import numpy as np




centerList = [[5.108163265306123, 3.487755102040816, 1.493877551020408, 0.24897959183673457], [5.883606557377049, 2.7409836065573776, 4.388524590163934, 1.4344262295081964], [6.853846153846154, 3.076923076923076, 5.715384615384614, 2.0538461538461537]	]

centerLoc=[]
point=[]



def distanceOfTwoProperty(property1, property2):
    temp = [(property1[i] - property2[i]) ** 2 for i in range(0, len(property1))]
    return sum(temp)


for line in sys.stdin:
    val = [float(i) for i in line.strip().split()]
    minDistance = distanceOfTwoProperty(val, centerList[0])
    minCenter = centerList[0]
    id=0

    for i in range(1, len(centerList)):
        dist = distanceOfTwoProperty(val, centerList[i])
        if dist < minDistance:
            minCenter = centerList[i]
            id = i
            minDistance = dist
    centerLoc.append(id)
    point.append(val)

print(centerLoc)
print(point)

x0, x1, x2 = [], [], []
for i in range(150):
    if centerLoc[i] == 0:
        plt.scatter(point[i][0], point[i][1], c = "red", marker='o')
    elif centerLoc[i] == 1:
        plt.scatter(point[i][0], point[i][1], c="green", marker='*')
    else:
        plt.scatter(point[i][0], point[i][1], c="blue", marker='+')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend(loc=2)
plt.show()



# centerList = [[4.981818181818183, 3.4909090909090907, 1.4727272727272729, 0.21818181818181817], [5.545098039215685, 2.6705882352941175, 3.764705882352941, 1.16078431372549], [6.177272727272726, 3.257954545454547, 4.055681818181818, 1.3454545454545452]]
# 每次运行后line7会被更新成center坐标