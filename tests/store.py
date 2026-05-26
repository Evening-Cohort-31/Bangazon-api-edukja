import json
import datetime
from rest_framework import status
from rest_framework.test import APITestCase

class StoreTests(APITestCase):
    def setUp(self) -> None:
        """
        Create a new account
        """
        url = "/register"
        data = {"username": "steve", "password": "Admin8*", "email": "steve@stevebrownlee.com",
                "address": "100 Infinity Way", "phone_number": "555-1212", "first_name": "Steve", "last_name": "Brownlee"}
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_store(self):
        """
        Ensure we can create a new store
        """
        url="/stores"
        data = {
            "name": "Express Products",
            "description": "Get your products, fast"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["name"], "Express Products")
        self.assertEqual(json_response["description"], "Get your products, fast")

    def test_retrieve_store(self):
        """
        Ensure we can retrieve a single store
        """
        self.test_create_store()
        url="stores/1"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json_response = json.loads(response.content)

        self.assertEqual(json_response["name"], 'Express Products')
        self.assertEqual(json_response["description"], "Get your products, fast")
        self.assertEqual(json_response["customer"], "http://localhost:8000/customers/1")
