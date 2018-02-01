"""
Uniform distribution
"""

from scipy.stats import uniform


class Uniform():
    """
    Uniform distribution
    """

    def __init__(self, a, b):
        """
        initialize
        """
        self.low = a
        self.high = b

    def mean(self):
        """mean"""
        return uniform.mean(loc=self.low, scale=self.high - self.low)

    def var(self):
        """variance"""
        return uniform.var(loc=self.low, scale=self.high - self.low)

    def sample(self):
        """sampling"""
        return uniform.rvs(loc=self.low, scale=self.high - self.low)
