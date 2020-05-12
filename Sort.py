class Sort():
    """A class that sorts letters."""

    def __init__(self, word):
        """Initialize a word."""
        self.word = word

    def sort_word(self):
        """Return a sorted word."""
        return sorted(self.word)