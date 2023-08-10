import unittest

from double_linked_list import DoubleLinkedList



# 유닛 테스트 목록
# 1. 삽입 - 카운트가 있는 경우, 카운트가 없는 경우, find가 있는 경우
# 2. 삭제 - 카운트가 있는 경우, find가 있는 경우
# 3. 수정 - 카운트가 있는 경우, find가 있는 경우
# 4. 출력 - start, end가 있는 경우, 없는 경우
# 5. 역순

class BaseTestList(unittest.TestCase):
    def setUp(self):
        self.double_linked_list = DoubleLinkedList()
        self.double_linked_list.insert(insert_data="다현")
        self.double_linked_list.insert(insert_data="정연")
        self.double_linked_list.insert(insert_data="세리")
        self.double_linked_list.insert(insert_data="세아")
        self.double_linked_list.insert(insert_data="시민")


class TestDoubleList_Insert(BaseTestList):
    def test_insert_valid(self):
        length = self.double_linked_list.length
        self.assertEqual(length, 5)
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '다현 정연 세리 세아 시민')
        self.assertEqual(self.double_linked_list.head.link.prev.data, '다현')
        self.assertEqual(self.double_linked_list.head.link.link.prev.data, '정연')
        self.assertEqual(self.double_linked_list.head.link.link.link.prev.data, '세리')


    def test_insert_find_data_between(self):
        self.double_linked_list.insert(find_data='정연', insert_data="리아")
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '다현 리아 정연 세리 세아 시민')
        self.assertEqual(self.double_linked_list.head.link.prev.data, '다현')

    def test_insert_position(self):
        self.double_linked_list.insert(count=3, insert_data='리아')
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '다현 정연 리아 세리 세아 시민')
        self.assertEqual(self.double_linked_list.head.link.link.prev.data, '정연')

    def test_insert_postion_error(self):
        result = self.double_linked_list.insert(count=100, insert_data='리아')
        self.assertEqual(result, -1)


class TestLinkedList_Delete(BaseTestList):

    def test_delete_position(self):
        self.double_linked_list.delete(count=3)
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '다현 정연 세아 시민')

    def test_delete_data(self):
        self.double_linked_list.delete(delete_data='정연')
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '다현 세리 세아 시민')
        self.assertEqual(self.double_linked_list.head.link.link.prev.data, '세리')
        self.assertEqual(self.double_linked_list.head.link.link.data, '세아')


    def test_delete_data_error(self):
        result = self.double_linked_list.delete(count=100)
        self.assertEqual(result, -1)

    def test_delete_count_error(self):
        result = self.double_linked_list.delete(delete_data="나리")
        self.assertEqual(result, -1)


class TestLinkedList_Update(BaseTestList):

    def test_update_position(self):
        self.double_linked_list.update(count=1, new_data = "나리")
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '나리 정연 세리 세아 시민')

        self.double_linked_list.update(count=3, new_data="수현")
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '나리 정연 수현 세아 시민')

    def test_update_data(self):
        self.double_linked_list.update(old_data="정연", new_data="나리")
        result = self.double_linked_list.print_node()
        self.assertEqual(result, '다현 나리 세리 세아 시민')


class TestLinkedList_Reverse(BaseTestList):
    def test_reverse_list(self):
        self.double_linked_list.reverse()
        ressult = self.double_linked_list.print_node()
        self.assertEqual(ressult, '시민 세아 세리 정연 다현')



if __name__ == '__main__':
    unittest.main()