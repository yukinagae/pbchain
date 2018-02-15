class RandomVariable(object):
    """
    RandomVariable
    """

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
        """sampling"""
        raise NotImplementedError()

    def __str__(self):
        return "{}(\"{}\"{}{})".format(
            type(self).__name__,
            self.name,
            ", shape={}".format(self.shape),
            ", dtype={}".format(self.dtype.name) if self.dtype else "",
        )

    def __repr__(self):
        return "<pb.RandomVariable '{}' shape={} dtype={}>".format(
            self.name,
            self.shape,
            self.dtype.name,
        )

    def log_pdf(self, x):
        """log probability distribution function"""
        raise NotImplementedError()

    def mean(self):
        """mean"""
        raise NotImplementedError()

    def var(self):
        """variance"""
        raise NotImplementedError()

    def get_children(self):
        """get children nodes"""
        pass  # TODO: should be implemented

    def get_parents(self):
        """get parent nodes"""
        pass  # TODO: should be implemented

    def __lt__(self, other):
        raise TypeError("")

    def __le__(self, other):
        raise TypeError("")

    def __eq__(self, other):
        return id(self) == id(other)

    def __ne__(self, other):
        raise TypeError("")

    def __gt__(self, other):
        raise TypeError("")

    def __ge__(self, other):
        raise TypeError("")

    def __nonzero__(self):
        raise TypeError("")

    def __bool__(self):
        raise TypeError("")
