
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
d = [f"{value}_{suit}" for suit in suits for value in values]
print(d)

mas = ['J_hearts', 'Q_hearts', 'K_hearts', 'A_hearts']

def hand_value(hand):
    value_map = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    total = 0
    aces = 0

    for card in hand:
        rank = card.split('_')[0]
        print(rank)
        if rank in value_map:
            total += value_map[rank]
            if rank == 'A':
                aces += 1
        else:
            total += int(rank)

    while total > 21 and aces:
        total -= 10  # Перетворення туза з 11 на 1
        aces -= 1

    return total


print(hand_value(mas))
