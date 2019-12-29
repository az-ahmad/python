from random import shuffle

print('Hello and welcome to Black Jack 2-Player Ultimate Edition With Bonus DLC')
player1 = ''
player2 = ''
while player1 == '':
    player1 = input('Please enter the name of Player 1: ')

while player2 == '':
    player2 = input('Please enter the name of Player 2: ')
print(f'Welcome {player1} and {player2} to Blackjack. {player1} will go first.')

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
deck = []
player1hand = []
player2hand = []
player1value = 0
player2value = 0
player1bust = False
player2bust = False


class Deck:

    def __init__(self):

        for suit in suits:
            for rank in ranks:
                deck.append([rank, suit])
        print('\nDeck Created\n')

        print('\nShuffling Deck\n')
        shuffle(deck)


newdeck = Deck()

player1hand.append(deck.pop())
player1hand.append(deck.pop())
player2hand.append(deck.pop())
player2hand.append(deck.pop())

print(f'{player1} has the following cards:')
for cards in player1hand:
    print("{} of {}".format(str(cards[0]), str(cards[1])))
#     player1value+=values[cards[0]]
# print(f"{player1}'s hand total value : {player1value}")
print(f'\n{player2} has the following cards:')
for cards in player2hand:
    print(str(cards[0]) + ' of ' + str(cards[1]))
#     player2value+=values[cards[0]]
# print(f"{player2}'s hand total value : {player2value}")


while True:
    player1HS = input(f'\n{player1}, would you like to hit or stand? Type "H" or "S"')
    if player1HS.lower() == 'h':
        print(f'{player1} hits\n')
        print(f"{player1}'s new hand: ")
        pop1 = deck.pop()
        #         player1value+=values[pop1[0]]
        player1hand.append(pop1)
        for cards in player1hand:
            print("{} of {}".format(str(cards[0]), str(cards[1])))
        for cards in player1hand:
            player1value += values[cards[0]]

        for cards in player1hand:
            if cards[0] == 'Ace' and player1value > 21:
                player1value -= 10
        print(player1value)
        if player1value > 21:
            print('BUST')
            player1bust = True
            break
        elif player1value == 21:
            print('BLACKJACK!')
            break
        else:
            continue
    elif player1HS.lower() == 's':
        player1value = 0
        for cards in player1hand:
            player1value += values[cards[0]]
        print(f'{player1} stands on {player1value}')
        break
print(f"\n{player2}'s turn: \n")
while True:
    player2HS = input(f'\n{player2}, would you like to hit or stand? Type "H" or "S"')
    if player2HS.lower() == 'h':
        print(f'{player2} hits\n')
        print(f"{player2}'s new hand: ")
        pop2 = deck.pop()
        player2hand.append(pop2)
        #         player2value+=values[pop2[0]]
        for cards in player2hand:
            print("{} of {}".format(str(cards[0]), str(cards[1])))
        for cards in player2hand:
            player2value += values[cards[0]]
        for cards in player2hand:
            if cards[0] == 'Ace' and player2value > 21:
                player2value -= 10
        print(player2value)
        if player2value > 21:
            print('BUST')
            player2bust = True
            break
        elif player2value == 21:
            print('BLACKJACK!')
            break
        else:
            continue
    elif player2HS.lower() == 's':
        player2value = 0
        for cards in player2hand:
            player2value += values[cards[0]]
        print(f'{player2} stands on {player2value}')
        break
if player1bust == True:
    print(f'{player2} WINS')
elif player2bust == True:
    print(f'{player1} WINS')
elif player1value > player2value and player1value <= 21:
    print(f'{player1} WINS')
elif player2value > player1value and player2value <= 21:
    print(f'{player2} WINS')