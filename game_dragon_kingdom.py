# Игра "Царство драконов"
import random, time

def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры.
    В одной из них - дружелюбный дракон,
    который готов поделиться с вами своими сокровищами.
    Во второй - жадный и голодный дракон, который мигом вас съест.
    
    ''')

def chooseCave():
    cave = ''
    print('В какую пещеру вы войдёте? Нажмите 1 или 2')
    cave = int(input())


    return cave

def checkCave(choosen_cave):
    print('Вы приближаетесь к пещере ... ')
    time.sleep(3)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(3)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    time.sleep(3)
    friendly_cave = random.randint(1, 2)
    if choosen_cave == friendly_cave:
        print('...делится с вами своими сокровищами')
    else:
        print('...моментально вас съедает')

play_again = 'да'
displayIntro()

while play_again == 'да':
    checkCave(chooseCave())
    print('Попытайте удачу ещё раз? (да или нет)')
    play_again = input()
    play_again = play_again.lower()
