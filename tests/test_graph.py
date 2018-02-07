"""
graph test
"""

import pytest

from pbchain.distributions.normal import Normal


def test_graph():

    a = Normal(name="a", mu=0.0, sigma=1.0)
    b = Normal(name="b", mu=a, sigma=1.0)
    c = Normal(name="c", mu=0.0, sigma=1.0)
    d = Normal("d", mu=b + c, sigma=1.0)

    print(d)
