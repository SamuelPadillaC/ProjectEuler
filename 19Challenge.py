##############################
# Created by Samuelito Perro #
##############################
# A program that finds how many sundays
# fell on the first day of the month between 1901 and 2000

from time import time
start = time()

day = 1
week = range(1, 8)
FirstSun = 0
year = 1900
month = 1
weekday = 1

while year < 2001:
    # Se ano e bisexto
    if year%4 == 0 and year != 1900:
        bis = True
    else:
        bis = False
    month = 1

    # Contando os meses
    while month < 13:
        day = 1
        # Definindo os dias do mes
        if month == 4 or month == 6 or month == 9 or month == 11: 
            N = 31
        else:
            N = 32
        if month == 2 and bis == False:
            N = 29
        if month == 2 and bis == True:
            N =30
        # Contando os dias do mes
        while day < N:
            # Se domingo e dia 1, soma
            if weekday == 7 and day == 1 and year != 1900:
                FirstSun += 1
            if weekday == 7: #Zera a semana
                weekday = 0
            weekday += 1
            day +=1

        month +=1

    year +=1

end = time()
print('Run and found', FirstSun)
print ('Execution time was:', end-start) # 0.015623807907s