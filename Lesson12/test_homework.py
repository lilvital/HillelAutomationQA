import requests
import pytest

class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password

class UserSignInModel:
    def __init__(self, email, password, remember):
        self.email = email
        self.password = password
        self.remember = remember


# def test_register_new():
#     user_to_sign_up = UserSignUpModel("John", "Dou", "sa1da1s11112da121a3123131s@test.com", "Qwerty12345", "Qwerty12345")
#     session = requests.session()
#     post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_to_sign_up.__dict__)
#     print(post_new_user.text)
#
#     # assert "ok" in post_new_user.text
#     assert post_new_user.status_code == 201


# def test_signin():
#     user_to_sign_in = UserSignInModel(email="sada1s1111da11a3123131s@test.com",password="Qwerty12345",remember=True)
#     session = requests.session()
#     get_reg_user = session.post(url="https://qauto2.forstudy.space/api/auth/signin",json=user_to_sign_in.__dict__)
#     print(get_reg_user.text)
#
#     # assert "ok" in get_reg_user.text
#     assert get_reg_user.status_code == 200


# def test_check_user_profile():
#     session = requests.session()
#
#     user_to_sign_in = UserSignInModel(email="sada1s1111da11a3123131s@test.com",password="Qwerty12345",remember=True)
#     get_reg_user = session.post(url="https://qauto2.forstudy.space/api/auth/signin",json=user_to_sign_in.__dict__)
#
#     get_user_profile = session.get(url="https://qauto2.forstudy.space/api/users/profile")
#     print(get_user_profile.text)
#
#     # assert "data" in get_user_profile.text
#     assert get_user_profile.status_code == 200

#
# user_data = [
#     ("John", "Dou", "sa11da1s11112ddfsfsasdadadfsfs121aasd312sgs3131s@test.com", "Qwerty12345", "Qwerty12345"),
#     ("Jane", "Smith", "janesmith@e11xample.com", "qwert", "qwert"),
# ]
# @pytest.mark.parametrize("name, last_name, email, password, repeat_password", user_data)
# def test_register_user(name, last_name, email, password, repeat_password):
#     payload = {
#         "name": name,
#         "lastName": last_name,
#         "email": email,
#         "password": password,
#         "repeatPassword": repeat_password
#     }
#     session = requests.session()
#     post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=payload)
#
#     assert post_new_user.status_code == 201




