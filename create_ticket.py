from get_api_key import *
from enum_values import *
import requests
import json

api_key = get_api_key()
domain = get_domain()

headers = {'Content-Type': 'application/json'}

ticket = {
    'subject': 'Create Ticket over API',
    'description': 'Testing the API to create tickets with python',
    'email': 'phin@softrite.co.zw',
    'priority': LOW,
    'status': OPEN,
    'group_id': 150000378499,
    'type': 'Internal Testing / Programming',
    'responder_id': 150028076593,
    'cc_emails': ['courtney@softrite.co.zw', 'phin@softrite.co.zw']
}

r = requests.post(f"https://{domain}/api/v2/tickets", auth=(api_key, "X"), headers=headers,
                  data=json.dumps(ticket))

if r.status_code == 201:
    print("Ticket created successfully, the response is given below" + json.dumps(json.loads(r.content), indent=4))
    print("Location Header : " + r.headers['Location'])
else:
    print("Failed to create ticket, errors are displayed below,")
    response = json.loads(r.content)
    print(response["errors"])
