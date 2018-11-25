##############################
# Created by Samuelito Perro #
##############################
# A program that finds the product of
# the only pythagoran triplet for which
# a+b+c = 1000

import time
start = time.time()

breaker = None

for a in range (1, 1000):
    print('A is: ', a)
    for b in range(a+1, 1000):
        print('B is: ', b)
        for c in range (b+1, 1000):
            print('C is: ', c)
            if pow(a, 2) + pow(b,2) == pow(c,2) and a+b+c == 1000:
                final = a*b*c
                breaker = True
                break
        if breaker == True:
            break
    if breaker == True:
        break            

end = time.time()
print('The product of a*b*c where abc is a pythagorean triplet that satisfies a+b+c=1000 is: \n', final)
print('The triplet is: ', a, b, c)
print('Execution time was: ', end-start)