import requests
import json

def call_apim(url, body, ocp_apim_subscription_key):
    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }

    # POST リクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(body)) 
    
    return response