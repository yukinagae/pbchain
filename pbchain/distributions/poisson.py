"""
Poisson distribution
"""


import chainer.functions as F
import numpy as np

from pbchain.random_variable import RandomVariable


class Poisson(RandomVariable):
    """
    Poisson distribution
    """

    def __init__(self, lam):
        """
        initialize
        """
        self.lam = lam

    def sample(self):
        """sampling"""
        pass

    def log_pdf(self, x):
        """log probability distribution function"""
        pass

    def analytic_mean(self):
        """mean"""
        return self.lam

    def analytic_var(self):
        """variance"""
        return self.lam
