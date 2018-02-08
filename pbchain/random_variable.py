import numpy as np


class RandomVariable(object):

    def __init__(self, *args, **kwargs):

        name = kwargs.get('name', type(self).__name__)
        data = kwargs.pop('data', None)

        self._args = args
        self._kwargs = kwargs.copy()

        if data is not None:
              self._kwargs['data'] = data

        super(RandomVariable, self).__init__(*args, **kwargs)

        if data is not None:
            self._data = data
        else:
            self._data = self.sample()

    def sample(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def eval(self):
        raise NotImplementedError()

    def get_children(self):
        raise NotImplementedError()

    def get_parents(self):
        raise NotImplementedError()
