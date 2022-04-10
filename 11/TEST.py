import requests

r = requests.get('http:/ your web services')

# print(r.text)

data = r.json()
# print(data)
# print(data['harat_naghdi_buy']['value'])

for item in data:
    print(item + ' ' + data[item]['value'])