from functools import wraps
from deque import Decorators


class SimpleDecorators(Decorators):
    @staticmethod
    def check_queue_is_extend(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            other_queue = args[0] if args else kwargs.get('other_queue')

            if not isinstance(other_queue, list):
                print("Other queue is not an instance of list!")

            if len(other_queue) > self.size - len(self.queue):
                raise ValueError("Not enough space in the queue to add all elements from the other queue!")

            func(self, *args, **kwargs)
            return wrapper



class ListQueue:
    def __init__(self, size=999, arr=None):
        self.queue = list(arr or [])
        self.size = size

    @SimpleDecorators.check_queue_is_full
    def enqueue(self, item):
        self.queue.append(item)

    @SimpleDecorators.check_queue_is_empty
    def dequeue(self):
        return self.queue.pop(0)

    @property
    @SimpleDecorators.check_queue_is_empty
    def front(self):
        return self.queue[0]

    @property
    @SimpleDecorators.check_queue_is_empty
    def rear(self):
        return self.queue[-1]

    @property
    def is_empty(self):
        return len(self.queue) == 0

    @SimpleDecorators.check_queue_is_resize
    def resize(self, new_size):
        self.size = new_size
        self.queue = list(self.queue)[:new_size]

    @SimpleDecorators.check_queue_is_extend
    def from_queue(self, other_queue):
        self.queue.extend(other_queue)


    def find_index(self, value):
        try:
            return self.queue.index(value)
        except ValueError:
            return -1