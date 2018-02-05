"""
Uniform distribution
"""


import chainer.functions as F
import numpy as np


class Uniform():
    """
    Uniform distribution
    """

    def __init__(self, name, a, b):
        """
        initialize
        """
        self.name = name
        self.a = a
        self.b = b

    def __str__(self):
        return "Uniform(\"{}\",{},{})".format(self.name, self.a, self.b)

    def sample(self):
        """sampling"""
        eps = np.random.ranf(1)
        return self.a + eps * (self.b - self.a)

    def log_pdf(self, x):
        """log probability distribution function"""
        if x.data[0] < self.a.data[0] or x.data[0] > self.b.data[0]:
            return F.log(0.0)
        return F.log(1.0 / (self.b - self.a))

    def analytic_mean(self):
        """mean"""
        return 0.5 * (self.a + self.b)

    def analytic_var(self):
        """variance"""
        return (self.b - self.a) ** 2 / 12
