from Excercises.euler.problem01 import problem001, problem002, problem003, \
    get_prime_sieve


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
