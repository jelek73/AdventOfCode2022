import os
absolute_path = os.path.abspath(__file__)
print("Full path: " + absolute_path)
print("Directory Path: " + os.path.dirname(absolute_path))

visibles = set()
matrix = []

with open(os.path.dirname(absolute_path)+"/input.txt", "r") as f:
    for line in f:
        #l = len(line)
        line = line.strip('\n')
        matrix.append(line)

#print(matrix) 
R = len(matrix)
C = len(matrix[0])

#add column edges
for r in range(0,R):
    visibles.add((r,0))
    visibles.add((r,C-1))

#add row edges
for c in range(0, C):
    visibles.add((0, c))
    visibles.add((R-1,c)) 

#add visibles for rows
for r in range(0, R):
    maxTree = matrix[r][0]
    for c in range(1, C):
        if matrix[r][c]>maxTree:
            visibles.add((r,c))
            maxTree=matrix[r][c]

for r in range(0,R):
    maxTree = matrix[r][C-1]
    for c in range(C-2, -1, -1):
        if matrix[r][c]>maxTree:
            visibles.add((r,c))
            maxTree=matrix[r][c]                    

#add visibles for columns
for c in range(0, C):
    maxTree = matrix[0][c]
    for r in range(1, R):
        if matrix[r][c]>maxTree:
            visibles.add((r,c))
            maxTree=matrix[r][c]

for c in range(0,C):
    maxTree = matrix[R-1][c]
    for r in range(R-2, -1, -1):
        if matrix[r][c]>maxTree:
            visibles.add((r,c))
            maxTree=matrix[r][c] 
        
print(len(visibles)) 

#part1 - 1715

maxView = 0

for r in range(R-1):
    for c in range(C-1):
        pos = matrix[r][c]
        val = 0
        view = 0
        #up
        for i in range(r-1,-1,-1):
            #if matrix[i][c]<=pos:
            #    val+=1
            val+=1
            if matrix[i][c]>=pos:
                break
        print('val1=',val, end=' ')    
        view = val
        #down
        val=0
        for i in range(r+1,R):
            #if matrix[i][c]<=pos:
            #    val+=1
            val+=1
            if matrix[i][c]>=pos:
                break 
        print('val2=',val, end=' ')    
        view*=val
        val=0
        #right
        for i in range(c+1,C):
            #if matrix[r][i]<=pos:
            #    val+=1
            val+=1
            if matrix[r][i]>=pos:
                break
        print('val3=',val, end=' ')    
        view*=val
        val=0
        #left
        for i in range(c-1,-1,-1):
            #if matrix[r][i]<=pos:
            #    val+=1
            val+=1
            if matrix[r][i]>=pos:
                break
        print('val4=',val, end=' ')    
        view*=val

        maxView = max(maxView, view)
        print('current maxView', maxView)
print('maxView = ', maxView)
#part2 = 374400
