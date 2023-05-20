import requests
from pymongo import MongoClient

PATH = 'https://api.polygonscan.com/api'
ADDRESS = '0xf57C5d032a0Eb0b9e9a2081F4b7992bed90336D3'
CONTRACT = '0xAe07B360cF41C8971F6c544620A6ed428Ff3a661'
API_KEY = 'dummy'

# response = requests.get(f'{PATH}?module=account&action=tokentx&contractaddress={CONTRACT}&address={ADDRESS}&startblock=0&endblock=99999999&page=10&offset=5&sort=asc&apikey={API_KEY}')

# response_value = response.json()

# amount = response_value['result'][0]['value']

def get_transaction_address():
    response = requests.get(f'{PATH}?module=account&action=tokentx&contractaddress={CONTRACT}&address={ADDRESS}&startblock=0&endblock=99999999&page=32&offset=5&sort=asc&apikey={API_KEY}')
    response = response.json()
    latest_transaction = response['result']
    return latest_transaction

latest = get_transaction_address()
addresses = [data['from'] for data in reversed(latest)]

client = MongoClient('localhost', 27017)

db = client['polygonscan']
collection = db['transaction']

for address in addresses:
    collection.insert_one({'received_from': address})
