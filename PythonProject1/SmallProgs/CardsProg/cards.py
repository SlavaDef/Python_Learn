import random

cards = ['2_hearts', '3_hearts', '4_hearts','5_hearts','6_hearts', '7_hearts', '8_hearts', '9_hearts',
         '10_hearts', 'J_hearts', 'Q_hearts', 'K_hearts', 'A_hearts', '2_diamonds', '3_diamonds',
         '4_diamonds','5_diamonds','6_diamonds', '7_diamonds', '8_diamonds', '9_diamonds', '10_diamonds',
         'J_diamonds', 'Q_diamonds', 'K_diamonds', 'A_diamonds',
         '2_spades', '3_spades', '4_spades','5_spades','6_spades', '7_spades', '8_spades', '9_spades',
         '10_spades', 'J_spades', 'Q_spades', 'K_spades', 'A_spades', '2_clubs', '3_clubs',
         '4_clubs','5_clubs','6_clubs', '7_clubs', '8_clubs', '9_clubs', '10_clubs',
         'J_clubs', 'Q_clubs', 'K_clubs', 'A_clubs']



def shuffle(car):
    for i in range(4):
        random.shuffle(car)


def remember():
    shuffle(cards)

    first_card = random.choice(cards)
    second_card = random.choice(cards)
    cards.remove(first_card)
    cards.remove(second_card)
    card_list = [first_card, second_card]

    print('Your cards is:', first_card, second_card, 'count = ', count_cards(card_list), sep=' ')



    tempo = play(card_list)
    a = 0
    if tempo <= 20:
        a = comp_play(cards)
    if tempo > a and a!=0:
        print('You win!')

    elif tempo < a < 22:
        print('Computer win!')
    elif tempo < a >= 22:
        print('You win!')
    elif tempo == a:
        print('Draw!')



def play(card_list):
    temp = True
    while True:
        try:
           choiсe = int(input('1. Stop\n2. Continue\n> '))
           if choiсe == 1:
               break
           if choiсe == 2:
               new_card = random.choice(cards)
               card_list.append(new_card)
               cards.remove(new_card)
               print('Your cards is:', card_list, 'count = ', count_cards(card_list), end=' ')
               print()
               if count_cards(card_list) > 21:
                   print('You lose!')
                   temp = False
                   break
               if count_cards(card_list) == 21:
                   print('Congratulations, You win!')
                   temp = False
                   break

        except ValueError:
            print("❌ Некоректний ввід! Спробуйте ще раз.")
    #return temp
    return  count_cards(card_list)



def comp_play(cards2):

    new_card = random.choice(cards2)
    new_card2 = random.choice(cards2)
    card_list22 = [new_card, new_card2]
    cards2.remove(new_card)
    cards2.remove(new_card2)

    while True:
        print('Computer cards is:', card_list22, 'count =', count_cards(card_list22))

        if count_cards(card_list22) <= 19:
            print('Computer to continue')
            new_card3 = random.choice(cards2)
            card_list22.append(new_card3)
            cards2.remove(new_card3)

        if count_cards(card_list22) == 20:
            print('Computer cards is:', card_list22, 'count =', count_cards(card_list22))
            break

        if count_cards(card_list22) == 21:
            print('Computer cards is:', card_list22, 'count =', count_cards(card_list22))
            print('Comp win!')
            break

        if count_cards(card_list22) > 21:
            print('Computer cards is:', card_list22, 'count =', count_cards(card_list22))
            print('Comp to get over, player win!')
            break
    return count_cards(card_list22)


def count_cards(cards_list):

    result68 = 0
    for i in cards_list:

        res = i.split('_')

        try:
            new_res = int(res[0])
            result68+=new_res
        except ValueError:

            if res[0] == 'J':
               new_res = 2
               result68 += new_res

            if res[0] == 'Q':
               new_res = 3
               result68 += new_res

            if res[0] == 'K':
                new_res = 4
                result68 += new_res

            if res[0] == 'A':
                new_res = 11
                result68 += new_res

    return result68



remember()







