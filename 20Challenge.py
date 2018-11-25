##############################
# Created by Samuelito Perro #
##############################
# A program that finds the sum of the digits of 100!

from time import time
start = time()

fac = 1
for i in range (1, 101):
    fac *= i

strfac = str(fac)

result = 0
for n in strfac:
    result += int(n)

end = time()
print('Sum of terms of 100! is: ', result)
print('Execution time was: ', end-start) #0.0s