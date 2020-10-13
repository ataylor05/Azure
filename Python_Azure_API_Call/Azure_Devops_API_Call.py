import requests
import time
import logging
import base64
import json

def _adoRequest(pat, url, verb, data=""):
    try:
        auth = str(base64.b64encode(bytes(":"+pat, "ascii")), 'ascii')
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic "+auth
        }
        print(headers)
        if verb == "get":
            response = requests.get(url, headers=headers, verify=False)
        elif verb == "post":
            response = requests.post(url=url, headers=headers, data=data, verify=False)
        elif verb == "delete":
            response = requests.delete(url=url, headers=headers, verify=False)
        return response.text
    except Exception as e:
        logging.error(e)

url = "https://dev.azure.com/humana/_apis/distributedtask/pools/55/jobrequests"
request = _adoRequest("12345", url, "get")

json_request = json.loads(request)
json_list = json_request["value"]