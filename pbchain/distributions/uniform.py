"""
Uniform distribution
"""


from chainer import Variable
import chainer.functions as F
import numpy as np
from scipy.stats import uniform

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
        return self._a

    @property
    def b(self):
        return self._b

    def sample(self, *args, **kwargs):
        return uniform.rvs(loc=self.a.data, scale=self.b.data-self.a.data, size=self.a.shape, random_state=None)

    def log_pdf(self, x, *args, **kwargs):
        if isinstance(x, Variable):
            return uniform.logpdf(x.data, loc=self.a.data, scale=self.b.data-self.a.data)
        return norm.logpdf(x, loc=self.a.data, scale=self.b.data-self.a.data)

    def mean(self, *args, **kwargs):
        return 0.5 * (self.a + self.b)

    def var(self, *args, **kwargs):
        return (self.b - self.a) ** 2 / 12
