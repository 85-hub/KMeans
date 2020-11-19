#!/usr/bin/env python3
#KMeansReducer.py

import sys

(last_Center, sumOfProperty) = ([], [])
sizeOfSameCenter = 0
#[5.1, 3.5, 1.4, 0.2]	[5.4, 3.9, 1.7, 0.4]
for line in sys.stdin:
    (center, p) = line.strip('[] \n').split("\t")#center=   5.1, 3.5, 1.4, 0.2]
    # print(center)
    # print(p)
    p = [float(i) for i in p.strip('[] ').split(',')]#p=[5.4, 3.9, 1.7, 0.4]
    # print(p)
    if last_Center and last_Center != center:
        avgProperty = [i / sizeOfSameCenter for i in sumOfProperty]
        print('%s'%(avgProperty), end = ', ')

        (last_Center, sumOfProperty) = (center, p)
        sizeOfSameCenter = 1
    elif not(last_Center):
        sumOfProperty = [float(i) for i in center.strip('[] ').split(',')]
        # print(sumOfProperty)#[5.1, 3.5, 1.4, 0.2]
        last_Center = center
        sumOfProperty =  [(sumOfProperty[i] + p[i]) for i in range(0, len(p))]
        # print(sumOfProperty)
        sizeOfSameCenter = sizeOfSameCenter + 1
        # print(sizeOfSameCenter)
    else:
        sumOfProperty =  [(sumOfProperty[i] + p[i]) for i in range(0, len(p))]
        sizeOfSameCenter = sizeOfSameCenter + 1

avgProperty = [i / sizeOfSameCenter for i in sumOfProperty]
print(avgProperty)
