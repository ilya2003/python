# программа для автоматизации навыков счёта
from random import randint, choice
from time import sleep

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
    correct_answers = 0
    fails = 0

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
            answer = input()
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

    print('Правильных ответов: ' +correct_answers)
    print('Ошибок: '+fails)
if ready == 'нет':
    print('''Передумал? Хорошо,может как-нибудь в следующий раз...
Пока!''')

