import requests

r = requests.get('http://api.navasan.tech/latest/?api_key=freeGtzudwaCF4hUHENnQhcosDd8Acyk')

# print(r.text)

data = r.json()
# print(data)
# print(data['harat_naghdi_buy']['value'])

for item in data:
    print(item + ' ' + data[item]['value'])