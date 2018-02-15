"""
Normal distribution
"""


from chainer import Variable
from scipy.stats import norm

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
        self._mu = mu
        self._sigma = sigma

        # TODO: shape check

        super(Normal, self).__init__(*args, **kwargs)

    @property
    def mu(self):
        return self._mu

    @property
    def sigma(self):
        return self._sigma

    def sample(self, *args, **kwargs):
        return norm.rvs(loc=self.mu.data, scale=self.sigma.data, size=self.mu.shape, random_state=None)

    def log_pdf(self, x, *args, **kwargs):
        if isinstance(x, Variable):
            return norm.logpdf(x.data, loc=self.mu.data, scale=self.sigma.data)
        return norm.logpdf(x, loc=self.mu.data, scale=self.sigma.data)

    def mean(self, *args, **kwargs):
        return norm.mean(loc=self.mu, scale=self.sigma)

    def var(self, *args, **kwargs):
        return norm.var(loc=self.mu, scale=self.sigma)
