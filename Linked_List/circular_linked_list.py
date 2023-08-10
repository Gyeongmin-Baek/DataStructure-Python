
from simple_linked_list import LinkedList
from simple_linked_list import Decorators

# 원형 연결 리스트 - 단순 연결리스트 상송
class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    @property
    def length(self):
        len_count = 0
        if self.head is None:
            return -1
        else:
            self.current = self.head
            len_count += 1
            while self.current is not self.tail:
                self.current = self.current.link
                len_count += 1
            return len_count

    @Decorators.check_over_length_for_insert
    def insert(self, count=None, find_data=None, insert_data=None):
        # 어떤 노드도 없을 때는 노드를 생성
        if self.head is None:
            node = self._create_node(insert_data)
            self.head = node
            self.tail = node
            self.tail.link = self.head
            return

        # count 설정
        self._set_up(count)

        # 노드를 삽입하는 경우 위치가 3곳이 있을 수 있음
        # 처음 삽입
        if (count is not None and self.count == 0) or (find_data is not None and self.head.data == find_data):
            node = self._create_node(insert_data)
            self._insert_node(node, prev=None, next=self.head)
            self.head = node
            self.tail.link = self.head
            return

        # 중간 삽입
        # self.current = self.head
        current_count = 0
        while insert_data is not None and self.current is not self.tail:
            self.pre = self.current
            self.current = self.current.link
            current_count += 1
            if (self.count is not None and current_count == self.count) or (find_data is not None and self.current.data == find_data):
                node = self._create_node(insert_data)
                self._insert_node(node, prev=self.pre, next=self.current)
                return

        if find_data is not None:
            return -1

        # 마지막 노드 삽입
        node = self._create_node(insert_data)
        self._insert_node(node, prev=self.tail, next=self.head)
        self.tail = node

    @Decorators.check_over_length_for_update_and_delete
    def delete(self, count=None, delete_data=None):
        # 삭제 시 카운트 번호, 데이터도 모두 없는 경우에는 삭제 기능을 하지 않음
        if count is None and delete_data is None:
            return -1

        self._set_up(count)

        # 첫 번째 노드 삭제
        if self.count == 0 or self.head.data == delete_data:
            self.current = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self._delete_node(prev=None, current=self.head)
                self.head = self.head.link
                self.tail.link = self.head
            return

        # 첫번째 외 노드 삭제
        # self.current = self.head
        current_count = 0
        # 마지막 노드까지 순회
        while self.current is not self.tail:
            self.pre = self.current
            self.current = self.current.link
            current_count += 1
            if (self.count is not None and current_count == self.count) or (delete_data is not None and self.current.data == delete_data):
                if self.current == self.tail:
                    self.tail = self.pre
                self._delete_node(prev=self.pre, current=self.current)
                return

        if delete_data is not None:
            return -1


    # 명시적으로 적어둠
    @Decorators.check_over_length_for_update_and_delete
    def update(self, count=None, old_data=None, new_data=None):
        super().update(count, old_data, new_data)


    # 노드 검색의 경우 반영할 필요 없음
    def print_node(self, start=0, end=0):
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
        while self.current.link is not None and self.current.link != self.head:
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

    def reverse(self):
        self.pre = None
        self.current = self.head
        self.tail = self.head
        while self.current.link != self.head:
            self.next = self.current.link
            self.current.link = self.pre
            self.pre = self.current
            self.current = self.next
        self.next.link = self.pre
        self.head = self.next