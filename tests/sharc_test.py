
from sharc import Counter


class TestSharC:
    def testExistance(self, ndb):
        assert not Counter('A').exists()

        assert Counter('A').value == 0
        assert Counter('A').exists()
        Counter('A').delete()
        assert not Counter('A').exists()

    def testIncrDecr(self, ndb):
        assert Counter('A').value == 0
        counter = Counter('A')
        counter += 1
        Counter('A') + 1
        Counter('A').increment()
        assert Counter('A').value == 3

        counter -= 1
        Counter('A') - 1
        Counter('A').decrement()

        assert Counter('A').value == 0


    def testCmp(self, ndb):
        Counter('A') + 3

        assert Counter('A') == 3
        assert Counter('A') != 0
        assert Counter('A') < 4
        assert Counter('A') > 2
        assert Counter('A') <= 3
        assert Counter('A') >= 3


    def testNumShards(self, ndb):
        assert Counter('A').shards == 20
        Counter('A').increase_shards(5)
        assert Counter('A').shards == 5

        assert Counter('B').shards == 20
        Counter('B').increment()
        Counter('B').increase_shards(5)
        assert Counter('B').shards != 5

        Counter('C').shards = 5
        assert Counter('C').shards == 5

    def testInitialValue(self, ndb):
        Counter('A', 5)
        assert Counter('A') == 5


    def testReadMe(self, ndb):
        assert not Counter('A').exists()

        Counter('A', initial_value=5, shards=5)
        assert Counter('A').exists()
        assert Counter('A') == 5

        Counter('A').increment()
        Counter('A').decrement()
        Counter('A') + 2
        Counter('A') - 2

        assert Counter('A') == 5

        Counter('A').shards = 10

        Counter('A').delete()   # .delete_async()
        assert not Counter('A').exists()



