import unittest
import os
from unittest import IsolatedAsyncioTestCase
from utils.call_apim import post_apim_with_httpx

AZURE_APIM_ENDPOINT = os.getenv("AZURE_APIM_ENDPOINT") + 'chat'
APIM_SUB_KEY = os.getenv("APIM_SUB_KEY")

body = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"}
    ], 
    "context": {}
}

class TestDocSearchAPIAysnc(IsolatedAsyncioTestCase):

    async def test_docsearch_api_async_success(self):
        # Call the function with the test parameters
        response = await post_apim_with_httpx(AZURE_APIM_ENDPOINT, body, APIM_SUB_KEY)

        # Assert that the response is as expected
        self.assertEqual(response.status_code, 200)
        
    async def test_docsearch_api_fail_invalid_endpoint(self):
        # Use an incorrect endpoint
        incorrect_endpoint = "http://incorrect.endpoint"

        # Call the function with the test parameters and check if an exception is raised
        with self.assertRaises(Exception):
            await post_apim_with_httpx(incorrect_endpoint, body, APIM_SUB_KEY)        
    
    async def test_docsearch_api_fail_invalid_key(self):
        # Use an incorrect subscription key
        incorrect_key = "incorrect_key"
        
        response = await post_apim_with_httpx(AZURE_APIM_ENDPOINT, body, incorrect_key)
        self.assertEqual(response.status_code, 401)

    async def test_docsearch_api_fail_invalid_body(self):
        # Define an incorrect body
        incorrect_body = {
            "incorrect": "body"
        }

        response = await post_apim_with_httpx(AZURE_APIM_ENDPOINT, incorrect_body, APIM_SUB_KEY)
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()