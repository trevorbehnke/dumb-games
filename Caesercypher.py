class Cypher():
    """A class representing an encrypted message."""

    def __init__(self, mode, key, message):
        """Initialize a single die."""
        self.mode = mode
        self.key = key
        self.message = message

    def encode(self):
        """Return the encrypted message"""

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        translated = ''

        mode = self.mode

        message = self.message

        if mode.startswith('e'):
            mode = 'encrypt'

        elif mode.startswith('d'):
            mode = 'decrypt'

        for symbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(SYMBOLS):
                    num = num - len(SYMBOLS)
                elif num < 0:
                    num = num + len(SYMBOLS)

                translated = translated + SYMBOLS[num]
            else:
                translated = translated + symbol

        return translated