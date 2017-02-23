import math


class HashTable:
    def __init__(self, size=128):
        self.size = size
        self.table = [None] * self.size


    def _hash(self, k):
        m = self.size
        a = (math.sqrt(5) - 1) / 2
        return math.floor(m * ((k * a) % 1))


    def insert(self, k):
        s = 0

        while s < self.size:
            h = self._hash(k + s)
            if self.table[h] is None:
                self.table[h] = k
                return h
            s += 1

        print('Hash table full')


    def search(self, k):
        s = 0

        while s < self.size:
            h = self._hash(k + s)
            if self.table[h] is None:
                break
            if self.table[h] == k:
                return h
            s += 1

        print('Not in hash table')
