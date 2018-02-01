"""
distributions test
"""

import pytest

from pbchain.distributions.uniform import Uniform


def test_uniform_distribution():
    """uniform distribution test"""
    a = 1.0
    b = 3.0
    uniform = Uniform(a, b)
    assert uniform.a == a
    assert uniform.b == b
    for _ in range(0, 10):
        sample = uniform.sample()
        assert a <= sample <= b
        log_pdf = uniform.log_pdf(1.95)
        assert log_pdf == pytest.approx(-0.6931471824645996, abs=1e-5)
