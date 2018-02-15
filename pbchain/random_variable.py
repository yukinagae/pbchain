class RandomVariable(object):

    def __init__(self, *args, **kwargs):

        #
        # deal with arguments
        #

        name = kwargs.get('name', type(self).__name__)
        # TODO: name should be unique in a computational graph
        kwargs['name'] = name

        data = kwargs.pop('data', None)

        self._args = args
        self._kwargs = kwargs.copy()

        if data is not None:
            self._kwargs['data'] = data

        #
        # `__init__()` of Variable class
        #
        super(RandomVariable, self).__init__(*args, **kwargs)

        #
        # override Variable class values for child class
        #
        if data is not None:
            self.data = data  # TODO: convert data to Variable
        else:
            self.data = self.sample()

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
