#https://adventofcode.com/2022/day/1

#find top one
with open('input.txt','r') as f:
    maxCal = 0
    currCal = 0
    for line in f:
        #print(line)
        line = line.strip('\n')
        if len(line)==0:
            maxCal=max(maxCal, currCal)
            currCal=0
        else:
            currCal+=int(line)

print(maxCal)    
#correct!!!
#69501       
print('------------------------------------------')
#find top three
with open('input.txt','r') as f:
    maxCals = []
    currCal = 0
    for line in f:
        #print(line)
        line = line.strip('\n')
        if len(line)==0:
            maxCals.append(currCal)
            currCal=0
        else:
            currCal+=int(line)

print(maxCals)
maxCals.sort(reverse=True)
print(maxCals)
print(sum(maxCals[0:3]))
#correct!!!
#202346
