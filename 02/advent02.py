#https://adventofcode.com/2022/day/2

score=0
elf={'A':1, 'B':2, 'C':3}
player={'X':1, 'Y':2, 'Z':3}
win=6
draw=3
loss=0
tmp_list = []

with open('input.txt','r') as f:
#with open('input_test.txt','r') as f:
    for line in f:
        l = line.split()
        tmp_score=0
        tmp_score += player[l[1]]
        '''
        if player[l[1]] > elf[l[0]]:
            tmp_score+=win
        elif player[l[1]] == elf[l[0]]:
            tmp_score+=draw
        else:
            tmp_score+=loss
        '''
        if (l[1]=='X' and l[0]=='A') or (l[1]=='Y' and l[0]=='B') or (l[1]=='Z' and l[0]=='C'):
            tmp_score+=3
        elif (l[1]=='X' and l[0]=='C') or (l[1]=='Z' and l[0]=='B') or (l[1]=='Y' and l[0]=='A'):
            tmp_score+=6


        #A for Rock, B for Paper, and C for Scissors
        #X for Rock, Y for Paper, and Z for Scissors
        #1 for Rock, 2 for Paper, and 3 for Scissors
        
        d1 = {'A':'Rock', 'B':'Paper','C':'Scissors'}
        d2 = {'X':'Rock', 'Y':'Paper','Z':'Scissors'}

        #Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
        #X>C                    Z>B                     Y>A

        #print(line, l, tmp_score, player[l[1]], d2[l[1]], elf[l[0]], d1[l[0]])         
        tmp_list.append(tmp_score)
        score+=tmp_score

print(score, sum(tmp_list), tmp_list)    
# part1 correct = 14069

# PART 2
print('----------------------------PART2 --------------------------------')
#X means you need to lose, A->Y, B->Z, C->X 
#Y means you need to end the round in a draw A->X, B->Y, C->Z
#Z means you need to win. Good luck!" A->Y, B->Z, C->X


score=0
tmp_list=[]
with open('input.txt','r') as f:
#with open('input_test.txt','r') as f:
    for line in f:
        l = line.split()
        tmp_score=0
        
        '''
        if player[l[1]] > elf[l[0]]:
            tmp_score+=win
        elif player[l[1]] == elf[l[0]]:
            tmp_score+=draw
        else:
            tmp_score+=loss
        '''
        if (l[1]=='X'):
            tmp_score+=0
            if l[0]=='A': tmp_score+=3
            if l[0]=='B': tmp_score+=1
            if l[0]=='C': tmp_score+=2
        elif (l[1]=='Y'):
            tmp_score+=3
            if l[0]=='A': tmp_score+=1
            if l[0]=='B': tmp_score+=2
            if l[0]=='C': tmp_score+=3
        elif (l[1]=='Z'):
            tmp_score+=6
            if l[0]=='A': tmp_score+=2
            if l[0]=='B': tmp_score+=3
            if l[0]=='C': tmp_score+=1    


        #A for Rock, B for Paper, and C for Scissors
        #X for Rock, Y for Paper, and Z for Scissors
        #1 for Rock, 2 for Paper, and 3 for Scissors
        
        d1 = {'A':'Rock', 'B':'Paper','C':'Scissors'}
        d2 = {'X':'Rock', 'Y':'Paper','Z':'Scissors'}

        #Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
        #X>C                    Z>B                     Y>A

        #print(line, l, tmp_score, player[l[1]], d2[l[1]], elf[l[0]], d1[l[0]])         
        tmp_list.append(tmp_score)
        score+=tmp_score

print(score, sum(tmp_list), tmp_list) 

# 12411 - CORRECT !!!