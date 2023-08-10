from contextlib import contextmanager
from enum import Enum

@contextmanager
def check_base(base):
    if not (2 <= base <= 36):
        raise ValueError("base must be between 2 and 36")
    yield


@contextmanager
def check_input_num(input_num, base):
    valid_digits = list(BaseTransformation.BASE36.values())[:base]
    for digit_num in str(input_num):
        if digit_num not in valid_digits:
            raise ValueError(f"Invalid input number {input_num} for base {base}")
    yield


class BaseTransformation:

    BASE36 = {i: str(i) if i < 10 else chr(ord('A') + i - 10) for i in range(36)}

    @classmethod
    def base_transformation(cls, num, base):
        with check_base(base):
            quo = num // base
            remain = num % base
            result_digit = str(cls.BASE36[remain])
            if num < base:
                return result_digit
            digit_num = cls.base_transformation(quo, base) + result_digit
            return digit_num

    @staticmethod
    def base_to_digit_transformation(num, base):
        if not num:
            return 0
        last_digit = int(num[-1])
        return last_digit + base * BaseTransformation.base_to_digit_transformation(num[:-1], base)


    @classmethod
    def base_to_base_transformation(cls, input_base, input_num ,output_base):
        with check_base(input_base), check_base(output_base), check_input_num(input_num, input_base):
            str_input_num = str(input_num)
            input_digit_num = BaseTransformation.base_to_digit_transformation(str_input_num, input_base)
            output_digit_num = BaseTransformation.base_transformation(input_digit_num, output_base)
            return output_digit_num


    @staticmethod
    def check_palindrome(input_num):
        if len(input_num) == 1:
            return True
        if input_num[0] != input_num[-1]:
            return False
        return BaseTransformation.check_palindrome(input_num[1:-1])


    @classmethod
    def base_palindrome(cls, input_base, input_num):
        with check_base(input_base):
            digit_num = BaseTransformation.base_transformation(input_num, input_base)
            str_input_num = str(input_num)
            check = BaseTransformation.check_palindrome(str_input_num)
            return check, digit_num





# Enum 마무리
class SelectState(Enum):
    BASETRANSFORM = 1  # 10진법의 정수를 다른 진법의 정수로 변환
    BASETOBASE = 2  # 다른 진법의 수를 다른 진법의 정수로 변환
    PALINDROME = 3  # 10진법의 정수를 다른 진법의 정수로 변환하여 회문 판단
    EXIT = 4  # 프로그램 종료


class SelectClass:
    def __init__(self):
        self.STATE_HANDLERS = {
            SelectState.BASETRANSFORM: SelectClass.base_transform,
            SelectState.BASETOBASE: SelectClass.base_to_base_transform,
            SelectState.PALINDROME: SelectClass.base_palindrome,
            SelectState.EXIT : SelectClass.exit_node
        }

    @staticmethod
    def base_transform():
        num = int(input("변환할 10진법의 숫자를 입력하세요: "))
        base = int(input("변환할 진법을 입력하세요(2진법~36진법): "))
        trans_digit = BaseTransformation.base_transformation(num, base)
        print(f"{base} 진법으로 변환된 숫자는 {trans_digit}입니다.")

    @staticmethod
    def base_to_base_transform():
        from_base = int(input("현재 진법을 입력하세요(2진법~36진법): "))
        from_number = int(input("현재 진법의 숫자를 입력하세요: "))
        to_base = int(input("변환할 진법을 입력하세요(2진법~36진법): "))
        base_to_base_digit = BaseTransformation.base_to_base_transformation(from_base, from_number, to_base)
        print(f"{to_base} 진법으로 변환된 숫자는 {base_to_base_digit}입니다.")

    @staticmethod
    def base_palindrome():
        number = int(input("변환할 10진법의 숫자를 입력하세요: "))
        pal_base = int(input("회문을 판단할 진법을 입력하세요(2진법~36진법): "))
        pal_check, pal_digit_num = BaseTransformation.base_palindrome(pal_base, number)
        if pal_check:
            print(f"{pal_base} 진법으로 변환한 {pal_digit_num}는 회문 입니다.")
        else:
            print(f"{pal_base} 진법으로 변환한 {pal_digit_num}는 회문이 아닙니다.")

    @staticmethod
    def exit_node():
        exit()


SELECT = -1

if __name__ == "__main__":

    while SELECT != 4:
        state_class = SelectClass()

        try:
            SELECT = int(input('선택하세요(1: 10진법의 정수를 다른 진법의 정수로 변환, 2: 다른 진법의 수를 다른 진법의 정수로 변환, 3: 10진법의 정수를 다른 진법의 정수로 변환하여 회문 판단, 4: 종료)---> '))
            state = SelectState(SELECT)
            handler = state_class.STATE_HANDLERS[state]
            handler()
            print()

        except ValueError:
            print("1~4번 중 하나를 다시 입력하세요")
