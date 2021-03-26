import json
from django.test import Client, TestCase
from users.models import User


class SignUpViewTest(TestCase):
    def setUp(self):
        User.objects.create(
            name="test2_name",
            email="test@ddd.com",
            username="test2",
            password="111",
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_exist_email(self):
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

    def test_exist_username(self):
        client = Client()

        user = {
            "email": "test1@ddd.com",
            "password": "111",
            "username": "test2",
            "name": "test2_name"
        }

        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "EXISTS_USERNAME"})

    def test_signup(self):
        client = Client()

        user = {
            "email": "test4@ddd.com",
            "password": "444",
            "username": "test4",
            "name": "test4_name"
        }

        response = client.post(
            "/users/signup", json.dumps(user), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCCESS"})


class LoginViewTest(TestCase):
    def setUp(self):
        User.objects.create(
            email="test@ddd.com",
            username="test2",
            name="test2_name",
            password="111",
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_login(self):
        client = Client()

        user = {
            "email": "test@ddd.com",
            "password": "111",

        }

        response = client.post(
            "/users/login", json.dumps(user), content_type="application/json")
        self.assertEqual(response.json(), {"message": "SUCCESS"})
        self.assertEqual(response.status_code, 200)
