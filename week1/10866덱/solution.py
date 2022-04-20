class Deque():
    def __init__(self):
        self.deque = []

    def push_front(self, x):
        self.deque.append(x)
    
    def push_back(self, x):
        self.deque.insert(0, x)

    def pop_front(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque.pop())

    def pop_back(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque.pop(0))

    def size(self):
        print(len(self.deque))

    def empty(self):
        if len(self.deque) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque[-1])

    def back(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque[0])

myDeque = Deque()
orders = [input().split() for _ in range(int(input()))]

for order in orders:
    if order[0] == 'push_front':
        myDeque.push_front(int(order[1]))
    elif order[0] == 'push_back':
        myDeque.push_back(int(order[1]))
    elif order[0] == 'pop_front':
        myDeque.pop_front()
    elif order[0] == 'pop_back':
        myDeque.pop_back()
    elif order[0] == 'size':
        myDeque.size()
    elif order[0] == 'empty':
        myDeque.empty()
    elif order[0] == 'front':
        myDeque.front()
    elif order[0] == 'back':
        myDeque.back()