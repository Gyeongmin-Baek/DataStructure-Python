from collections import deque
from functools import wraps


class Decorators:
    @staticmethod
    def check_queue_is_full(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if len(self.queue) == self.size:
                return None
            func(self, *args, **kwargs)
            return wrapper

    @staticmethod
    def check_queue_is_empty(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if len(self.queue) == 0:
                return None
            func(self, *args, **kwargs)
            return wrapper

    @staticmethod
    def check_queue_is_resize(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            new_size = args[0] if args else kwargs.get('new_size')
            if new_size < len(self.queue):
                print("New size is smaller than the current number of elements in the queue!")
            func(self, *args, **kwargs)
            return wrapper

    @staticmethod
    def check_queue_is_extend(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            other_queue = args[0] if args else kwargs.get('other_queue')

            if not isinstance(other_queue, deque):
                print("Other queue is not an instance of deque!")

            if len(other_queue) > self.size - len(self.queue):
                raise ValueError("Not enough space in the queue to add all elements from the other queue!")

            func(self, *args, **kwargs)
            return wrapper


class DeQueue:
    def __init__(self, size=999, arr=None):
        self.queue = deque(arr or [], maxlen=size)
        self.size = size

    @Decorators.check_queue_is_full
    def enqueue(self, item):
        self.queue.append(item)

    @Decorators.check_queue_is_empty
    def dequeue(self):
        return self.queue.popleft()

    @property
    @Decorators.check_queue_is_empty
    def front(self):
        return self.queue[0]


    @property
    @Decorators.check_queue_is_empty
    def rear(self):
        return self.queue[-1]


    @property
    def is_empty(self):
        return len(self.queue) == 0

    @Decorators.check_queue_is_resize
    def resize(self, new_size):
        self.size = new_size
        self.queue = deque(list(self.queue), maxlen=new_size)


    @Decorators.check_queue_is_extend
    def from_queue(self, other_queue):
        self.queue.extend(other_queue)


    def find(self, value):
        for item in self.queue:
            if item == value:
                return True
        return False