import math
import operator
from functools import reduce


def problem001(count):
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    :param count:
    :return:
    '''

    values = (x for x in range(1, count) if x % 5 == 0 or x % 3 == 0)
    return reduce(lambda x, y: x + y, values)


def problem002(limit):
    '''

    Each new term in the Fibonacci sequence is generated by adding the previous
     two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    '''

    n = 1

    list_of_fibs = [n]
    while True:
        previous = n
        n = list_of_fibs[-1]
        fib = previous + n

        if fib > limit:
            break
        list_of_fibs.append(fib)

    return sum(filter(lambda x: x % 2 == 0, list_of_fibs))


def problem003(number):
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

        divide number by 2
        generate all primes until get that number
        check max num that divides without reminder
    '''
    max_prime = -1

    while number % 2 == 0:
        max_prime = 2
        number >>= 1

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            max_prime = i
            number /= i

    if number > 2:
        max_prime = number

    return int(max_prime)


def get_prime_sieve(limit):
    m = limit + 1

    numbers = [True] * m
    for i in range(2, int(limit ** 0.5 + 1)):
        if numbers[i]:
            for j in range(i * i, m, i):
                numbers[j] = False
    primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
    return primes


def is_prime(a):
    if a < 2:
        return False
    if a != 2 and a % 2 == 0:
        return False
    else:
        return all(a % i for i in range(3, int(a ** 0.5) + 1))


def get_primes(limit):
    primes = []
    while limit % 2 == 0:
        primes.append(2)
        limit >>= 1

    for i in range(3, int(math.sqrt(limit)) + 1, 2):
        while limit % i == 0:
            primes.append(i)
            # limit /= i

    return primes


def problem004(digit_count):
    '''
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    :return:
    '''
    min_val, max_val = get_min_and_max_from_digit_count(digit_count)
    max_palindrome = -1

    for i in range(min_val, max_val + 1):
        for j in range(min_val, max_val + 1):
            product = i * j
            if is_palindrome(product):
                if product > max_palindrome:
                    max_palindrome = product

    return max_palindrome


def get_min_and_max_from_digit_count(num):
    if isinstance(num, int):
        return int('1' * num), int('9' * num)
    else:
        raise Exception("you need provide a number")


def is_palindrome(number):
    '''
    checks whether the int number is a palindrome
    :param number:
    :return:
    '''
    str_number = str(number)

    return bool(str_number == str_number[::-1])


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    '''
    lowest
    :param a:
    :param b:
    :return:
    '''
    return (a * b) / gcd(a, b)


def problem005(to_range_divisible):
    '''
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20?

    :param to_range_divisible:
    :return:
    '''
    values = list(range(1, to_range_divisible + 1))
    return int(reduce(lcm, values))


def problem006(range_num):
    """
    The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    :return:
    """
    values = range(0, range_num + 1)
    sum_of_squares = reduce(lambda x, y: x + math.pow(y, 2),
                            values)
    square_of_sum = math.pow(reduce(operator.add, values), 2)

    return int(square_of_sum - sum_of_squares)


def problem007(limit):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
    see that the 6th prime is 13.
    What is the 10 001st prime number?
    :param limit:
    :return:
    """

    primes = get_prime_sieve(limit)
    return primes[-1]
