import pandas as pd
import numpy as np

file = open('zigzag_easy_sample_input.txt', 'r')
#file = open()
output = open('output.txt', 'w')
Lines = file.readlines()
for line in Lines:
    n = int(line)
    break

print(36*3*n)
output.write(str(36*3*n))
output.close() 
