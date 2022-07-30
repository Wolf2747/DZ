year_of_birth = int(input('Какой год рождения у Пушкина?:'))

if year_of_birth == 1799:
    birthday = int(input('Какой день рождения у Пушкина?'))

    if birthday == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')

