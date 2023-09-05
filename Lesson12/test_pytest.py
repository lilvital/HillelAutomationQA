import pytest

@pytest.mark.parametrize("first_num, second_num, expected_num", [(1,2,3),(2,2,4),(5,5,11)])
def test_check_sum(first_num, second_num, expected_num):
    assert custom_sum(first_num, second_num) == expected_num



def custom_sum(first_num,  second_num):
    return first_num - second_num