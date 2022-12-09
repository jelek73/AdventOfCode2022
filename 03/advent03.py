score = 0

import os
absolute_path = os.path.abspath(__file__)
print("Full path: " + absolute_path)
print("Directory Path: " + os.path.dirname(absolute_path))

def getNum(c):
    if c>='a' and c<='z':
        return (ord(c)-ord('a')+1)
    if c>='A' and c<='Z':
        return (ord(c)-ord('A')+27)


with open(os.path.dirname(absolute_path)+"/input.txt", "r") as f:
    for line in f:
        l = len(line)
        line = line.strip('\n')
        first = line[0:l//2]
        second = line[l//2:]
        #print(line, first, second)
        d1={}
        d2={}
        for c in first:
            if c in d1:
                d1[c]+=1
            else:
                d1[c]=1
        for c in second:
            if c in d2:
                d2[c]+=1
            else:
                d2[c]=1 

        print("-> ", end="")
        for item in d1:
            if item in d2:
                print(item, " ", min(d1[item], d2[item]), " ", end="")
                #score+=min(d1[item], d2[item])*getNum(item)
                score+=getNum(item)
        print()                               
    print(score) 

    # 9323 when we count all occurences
    # 8139 correct !!!

score2 = 0
l1 = ''
l2 = ''
l3 = ''
lineCount=0

with open(os.path.dirname(absolute_path)+"/input.txt", "r") as f:
    for line in f:
        
        line = line.strip('\n')
        if lineCount==0:
            l1 = line
            lineCount=1
        elif lineCount==1:
            l2 = line
            lineCount=2
        elif lineCount==2:
            l3 = line 
            lineCount=0

            for c in l1:
                if c in l2 and c in l3:
                    score2+=getNum(c)
                    break   

            l1=''
            l2=''
            l3=''           
        
    print(score2) 
# 3559 too high
# 2668 correct !!!!!

