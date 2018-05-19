import timeit
from xxhash import xxh64


class Pair1:
    """
    A class specifically created to store a pair of filenames in a frozenset
    so that they can be hashed in order to be used as dictionary keys.
    """

    def __init__(self, a, b):
        self.A = a
        self.B = b

    def __hash__(self):
        return hash(frozenset((self.A, self.B)))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (hash(self) == hash(other))


class Pair2:
    """
    A class specifically created to store a pair of filenames in a frozenset
    so that they can be hashed in order to be used as dictionary keys.
    """

    def __init__(self, a, b):
        self.A = a
        self.B = b

    def __hash__(self):
        return hash(''.join([self.A, self.B]))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (hash(self) == hash(other))


class Pair3:
    """
    A class specifically created to store a pair of filenames in a frozenset
    so that they can be hashed in order to be used as dictionary keys.
    """

    def __init__(self, a, b):
        self.A = a
        self.B = b

    def __hash__(self):
        return xxh64(''.join([self.A, self.B])).intdigest()

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (hash(self) == hash(other))


def test1():
    p1 = Pair1("./dHash/bulktest/shit.jpg",
               "./dHash/bulktest/this.jpg")
    p2 = Pair1("./dHash/bulktest/this.jpg",
               "./dHash/bulktest/shit.jpg")
    p1 == p2


def test2():
    p1 = Pair2("./dHash/bulktest/shit.jpg",
               "./dHash/bulktest/this.jpg")
    p2 = Pair2("./dHash/bulktest/this.jpg",
               "./dHash/bulktest/shit.jpg")
    p1 == p2


def test3():
    p1 = Pair3("./dHash/bulktest/shit.jpg",
               "./dHash/bulktest/this.jpg")
    p2 = Pair3("./dHash/bulktest/this.jpg",
               "./dHash/bulktest/shit.jpg")
    p1 == p2

if __name__ == '__main__':
    print("\nTESTING Pair1\n=====")
    print(timeit.timeit("test1()", setup="from __main__ import test1", number=1000000))
    print("TESTING Pair2\n=====")
    print(timeit.timeit("test2()", setup="from __main__ import test2", number=1000000))
    print("TESTING Pair3\n=====")
    print(timeit.timeit("test3()", setup="from __main__ import test3", number=1000000))

