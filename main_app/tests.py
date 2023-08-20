import unittest
from django.urls import reverse
from rest_framework.test import APIClient

class Testing(unittest.TestCase):

    def __init__(self,methodName='runTest') -> None:
        super().__init__(methodName=methodName)
        self.client = APIClient()
        self.token = "Token d2b40cba71908e81b165342b182ee723e00cbaf7"
    def setRoute(self,route,data={}):
        if data:
            return self.client.get(reverse(route), data, format='json', HTTP_AUTHORIZATION=self.token)
        return self.client.get(reverse(route), HTTP_AUTHORIZATION=self.token)


    def test_greeting(self): 
        response = self.setRoute('greeting')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "HI {}".format("yogi@gmail.com"))
    
    def test_get_total_marks(self):
        response = self.setRoute('get-total-marks')
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_get_test_mark(self):
        response = self.setRoute('get-test-marks')
        print(response.json())
        self.assertEqual(response.status_code, 200)
    
    def test_get_test_rating(self):
        response = self.setRoute('get-test-rating',{"subject":"dbms"})
        print(response.json())
        self.assertEqual(response.status_code, 200)
    


if __name__ == '__main__':
    unittest.main()
