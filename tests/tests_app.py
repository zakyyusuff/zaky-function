import pytest
from mymodule.funcs import multiply, divide

def dikalikan_dua():
    return multiply()

def dibagi_dua(x):
    return divide()

def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = dikalikan_dua(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = dibagi_dua(numbers[1])
        assert res == numbers[0]
