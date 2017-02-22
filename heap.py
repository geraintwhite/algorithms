class Heap:
    def __init__(self):
        self.heap = []
        self.heapsize = 0
        self.largest = 0

    def build(self, array):
        self.heap = array
        self.heapsize = len(array) - 1

        for i in range(self.heapsize // 2, -1, -1):
            self._max_heapify(i)

    def sort(self):
        for i in range(self.heapsize, 0, -1):
            self._swap(0, i)
            self.heapsize -= 1
            self._max_heapify(0)

    def insert(self, key):
        self.heapsize += 1
        if self.heapsize >= len(self.heap):
            self.heap.append(0)
        self.heap[self.heapsize] = -float('inf')
        self._increase_key(self.heapsize, key)

    def _increase_key(self, i, key):
        self.heap[i] = key
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _max_heapify(self, i):
        left = self._left(i)
        right = self._right(i)

        if left <= self.heapsize and self.heap[left] > self.heap[i]:
            self.largest = left
        else:
            self.largest = i

        if right <= self.heapsize and self.heap[right] > self.heap[self.largest]:
            self.largest = right

        if not self.largest is i:
            self._swap(i, self.largest)
            self._max_heapify(self.largest)

    def _swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2
