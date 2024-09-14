import requests
import pprint

params = {
    'userid' : '1'
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

response_json = response.json()

print(response.status_code)
pprint.pprint(response_json)