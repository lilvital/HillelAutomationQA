import requests

test_dict = {
  "name": "John",
  "lastName": "Dou",
  "email": "test@tedasdadadasdaasdadq1231dasst11.com",
  "password": "Qwerty123451",
  "repeatPassword": "Qwerty123451"
}

session = requests.session()

get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
post_new_user = session.post("https://qauto2.forstudy.space/api/auth/signup", json=test_dict)
get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
print(get_current_user.text)
print(post_new_user.text)
print(get_current_user_after_post.text)