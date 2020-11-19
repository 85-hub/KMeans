#!/usr/bin/env python3
# KMeansMapper.py

import sys
import linecache
import random
centerList = [[5.1,3.5,1.4,0.2], [4.9,3.0,1.4,0.2], [4.7,3.2,1.3,0.2]]




def distanceOfTwoProperty(property1, property2):
    temp = [(property1[i] - property2[i]) ** 2 for i in range(0, len(property1))]
    return sum(temp)

for line in sys.stdin:
    val = [float(i) for i in line.strip().split()]
    minDistance = distanceOfTwoProperty(val, centerList[0])
    minCenter = centerList[0]
    
    for i in range(1, len(centerList)):
        dist = distanceOfTwoProperty(val, centerList[i])
        if dist < minDistance:
            minCenter = centerList[i]
            minDistance = dist
    print('%s\t%s'%(minCenter, val))
        
# centerList = [[4.981818181818183, 3.4909090909090907, 1.4727272727272729, 0.21818181818181817], [5.545098039215685, 2.6705882352941175, 3.764705882352941, 1.16078431372549], [6.177272727272726, 3.257954545454547, 4.055681818181818, 1.3454545454545452]]
#每次运行后line7会被更新成center坐标