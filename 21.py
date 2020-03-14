from random import shuffle
from time import sleep
from lib import check_input



play_again = 'да'

while play_again == 'да':

    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
    shuffle(cards)
    your_points = 0
    dealer_points = 0
    max_point = 21
    min_dealer_point = 17

    move =1
    more = 'да'


    while more == 'да':
        dealer_card = cards.pop()
        dealer_points += dealer_card
        
        if move == 1:
            list_cards = []
            for  i in range(2):
                your_card = cards.pop()
                list_cards.append(your_card)
                your_points += your_card
        else:
            your_card = cards.pop()
            your_points += your_card

        print(f'''
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        ''')

        if move == 1:
            print(f'Вам выпали карты номиналом {list_cards[0]} и {list_cards[1]}')
        else:
            print(f'Вам выпала карта номиналом {your_card}')

        
        if your_points > max_point:
            print('Перебор')
            break
        elif your_points == max_point:
            more = 'нет'
        else:
            more = check_input(input('Ещё? да или нет\n'), ['да', 'нет'])
            move +=1

    else:
        while dealer_points <= min_dealer_point:
            dealer_card = cards.pop()
            dealer_points += dealer_card
            print(f'''
            =============
            ОЧКИ:
            Крупье: {dealer_points}
            Вы: {your_points}

            Крупье выпала карта номиналом {dealer_card}
            ''')
            sleep(3)

        
        if dealer_points > max_point:
                print("Вы выиграли")
        elif your_points == dealer_points:
            print('Ничья')
        else:
            print('Крупье выиграл')

    play_again = check_input(input('Сыграем ещё? да или нет\n'), ['да', 'нет']) 