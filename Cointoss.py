import random

class Coin():
    """A class representing a single die."""

    def __init__(self):
        """Initialize a single die."""
        # self.num_sides = num_sides

    def toss(self):
        """Return a random value between 1 and number of sides"""
        sides = ['Heads', 'Tails']
        return random.choice(sides)