import os
from get_api_key import *
from enum_values import *
import requests
import json

api_key = get_api_key() # has since changed from Phin's xkuRCez8ANDiuZ7qAt to Courtney's xy6WSOeBAwQtZLwx46
domain = get_domain()

attachment_file = r"C:\Users\User\Desktop\the database\Poems\Ozymandias_The_Examiner_1818.jpg"

form_data = {
    'email': 'courtney@softrite.co.zw',
    'subject': 'Look on my Works, ye Mighty, and despair!',
    'priority': LOW,
    'status': OPEN,
    'cc_emails[]': 'courtney@softrite.co.zw',
    'cc_emails[]': 'phin@softrite.co.zw',
    'description': 'My Name is Ozymandias, King of Kings...',
    'group_id': 150000389235,
    'type': 'Internal Testing / Programming',
    'responder_id': 150036888462
}

files = {
    'attachments[]': (os.path.basename(attachment_file), open(attachment_file, 'rb'), 'image/png')
}

r = requests.post(f"https://{domain}/api/v2/tickets", auth=(api_key, "X"), data=form_data, files=files)

if r.status_code == 201:
    print("Ticket created successfully, the response is given below" + json.dumps(json.loads(r.content), indent=4))
    print("Location Header : " + r.headers['Location'])
else:
    print("Failed to create ticket, errors are displayed below,")
    response = json.loads(r.content)
    print(json.dumps(response, indent=4))