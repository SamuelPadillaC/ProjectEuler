##############################
# Created by Samuelito Perro #
##############################
# A program that finds the first triangle number
# with over 500 divisors

from time import time

start = time()

firstprimes = [2,3,5,7,11,13,17,19]
i = 1
triangle = 0 

while i:
    primefactors = []
    
    #Creating triangle numbers using AP rules
    if i%2 == 0: #if AP even, sum of extremes * total terms/2
        triangle = (1 + i)*(i//2)
    else: #is AP odd, middle term * num of terms
        triangle = ((1+i)//2)*i
        
    new = triangle

    # Prime Factorization
    while new > 0:
        for p in firstprimes:
            if new%p == 0:
                new = new//p
                primefactors.append(p)
                break
            if new == 1:
                new = -1
                break
            if p == firstprimes[len(firstprimes)-1]: # Is this a mathematically valid reason for a number to be prime?
                firstprimes.append(new) 
                new = -1
                break

    # Checking for number of occurences
    power = 0
    previous = 0
    powers = []
    for a in primefactors:
        if a != previous:
            for b in primefactors:
                if a==b:
                    power += 1
            powers.append(power+1)
            power = 0
        previous = a
    
    result = 1
    for z in powers:
        result *= z

    if result > 500:
        break
    else:    
        i += 1

end = time()
print ('The first triangle number to have over 500 divisors is: ', triangle)
print ('It has ', result, 'divisors')
print ('It is the ', i, 'triangle number')
print('Execution time was: ', end-start) # Just 2.249037 seconds