"""
Poisson distribution
"""


from chainer import Variable

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

    def sample(self, *args, **kwargs):
        pass

    def log_pdf(self, x, *args, **kwargs):
        pass

    def mean(self, *args, **kwargs):
        return self.lam

    def var(self, *args, **kwargs):
        return self.lam
