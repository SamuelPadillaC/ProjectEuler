##############################
# Created by Samuelito Perro #
##############################
# A program that find the longest
# Collatz sequence

from time import time
start = time()

i = 2
LongCh = 0 
LongI = i
while i < 1000000:
    Coz = i #Assing starting value
    chain = 1 #Counting last 1
    while Coz != 1: #Work with the sequence
        chain += 1 #Add to chain for every new number
        if Coz%2==0:
            Coz = Coz//2
        else:
            Coz = 3*Coz + 1

    if chain > LongCh:
        LongCh = chain
        LongI = i
    
    i += 1

end = time()
print('The starting number under a million that produces the longest Collatz chain is: ', LongI)
print('It produced a chain with', LongCh, 'terms')
print('Execution time was: ', end-start)