import requests
import json
import httpx

# httpx (https://pypi.org/project/httpx/) を使った実装例
async def call_apim_with_httpx(url, body, ocp_apim_subscription_key):
    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }
    
    # POST リクエストを送信
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, content=json.dumps(body))
        return response

# requests (https://pypi.org/project/requests/) を使った実装例
def call_apim_with_requests(url, body, ocp_apim_subscription_key):
    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }

    # POST リクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(body)) 
    
    return response

