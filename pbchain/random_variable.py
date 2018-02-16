"""
RandomVariable module
"""

from abc import abstractmethod, ABCMeta
from six import add_metaclass


@add_metaclass(ABCMeta)
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

        self._args = args
        self._kwargs = kwargs.copy()

        #
        # `__init__()` of Variable class
        #
        super(RandomVariable, self).__init__(*args, **kwargs)

        #
        # override Variable class values for child class
        #
        self.data = self.sample()

    @abstractmethod
    def sample(self, *args, **kwargs):
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

    @abstractmethod
    def log_pdf(self, x, *args, **kwargs):
        """log probability distribution function"""
        raise NotImplementedError()

    @abstractmethod
    def mean(self, *args, **kwargs):
        """mean"""
        raise NotImplementedError()

    @abstractmethod
    def var(self, *args, **kwargs):
        """variance"""
        raise NotImplementedError()

    def get_children(self):
        """get children nodes"""
        if self.creator is not None:
            return [o().get_variable() for o in self.creator.outputs]
        return [o().get_variable() for o in self.data.creator.outputs]

    def get_parents(self):
        """get parent nodes"""
        if self.creator is not None:
            return [i.get_variable() for i in self.creator.inputs]
        return [i.get_variable() for i in self.data.creator.inputs]

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return id(self) == id(other)

    def __lt__(self, other):
        raise TypeError("")

    def __le__(self, other):
        raise TypeError("")

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
