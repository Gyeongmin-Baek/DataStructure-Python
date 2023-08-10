import os
from functools import wraps
""""
연결리스틀 활용하여 스택을 구현해 보자.

목표
- 리스트 자료구조를 사용하지 않고 연결 리스트로 구현하기
- 연결 리스트의 삽입, 삭제, 수정, 탐색 기능까지 넣기

- 구현해야 할 대상 : 노드, 연결 리스트, 스택
- 노드 : 각 노드는 자료와 포인터를 갖고 있어 다음 자료가 어디 있는지를 알 수 있음
- 연결 리스트 : 각 노드들을 저장한 것으로 길이, 헤더를 갖고 있음 - 삽입, 수정, 삭제, 탐색, 역순, 빈 리스트인지 확인, 처음 데이터 확인 및 마지막 데이터 확인 및 가져오기
- 스택 : 연결 리스트의 데이터를 추가하거나 삭제할 수 있으며 수정과 탐색 기능까지 갖고 있음
"""


# 노드 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None


# 데코레이터 클래스 정의 - 노드의 삽입, 수정, 삭제 시 모두 사용되는 경우
# 헤드가 None, 검색
class Decorators:
    @staticmethod
    # 삽입의 경우 개수가 있을 때 마지막 노드 다음 노드에 추가하지 않는다면 에러
    def check_over_length_for_insert(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            count = args[0] if args else kwargs.get('count')
            if count is not None and self.length + 1 < count:
                return -1
            else:
                result = func(self, *args, **kwargs)
                return result

        return wrapper

    @staticmethod
    # 수정과 삭제의 경우 길이보다 큰 경우에는 에러
    def check_over_length_for_update_and_delete(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            count = args[0] if args else kwargs.get('count')
            if count is not None and self.length < count:
                return -1
            else:
                result = func(self, *args, **kwargs)
                return result

        return wrapper


# 연결 리스트 정의
# 연결 리스트의 삽입 삭제 수정을 위해서 head(처음), pre(이전), current(현재)을 정의
# tail은 추후 원형연결리스트를 상속할 때 tail 부분을 다시 찾지 않기 위해 연결리스트 클래스에서 정의하였음
class LinkedList:
    def __init__(self):
        self.head = None
        self.pre = None
        self.next = None
        self.current = None
        self.count = None

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


    def _create_node(self, data):
        node = Node()
        node.data = data
        return node


    def _insert_node(self, node, prev, next):
        node.link = next
        if prev is not None:
            prev.link = node


    def _set_up(self, count):
        if isinstance(count, int):
            count -= 1
        self.count = count
        self.current = self.head

    @Decorators.check_over_length_for_insert
    # 노드 삽입 - 노드의 삽입은 대상 노드와 추가할 노드로 구성
    # 노드 삽입 - 순서가 들어갈 수도 있음
    def insert(self, count=None, find_data=None, insert_data=None):

        # 어떤 노드도 없을 때는 노드를 생성
        if self.head is None:
            node = self._create_node(insert_data)
            self.head = node
            return

        # 노드를 삽입하는 경우 위치가 3곳이 있을 수 있음
        # 처음 삽입
        # self.count = count
        self._set_up(count)

        if (self.count is not None and self.count == 0) or (find_data is not None and self.head.data == find_data):
            node = self._create_node(insert_data)
            self._insert_node(node, prev=None, next = self.head)
            self.head = node
            return

        # 중간 삽입
        # self.current = self.head
        current_count = 0
        while insert_data is not None and self.current is not None:
            self.pre = self.current
            self.current = self.current.link
            current_count += 1
            if self.current is not None:
                if (self.count is not None and current_count == self.count) or self.current.data == find_data:
                    node = self._create_node(insert_data)
                    self._insert_node(node, prev=self.pre, next=self.current)
                    return

        if find_data is not None:
            return -1

        # 마지막 노드 삽입
        # 노드가 1개 뿐인 경우에는 현재 노드가 None이므로 예외 처리를 해주어야 함
        if self.current is None:
            node = self._create_node(insert_data)
            self._insert_node(node, prev=self.pre, next=None)


    def _delete_node(self, prev, current):
        if prev is not None:
            prev.link = current.link

    @Decorators.check_over_length_for_update_and_delete
    # 노드 삭제 - 순서, 찾는 데이터 - 삭제 시 del을 사용하지 않아도 파이썬 가비지 컬렉터에 의해 제거됨
    def delete(self, count=None, delete_data=None):

        # 삭제 시 카운트 번호, 데이터도 모두 없는 경우에는 삭제 기능을 하지 않음
        if count is None and delete_data is None:
            return -1

        self._set_up(count)

        # 첫 번째 노드 삭제
        if self.count == 0 or self.head.data == delete_data:
            self.current = self.head
            self._delete_node(prev=None, current=self.head)
            self.head = self.head.link
            return

        # 첫번째 외 노드 삭제
        # self.current = self.head
        current_count = 0
        # 마지막 노드까지 순회
        while self.current.link is not None:
            self.pre = self.current
            self.current = self.current.link
            current_count += 1
            if (self.count is not None and current_count == self.count) or self.current.data == delete_data:
                self._delete_node(prev=self.pre, current=self.current)
                return

        if delete_data is not None:
            return -1

    def _update_node(self, current, new_data):
        current.data = new_data

    @Decorators.check_over_length_for_update_and_delete
    def update(self, count=None, old_data=None, new_data=None):

        if (count is None and old_data is None) or new_data is None:
            return -1

        self._set_up(count)

        # 첫 번째 노드 수정
        if self.count == 0 or self.head.data == old_data:
            self._update_node(current=self.head, new_data=new_data)
            return

        # 중간 및 마지막 노드 수정
        # self.current = self.head
        current_count = 0
        while self.current is not None:
            if (self.count is not None and current_count == self.count) or self.current.data == old_data:
                self._update_node(current=self.current, new_data=new_data)
                # node = Node()
                # node.data = new_data
                # node.link = self.current.link
                # self.pre.link = node
                # del self.current
                # self.current = node
                return
            self.pre = self.current
            self.current = self.current.link
            current_count += 1


    # 노드 검색
    def find(self, find_data):
        self.current = self.head
        if self.current.data == find_data:
            return self.current
        while self.current.link is not None:
            self.current = self.current.link
            if self.current.data == find_data:
                return self.current
        return Node()


    # 노드 출력 - 프로퍼티로 쓰는게 낫지 않나? 명사형인데
    # 노드 출력의 경우 시작점과 끝점을 정할 수 있음
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


    # 노드 역정렬
    # 역정렬의 핵심 - 방향전환 : 현재노드가 가리키는 방향이 이전노드가 되어야 역정렬이 됨. 그렇지 않으면 무한루프 주의!
    def reverse(self):
        self.pre = None
        self.current = self.head
        while self.current is not None:
            self.next = self.current.link
            self.current.link = self.pre
            self.pre = self.current
            self.current = self.next
        self.head = self.pre