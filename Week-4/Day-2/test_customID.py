import pytest


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (" hello  ","hello"),
        ("\tword\n","word")
    ],
    ids=["trimspaces","TrimNewlines"]
)
def test_string_trimmer(input_str,expected):
    assert input_str.strip()==expected