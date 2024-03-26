import unittest
import os
from unittest import IsolatedAsyncioTestCase
from utils.docsearch import call_apim_async

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
        response = await call_apim_async(AZURE_APIM_ENDPOINT, body, APIM_SUB_KEY)

        # Assert that the response is as expected
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()