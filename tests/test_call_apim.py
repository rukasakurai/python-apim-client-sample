import unittest
from utils.call_apim import post_apim_with_requests
import os

AZURE_APIM_ENDPOINT = os.getenv("AZURE_APIM_ENDPOINT") + 'chat'
APIM_SUB_KEY = os.getenv("APIM_SUB_KEY")

body = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"}
    ], 
    "context": {}
}

class TestDocSearchAPI(unittest.TestCase):

    def test_docsearch_api_success(self):
        # Call the function with the test parameters
        response = post_apim_with_requests(AZURE_APIM_ENDPOINT, body, APIM_SUB_KEY)

        # Assert that the response is as expected
        self.assertEqual(response.status_code, 200)
        
    def test_docsearch_api_fail_invalid_endpoint(self):
        # Use an incorrect endpoint
        incorrect_endpoint = "http://incorrect.endpoint"

        # Call the function with the test parameters and check if an exception is raised
        with self.assertRaises(Exception):
            post_apim_with_requests(incorrect_endpoint, body, APIM_SUB_KEY)        
    
    def test_docsearch_api_fail_invalid_key(self):
        # Use an incorrect subscription key
        incorrect_key = "incorrect_key"
        
        response = post_apim_with_requests(AZURE_APIM_ENDPOINT, body, incorrect_key)
        self.assertEqual(response.status_code, 401)

    def test_docsearch_api_fail_invalid_body(self):
        # Define an incorrect body
        incorrect_body = {
            "incorrect": "body"
        }

        response = post_apim_with_requests(AZURE_APIM_ENDPOINT, incorrect_body, APIM_SUB_KEY)
        self.assertEqual(response.status_code, 500)
                
if __name__ == '__main__':
    unittest.main()
