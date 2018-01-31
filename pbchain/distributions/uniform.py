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
        """
        self.a = a
        self.b = b
        self.dist = uniform(a, b)
