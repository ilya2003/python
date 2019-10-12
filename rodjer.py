# программа для автоматизации навыков счёта
from random import randint, choice
from time import sleep
from timeit import default_timer

print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, '+name)
sleep(1)
print('Давай проверим твои знания в математике.')
sleep(1)
print('Ты готов (да или нет)')
ready = input()
ready = ready.lower()

while ready not in {'да', 'нет'}:
    print('''Должно быть 'да' или 'нет'.
Введи заново''')
    ready = input()
    ready = ready.lower()

if ready == 'да':

    examples_quantity = ''  # Количество примеров
    count_to = ''  # До скольки будем считать
    correct_answers = 0  # правильные ответы
    fails = 0  # ошибки
    answers_time = 0  # затраченное время 

    while not examples_quantity.isdigit():
        print('Сколько примеров ты готов решить?')
        examples_quantity = input()
        if examples_quantity.isdigit():
            while int(examples_quantity) < 1:
                print('Введи число больше 0')
                examples_quantity = input()
                while not examples_quantity.isdigit():
                    print('Должна быть цифра')
                    examples_quantity = input()
        else:
            print('Должна быть цифра')

    while not count_to.isdigit():
        print('До скольки будем считать? Например до 100')
        count_to = input()
        if count_to.isdigit():
            while int(count_to) < 2:
                print('Введи число больше 1')
                count_to = input()
                while not count_to.isdigit():
                    print('Должна быть цифра')
                    count_to = input()
        else:
            print('Должна быть цифра')

    print('Хорошо, тогда начинаем...')

    examples_quantity = int(examples_quantity)
    count_to = int(count_to)

    for i in range(examples_quantity):
        print('пример ' + str(i+1) + ':')
        number1 = randint(1, count_to)
        number2 = randint(1, count_to)
        sign = choice('+-')


        if  sign == '-':
            while number1 < number2:
                number1 = randint(1, count_to)
            right_answer = number1 - number2

        if  sign == '+':
            while number1 + number2 > count_to:
                number1 = randint(1, count_to)
                number2 = randint(1, count_to)
            right_answer = number1 + number2

        print('сколько будет ' + str(number1) + sign + str(number2))

        answer = ''  # Ответ пользователя
        while not answer.isdigit():

            start = default_timer()  # начнем отсчёт
            answer = input()
            stop = default_timer()  # закончим отсчёт

            answers_time += stop - start


            if not answer.isdigit():
                print('Должна быть цифра')
                print('сколько будет ' + str(number1) + sign + str(number2))

        answer = int(answer)

        if answer == right_answer:
            print('Правильно, молодец')
            correct_answers += 1
        else:
            print('Неправильно')
            print('Правильный ответ: '+str(right_answer))
            fails += 1
    
    # узнаем количество затраченного времени в минутах и секундах
    if answers_time < 60: # если меньше одной минуты
        time_in_seconds = str(answers_time)
        # затраченное время на все ответы
        time_spent = time_in_seconds +'секунд'
    else:
        time_in_minutes_and_seconds = str(round(answers_time/60, 2))  # например, 2.17
        time_spent = time_in_minutes = time_in_minutes_and_seconds.split('.')  # разобьем на минуты и секунды [2.17]

        time_in_minutes = time_in_minutes_and_seconds[0]  # время в минутах
        time_in_seconds = time_in_minutes_and_seconds[1]  # время в секундах

        # подсчитаем количество секунд 
        seconds = '0.'
        seconds = seconds + time_in_seconds # приведём к виду 0.17
        seconds = str(round(float(seconds)*60)) # рассчитаем по формуле 0.17*60
        # затраченное время на все ответы
        time_spent = time_in_minutes + 'минут и ' + seconds +'секунд'

    if fails == 0:
        print(f'Молодец, {name}!Ты правильно ответил на все вопросы за {time_spent}')
    else:
        print('Правильных ответов: ' +correct_answers)
        print('Ошибок: '+fails)
        print(f'{name}!Ты ответил на все вопросы за {time_spent}')
if ready == 'нет':
    print('''Передумал? Хорошо,может как-нибудь в следующий раз...
Пока!''')

