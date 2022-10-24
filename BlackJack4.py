import time
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4


class Player:

    def __init__(self, name):
        self.name = name
        self.handList = []
        self.hand = sum(self.handList)
        self.Ace = 0

    def bustCheck(self):
        if self.hand > 21 and 11 not in self.handList:
            print(f'{self.name} BUST!!!')
            quit()
        if self.hand > 21 and 11 in self.handList and self.Ace != 0:
            print(f'{self.name} BUST!!!')
            quit()
        elif self.hand > 21 and 11 in self.handList and self.Ace == 0:
            self.hand -= 10
            self.Ace += 1

    def pick(self):
        time.sleep(0.5)
        random.shuffle(cards)
        selection = cards.pop()
        self.handList.append(selection)
        print(f'card = {selection}')
        self.hand += selection
        self.bustCheck()
        print(f'{self.name} hand is: {self.hand}', end='\n\n')

    def continuePlayer(self):
        hit = ' '
        while hit != 'n':
            hit = input('Do you wish to hit Y/N?' + '\n').casefold()
            if hit == 'y':
                self.pick()

    def continueDealer(self):
        while self.hand < 17:
            self.pick()


player1 = Player('Player1')
dealer = Player('Dealer')


def evaluate():
    if player1.hand > dealer.hand:
        print('YOU WIN!!!')
    elif player1.hand == dealer.hand:
        print("IT'S A DRAW")
    elif player1.hand < dealer.hand:
        print('YOU LOSE :(((')


def main():
    dealer.pick()
    player1.pick()
    player1.pick()
    player1.continuePlayer()
    dealer.continueDealer()
    evaluate()


if __name__ == '__main__':
    main()