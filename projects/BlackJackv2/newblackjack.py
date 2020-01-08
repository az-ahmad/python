import random

playerList = []

def greeting():
    print('Welcome to BlackJack 2 player v.02')
    while True:
        try:
            numPlayers = int(input('How many players will there be? '))
        except:
            print('Enter a valid number between 1 and 10')
            continue
        if numPlayers>0 and numPlayers<10:
            break
    while numPlayers > 0:
        player = input('Enter a players name: ')
        playerList.append(player)
        numPlayers-=1
    print('Welcome:', ', '.join(playerList[:-1]), 'and', ''.join(playerList[-1])+'.')

if __name__ == "__main__":
    greeting()