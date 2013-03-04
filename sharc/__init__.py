"""
    sharc

    Sharded Counter on Google Appengine.

    :copyright: (c) 2013 by Herrn Kaste <herr.kaste@gmail.com>.
    :license: Apache 2.
"""

__version__ = "0.1.0"


from google.appengine.api import memcache
from google.appengine.ext import ndb

from . import sharc

DEFAULT_VALUE = 0
DEFAULT_SHARDS = 20

class Counter(object):

    def __init__(self, name, initial_value=DEFAULT_VALUE, shards=DEFAULT_SHARDS):
        self.name = name
        if shards != DEFAULT_SHARDS and not self.exists():
            self.num_shards = shards
        if initial_value != DEFAULT_VALUE and not self.exists():
            self.increment(initial_value)

    def exists(self):
        return sharc.GeneralCounterShardConfig.get_by_id(self.name) is not None

    def increment(self, delta=1):
        sharc.increment(self.name, delta=delta)

    def decrement(self, delta=1):
        sharc.increment(self.name, delta=-delta)

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can only increment with ints.")

        self.increment(delta=other)
        return self
    __iadd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can only decrement with ints.")

        self.increment(delta=-other)
        return self
    __isub__ = __sub__

    def __cmp__(self, other):
        return self.value.__cmp__(other)

    @property
    def value(self):
        return sharc.get_count(self.name)

    def delete(self):
        self.delete_async().get_result()

    @ndb.tasklet
    def delete_async(self):
        yield ndb.delete_multi_async(
            sharc.GeneralCounterShardConfig.all_keys(self.name) +
            [ndb.Key(sharc.GeneralCounterShardConfig, self.name)]
        ), ndb.get_context().memcache_delete(self.name)


    @property
    def shards(self):
        config = sharc.GeneralCounterShardConfig.get_by_id(self.name)
        if config:
            return config.num_shards

        return sharc.DEFAULT_NUM_SHARDS

    @shards.setter
    def shards(self, num_shards):
        self.increase_shards(num_shards)

    def increase_shards(self, num_shards):
        sharc.increase_shards(self.name, num_shards)

    def __repr__(self):
        return "Counter(%r)" % self.name
