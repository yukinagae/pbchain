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
        self._a = a
        self._b = b

        # TODO: shape check

        super(Uniform, self).__init__(*args, **kwargs)

    @property
    def a(self):
        """lower property"""
        return self._a

    @property
    def b(self):
        """higher property"""
        return self._b

    def sample(self, *args, **kwargs):
        eps = np.random.random_sample(self.a.shape)
        return self.a + eps * (self.b - self.a)

    def log_pdf(self, x, *args, **kwargs):
        if x.data[0] < self.a.data[0] or x.data[0] > self.b.data[0]:
            return F.log(0.0)
        return F.log(1.0 / (self.b - self.a))

    def mean(self, *args, **kwargs):
        return 0.5 * (self.a + self.b)

    def var(self, *args, **kwargs):
        return (self.b - self.a) ** 2 / 12
