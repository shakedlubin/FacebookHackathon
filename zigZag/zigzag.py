# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:12:26 2021

@author: user
"""

def readFile():
    file = open("zigzag_easy_input.txt")
    n = int(file.readline())
    
    output = open("zigzag.txt", 'w')
    output.write(str(36 * 3 * n))

if __name__ == "__main__":
    readFile()
