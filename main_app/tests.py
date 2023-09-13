import unittest
from django.urls import reverse
from rest_framework.test import APIClient
from .answers import totest
import json

class Testing(unittest.TestCase):

    def __init__(self,methodName='runTest') -> None:
        super().__init__(methodName=methodName)
        self.client = APIClient()
        self.token = "Token 6ac21766148674d831ccd2f4cbcc44b3e9e3bbf6"


    def test_send_answers(self):
        json_totest = json.dumps(totest)
        response = self.client.post(reverse('GetRating'), data = json_totest,content_type='application/json', HTTP_AUTHORIZATION=self.token)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_greeting(self): 
        response = self.client.get(reverse('greeting'), HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "HI {}".format("test@gmail.com"))
    
    def test_get_total_marks(self):
        response = self.client.get(reverse('get-total-marks'), HTTP_AUTHORIZATION=self.token)
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_get_test_mark(self):
        response = self.client.get(reverse('get-test-marks'), HTTP_AUTHORIZATION=self.token)
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_get_test_rating(self):
        response = self.client.get(reverse('get-test-rating'), data = {"subject":"dbms"}, HTTP_AUTHORIZATION=self.token)
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_get_resources(self):
        response = self.client.get(reverse('get-resources'),data = {"subject":"dbms"}, HTTP_AUTHORIZATION=self.token)
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_senior_data(self):
        response = self.client.get(reverse('get-seniordata'), HTTP_AUTHORIZATION=self.token)
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_get_scoreboard(self):
        response = self.client.get(reverse('get-scoreboard'))
        print(response.json())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
