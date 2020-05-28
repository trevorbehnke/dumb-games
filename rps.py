"""Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
The classic hand game of luck.
This and other games are available at https://nostarch.com/XX
Tags: short, game"""
__version__ = 0
import random, time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # Main game loop.
    while True:  # Keep asking until player enters R, P, S, or Q.
        playerMove = input('> ').upper()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break

    # Display what the player chose:
    if playerMove == 'R':
        print('ROCK versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'

    

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'ROCK'
    elif randomNumber == 2:
        computerMove = 'PAPER'
    elif randomNumber == 3:
        computerMove = 'SCISSORS'
        print(computerMove)


    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It\'s a tie!')
        
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
       
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
      
    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You lose!')
       
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You lose!')
       
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lose!')
        