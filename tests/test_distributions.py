from pbchain.distributions.uniform import Uniform


def test_uniform_distribution():
    uniform = Uniform(1.0, 2.0)
    assert uniform.a == 1.0
    assert uniform.b == 2.0
    for i in range(0, 10):
        sample = uniform.sample()
        assert 1.0 <= sample <= 2.0
