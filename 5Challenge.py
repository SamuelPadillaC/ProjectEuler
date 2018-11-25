##############################
# Created by Samuelito Perro #
##############################
# A program that finds the smallest
# nunmber that is divisible by all
# numbers from 1 to 20.

import time

starting = time.time()


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# To reduce the computing time:
# Add by 10 - a number is only divisible by 10 if ends in 0

start = 80057330
breaker = None

while start:
    for i in nums:
        if start%i != 0:
            break
        if i == 20:
            final = start
            breaker = True
            break
    if breaker == True:
        break
    start = start + 10

end = time.time()

# Man... what a crazy number - the result is: 232792560

print ('The smallest number divisble by all numbers from 1 to 20 is: ', start)
print('Execution time was: ', end-starting) # It only took 20 minutes to find... (AFTER RUNING THE CODE TWICE BEFORE)
