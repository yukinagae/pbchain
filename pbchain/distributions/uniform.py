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
        self.a = a
        self.b = b

    def sample(self):
        """sampling"""
        import random
        return self.a + random.random() * (self.b - self.b)

    def log_pdf(self, x):
        """log probability distribution function"""
        from math import log
        if x < self.a or x > self.b:
            return log(0.0)
        return log(1.0 / (self.b - self.a))

    def analytic_mean(self):
        """mean"""
        return 0.5 * (self.a + self.b)

    def analytic_var(self):
        """variance"""
        return (self.b - self.a) ** 2 / 12
