from freshdesk.api import API
from get_api_key import *

api_key = get_api_key()
domain = get_domain()

print(domain)

api = API(domain, api_key)

tickets = api.tickets.list_tickets()

for index, ticket in enumerate(tickets):
    print(f"{index + 1}.", ticket.subject)
