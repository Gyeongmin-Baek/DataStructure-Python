from simple_linked_list import LinkedList
from simple_linked_list import Node

class DoubleNode(Node):
    def __init__(self):
        super().__init__()
        self.prev = None

class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def _create_node(self, data):
        node = DoubleNode()
        node.data = data
        return node


    def _insert_node(self, node, prev, next):
        super()._insert_node(node, prev, next)
        node.prev = prev
        if next is not None:
            next.prev = node

    def _delete_node(self, prev, current):
        if prev is not None:
            prev.link = current.link
        if current.link is not None:
            current.link.prev = prev
        del current


    def _update_node(self, current, new_data):
        return super()._update_node(current, new_data)



    def reverse(self):
        self.pre = None
        self.current = self.head
        while self.current is not None:
            self.current.prev, self.current.link = self.current.link, self.current.prev
            self.head = self.current
            self.current = self.current.prev




