from get_api_key import *
from enum_values import *
import requests
import json

api_key = get_api_key()
domain = get_domain()

headers = {
    "Content-Type": "application/json"
}

ticket_id = 1168

update = {
    "status": CLOSED,

}

result = requests.put(f"https://{domain}/api/v2/tickets/{ticket_id}", auth=(api_key, "X"), headers=headers,
                      data=json.dumps(update))

if result.status_code == 200:
    print("Request processed successfully, the response is given below")
    print(json.dumps(json.loads(result.content), indent=4))
else:
    print("Failed to update ticket")
    responses = json.loads(result.content)
    print(json.dumps(responses, indent=4))
