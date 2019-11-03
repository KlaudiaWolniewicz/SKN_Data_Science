import random

x = random.randint(1, 11)

print('Zgadnij liczbę z przedziału od 1 do 10')

counter = 1
for i in range(1, 11):
    num = input()

    if str(num) == 'exit':
        break
    elif int(num) == x:
        print('Brawo!')
        print('Udało ci się zgadnąć w liczbie prób: ' + str(counter))
        break
    elif int(num) > x:
        counter += 1
        print('Za duża liczba!')
    else:
        counter += 1
        print('Za mała liczba!')




