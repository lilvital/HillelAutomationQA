import pytest
import requests
# @pytest.mark.parametrize("first_num, second_num, expected_num", [(1, 2, 3),(2, 2, 4),(5, 5, 11)])
# def test_check_sum(first_num, second_num, expected_num):
#     assert custom_sum(first_num, second_num) == expected_num
#
#
#
# def custom_sum(first_num, second_num):
#     return first_num + second_num
#
# user_data = [
#     ("John", "Dou", "sa1da1s11112da121aasd312sgs3131s@test.com", "Qwerty12345", "Qwerty12345"),
#     ("Jane", "Smith", "janesmith@e11xample.com", "Qwerty12345", "Qwerty12345"),
#     ("", "Johnson", "john.johnson@example.com", "password789", "password789"),
# ]
#
# @pytest.mark.parametrize("name, last_name, email, password, repeat_password", user_data)
# def test_register_user(name, last_name, email, password, repeat_password):
#     payload = {
#         "name": name,
#         "last_name": last_name,
#         "email": email,
#         "password": password,
#         "repeat_password": repeat_password
#     }
#     session = requests.session()
#     post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=payload)
#
#     assert post_new_user.status_code == 201