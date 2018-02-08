"""
random variable test
"""

import pytest

from pbchain.distributions.normal import Normal


def test_random_variable():

    a = Normal(name="a", mu=0.0, sigma=1.0)
    b = Normal(name="b", mu=1.0, sigma=10.0)

    print(a)
    print(b)

    c = a + b
    print(c)
