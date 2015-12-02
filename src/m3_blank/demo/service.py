from itertools import repeat
from spyne import srpc, Integer, Unicode, Iterable

@srpc(_returns=Iterable(Unicode))
def SayHello():
    return u"Hello, 12312312323!"