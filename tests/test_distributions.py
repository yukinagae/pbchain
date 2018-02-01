"""
distributions test
"""

from pbchain.distributions.uniform import Uniform


def test_uniform_distribution():
    """uniform distribution test"""
    low = 1.0
    high = 2.0
    uniform = Uniform(low, high)
    assert uniform.low == low
    assert uniform.high == high
    for _ in range(0, 10):
        sample = uniform.sample()
        assert low <= sample <= high
        mean = uniform.mean()
        assert mean == (low + high) / 2
        var = uniform.var()
        assert var == (low - high) ** 2 / 12
