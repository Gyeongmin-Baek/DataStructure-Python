import heapq
from simple_queue import ListQueue
from simple_queue import SimpleDecorators

class PriorityListQueue(ListQueue):
    def __init__(self, size=999, arr=None, order='min'):
        super().__init__(size, arr)
        self.order = order
        if order == 'max':
            self.queue = [(-priority, item) for priority, item in self.queue]
        heapq.heapify(self.queue)

    @SimpleDecorators.check_queue_is_full
    def enqueue(self, item, priority=None):

        if priority is None:
            priority = item

        if self.order == 'max':
            priority = -priority

        heapq.heappush(self.queue, (priority, item))

    @SimpleDecorators.check_queue_is_empty
    def dequeue(self):
        priority, item = heapq.heappop(self.queue)
        return item

    @SimpleDecorators.check_queue_is_extend
    def from_queue(self, other_queue):
        if self.order == 'max':
            other_queue = [(-priority, item) for priority, item in other_queue]
        self.queue.extend(other_queue)
        heapq.heapify(self.queue)