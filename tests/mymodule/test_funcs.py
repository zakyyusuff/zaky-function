import pytest

from tests.mymodule.funcs import *


@pytest.mark.easy_operation
def test_add():
    # penjumlahan
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    # pengurangan
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    # perkalian
    assert multiply(5, 5) == 25

@pytest.mark.difficult_operation
def test_divide():
    # pembagian
    assert divide(21, 3) == 7
