import requests
import json
import logging

logging.basicConfig(level=logging.INFO) ## DEBUG, INFO, WARNING, ERROR, CRITICAL. Update this to change the level of logging

def docsearch_api(apim_endpoint, body, ocp_apim_subscription_key):
    url = apim_endpoint + 'chat'

    # POST リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "ocp-apim-subscription-key": ocp_apim_subscription_key
    }

    logging.debug("url: %s", url)
    logging.debug("ocp-apim-subscription-key: %s", ocp_apim_subscription_key)
    logging.debug("headers: %s", headers)
    logging.debug("body: %s", json.dumps(body))

    # POST リクエストを送信
    try:
        response = requests.post(url, headers=headers, data=json.dumps(body))
    except requests.exceptions.RequestException as e:
        raise Exception(f'Error sending request: {e}')

    if response.status_code > 299 or not response.ok:
        try:
            parsed_response = response.json()
            error_message = parsed_response.get('error', 'Unknown error')
        except json.JSONDecodeError:
            error_message = 'Unknown error'
        raise Exception(error_message)

    return response