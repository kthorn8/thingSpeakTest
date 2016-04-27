import requests

url = 'https://api.thingspeak.com/update'

keywordTest = {'key': 'VZ7NX36F9R4CK5GZ'}

field1 = 55
field2 = 70

r = requests.post(url, data={'key': 'VZ7NX36F9R4CK5GZ', 'field1': field1, 'field2': field2},)
print("URL: ", r.url, " Encoding:", r.encoding, "Field1: ", field1, "Field2: ", field2)
print(r.text)

