import requests

class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeat_password



# test_dict = {
#   "name": "John",
#   "lasstName": "Dou",
#   "email": "sadasdaasdsaasdasdsddas@test.com",
#   "password": "Qwerty12345",
#   "repeatPassword": "Qwerty12345"
# }


# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}
#
# r = requests.post(url=url, json=payload, headers=headers)

# class TestRegistration:
#
#     def setup_class(self):
#         self.user_to_sign_up = UserSignUpModel("John", "Dou", "s1ad11as1daa31231123131s@test.com", "Qwerty12345", "Qwerty12345")
#
#     def setup_method(self):
#         self.session = requests.session()
#
#     def test_check_successful_user_registration(self):
#         post_new_user = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_to_sign_up.__dict__)
#         assert post_new_user.status_code == 201
#     def test_check_successful_user_registration1(self):
#         post_new_user = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=self.user_to_sign_up.__dict__)
#         assert post_new_user.status_code == 201
#
#     def teardown_method(self):
#         self.session.delete("https://qauto2.forstudy.space/api/users")
