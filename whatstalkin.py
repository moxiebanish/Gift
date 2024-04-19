import requests


def talkwhatsapp(concantinated_name, content, recipient, gift_url):
    import requests
    BASE_URL = "https://j3p88v.api.infobip.com"
    API_KEY = "App 68ce922e1176ba247a169b5f8d1dcc50-6691fee2-1cbe-43e7-87e9-d7bd25589ba2"

    SENDER = "254792812817"
    RECIPIENT = recipient
    name = concantinated_name
    wish = content

    payload = {
        "messages":
            [
                {
                    "from": SENDER,
                    "to": RECIPIENT,
                    "content": {
                        "templateName": "wish_7",
                        "templateData": {
                            "body": {
                                "placeholders": [
                                    name,
                                    wish
                                ]
                            },
                            "header": {
                                "type": "IMAGE",
                                "mediaUrl": gift_url
                            },
                            "actions": {
                                "buttons": [
                                    {
                                        "type": "URL",
                                        "id": "website_button",
                                        "title": "Visit Website",
                                        "url": "https://www.example.com"
                                    }
                                ]
                            }
                        },
                        "language": "en"
                    }
                }
            ]
    }

    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(BASE_URL + "/whatsapp/1/message/template", json=payload, headers=headers)

    print(response.json())

from paystack.resource import TransactionResource

import random
import string

def main():
    rand = ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in range(16)])
    secret_key = 'c500369f0dec909c653cf5ee3d142c9466e88991cdfb54024a1fc42ffcedc3da'
    random_ref = rand
    test_email = 'samuelnjeri111@gmail.com'
    test_amount = '10'
    plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = client.initialize(test_amount,
                                 test_email,
                                 plan)
    print(response)
    client.authorize() # Will open a browser window for client to enter card details
    verify = client.verify() # Verify client credentials
    print(verify)
    print(client.charge())