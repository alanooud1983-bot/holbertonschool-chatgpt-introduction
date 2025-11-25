#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n. It is denoted by n! and defined as:
    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
    By definition, 0! = 1.

    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the given number n.

    Examples:
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
