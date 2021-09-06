import pandas as pd
import numpy as np

global count
count = 0

file = open('commercial_operations_easy_input.txt', 'r')
#file = open('commercial_operations_easy_sample_input.txt', 'r')
Lines = file.readlines()
output = open('output.txt', 'w')

df = pd.DataFrame(columns=['start','end','cost_t','cost'])
first = True
res = ''
# Strips the newline character
for line in Lines:
    if first:
        first = False
        nums = line.split(' ')
        N = nums[0]
        M = nums[1]
        source = 1
        destination = N
        
    else:
        parts = line.split(' ')
        start = parts[0]
        end = parts[1]
        cost_t = parts[2]
        cost = parts[3]
        df = df.append({"start":start,"end":end,"cost_t":cost_t,"cost":cost}, ignore_index=True)




def longest_rec(source, destination,t):
    if source==destination:
            return 0
        
    else:
        k = (source,destination)
        if k in mem.keys():
            return mem[k]
        
        else:
            mini = np.inf
            for opt in df[df["start"]==source].itertuples():
                if opt.end!=destination:
                    m = longest_rec(opt.end,destination,t)
                    m += int(opt.cost) + int(opt.cost_t)*t
                
                else:
                    d = df[df["start"]==source]
                    d = d[d["end"]==destination]
                    if d.shape[0]==1:
                        c = int(d.iloc[0]["cost"])
                        d = int(d.iloc[0]["cost_t"])*t
                        m = c+d
   
                if m < mini:
                    mini = m
                           
            mem[k] = mini
            return mini
    
    



mem = {}
total_max = np.NINF
for t in range(0,9):
    mini = longest_rec(str(source), str(destination),t)
            
    if mini > total_max:
        total_max = mini

    
output.write(str(total_max))
file.close()
output.close() 
