"""
Poisson distribution
"""


from chainer import Variable
import chainer.functions as F
import numpy as np

from pbchain.random_variable import RandomVariable


class Poisson(RandomVariable, Variable):
    """
    Poisson distribution
    """

    def __init__(self, lam, *args, **kwargs):
        """
        Args:
            lam (TODO: type): lam
        """
        self.lam = lam
        super(Poisson, self).__init__(*args, **kwargs)

    def sample(self):
        pass

    def log_pdf(self, x):
        pass

    def mean(self):
        return self.lam

    def var(self):
        return self.lam
