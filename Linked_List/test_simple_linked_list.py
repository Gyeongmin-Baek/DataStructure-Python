import unittest
from simple_linked_list import LinkedList


# 유닛 테스트 목록
# 1. 삽입 - 카운트가 있는 경우, 카운트가 없는 경우, find가 있는 경우
# 2. 삭제 - 카운트가 있는 경우, find가 있는 경우
# 3. 수정 - 카운트가 있는 경우, find가 있는 경우
# 4. 출력 - start, end가 있는 경우, 없는 경우
# 5. 역순

class BaseTestList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.insert(insert_data="다현")
        self.linked_list.insert(insert_data="정연")
        self.linked_list.insert(insert_data="세리")
        self.linked_list.insert(insert_data="세아")
        self.linked_list.insert(insert_data="시민")



class TestLinkedList_Insert(BaseTestList):

    def test_insert_valid(self):
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 정연 세리 세아 시민')
        length = self.linked_list.length
        self.assertEqual(length, 5)

    def test_insert_find_data_between(self):
        self.linked_list.insert(find_data='정연', insert_data="리아")
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 리아 정연 세리 세아 시민')

    def test_insert_find_data_first(self):
        self.linked_list.insert(find_data='다현', insert_data="리아")
        result = self.linked_list.print_node()
        self.assertEqual(result, '리아 다현 정연 세리 세아 시민')

    def test_insert_find_data_last(self):
        self.linked_list.insert(find_data='시민', insert_data="리아")
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 정연 세리 세아 리아 시민')

    def test_insert_find_data_error(self):
        result = self.linked_list.insert(find_data='경민', insert_data='리아')
        self.assertEqual(result, -1)

    def test_insert_position(self):
        self.linked_list.insert(count=3, insert_data='리아')
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 정연 리아 세리 세아 시민')

    def test_insert_position_head(self):
        self.linked_list.insert(count=1, insert_data='리아')
        result = self.linked_list.print_node()
        self.assertEqual(result, '리아 다현 정연 세리 세아 시민')

    def test_insert_position_last(self):
        self.linked_list.insert(count=self.linked_list.length+1, insert_data='리아')
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 정연 세리 세아 시민 리아')

    def test_insert_postion_error(self):
        result = self.linked_list.insert(count=100, insert_data='리아')
        self.assertEqual(result, -1)


class TestLinkedList_Delete(BaseTestList):

    def test_delete_position(self):
        self.linked_list.delete(count=3)
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 정연 세아 시민')

    def test_delete_data(self):
        self.linked_list.delete(delete_data='정연')
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 세리 세아 시민')


    def test_delete_data_error(self):
        result = self.linked_list.delete(count=100)
        self.assertEqual(result, -1)

    def test_delete_count_error(self):
        result = self.linked_list.delete(delete_data="나리")
        self.assertEqual(result, -1)


## 수정의 경우 예외적으로 검색도 할 수 있어야 함! -> 나중에 추가적인 클래스로 구현해야 함! 현재는 base
class TestLinkedList_Update(BaseTestList):

    def test_update_position(self):
        self.linked_list.update(count=1, new_data = "나리")
        result = self.linked_list.print_node()
        self.assertEqual(result, '나리 정연 세리 세아 시민')

        self.linked_list.update(count=3, new_data="수현")
        result = self.linked_list.print_node()
        self.assertEqual(result, '나리 정연 수현 세아 시민')

    def test_update_data(self):
        self.linked_list.update(old_data="정연", new_data="나리")
        result = self.linked_list.print_node()
        self.assertEqual(result, '다현 나리 세리 세아 시민')


class TestLinkedList_Reverse(BaseTestList):
    def test_reverse_list(self):
        self.linked_list.reverse()
        ressult = self.linked_list.print_node()
        self.assertEqual(ressult, '시민 세아 세리 정연 다현')



class TestLinkedList_Find(BaseTestList):
    def test_find_data(self):
        result = self.linked_list.find(find_data='정연')
        self.assertEqual(result.data, '정연')


class TestLinkedList_Print(BaseTestList):
    def test_print_data(self):
        result = self.linked_list.print_node(start=1, end=3)
        self.assertEqual(result, '다현 정연 세리')




if __name__ == '__main__':
    unittest.main()