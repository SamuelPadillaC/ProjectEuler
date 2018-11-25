##############################
# Created by Samuelito Perro #
##############################
# A program that finds the first 10 digits of the product
# of 100 50 digit numbers

import time

start = time.time()

nums = []
result = []

# Reading file and creating list with ints
fo = open('./text13.txt', 'r')
n = 0
while n < 100:
    li = int(fo.readline())
    nums.append(li)
    n+=1
fo.close()

huge = 0
for i in nums: #Sum
    huge += i

hugestr = str(huge) # Transform to string to access first 10 digits
for i in range (0, 10):
    result.append(hugestr[i])


final = map(str, result)
final = ''.join(final)
end = time.time()
print(final)
print('Execution time was: ', end-start)