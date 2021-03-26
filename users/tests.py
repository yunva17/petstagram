import json
from django.test import Client, TestCase
from users.models import User


# class LoginViewTest(TestCase):
#     def setup(self):
#         User.objects.create(
#             email="test@ddd.com",
#             username="test2",
#             name="test2_name",
#             password="111",
#         )

#     def tearDown(self):
#         User.objects.all().delete()

#     def test_login(self):
#         client = Client()

#         user = {
#             "email": "test@ddd.com",
#             "password": "111",

#         }

#         response = client.post(
#             "/users/login", json.dumps(user), content_type="application/json")
#         self.assertEqual(response.json(), {"message": "SUCCESS"})
#         self.assertEqual(response.status_code, 200)


class SignUpViewTest(TestCase):
    def setup(self):
        User.objects.create(
            email="test@ddd.com",
            username="test2",
            name="test2_name",
            password="111",
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_sign_up(self):
        client = Client()

        user = {
            "email": "test@ddd.com",
            "password": "111",
            "username": "test2",
            "name": "test2_name"
        }

        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "EXISTS_EMAIL"})
