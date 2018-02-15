"""
Uniform distribution
"""


from chainer import Variable
import chainer.functions as F
import numpy as np

from pbchain.random_variable import RandomVariable


class Uniform(RandomVariable, Variable):
    """
    Uniform distribution
    """

    def __init__(self, a, b, *args, **kwargs):
        """
        Args:
            a (TODO: type): lower
            b (TODO: type): higher
        """
        self.a = a
        self.b = b
        super(Uniform, self).__init__(*args, **kwargs)

    def sample(self, *args, **kwargs):
        """sampling"""
        eps = np.random.random_sample()
        return self.a + eps * (self.b - self.a)

    def log_pdf(self, x, *args, **kwargs):
        """log probability distribution function"""
        if x.data[0] < self.a.data[0] or x.data[0] > self.b.data[0]:
            return F.log(0.0)
        return F.log(1.0 / (self.b - self.a))

    def mean(self, *args, **kwargs):
        """mean"""
        return 0.5 * (self.a + self.b)

    def var(self, *args, **kwargs):
        """variance"""
        return (self.b - self.a) ** 2 / 12
