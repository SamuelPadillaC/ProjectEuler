##############################
# Created by Samuelito Perro #
##############################
# A program that sums all primes below 1m

import time

start = time.time()

primes = [2,3,5,7,11,13,17] #148933 prime numbers
primate =  58 #142913828922 - This is the answer
i = 19

while i < 2000000:
    print(i)
    for n in primes: # Eliminating any even number, a number is only divisible by prime numbers
        if i%n == 0:
            break
        if n == primes[len(primes)-1]: # If it makes it to the end of list, it is prime
            primes.append(i)
            primate += i
    i += 2 # Prime numbers can't be even (besides 2) - add by 2.

end = time.time()
print('The sum of all prime numbers below 1m is: \n', primate)
print('And there are ', len(primes), ' prime numbers under 2M')
print('Execution time was: ', end-start) # IT TOOK MY COMPUTER 8 HOURS!!!!! -  29323  seconds