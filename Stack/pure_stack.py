from functools import wraps

# 데코레이션
class Decorators:
    @staticmethod
    def check_satck_is_full(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if len(self.stack) == self.max_size:
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
        def wrapper(self, *args, **kwargs):

            items = args[0] if args else kwargs.get('items')

            if not isinstance(items, list):
                raise TypeError('items must be a list')

            if self.max_size is not None and len(self.stack) + len(items) > self.max_size:
                raise Exception('Stack overflow')

            func(self, *args, **kwargs)
            return wrapper


# 스택의 모든 기능을 구현해서 만들어 보기

class Stack:

    def __init__(self, max_size=9999, lst=None):
        self.max_size = max_size
        self.stack = lst if lst is not None else []
        self.top = -1

    def __len__(self):
        return len(self.stack)

    # 스택이 비어 있는지 확인
    @property
    def is_empty(self):
        return not bool(self.stack)

    @property
    def is_full(self):
        return len(self.stack) == self.max_size

    # 추후 데코레이션으로 가득 찼는지 확인
    @Decorators.check_satck_is_full
    def push(self, data):
        self.top += 1
        self.stack.append(data)

    @Decorators.check_stack_is_empty
    def peek(self):
        return self.stack[self.top]

    # 추후 데코레이션으로 스택이 비어 있는지 확인
    @Decorators.check_stack_is_empty
    def pop(self, data):
        data = self.stack[self.top]
        self.stack.pop()
        self.top -= 1
        return data

    # 스택 리사이즈
    def stack_resize(self, resize):

        # 1. 현재 스택의 크기와 resize를 비교
        # 2. 현재 스택의 크기가 resize보다 작다면 늘리고
        # 3. 현재 스택의 크기가 resize보다 크다면 줄여주자

        if len(self.stack) < resize:
            # 스택의 크기를 늘린다.
            self.max_size = resize
        elif len(self.stack) > resize:
            # 스택의 크기를 줄인다.
            del self.stack[resize:]
        else:
            return -1

    @Decorators.check_stack_is_extend()
    def extend(self, items):
        self.stack.extend(items)