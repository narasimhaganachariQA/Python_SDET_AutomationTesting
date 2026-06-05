import pytest

@pytest.fixture
def empty_cart():
    """provide a fresh empty list for setup"""
    return[]

def test_add_item_to_cart(empty_cart):
    empty_cart.append("apple")
    print("length ", len(empty_cart))

    assert len(empty_cart)==1
    assert "apple" in empty_cart

def test_cart_starts_empty(empty_cart):
    print("print")
    assert len(empty_cart)==0
    print("exection completed")