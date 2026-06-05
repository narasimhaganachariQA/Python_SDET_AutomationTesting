import pytest

def divide_number(a,b):
    print("execution divide_number")
    return a/b

def test_zero_div():
    print("test_zero_div started")
    with pytest.raises(ZeroDivisionError):
        print("execution started")
        divide_number(10,0)
        print("execution completed")

