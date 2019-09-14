# Игра "Угадай число"
import random

play_again = 'да'
print('Привет! Как тебя зовут?')
name = input()

def guessNumber():

    print('Что ж '+name+', я загадываю число от 1 до 20.')

    number = random.randint(1,20)
    counter = 0

    for counter in range(6):
        if counter == 0:
            print('Попробуй угадать:')
        else:
            print('Попробуй ещё раз')

        guess_number = int(input())

        if guess_number > number:
            print('Твоё число слишком большое')
        if guess_number < number:
            print('Твоё число слишком маленькое')
        if guess_number == number:
            break

    if guess_number == number:
        counter = str(counter+1)
        print('Отлично, '+name+'! Ты справился за '+counter+' попытки!')
    if guess_number != number:
        number = str(number)
        print('Увы. Я загадала число '+number)

while play_again == 'да':
    guessNumber()
    print("Сиграем ещё? ('да', 'нет')")
    play_again = input()