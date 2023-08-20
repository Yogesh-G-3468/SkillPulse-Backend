from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class TestRegisterNewUser(TestCase):

    def test_create_new_user(self):
        email = "test@gmail.com"
        password = "password"

        client = APIClient()

        response = client.post(reverse('register-user'), {'email': email, 'password': password})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], f"User {email} Created Successfully")
