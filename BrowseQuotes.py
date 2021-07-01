
import requests

url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/FR/eur/en-US/uk/us/anytime/anytime?apikey=fl364355903022705126954397234126"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
