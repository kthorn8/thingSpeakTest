import requests
import logging


url = 'https://api.thingspeak.com/update'

FORMAT = '%(asctime)-15s %(message)s'

logging.basicConfig(filename='example.log', level=logging.DEBUG, format=FORMAT)

keywordTest = {'key': 'VZ7NX36F9R4CK5GZ'}

field1 = 40
field2 = 45

r = requests.post(url, data={'key': 'VZ7NX36F9R4CK5GZ', 'field1': field1, 'field2': field2},)
logging.debug('Test Channel Upload- Field1: %s, Field2: %s', field1, field2)


