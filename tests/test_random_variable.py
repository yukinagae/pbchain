"""
random variable test
"""

import pytest

import numpy as np
from pbchain.distributions.normal import Normal


def test_random_variable():

    print("")

    a = Normal(name="a", mu=np.array([0.0]), sigma=np.array([1.0]))
    b = Normal(name="b", mu=np.array([1.0]), sigma=np.array([10.0]))

    print("a: {}".format(a))
    print("a data: {}".format(a.array))
    print("a shape: {}".format(a.array.shape))
    print("b: {}".format(b))

    c = a + b
    print("c: {}".format(c))
    print("check: {}".format(a.data + b.data))

    d = Normal(name="d", mu=a, sigma=np.array([2.0]))
    print("d: {}".format(d))
    print("d data: {}".format(d.array))
    print("d shape: {}".format(d.array.shape))
