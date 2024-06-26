import requests
import json
import httpx
import urllib.request

# httpx (https://pypi.org/project/httpx/) を使った実装例
async def post_apim_with_httpx(url, body, ocp_apim_subscription_key):
    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }
    
    # POST リクエストを送信
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, content=json.dumps(body))
        return response

# httpx (https://pypi.org/project/httpx/) を使った実装例
async def get_apim_with_httpx(url, ocp_apim_subscription_key):
    # GET リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }
    
    # GET リクエストを送信
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response

# requests (https://pypi.org/project/requests/) を使った実装例
def post_apim_with_requests(url, body, ocp_apim_subscription_key):
    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }

    # POST リクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(body)) 
    
    return response

def call_with_urllib(ocp_apim_subscription_key):
    try:
        url = "https://apim-rag-client-temp.azure-api.net/search/docs/$count"

        hdr ={
        # Request headers
        'Ocp-Apim-Subscription-Key': ocp_apim_subscription_key,
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        # print(response.getcode())
        # print(response.read())
    except Exception as e:
        print(e)
    
    return response