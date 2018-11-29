import json
from urllib.request import urlopen

apikey = 'b8d6801beb79d0e8ad10db8f9ec729b4'

with urlopen(f"http://www.apilayer.net/api/live?access_key={apikey}&format=1") as response:
    source= response.read()


data = json.loads(source)

usd_rates = dict()

for item in data['quotes']:
    name = item
    price = data['quotes'][item]
    usd_rates[name] = price

print(50 * float(usd_rates['USDINR']))
