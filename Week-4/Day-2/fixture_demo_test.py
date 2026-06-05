import pytest

@pytest.fixture
def user_profile():
    #setup session
    print("loaded active user account")
    user ={
        "username":"user01",
        "role":"admin"
    }
    yield user #it provides user dic to the test
    #cleanuo
    print("user logining out")
    user.clear()

def test_user_access(user_profile): #dependance injection
    print("checking user previlage")
    assert user_profile["username"]=="user01"
    assert user_profile["role"]=="admin"
