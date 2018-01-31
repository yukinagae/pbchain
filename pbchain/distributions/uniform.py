"""
Uniform distribution
"""

from scipy.stats import uniform


class Uniform():
    """
    Uniform distribution
    """

    def __init__(self, a, b, *args, **kwargs):
        """
        """
        self.a = a
        self.b = b

    def sample(self):
        return uniform.rvs(
                loc=self.a,
                scale=self.b - self.a
                )
