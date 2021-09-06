# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:17:24 2021

@author: user
"""

def triagArea(x1,y1,x2,y2,x3,y3):
        return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0)
    
def isInside(x1,y1,x2,y2,x3,y3,p1,p2):
    totalArea = triagArea(x1,y1,x2,y2,x3,y3);
    A1 = triagArea(x1,y1,x2,y2,p1,p2);
    A2 = triagArea(x1,y1,p1,p2,x3,y3);
    A3 = triagArea(p1,p2,x2,y2,x3,y3);
    if totalArea == A1 + A2 + A3:
        return 1
    return 0

def isInRect(x1,y1,d,p1,p2):
    return x1 < p1 and p1 < x1 + d and y1 < p2 and p2 < y1 + d

def readFile():
    file = open("data_centers_hard_input.txt")
    line0 = file.readline()
    line0 = line0[:-1]
    line0 = line0.split(" ")
    N = int(line0[0])
    Q = int(line0[1])
    centers = []
    for i in range(N):
        current = file.readline()
        current = current[:-1]
        current = current.split(" ")
        x,y = int(current[0]), int(current[1])
        centers.append((x,y))

    triags = []
    for j in range(Q):
        current = file.readline()
        current = current[:-1]
        current = current.split(" ")
        x,y,d = int(current[0]), int(current[1]), int(current[2])
        triags.append(((x+d,y),(x,y),(x,y+d)))

    output = open("hardOutput.txt", 'w')
    counter = 0;
    triCounter = 1;
    for triag in triags:
        for center in centers:
            if isInRect(triag[1][0], triag[1][1], triag[2][1]-triag[1][1], center[0],center[1]):
                counter += isInside(triag[0][0],
                                triag[0][1],
                                triag[1][0],
                                triag[1][1],
                                triag[2][0],
                                triag[2][1],
                                center[0],
                                center[1])
        output.write(str(counter)+"\n")
        counter = 0;
        print(triCounter)
        triCounter += 1
    
    
if __name__ == "__main__":
    readFile()
    