##############################
# Created by Samuelito Perro #
##############################
# A program that finds the difference
# between the sum of the squares of
# the first 100 numbers and the square of the sum

import time

start = time.time()

sumsqr = 0
sqrsum = 0

# Finding sum of the squares
for i in range(1,101):
    sumsqr += pow(i, 2)

# Finding square of the sum
# The legend says that when my boy Carl Friedrich Gauss was merely
# 8 years old, during a task his professor gave the class of summing
# every number from 1 - 100, he perceived that the sum of the oposit terms
# of an AP was a constant. Finding, this way, the formula to calculate the 
# sum of the terms of an AP... Way to go my boy Gauss
sqrsum = pow(101*50, 2)

end = time.time()
print('The difference between the sum of the square and the square of the sum of every natural number from 1 to 100 is: \n', sqrsum - sumsqr)
print('Execution time was: ', end-start)