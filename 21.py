from random import shuffle, choice
from time import sleep
from lib import check_input

def get_deck():
    deck = []

    for suit in ('черви','буби', 'пики','крести'):
        for card in range(2,11):
            deck.append(f'{card} {suit}')
        for card in ('валет', 'дама','король','туз'):
            deck.append(f'{card} {suit}')
    
    shuffle(deck)
    return(deck)


def get_card_points(card, dealer=False):
    card_name = card.split()

    card_points = {}
    for card in range(2,11):
        card_points[f'{card}'] = card
    for card in ('валет', 'дама','король'):
        card_points[f'{card}'] = 10
    
    if card_name[0] == 'туз':
        if dealer:
            points = choice([1, 11])
        else:
            points = int(input('1 или 11?\n'))
    else:
        points = card_points[card_name[0]] 

    return points    


balance = 100
play_again = 'да'

while play_again == 'да':
    print(f'Баланс: {balance}$')
    deposit = int(input('Ваша ставка?\n'))
    if deposit > balance:
        print('Депозит не может превышать баланс')
        deposit = int(input('Ваша ставка?\n'))
    elif balance == 0:
        print('У вас закончились деньги')
        break   
    deck = get_deck()
    your_points = 0
    dealer_points = 0
    max_point = 21
    min_dealer_point = 17

    move =1
    more = 'да'


    while more == 'да':
        
        if move == 1:
            dealer_card = deck.pop()
            dealer_points += get_card_points(dealer_card, True)

            list_cards = []
            for  i in range(2):
                your_card = deck.pop()
                list_cards.append(your_card)
                your_points += get_card_points(your_card)
        else:
            your_card = deck.pop()
            your_points += get_card_points(your_card)

        print(f'''
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============
        ''')

        if move == 1:
            print(f'Вам выпали карты {list_cards[0]} и {list_cards[1]}')
        else:
            print(f'Вам выпала карта {your_card}')

        
        if your_points > max_point:
            balance -= deposit
            print('Перебор')
            break
        elif your_points == max_point:
            more = 'нет'
        else:
            more = check_input(input('Ещё? да или нет\n'), ['да', 'нет'])
            move +=1

    else:
        while dealer_points <= min_dealer_point:
            dealer_card = deck.pop()
            dealer_points += get_card_points(dealer_card, True)
            print(f'Крупье выпала карта номиналом {dealer_card}')
            sleep(3)

        print(f'''
            =============
            ОЧКИ:
            Крупье: {dealer_points}
            Вы: {your_points}
            =============
            ''')
        
        if dealer_points > max_point:
            balance += deposit
            print("Вы выиграли")
        elif your_points == dealer_points:
            print('Ничья')
        else:
            balance += deposit
            print('Вы выиграли')

    play_again = check_input(input('Сыграем ещё? да или нет\n'), ['да', 'нет']) 