print('Wprowadź numer')
number = int(input())

if number % 4 == 0:
    print('Ta liczba jst wielokrotnością 4!')
elif number % 2 == 0:
    print('parzysta')
else:
    print('nieparzysta')

print('Podaj jeszcze dwa numery. Każdy z nich zatwierdź enterem.')
num1 = int(input())
num2 = int(input())

if num1 % num2 == 0:
    print('Pierwsza podana przez ciebie liczba dzieli się przez drugą bez reszty')
else:
    print('Pierwsza podana przez ciebie liczba nie dzieli się przez drugą bez reszty')

