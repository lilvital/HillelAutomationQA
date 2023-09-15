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

user_to_sign_up = UserSignUpModel("John", "Dou", "s1adas1daa31231123131s@test.com", "Qwer", "Qwer")

session = requests.session()
# session.headers.
get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
post_new_user = session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_to_sign_up.__dict__)
# get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
# get_user_profile = session.get(url="https://qauto2.forstudy.space/api/users/profile")
# print(get_current_user.text)
print(post_new_user.text)
# print(get_current_user_after_post.text)
# print(get_user_profile.text)


# session = requests.session()

#
# post_new_user = session.post("https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
# get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
# print(get_current_user.text)
# print(post_new_user.text)
# print(get_current_user_after_post.text)