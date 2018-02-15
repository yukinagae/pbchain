"""
graph test
"""

import pytest
import numpy as np
from pbchain.distributions.normal import Normal


def test_get_parents():

    print("")

    a = Normal(name="a", mu=np.array([0.0]), sigma=np.array([1.0]))
    b = Normal(name="b", mu=a.data, sigma=np.array([1.0]))
    c = Normal(name="c", mu=np.array([0.0]), sigma=np.array([1.0]))
    d = Normal(name="d", mu=b*c, sigma=np.array([1.0]))

    print("a data: {}".format(a.data))
    print("a _data: {}".format(a._data))
    print("b data: {}".format(b.data))
    print("b _data: {}".format(b._data))
    print("c data: {}".format(c.data))
    print("c _data: {}".format(c._data))

    print("parents: {}".format(d.get_parents()))

    # assert set(d.get_parents()) == set([b, c])


def test_get_children():
    pass
