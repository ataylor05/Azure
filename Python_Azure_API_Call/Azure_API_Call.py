import requests
import json
import adal
import logging


def authenticate_client(client_id, client_secret, tenant):
    authority_host_uri = 'https://login.microsoftonline.com'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    context = adal.AuthenticationContext(authority_uri, api_version=None)
    mgmt_token = context.acquire_token_with_client_credentials(resource_uri, client_id, client_secret)
    return mgmt_token["accessToken"]


def az_get_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        return json.dumps(response.json(), indent=4, separators=(',', ': '))
    except Exception as e:
        logging.error(e)


def az_put_request(url, headers, data):
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.put(url, headers=headers, data=data)
        return json.dumps(response.json(), indent=4, separators=(',', ': '))
    except Exception as e:
        logging.error(e)


def get_aks_info(headers, subscription, resource_group, cluster_name):
    # https://docs.microsoft.com/en-us/rest/api/aks/managedclusters/get
    url = "https://management.azure.com/subscriptions/" + subscription + "/resourceGroups/" + resource_group + "/providers/Microsoft.ContainerService/managedClusters/" + cluster_name + "?api-version=2020-04-01"
    request = az_get_request(url, headers)
    return request


tenant = ""
client_id = ""
client_secret = ""
token = authenticate_client(client_id, client_secret, tenant)
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

print(get_aks_info(headers, "", "", ""))