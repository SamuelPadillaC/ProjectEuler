##############################
# Created by Samuelito Perro #
##############################
# A program that finds the largest multiplication
# of 4 digits from a grid

import time

start = time.time()

# Reading file and creating nested list
grid = []

fo = open('./text11.txt', 'r')
n = 0
while n < 20:
    li = fo.readline().split()
    grid.append(li)   
    n+=1
fo.close()

greatest = 1
# Vertical multiplication
for c in range (0, 20): #These are the colums
    for r in range (0, 17): #These are the rows
        prov = 1
        for n in range (r, r + 4):
            prov *= int(grid[n][c])
        if prov > greatest:
            greatest = prov

# Horizontal multiplication
for r in range (0, 20): #These are the rows
    for c in range (0, 17): #These are the columns
        prov = 1
        for n in range (c, c + 4):
            prov *= int(grid[r][n])
        if prov > greatest:
            greatest = prov


# Diagonal Left to right
for r in range (0, 17): #These are the rows
    for c in range (0, 17): #These are the columns
        prov = 1
        for n in range (0, 4):
            prov *= int(grid[r+n][c+n])
        if prov > greatest:
            dLR = prov


# Diagonal Right to left
for r in range (0, 17): #These are the rows
    for c in range (17, 0, -1): #These are the columns
        prov = 1
        for n in range (0, 4):
            prov *= int(grid[r+n][c-n])
        if prov > greatest:
            greatest = prov

end = time.time()

print('The largest product of 4 adjacent numbers in the grid is: ', greatest)
print('Execution time was: ', end-start) # Execution time was: 0.003999233245s
