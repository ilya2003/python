# программа для автоматизации навыков счёта
import os
from random import randint, choice
from time import sleep
from timeit import default_timer

# Функция преобразования временных окончаний
def time_endings(v):

    v_str = str(v)
    v_last = int(v_str[-1])

    if 9<int(v)<20:
        return ''
    else:
        if v_last == 1:
            return 'у'
        if 1<v_last<5:
            return 'ы'
        else:
            return ''


def seconds_convert(time_in_seconds):
    # узнаем количество затраченного времени в минутах и секундах
    if time_in_seconds < 60: # если меньше одной минуты
        seconds = str(time_in_seconds)
        # затраченное время на все ответы
        time_spent = seconds +' секунд'+ time_endings(seconds) 
    else:
        minutes = str(time_in_seconds//60)
        seconds = time_in_seconds - (int(minutes)*60)

        # затраченное время на все ответы
        if seconds == 0:
            time_spent = minutes + ' минут' + time_endings(minutes)
        else:
            time_spent = minutes + ' минут' + time_endings(minutes) + ' и ' + str(seconds) + ' секунд' + time_endings(seconds)

    return time_spent


def mode_select():
    if os.path.exists(file_name):
        mode = ''
        print()
        print('Работа над ошибками - 1')
        print('Проверить знания в математике - 2')

        while mode not in {'1', '2'}:
            print('Введите номер:')
            mode = input()
            if mode not in {'1', '2'}:
                print('Должно быть 1 или 2')
    else:
        mode = '2'

    return mode


# Функция проверки знаний в математике
def count():
    if not os.path.exists(file_name):
        print('Давай проверим твои знания в математике.')
    sleep(1)
    
        
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

            answers_time += round(stop - start)


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
            
            # создадим файл для записи ошибок
            f = open(file_name, 'a')

            #  запишем ошибку в файл
            if fails > 0:
                f.write('\n')
            f.write(f'{number1} {sign} {number2}')

    if fails == 0:
        print(f'Молодец, {name}! Ты правильно ответил на все примеры за {seconds_convert(answers_time)}')
    else:
        print(f'Правильных ответов: {correct_answers}')
        print('Ошибок: '+ str(fails))
        print(f'{name}! Ты ответил на все примеры за {seconds_convert(answers_time)}')
        f.close()


# Функция работы над ошибками
def fix_errors():

    with open(file_name, 'r') as f:
        line = f.readline()
        separated_line = line.split()
        print(separated_line)
        number1, sign, number2 = separated_line



# Основной блок программы
print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, '+name)
sleep(1)

file_name = f'{name}_errors.txt'

start_type = mode_select()

# проверка знаний в математике
if start_type == '1':
    fix_errors()
# работа над ошибками
elif start_type == '2':
    count()
else:
    pass
    
    