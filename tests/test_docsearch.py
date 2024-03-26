import json
import unittest
from utils.docsearch import docsearch_api
import os

AZURE_APIM_ENDPOINT = os.getenv("AZURE_APIM_ENDPOINT")
APIM_SUB_KEY = os.getenv("APIM_SUB_KEY")

class TestDocSearchAPI(unittest.TestCase):

    def test_docsearch_api_success(self):
        # Define the input parameters for the test
        body = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"}
            ], 
            "context": {}
        }

        # Call the function with the test parameters
        response = docsearch_api(AZURE_APIM_ENDPOINT, body, APIM_SUB_KEY)

        # Assert that the response is as expected
        self.assertEqual(response.status_code, 200)

    def test_docsearch_api_fail_invalid_endpoint(self):
        # Define the input parameters for the test
        body = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"}
            ], 
            "context": {}
        }

        # Use an incorrect endpoint
        incorrect_endpoint = "http://incorrect.endpoint"

        # Call the function with the test parameters and check if an exception is raised
        with self.assertRaises(Exception):
            docsearch_api(incorrect_endpoint, body, APIM_SUB_KEY)
    
    def test_docsearch_api_fail_invalid_key(self):
        # Define the input parameters for the test
        body = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"}
            ], 
            "context": {}
        }

        # Use an incorrect subscription key
        incorrect_key = "incorrect_key"

        # Call the function with the test parameters and check if an exception is raised
        with self.assertRaises(Exception):
            docsearch_api(AZURE_APIM_ENDPOINT, body, incorrect_key)

    def test_docsearch_api_fail_invalid_body(self):
        # Define an incorrect body
        incorrect_body = {
            "incorrect": "body"
        }

        # Call the function with the test parameters and check if an exception is raised
        with self.assertRaises(Exception):
            docsearch_api(AZURE_APIM_ENDPOINT, incorrect_body, APIM_SUB_KEY)

if __name__ == '__main__':
    unittest.main()
