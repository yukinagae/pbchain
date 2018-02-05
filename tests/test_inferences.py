"""
inferences test
"""

import pytest

from chainer import Variable
import numpy as np

from pbchain.distributions.uniform import Uniform
from pbchain.distributions.normal import Normal
from pbchain.inferences.map import MAP, Guess


def test_map_run():
    # input
    x_data = np.array([9.72421399, 9.44789193, 10.12074736, 10.74821562, 11.60869097])
    sd = 1.0
    a, b = (9.0, 12.0)
    print(x_data)

    # model
    mu = Uniform("mu", a=a, b=b)
    x = Normal("x", mu=mu, sigma=1.0)
    print(x)

    # TODO: guess
    qmu = Guess(10.0)

    # inference
    inference = MAP(vars={mu: mu}, data={x: x_data})
    inference.run(n_iter=1000)
