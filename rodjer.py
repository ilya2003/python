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

    examples = ''
    max_answer = ''

    while not examples.isdigit():
        print('Сколько примеров ты готов решить?')
        examples = input()
        if examples.isdigit():
            while int(examples) < 1:
                print('Введи число больше 0')
                examples = input()
                while not examples.isdigit():
                    print('Должна быть цифра')
                    examples = input()
        else:
            print('Должна быть цифра')

    while not max_answer.isdigit():
        print('До скольки будем считать? Например до 100')
        max_answer = input()
        if max_answer.isdigit():
            while int(max_answer) < 2:
                print('Введи число больше 1')
                max_answer = input()
                while not max_answer.isdigit():
                    print('Должна быть цифра')
                    max_answer = input()
        else:
            print('Должна быть цифра')



    print('Хорошо, тогда начинаем...')

    for i in range(examples):
        print('пример ' + str(i+1) + ':')
        number1 = randint(1, max)
        number2 = randint(1, max)
        sign = choice('+-')

        while number1 < number2:
            number1 = randint(1, max)

        while number1 + number2 < max:
            number1 = randint(1, max)

        print('сколько будет '+str(number1)+sign+str(number2))

        answer = int(input())
        if  sign == '-':
            right_answer = number1 - number2

        if  sign == '+':
            right_answer = number1 + number2

        if answer == right_answer:
            print('Правильно, молодец')
if ready == 'нет':
    print('''Передумал? Хорошо,может как-нибудь в следующий раз...
Пока!''')
