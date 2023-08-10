
from functools import wraps
# 연결리스트를 사용해서 스택을 구현하기

# 연결리스트의 기본 삽입
# 노드 생성
# 길이,

# 노드 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None

class Decorators:
    @staticmethod
    def check_satck_is_full(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.top +1 == self.max_size:
                return None
            func(self, *args, **kwargs)
            return wrapper


    @staticmethod
    def check_stack_is_empty(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.top == -1:
                return None
            func(self, *args, **kwargs)
            return wrapper


    @staticmethod
    def check_stack_is_extend(func):
        @wraps(func)
        def wrapper(self, data):
            if isinstance(data, LinkedList):
                if self.length + data.length > self.max_size:
                    raise ValueError("Data is too large to fit in the stack")
            elif isinstance(data, list):
                if self.length + len(data) > self.max_size:
                    raise ValueError("Data is too large to fit in the stack")
            return func(self, data)
        return wrapper

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    @property
    def length(self):
        len_count = 0
        if self.head is None:
            return -1
        else:
            self.current = self.head
            len_count += 1
            while self.current.link is not None:
                self.current = self.current.link
                len_count += 1
            return len_count


    def print_node(self, start=1, end=1):
        start -=1
        end -=1
        result = ""
        if start > end:
            return -1
        self.current = self.head
        current_count = 0
        if self.current is None:
            return

        if self.head.link is None:
            return str(self.current.data)

        current_count = 0

        # 시작 노드부터 마지막 노드 전 까지 출력
        while self.current.link is not None:
            if end != 0 or start != 0:
                if start <= current_count <= end:
                    result += str(self.current.data) + ' '
                current_count += 1
            else:
                result += str(self.current.data) + ' '
            self.current = self.current.link

        # 마지막 노드 출력
        if end != 0 or start != 0:
            if start <= current_count <= end:
                result += str(self.current.data) + ' '
        else:
            result += str(self.current.data) + ' '
        return result.strip()




class Stack(LinkedList):

    def __init__(self, max_size=9999, data=None):
        super().__init__()
        self.max_size = max_size
        self.top = -1
        if data is not None:
            self._init_data(data)

    def _init_data(self, data):
        if isinstance(data, LinkedList):
            self.head = data.head
        elif isinstance(data, list):
            for item in data:
                self.push(item)

    # 현재 스택의 크기
    def __len__(self):
        return self.top + 1

    @property
    def is_full(self):
        return self.top + 1 == self.max_size

    @property
    def is_empty(self):
        return self.top == -1


    def resize(self, new_size):
        if new_size < self.top + 1:
            raise ValueError("New size is too small to fit the current stack")
        self.max_size = new_size

    def _create_node(self, data):
        node = Node()
        node.data = data
        return node

    def _insert_node(self, node, next_data):
        # next_data : new data
        # node : header
        next_data.link = node
        self.head = next_data
        self.top += 1

    @Decorators.check_satck_is_full
    # 노드가 꽉 차면 더 이상 push 하지 못함
    def push(self, push_data):
        # 어떤 노드도 없을 때는 노드를 생성
        next_node = self._create_node(push_data)
        self._insert_node(node=self.head, next_data=next_node)


    @Decorators.check_stack_is_empty
    def peek(self):
        current_node = self.head
        return current_node


    @Decorators.check_stack_is_empty
    # 노드가 비어있는지 확인 - 참조 카운트에 의해 del을 반드시 적용할 필요가 없음
    def pop(self):
        current_node = self.head
        next_node = self.head.link
        self.head = next_node
        self.top -= 1
        return current_node

    @Decorators.check_stack_is_extend
    def extend(self, data):
        if isinstance(data, LinkedList):
            current = data.head
            while current is not None:
                self.push(current.data)
                current = current.link
        elif isinstance(data, list):
            for item in data:
                self.push(item)





