# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

# while True:
#     print('Do you want to (e)ncrypt or (d)ecrypt')
#     response = input().lower()
#     if response.startswith('e'):
#         mode = 'encrypt'
#         break
#     elif response.startswith('d'):
#         mode = 'decrypt'
#         break
#     print('Please enter "e" or "d"')

# while True:
#     print('Please enter a numeric key from 0 to {}'.format(len(SYMBOLS)))
#     response = input().upper
#     if not response().isdecimal():
#         print("Please enter an integer")
#         continue
#     if 0 <= int(response()) < len(SYMBOLS):
#         key = int(response())
#         break

# print('Enter the message to {}'.format(mode))
# message = input()

# message = message.upper()

# translated = ''

# for symbol in message:
#     if symbol in SYMBOLS:
#         num = SYMBOLS.find(symbol)
#         if mode == 'encrypt':
#             num = num + key
#         elif mode == 'decrypt':
#             num = num - key

#         if num >= len(SYMBOLS):
#             num = num - len(SYMBOLS)
#         elif num < 0:
#             num = num + len(SYMBOLS)

#         translated = translated + SYMBOLS[num]
#     else:
#         translated = translated + symbol

# print(translated)


class Cypher():
    """A class representing an encrypted message."""

    def __init__(self, key, message):
        """Initialize a single die."""
        self.key = key
        self.message = message

    def encode(self):
        """Return the encrypted message"""

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        translated = ''

        message = self.message

        for symbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                num = num + self.key

                if num >= len(SYMBOLS):
                    num = num - len(SYMBOLS)
                elif num < 0:
                    num = num + len(SYMBOLS)

                translated = translated + SYMBOLS[num]
            else:
                translated = translated + symbol

        return translated