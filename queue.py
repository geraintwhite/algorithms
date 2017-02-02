class Queue(object):

    def __init__(self, length):
        self.queue = [0]*length
        self.fp = 0
        self.rp = 0

    def add(self, data):
        if not ((self.fp % len(self.queue)) - (self.rp % len(self.queue))) == 1:
            self.queue[self.rp % len(self.queue)] = data
            self.rp += 1
        else:
            print('queue full')

    def remove(self):
        if not self.rp == self.fp:
            print(self.queue[self.fp % len(self.queue)])
            self.fp += 1
        else:
            print('queue empty')


queue = Queue(10)

while True:
    string = input('> [add or remove]: ')
    if string == 'add':
        queue.add(input('> data to be added: '))
    elif string == 'remove':
        queue.remove()
    else:
        print('unrecognised command')

    print(queue.queue)
