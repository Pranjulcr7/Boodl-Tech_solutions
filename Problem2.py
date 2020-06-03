"""
Assumptions:
    None

Algorithm:
    1. divisor = 10^(number of digits - 1)
    2. While n != 0
        a. first = (int) n / divisor
        b. last = (int) n % 10
        c. if head != tail:
            return False
        d. remove first and last element from n
        e. divide divisor by 100
    3. return True

Time complexity : O(log(n))

Space complexity : O(1)
"""

from math import log10


def is_palindrome(n: int):
    """
    To check whether a integer is a palindrome or not
    :param n: integer
    :return: Boolean
    """
    digits = int(log10(n))  # to get number of digits - 1
    divisor = 10 ** digits

    while n is not 0:

        # to get the first element
        head = n // divisor

        # to get the last element
        tail = n % 10

        if head is not tail:
            return False

        # removing head element from n
        n %= divisor

        # removing tail element from n
        n //= 10

        # reducing divisor by 100 as two elements have been removed
        divisor //= 100

    return True
