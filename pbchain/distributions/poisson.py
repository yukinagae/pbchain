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
        self._lam = lam

        # TODO: shape check

        super(Poisson, self).__init__(*args, **kwargs)

    @proerty
    def lam(self):
        return self._lam

    def sample(self, *args, **kwargs):
        pass # TODO: not yet implemented

    def log_pdf(self, x, *args, **kwargs):
        pass # TODO: not yet implemented

    def mean(self, *args, **kwargs):
        return self.lam

    def var(self, *args, **kwargs):
        return self.lam
