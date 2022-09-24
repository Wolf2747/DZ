rest = ''
correct_answer = 0
wrong_answer = 0

while rest != 'нет':

    emma = int(input('Каков год рождения у Эммы Уотсон?:'))
    # правильный ответ 1990
    if emma == 1990:
        correct_answer += 1
    else:
        wrong_answer += 1

    jim = int(input('Какой год рождения у Джима Керри?:'))
    # правильный ответ 1962
    if jim == 1962:
        correct_answer += 1
    else:
        wrong_answer += 1

    tom = int(input('Какой год рождения у Тома Харди?:'))
    # правильный ответ 1977
    if tom == 1977:
        correct_answer += 1
    else:
        wrong_answer += 1

    cil = int(input('Какой год рождения у Киллиана Мерфи?:'))
    # правильный ответ 1976
    if cil == 1976:
        correct_answer += 1
    else:
        wrong_answer += 1

    anj = int(input('Какой год рождения у Анджелины Джоли?:'))
    # правильный ответ 1975
    if anj == 1975:
        correct_answer += 1
    else:
        wrong_answer += 1

    print('Правильно:', correct_answer)
    print('Неправильно', wrong_answer)

    percentage_correct = correct_answer * 100 / 5
    percentage_of_incorrect = wrong_answer * 100 / 5
    print('процент правильных ответов:',percentage_correct)
    print('Процент неправильных ответов:',percentage_of_incorrect)
    rest = input('Хотите пройти еще раз?:')




