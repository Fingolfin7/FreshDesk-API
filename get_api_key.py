import base64


def get_api_key():
    with open("API_KEY.txt", 'r') as reader:
        for line in reader.readlines():
            if line.upper().startswith('KEY'):
                return line.strip().split('=')[1]




def get_base64_api_key():
    with open("API_KEY.txt", 'r') as reader:
        for line in reader.readlines():
            key = ""
            if line.upper().startswith('KEY'):
                key = line.strip().split('=')[1]

        return base64.b64encode(key.encode())

def get_domain():
    with open("API_KEY.txt", 'r') as reader:
        for line in reader.readlines():
            if line.upper().startswith('DOMAIN'):
                return line.strip().split('=')[1]
