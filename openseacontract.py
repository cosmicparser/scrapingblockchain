import requests
import re
import bs4
from bs4 import BeautifulSoup
import certifi
import pandas as pd
import requests, json, openpyxl, time
from Crypto.Hash import keccak

API_KEY = "WW8TF8W4DC4PRCQZY5D3VXIMKEA3JI4HUU"

url = 'https://api.etherscan.io/api'

params = {
  'module': 'block',
  'action': 'getblocknobytime',
  'timestamp' : int(time.time() // 1),
  'closest': 'before',
  'apikey': API_KEY
}

r = requests.get(url, params=params)
json_data = json.loads(r.text)["result"]
LATEST_BLOCK = int(json_data)

BLOCK_START = LATEST_BLOCK - 400

# API_KEY - Etherscan api key, you get one after registration
OPENSEA_CONTRACT = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'
url = 'https://api.etherscan.io/api'
params = {
  'module': 'logs',
  'action': 'getLogs',
  'fromBlock' : BLOCK_START,
  'toBlock': 'latest',
  'address': OPENSEA_CONTRACT,
  'apikey': API_KEY
}
r = requests.get(url, params=params)
json_data = json.loads(r.text)["result"]
print(json_data)
#print(json_data)




method = b'OrdersMatched(bytes32,bytes32,address,address,uint256,bytes32)'
k = keccak.new(digest_bits=256)
k.update(method)
print('0x'+k.hexdigest())


data = "0x00000000000000000000000000000000000000000000000000000000000000007656e0665c6bdc38947d580d2e8c4c19ba8fa4019abb8fef31cfaa1b7645f00d000000000000000000000000000000000000000000000000027f7d0bdb920000"
price_wei = int("0x" + data[-64:], 16)
price_eth = price_wei / 10**18
print(price_eth)







