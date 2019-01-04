from Excercises.euler.problem01 import problem001, problem002


def test_problem001():
    assert problem001(1000) == 233168


def test_problem002():
    assert problem002(4000000) == 4613732
