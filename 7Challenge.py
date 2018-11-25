##############################
# Created by Samuelito Perro #
##############################
# A program that finds the 10001st prime number
# and would probably make me rich if I could run it forever
# and identify a formula for prime numbers... Whateva

import time

start = time.time()

primes = [2,3,5,7,11,13]

i = 15

while i:
    print('i is: ', i)
    for n in range (2, i-1): # Try diving by all
        if (i%n == 0): # Not prime, break
            print('---not prime ', i, ' - divisible by', n)
            break
        if n == i-2: # It it makes it to here, is prime
            primes.append(i)
            print(i, ' PRIME AND PRIMES LENGTH IS: ', len(primes))
    if len(primes) == 10001:
        final = primes[10000]  
        break
    i = i + 2 # Prime numbers can't be even (besides 2) - add by 2, optimize

end = time.time()
print('The 10001st prime number is: \n', final)
print('Execution time was: ', end-start)