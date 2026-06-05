import pytest


def is_valid_email(email):
    return "@" in email and email. endswith(".com")

@pytest.mark.parametrize("test_input,expected_result",
                         [("user1@gmail.com",True),("user2@gmail.com",True),
                          ("user2@gmail.com",True),
                          ("user3@gmail.com",True),
                          ("user3",True)]
                          )
def test_email_validation(test_input,expected_result):
    assert is_valid_email(test_input)==expected_result

