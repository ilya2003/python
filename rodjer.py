# программа для автоматизации навыков счёта
import os
import json
from random import randint, choice
from time import sleep
from timeit import default_timer


def auth_and_register():
    login = input("введите имя пользователя\n") 

    users_file = 'users.json'
    users = {}

    if not os.path.exists(users_file):
        with open(users_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False)

    # открываем файл с пользователями
    with open(users_file, 'r', encoding="utf-8") as f:
        users = json.load(f)

    # если нет нужного пользователя
    if login not in users:
        password = input("придумайте пароль\n")
        users[login] = password
        with open(users_file, 'w', encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False)
            return login
    else:
        password = input("введите пароль\n")
        if users[login] == password:
            print('Успешная авторизация')
            return login
        else:
            print('''Ошибка авторизации!!!
Попробуйте ввести имя ещё раз, или введите новое имя для регистрации''')
            auth_and_register()
            

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
    mode = ''
    if not os.path.exists(file_name):
        
        print()
        print('Тренировка - 1')
        print('выход - 0')

        while mode not in {'1', '0'}:
            print('Введите номер:')
            mode = input()
            if mode not in {'1', '0'}:
                print('Должно быть 1 или 0')
    else:
        print()
        print('Работа над ошибками - 1')
        print('Тренировка - 2')
        print('выход - 0')

        while mode not in {'1', '2','0'}:
            print('Введите номер:')
            mode = input()
            if mode not in {'1', '2','0'}:
                print('Должно быть 1, 2 или 0')

    return mode


def get_settings():
    
    filename = "settings.json"
    if not os.path.exists(filename):

        settings = {
            'количество правильных ответов':'1',
            'показывать правильный ответ': 'да'
        }

        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False)
    
    with open(filename, 'r', encoding="utf-8") as f:
        settings = json.load(f)
    
    return settings


# Функция проверки знаний в математике
def count():
    if not os.path.exists(file_name):
        print('Давай проверим твои знания в математике.')
    sleep(1)

    settings = get_settings()
    
    my_warnings = ["Эх....", "А если подумать", "Проверь свой ответ прежде чем давать его", "Серьёзно?", "Напряги мозг"]   
    examples_quantity = ''  # Количество примеров
    example_number = 0 # номер примера
    count_to = ''  # До скольки будем считать
    uniques_examples = [] # уникальные примеры
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

    count_to = int(count_to)
    examples_quantity = int(examples_quantity)

    col_uniques_examples = count_to**2  # количество уникальных примеров
    print(f"Количество уникальных примеров: {col_uniques_examples}")

    print('Хорошо, тогда начинаем...')    
    
    # проверим не вышли ли за максимальное количество примеров
    while  not len(uniques_examples) == col_uniques_examples:

        # если номер примера не больше количества
        if not example_number > examples_quantity:

            for i in range(examples_quantity):
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

                example = f'{number1} {sign} {number2}'

                # проверим пример на уникальность и выведем
                while example not in uniques_examples:
                    uniques_examples.append(example)
                    example_number += 1

                    if example_number > examples_quantity:
                        break
                    print(f'пример:{example_number}')
                    print(f'сколько будет {example}')

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
                
                        print(my_warnings[randint(0, len(my_warnings)-1)])
                        if settings['показывать правильный ответ'] == 'да':
                            print('Правильный ответ: '+str(right_answer))
                        fails += 1
                        
                        # создадим файл для записи ошибок
                        f = open(file_name, 'a')

                        #  запишем ошибку в файл
                        f.write(f'{number1} {sign} {number2} 3\n')
        else:
            break
    else:
        print()
    
        if not example_number > examples_quantity:
            print("Исчерпаны всевозможные примеры в данном диапазоне")
           
    if fails == 0:
        print(f'Молодец, {user}! Ты правильно ответил на все примеры за {seconds_convert(answers_time)}')
    else:
        print(f'Правильных ответов: {correct_answers}')
        print('Ошибок: '+ str(fails))
        print(f'{user}! Ты ответил на все примеры за {seconds_convert(answers_time)}')
        f.close()


# Функция работы над ошибками
def fix_errors():

    correct_answers = 0  # правильные ответы
    fails = 0  # ошибки
    answers_time = 0  # затраченное время 

    with open(file_name, 'r') as f:
        line = f.readline()

        while line:
            separated_line = line.split()
            number1, sign, number2 = separated_line
            
            if  sign == '-':
                right_answer = int(number1) - int(number2)

            if  sign == '+':
                right_answer = int(number1) + int(number2)

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
                
                # создадим временный файл для записи ошибок
                with open(f'tmp_{file_name}', 'a') as f2:

                    #  запишем ошибку в файл
                    f2.write(f'{number1} {sign} {number2}\n')
            

            
            # Получим следующую строку
            line = f.readline()
    os.remove(file_name)
    if os.path.exists(f'tmp_{file_name}'):
        os.rename(f'tmp_{file_name}', file_name)


# Основной блок программы
print('Привет! Меня зовут Роджер')

user = auth_and_register()

file_name = f'{user}_settings.json'
settings = {
            'количество правильных ответов':'1',
            'показывать правильный ответ': 'да'
            }

with open(file_name, 'w', encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False)

while True:

    start_type = mode_select()

    if not os.path.exists(file_name):
        # проверка знаний в математике
        if start_type == '1':
            count()
        # выход
        elif start_type == '0':
            break
        else:
            pass
    else:
        # работа над ошибками
        if start_type == '1':
            fix_errors()
        # проверка знаний в математике
        elif start_type == '2':
            count()
        # выход
        elif start_type == '0':
            break
        else:
            pass
    
   