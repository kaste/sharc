
Joe Gregorio originally `posted <https://developers.google.com/appengine/articles/sharding_counters#implv2_python>`_ about Sharded Counters for Google Appengine.

This is like a downloadable gist::

    from sharc import Counter

    assert not Counter('A').exists()

    Counter('A', initial_value=5, shards=5)
    assert Counter('A').exists()

    Counter('A').increment()
    Counter('A').decrement()
    Counter('A') + 2
    Counter('A') - 2

    assert Counter('A') == 5

    Counter('A').shards = 10

    Counter('A').delete()   # .delete_async()
    assert not Counter('A').exists()




- Added decrement
- Increment and decrement variable deltas (default=1)
- Set initial value of the counter (default=0)
- Set initial value of the num of shards (default=20)
- Added delete()