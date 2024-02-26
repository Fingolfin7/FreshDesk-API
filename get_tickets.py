import requests
import json
from get_api_key import *

api_key = get_api_key()
domain = get_domain()

headers = {
    "Content-Type": "application/json"
}

result = requests.get(f"https://{domain}/api/v2/tickets?include=description&page=1",
                      auth=(api_key, "X"), headers=headers)

if result.status_code == 200:
    print("Request processed successfully, the response is given below")
    print(json.dumps(json.loads(result.content), indent=4, sort_keys=True))
else:
    print("Failed to read tickets")
    responses = json.loads(result.content)
    print(json.dumps(responses, indent=4))


print("x-request-id", result.headers['x-request-id'])
print("Status Code", result.status_code)
