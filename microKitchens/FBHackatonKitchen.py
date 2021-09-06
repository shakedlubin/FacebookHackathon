# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:14:35 2021

@author: user
"""

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def readFile():
    file = open("micro_kitchens_easy_input.txt")
    line0 = file.readline()
    line0 = line0[:-1]
    line0 = line0.split(" ")
    w = int(line0[0])
    h = int(line0[1])
    #n = int(line0[2])
    
    circles = []
    
    for i in range(w):
        line = file.readline().split(" ")
        for j in range(h):
            if line[j] == 'o' or line[j] == 'o\n':
                circles.append((i,j))
                                
    sumCur = 0;
    minI = 0;
    minJ = 0;
    minDist = float('inf')
    
    for i in range(w):
        for j in range(h):
            for t in circles:
                sumCur += dist(i,j,t[0],t[1])
                
            if sumCur < minDist:
                minDist = sumCur
                minI = i
                minJ = j
                
            sumCur = 0;
            
    print("(" + str(minJ) + ", " + str(minI)+ ")")
    

if __name__ == "__main__":
    readFile()
