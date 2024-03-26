import requests
import json
import httpx

def call_apim(url, body, ocp_apim_subscription_key):
    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }

    # POST リクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(body)) 
    
    return response

async def call_apim_async(url, body, ocp_apim_subscription_key):
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, content=json.dumps(body))
        return response