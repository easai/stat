from src.stat import *
import pytest
from math import *


def test_moment():
    x = [.5, 1.8, -2.3, .9]
    x = [.5, 1.8, -2.3, .86, .32]
    x = [.5, 1.8, -23, .86, .32]
    x = [.5, 1.2, .6, -.7, -.2]

    total = 0
    for i in x:
        total += i
    print(f"total={total}")
    m1 = total / len(x)
    print(f"ave = {m1}")

    total = 0
    for i in x:
        total += (i * i)
    print(f"total squared={total}")
    m2 = total / len(x)
    print(f"E[X^2] = {m2}")

    sigma = sqrt(m2 - m1 * m1)
    print(f"sigma = {sigma}")

    for i in range(7):
        moment = Moment.moment(x, i)
        print(f"{i=} {moment=}")
