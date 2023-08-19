from django.test import TestCase
import unittest
import django

from django.contrib.auth.models import User
from .views import RegisterNewUser, Greeting, TestHistory, TestMark, RatingRetrive, GetUserAnswers


class TestRegisterNewUser(unittest.TestCase):

    def test_create_new_user(self):
        email = "test@gmail.com"
        password = "password"

        user = RegisterNewUser.as_view()
        response = user(request=django.http.HttpRequest, data={"email": email, "password": password})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "User {} Created Successfully".format(email))


class TestGreeting(unittest.TestCase):

    def test_get_greeting_message(self):
        user = User.objects.create_user(username="test", password="password")

        greeting = Greeting.as_view()
        response = greeting(request=None, headers = {
    "Content-Type": "application/json",
    "Authorization": "Token d2b40cba71908e81b165342b182ee723e00cbaf7"
  })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "HI yogi@gmail.com")