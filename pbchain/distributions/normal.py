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
        initialize
        """
        self.mu = mu
        self.sigma = sigma
        super(Normal, self).__init__(*args, **kwargs)

    def __str__(self):
        return "Normal(\"{}\",{},{})".format(self.name, self.mu, self.sigma)

    def sample(self):
        """sampling"""
        eps = np.random.random_sample(self.sample_shape)
        print("eps: {}".format(eps))
        print("mu: {}".format(self.mu))
        if isinstance(self.mu, Variable):
            print("mu shape: {}".format(self.mu.shape))
            print("mu data: {}".format(self.mu.array))
        print("sigma: {}".format(self.sigma))
        s = self.mu + eps * self.sigma
        print("s: {}".format(s))
        if isinstance(s, Variable):
            print("s shape: {}".format(s.shape))
        return s

    def log_pdf(self, x):
        """log probability distribution function"""
        return -1*(F.log(self.sigma)+0.5*np.log(2.0*np.pi)+0.5*((x-self.mu)/self.sigma)**2)

    def analytic_mean(self):
        """mean"""
        return self.mu

    def analytic_var(self):
        """variance"""
        return self.sigma ** 2
