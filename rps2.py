import random

class RPS():

    def __init__(self, mychoice):
        self.mychoice = mychoice

    def round(self):
        choice = ['rock', 'paper', 'scissors']

        mychoice = self.mychoice

        compchoice = random.choice(choice)
    
        if mychoice == 'rock':
            print('ROCK versus...')
        elif mychoice == 'paper':
            print('PAPER versus...')
        elif mychoice == 'scissors':
            print('SCISSORS versus...')


        if compchoice == 'rock':
            print('ROCK')
        elif compchoice == 'paper':
            print('PAPER')
        elif compchoice == 'scissors':
            print('SCISSORS')


        if mychoice == compchoice:
            print("It's a tie")
        elif mychoice == 'rock' and compchoice == 'paper':
            print('You lost!')
        elif mychoice == 'rock' and compchoice == 'scissors':
            print('You win!')
        elif mychoice == 'paper' and compchoice == 'rock':
            print('You win!')
        elif mychoice == 'paper' and compchoice == 'scissors':
            print('You win!')
        elif mychoice == 'scissors' and compchoice == 'rock':
            print('You lose!')
        elif mychoice == 'scissors' and compchoice == 'paper':
            print('You win!')

        return(mychoice, compchoice)