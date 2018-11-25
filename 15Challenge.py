##############################
# Created by Samuelito Perro #
##############################
# A program that calculates the possible shortest
# routes in a 20x20 grid.

# This is just a simple permutation problem:
# 40 permutation with 2 variables repeting twice
# 40! // 20!^2

x = 1
for i in range (1, 41):
    x *= i

y = 1
for z in range (1, 21):
    y *= z

print(x//pow(y,2))
# In this solution I am not getting why the /2 40 choose 20 (40/20) print((x//y)//2)