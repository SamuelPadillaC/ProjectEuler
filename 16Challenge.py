##############################
# Created by Samuelito Perro #
##############################
# A programs that calculates the sum of the digits of
# 2^1000

x = str(pow(2, 1000))

result = 0
for i in x:
    result += int(i)

print('THe sum of the digits of 2^1000 is: ', result)
