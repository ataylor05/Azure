import cmd
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "test"
KVUri = "https://test.vault.azure.net/"
tenant_id = "123456789"
client_id = "123456789"
client_secret = "123456789"

with open('input.txt', 'r') as file:
    data = file.read()

credential = ServicePrincipalCredentials(tenant=tenant_id, client_id=client_id, secret=client_secret)
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "test"

client.set_secret(secretName, data)