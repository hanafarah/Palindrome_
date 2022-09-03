"""
Validates strings as palindromes.
"""

from collections import deque  # using the collection module


def is_palindrome(characters):
    """
    This function will take any characters and determine if it is palindrome
    or not.
    """
    characters = deque()  # create an empty list

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True


# is_palindrome('madam') # it will output as True
# is_palindrome('radar') # it will output as True
# is_palindrome('car') # it will output as False
