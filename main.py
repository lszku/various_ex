import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {}'.format(response.json()['origin']))

