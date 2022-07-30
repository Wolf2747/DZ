year_of_birth = int(input('Какой год рождения у Пушкина?:'))
while year_of_birth != 1799:
    print('Неверно')
    year_of_birth = int(input('Какой год рождения у Пушкина?:'))

birthday = int(input('Какой день рождения у Пушкина?'))
while birthday != 6:
    print('Неверно')
    birthday = int(input('Какой день рождения у Пушкина?'))
print('Верно')