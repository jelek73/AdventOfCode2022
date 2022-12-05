#https://adventofcode.com/2022/day/5

n=-1
numOfStacks=-1
stacks = []
processStacks = 1 #until empty line

#part2
stacks2 = []
import copy

from math import ceil

with open('input.txt','r') as f:
#with open('input_test.txt','r') as f:
    for line in f:
        l = line.strip('\n')
        
        if processStacks==1:
            #print(len(l), l)
            if len(l)==0:
                processStacks = 2 #reverse stacks
                continue

            if n==-1:
                n=len(l)
        
                numOfStacks = ceil(n/4)
                #print(numOfStacks)

                for i in range(numOfStacks):
                    stacks.append([])

            print(l)
            idx = 0
            for i in range(0, numOfStacks*4, 4):
                #print(l[i+1], end=' ')
                if l[i]=='[' and l[i+1]!=' ':
                    stacks[idx].append(l[i+1])
                idx+=1    
        
        
        if processStacks==2:
            print(stacks)
            for s in stacks:
                s = s.reverse()

            print(stacks)

            stacks2 = copy.deepcopy(stacks)

            processStacks = 3    

        if processStacks==3:
            m = list(l.split())
            if m[0]=='move':
                moves = int(m[1])
                source = int(m[3])-1
                target = int(m[5])-1

                for _ in range(moves):
                    stacks[target].append(stacks[source].pop())

                tmpStack = []
                for _ in range(moves):
                    tmpStack.append(stacks2[source].pop())

                for _ in range(moves):
                    stacks2[target].append(tmpStack.pop())    

for st in stacks:
    print(st[-1], end='')
print()
# LJSVLTWQM

#part2
for st in stacks2:
    print(st[-1], end='')
print()
# BRQWDBBJM







         
