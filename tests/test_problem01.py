import pytest

from Excercises.euler.problem01 import problem001, problem002, problem003, \
    get_prime_sieve, problem004, get_min_and_max_from_digit_count, \
    is_palindrome, problem005


def test_problem001():
    assert problem001(1000) == 233168


def test_problem002():
    assert problem002(4000000) == 4613732


def test_problem003_a():
    assert problem003(13195) == 29


def test_problem003_b():
    assert problem003(600851475143) == 6857


def test_problem003_c():
    assert problem003(25698751364526) == 328513


def test_get_primes():
    limit = 100
    prime_list = get_prime_sieve(limit)
    assert prime_list == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


@pytest.mark.parametrize('digit_count, max_palindrome', ([
    (2, 9009),
    (3, 906609)
]))
def test_problem004(digit_count, max_palindrome):
    assert problem004(digit_count) == max_palindrome


def test_generate_palindrom():
    pass


@pytest.mark.parametrize("param, result", [(4, (1111, 9999))])
def test_get_max_from_digit_count(param, result):
    assert get_min_and_max_from_digit_count(param) == result


@pytest.mark.parametrize('number, is_pal', ([
    (9009, True),
    (8448, True),
    (8765, False)
]))
def test_is_palindrome(number, is_pal):
    assert is_palindrome(number) == is_pal


@pytest.mark.parametrize("to_range_divisible, smallest_result", [
    (10, 2520),
    (20, 232792560)
])
def test_problem_005(to_range_divisible, smallest_result):
    assert problem005(to_range_divisible) == smallest_result
