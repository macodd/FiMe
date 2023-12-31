from enum import Enum


class SearchFormType(Enum):
    DIGIT = 0
    ONE_VALUE = 1
    TWO_VALUE = 2

    def is_digit(self):
        return self == self.DIGIT

    def is_one_value(self):
        return self == self.ONE_VALUE
