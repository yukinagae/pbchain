"""
distributions test
"""

import pytest

from chainer import Variable
import numpy as np

from pbchain.distributions.uniform import Uniform


def test_uniform_distribution():
    """uniform distribution test"""
    a = Variable(np.array([1.0]).astype(np.float32))
    b = Variable(np.array([3.0]).astype(np.float32))
    uniform = Uniform(a, b)
    assert uniform.a.data[0] == a.data[0]
    assert uniform.b.data[0] == b.data[0]
    x = Variable(np.array([1.95]).astype(np.float32))
    log_pdf = uniform.log_pdf(x)
    assert log_pdf.data[0] == pytest.approx(-0.6931471824645996, abs=1e-5)
    for _ in range(0, 100):
        sample = uniform.sample()
        assert a.data[0] <= sample.data[0] <= b.data[0]
