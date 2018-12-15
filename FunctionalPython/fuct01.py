from functools import partial
from multipledispatch import dispatch


class Thing(object): pass


class Rock(Thing): pass


class Paper(Thing): pass


class Scissors(Thing): pass


@dispatch(Rock, Rock)
def beats(x, y): return None


@dispatch(Rock, Paper)
def beats(x, y): return y


@dispatch(Rock, Scissors)
def beats(x, y): return x


@dispatch(Paper, Paper)
def beats(x, y): return None

paper = Paper()
rock = Rock()

print(beats(rock, paper))
