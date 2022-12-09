import os
absolute_path = os.path.abspath(__file__)
print("Full path: " + absolute_path)
print("Directory Path: " + os.path.dirname(absolute_path))

overlaps=0

overlaps_part2=0

with open(os.path.dirname(absolute_path)+"/input.txt", "r") as f:
    for line in f:
        #l = len(line)
        line = line.strip('\n')
        l1 = line.split(',')
        #print(l1)
        elf1 = list(map(int,l1[0].split('-')))
        elf2 = list(map(int,l1[1].split('-')))

        if (elf1[0]>=elf2[0] and elf1[1]<=elf2[1]) or (elf2[0]>=elf1[0] and elf2[1]<=elf1[1]):
            overlaps+=1
        if (elf1[0]>=elf2[0] and elf1[1]<=elf2[1]) or (elf2[0]>=elf1[0] and elf2[1]<=elf1[1]) or (elf1[0]>=elf2[0] and elf1[0]<=elf2[1]) or (elf1[1]>=elf2[0] and elf1[1]<=elf2[1]):
            overlaps_part2+=1
print(overlaps)    
#450 correct  
print(overlaps_part2) 
#837 correct     