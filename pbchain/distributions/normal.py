"""
Normal distribution
"""


import chainer.functions as F
import numpy as np

from pbchain.random_variable import RandomVariable


class Normal(RandomVariable):
    """
    Normal distribution
    """

    def __init__(self, name, mu, sigma):
        """
        initialize
        """
        self.name = name
        self.mu = mu
        self.sigma = sigma

    def __str__(self):
        return "Normal(\"{}\",{},{})".format(self.name, self.mu, self.sigma)

    def sample(self):
        """sampling"""
        eps = np.random.ranf(1)
        return self.mu + eps * self.sigma

    def log_pdf(self, x):
        """log probability distribution function"""
        return -1 * (F.log(self.sigma) + 0.5 * np.log(2.0 * np.pi) + 0.5 * ((x - self.mu) / self.sigma) ** 2)

    def analytic_mean(self):
        """mean"""
        return self.mu

    def analytic_var(self):
        """variance"""
        return self.sigma ** 2
