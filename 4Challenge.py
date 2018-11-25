##############################
# Created by Samuelito Perro #
##############################
# A program that calculates the
# largest palindromic number
# out of the product of 3-digit nums

import time

x = 999
plibla = []

start = time.time()

# Find pliandromic and append to list
while x > 99:
    y = 999
    while y > 99:
        number = str(x*y) # Transfrom to string to check "palindromicity"
        if number == number[::-1]:
            plibla.append(int(number))
            break
        else:
            y = y-1
    x = x-1

palindromic = plibla [0]
# Find largest:
for i in plibla: # This list has 628 items!!!!
    if i > palindromic:
        palindromic = i

end = time.time()

print('The largest palindromic number made of the product of 3-digit numbers is: \n', palindromic)
print('Execution time was: ', end-start) # 0.485s for the Record