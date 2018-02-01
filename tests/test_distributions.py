"""
distributions test
"""

import pytest

from chainer import Variable
import numpy as np

from pbchain.distributions.uniform import Uniform
from pbchain.distributions.normal import Normal


def test_uniform_distribution():
    """uniform distribution test"""
    a = Variable(np.array([1.0]).astype(np.float32))
    b = Variable(np.array([3.0]).astype(np.float32))
    uniform = Uniform(a, b)
    x = Variable(np.array([1.95]).astype(np.float32))
    log_pdf = uniform.log_pdf(x)
    assert log_pdf.data[0] == pytest.approx(-0.6931471824645996, abs=1e-5)
    for _ in range(0, 100):
        sample = uniform.sample()
        assert a.data[0] <= sample.data[0] <= b.data[0]


def test_normal_distribution():
    """normal distribution test"""
    a = Variable(np.array([1.0]).astype(np.float32))
    b = Variable(np.array([3.0]).astype(np.float32))
    normal = Normal(a, b)
    x = Variable(np.array([1.95]).astype(np.float32))
    log_pdf = normal.log_pdf(x)
    assert log_pdf.data[0] == pytest.approx(-2.067689895629883, abs=1e-5)
    # for _ in range(0, 100):
    #     sample = normal.sample()
    #     TODO: how to assert?
