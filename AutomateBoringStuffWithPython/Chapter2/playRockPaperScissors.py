import random
import sys
print('ROCK,PAPER,SCISSORS')

winCount = 0
lossCount = 0
tieCount = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

while True:
    print(str(winCount) + ' Wins, ' + str(lossCount) + ' Losses, ' + str(tieCount) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors (q)uit')
    v = input()

    if(v == 'q'):
        sys.exit()
    else:
        myMove = random.randint(1,3)
        yourMove = 0
        if v == 'r':
            yourMove=ROCK
            print('ROCK vs...\n')
        elif v == 'p':
            yourMove=PAPER
            print('PAPER vs...\n')
        elif v == 's':
            yourMove=SCISSORS
            print('SCISSORS vs...\n')
        else:
            continue
        if myMove == ROCK:
            print('ROCK!')
        elif myMove == PAPER:
            print('PAPER!')
        elif myMove == SCISSORS:
            print('SCISSORS!')
        else:
            print('ERROR!!!: ' + str(myMove))
        tie = False
        win = False
        loss = False
        if yourMove==myMove:
            tie = True
        elif yourMove == ROCK and myMove == SCISSORS:
            win = True
        elif yourMove == SCISSORS and myMove == PAPER:
            win = True
        elif yourMove == PAPER and myMove == ROCK:
            win = True
        else:
            loss = True
        if win == True:
            print('You win!')
            winCount = winCount + 1
        elif tie == True:
            print('It is a tie!')
            tieCount = tieCount + 1
        elif loss == True:
            print('You Lose!')
            lossCount = lossCount + 1



