"""
graph test
"""

import pytest

from pbchain.distributions.normal import Normal


def test_graph():

    a = Normal("a", mu=0.0, sigma=1.0)
    b = Normal("b", mu=a, sigma=1.0)
    c = Normal("c", mu=0.0, sigma=1.0)
    print(a.sample())
    # d = b + c
    # d = Normal("d", mu=b * c, sigma=1.0)

    # print(d)
