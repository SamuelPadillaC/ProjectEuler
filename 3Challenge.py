##############################
# Created by Samuelito Perro #
##############################
# A program that finds the largest
# prime factor of a very long number

number = 600851475143
factors = [4, 8, 10] # I am leaving these non-prime numbers here just to show that my non-prime algorith works
prime = []

# FIrst factor the number:
while number > 1:
    for i in range(2, number+1): # Trial and error from 2 up
        if number % i == 0: # If divisible by i
            factors.append(i) # Append to list
            number = int(number / i) # Overwrite number
            break # Start over

# Create list with only prime factors
for i in factors:
    for z in range (2, i+1):
        if i % z == 0 and z != i: # Not a prime number
            break
        else: 
            prime.append(i)
            break

# Highest prime factor:
print('The highest prime factor of 600851475143 is: \n', prime[len(prime)-1])