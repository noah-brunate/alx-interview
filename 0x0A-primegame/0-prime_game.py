#!/usr/bin/python3
"""Module defines the isWinner() function"""


def sieve_of_eratosthenes(n):
    primes = []  # List to store the prime numbers
    is_prime = [True] * (n+1)  # Initialize a list to mark numbers as Prime

    # Mark all multiples of 2 as non-prime
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            primes.append(p)  # Add the prime number to the list
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Add the remaining prime numbers to the list
    for p in range(int(n**0.5) + 1, n + 1):
        if is_prime[p]:
            primes.append(p)

    return primes


def isWinner(x, nums):
    """function returns a winner of the game"""

    if not nums or x < 1:
        return None

    Maria = 0
    Ben = 0

    for i in nums:
        if i == 0:
            Ben += 1
        if i < 0:
            return None
        primes = sieve_of_eratosthenes(i)
        size = len(primes)
        if size % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return 'Ben'
    elif Ben < Maria:
        return 'Maria'
    else:
        return None
