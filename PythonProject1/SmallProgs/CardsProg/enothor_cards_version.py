import random


class Blackjack:
    def __init__(self):
        self.deck = self.create_deck() # в конструкторі створюємо масив через метод create_deck()
        random.shuffle(self.deck) # перемішуємо масив


    def create_deck(self):
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # List comprehension генерує всі можливі комбінації, використовуючи вкладені цикли:
        # кожному значенню з масиву suits присвоється кожне значення з масиву values
        return [f"{value}_{suit}" for suit in suits for value in values]


    def deal_card(self):
        # deck.pop() видалить і поверне карту з масиву, роздача (мій спосіб був вибрати рендомну і потім її видалити)
        return self.deck.pop() if self.deck else None


    def hand_value(self, hand):
        value_map = {'J': 10, 'Q': 10, 'K': 10, 'A': 11} # dictionary
        total = 0
        aces = 0

        for card in hand: # hand = massive
            rank = card.split('_')[0] # get masive with J-A or 2-10
            if rank in value_map: # keys, first in dictionary
                total += value_map[rank] # total = total + value( it is number)  of the dictionary
                if rank == 'A': # if our key is 'A'
                    aces += 1 # aces+1
            else:
                total += int(rank) # else we have numbers 2-10 total=total+(2-10)

        while total > 21 and aces: # поки в руці є туз і total > 21
            total -= 10  # Перетворення туза з 11 на 1
            aces -= 1 # кожний туз + 1 к aces (лічильник тузів)

        return total # return our count


    def player_turn(self, hand):
        while True:
            print(f"Your cards: {hand}, count = {self.hand_value(hand)}") # отримуємо пару карт, рахуємо суму
            choice = input("1. Stop\n2. Continue\n> ") # вибір - далі чи стоп
            if choice == '1':
                break
            elif choice == '2':
                hand.append(self.deal_card())# в масив карт в руці додаємо якусь карту видалену з кінця колоди
                if self.hand_value(hand) > 21:# якщо в процесі підрахунку-обробки на руці більше чим 21
                    print(f"Your cards: {hand}, count = {self.hand_value(hand)}")# показуємо карти і каунт
                    print("You lose!")
                    return self.hand_value(hand)
            else:
                print("❌ Invalid input! Try again.")
        return self.hand_value(hand) # повертаємо кількість очок щоб далі їх порівняти з кілістю у компа


    def computer_turn(self):
        hand = [self.deal_card(), self.deal_card()] # комп отримує дві карти з кінця колоди видаливши їх з масиву карт
        while self.hand_value(hand) < 17: # поки метод повертає менше 17
            hand.append(self.deal_card()) # додаємо карту
        print(f"Computer's cards: {hand}, count = {self.hand_value(hand)}") # друк карт компа і його очки
        return self.hand_value(hand) # повертаємо загальну кількість очок компа


    def play_game(self):
        player_hand = [self.deal_card(), self.deal_card()] # початкові дві карти людини
        player_score = self.player_turn(player_hand) # в метод гри для гравця передаємо руку гравця

        if player_score > 21:
            return # вихід з методу бо гравець перебрав далі порівняння не йде

        computer_score = self.computer_turn()

        if computer_score > 21 or player_score > computer_score:
            print("You win!")
        elif player_score < computer_score:
            print("Computer wins!")
        else:
            print("Draw!")


if __name__ == "__main__":
    game = Blackjack()
    game.play_game()


#  Як це працює?
# total > 21 – перевіряємо, чи загальна кількість очок більше 21 (тобто перебір).
#
# aces – перевіряємо, чи є у нас тузи, які ще рахуються як 11.
#
# Якщо обидві умови True, то:
#
# Віднімаємо 10 від загальної суми (total -= 10), змінюючи один туз з 11 на 1.
#
# Зменшуємо лічильник тузів (aces -= 1), щоб більше не рахувати цей туз як 11.
#
# Якщо після цього total все ще > 21 і залишились тузи, цикл повторюється.

# Цей цикл автоматично коригує значення тузів, зменшуючи їх з 11 до 1, якщо загальна сума перевищує 21.
# 🔹 Це гарантує, що гравець отримає найбільш вигідний варіант підрахунку очок.
# 🔹 Використання while забезпечує гнучке коригування, навіть якщо в руці кілька тузів.


# if __name__ == "__main__":?
# Цей рядок використовується для перевірки, як саме запускається скрипт.
# Він дозволяє розрізняти, чи код виконується як основний файл чи його імпортують як модуль.
#
# 🔹 Як це працює?
# У Python кожен файл є модулем, і в ньому є спеціальна змінна __name__.
#
# Якщо файл запускається напряму (python my_script.py):
#
# __name__ буде рівним "__main__", отже, код у if __name__ == "__main__": буде виконаний.
#
# Якщо файл імпортують у інший файл (import my_script):
#
# __name__ буде "my_script" (назва файлу без .py), отже, код у if __name__ == "__main__": не виконається.

# Навіщо це потрібно?
# Щоб відокремити код, який виконується тільки при запуску напряму.
#
# Наприклад, blackjack.py може містити функції та класи, які можна імпортувати.
#
# Але якщо він запущений напряму, треба розпочати гру.
#
# Для тестування модулів.
#
# Коли пишеш код, можна додати print() або тестові виклики в if __name__ == "__main__":, щоб вони не заважали при імпорті.
#
# Щоб зробити скрипт багаторазовим.
#
# Код можна запускати напряму або використовувати в інших програмах без непотрібних побічних ефектів.