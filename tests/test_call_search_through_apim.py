import unittest
import os
from unittest import IsolatedAsyncioTestCase
from utils.call_apim import get_apim_with_httpx

AZURE_APIM_ENDPOINT = os.getenv("AZURE_APIM_ENDPOINT") + 'search/docs/$count'
APIM_SUB_KEY = os.getenv("APIM_SUB_KEY")

class TestDocSearchAPIAysnc(IsolatedAsyncioTestCase):

    async def test_search_api_async_success(self):
        # Call the function with the test parameters
        response = await get_apim_with_httpx(AZURE_APIM_ENDPOINT, APIM_SUB_KEY)
        # print(response.text)

        # Assert that the response is as expected
        self.assertEqual(response.status_code, 200)
        
    async def test_search_api_async_invalid_endpoint(self):
        # Use an incorrect endpoint
        incorrect_endpoint = "http://incorrect.endpoint"

        # Call the function with the test parameters and check if an exception is raised
        with self.assertRaises(Exception):
            await get_apim_with_httpx(incorrect_endpoint, APIM_SUB_KEY)        
    
    async def test_search_api_async_invalid_key(self):
        # Use an incorrect subscription key
        incorrect_key = "incorrect_key"
        
        response = await get_apim_with_httpx(AZURE_APIM_ENDPOINT, incorrect_key)
        self.assertEqual(response.status_code, 401)
        
if __name__ == '__main__':
    unittest.main()