import requests

API_URL = 'https://api2.binance.com/api/v3/avgPrice'

data = {'symbol': f'BTCUSDT'}  # e.g. BTCUSDT
response = requests.get(API_URL, data)
print(response.json()['price'])
