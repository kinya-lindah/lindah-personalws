import time
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


player1 = Player("Player 1")
computer = Player("Computer")


class Game:
    def __init__(self):
        self.winner = False
        self.chosen1 = None
        self.chosen2 = None
        self.docontinue = True
        self.gamenumber = 1

        while not self.winner and self.docontinue:
            print(f'Game number {self.gamenumber}')
            time.sleep(1)
            self.rules()
            time.sleep(1)
            self.playerchoice()

    def winners(self, x, y):  #player 1 rps= x, player 2 rps=y
        if (x == "s" and y == "p") or (x == "r" and y == "s") or (x == "p" and y == "r"):
            self.winner = True
            player1.score += 1
            time.sleep(1)
            print(f"\nPlayer 1 wins!\n\nPlayer 1 chose {x} and computer chose {y}. \n\nThe current score is \nPlayer 1: {player1.score} \nComputer: {computer.score}\n")

        elif (y == "s" and x == "p") or (y == "r" and x == "s") or (y == "p" and x == "r"):
            self.winner = True
            computer.score += 1
            time.sleep(1)
            print(f"\nComputer wins! \n\nPlayer 1 chose {x} and computer chose {y}.\n\nThe current score is \nPlayer 1: {player1.score} \nComputer: {computer.score}\n")

        else:
            print(f"\nIt was a draw\n\nPlayer 1 chose {x} and computer chose {y}.\n\nThe current score is: \nPlayer 1: {player1.score} \nComputer: {computer.score}\n")
        time.sleep(2)
        decision = input("Do you want to continue y/n: ").lower()

        if decision == 'y':
            self.docontinue = True
            self.winner = False
            self.gamenumber += 1
        else:
            self.docontinue = False

    def rules(self):
        print("Paper beats rock, rock beats scissors and scissors beats paper.")

    def playerchoice(self):
        self.chosen1 = input("\nPlease choose r for rock, p for paper and s for scisors: ").lower()
        self.chosen2 = random.choice(['r', 'p','s'])
        self.winners(self.chosen1, self.chosen2)


Game()