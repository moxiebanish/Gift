import africastalking

username = "SanjuCo"
api_key = '2c0783172842fe4be33bb7ab333787a5558d6bbe38c167d615847a41dc437d99'
africastalking.initialize(username, api_key)


def smsend(message, phone):
    sms = africastalking.SMS
    response = sms.send(message, [phone])
    print(response)
