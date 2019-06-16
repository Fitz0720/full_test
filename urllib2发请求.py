import json
import urllib


raw = {"number": "123456"}
print(raw)
data = parse.urlencode(raw).encode("utf-8")
request = urllib.request.Request(collectUserCoin_url, headers=headers, data=data)
response = urlopen(request)
html = response.read().decode("utf-8")
