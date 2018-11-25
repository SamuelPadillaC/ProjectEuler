# Created by Samuelito Perro
# A program that calculates the factorial of
# a numeric input using Python
######################

number = input ("Please enter a number to calculate the factorial: ");

# Generating the factorial list
NumbAr = [];
for z in range(1, int(number)+1):
    NumbAr.append(z);

# WHY NUMPY DIDNT WORK?
# x = np.linspace(1, number, number);

# Define the factorial as 1 and then multiply it by every number of NumbAr
factorial = 1;

# Creating the For loop
for i in NumbAr:
    factorial *= i;

#Output
print ("The factorial of ", number, " is ", factorial);
