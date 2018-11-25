##############################
# Created by Samuelito Perro #
##############################
# A program that finds the max top to bottom
# path for a triangle.

from time import time
start = time()

# Reading file and creating triangle
fo = open('./text18.txt', 'r')
n = 0
triangle = []
ints = []
while n < 15:
    li = fo.readline().split() # Read file
    for z in range(0, len(li)): # Transform strings to ints
        ints.append(int(li[z]))
    triangle.append(ints) # Append to triangle
    ints = []
    n += 1
fo.close()

memo = []
prov1 = 0
prov2 = 0
n = 1
# Starting from the bottom of the triangle
while n < 15:
    # Sum every adjacent numbers with the number in line above
    for i in range(0, len(triangle[len(triangle)-n])-1):
        prov1 = triangle[len(triangle)-n][i] + triangle[len(triangle)-n-1][i]
        prov2 = triangle[len(triangle)-n][i+1] + triangle[len(triangle)-n-1][i]
        
        # Find largest sum and append to memo
        if prov1 > prov2:
            memo.append(prov1)
        elif prov2 > prov1:
            memo.append(prov2)
    
    # Assign memo to the next line
    triangle[len(triangle)-n-1] = memo
    print(memo)
    memo = [] # Reset memo
    n += 1 # Move one line up and start over
end = time()
print('Execution time was: ', end-start)