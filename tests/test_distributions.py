from pbchain.distribution import Uniform

def test_answer():
    uniform = Uniform(1.0, 2.0)
    print(uniform)
    assert (1 + 1) == 2
