"""
Normal distribution
"""


from chainer import Variable
import chainer.functions as F
import numpy as np

from pbchain.random_variable import RandomVariable


class Normal(RandomVariable, Variable):
    """
    Normal distribution
    """

    def __init__(self, mu, sigma, *args, **kwargs):
        """
        Args:
            mu (TODO: type): mu
            sigma (TODO: type): sigma
        """
        self.mu = mu
        self.sigma = sigma

        # TODO: shape check => mu, sigma

        super(Normal, self).__init__(*args, **kwargs)

    def sample(self, *args, **kwargs):
        eps = np.random.random_sample(self.mu.shape).astype(self.mu.dtype)
        return self.mu + eps * self.sigma

    def log_pdf(self, x, *args, **kwargs):
        return -1 * (
            F.log(self.sigma) + 0.5 * np.log(2.0 * np.pi) +
            0.5 * ((x - self.mu) / self.sigma) ** 2
        )

    def mean(self, *args, **kwargs):
        return self.mu

    def var(self, *args, **kwargs):
        return self.sigma ** 2
