from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides):
        """Initialize a single die."""
        self.num_sides = num_sides

    def toss(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)