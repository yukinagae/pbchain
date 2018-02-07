class RandomVariable(object):

    def __init__(self, *args, **kwargs):
        self.value = self.sample(self)

    def value(self):
        return self.value

    def sample(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

    # def __repr__(self):
        # raise NotImplementedError()
        # pass

    def eval(self):
        raise NotImplementedError()

    def get_children(self):
        raise NotImplementedError()

    def get_parents(self):
        raise NotImplementedError()

    def __add__(self, rhs):
        value = self.value()
        return value + rhs.value()
