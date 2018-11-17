import requests
import xmltodict
import csv


customers = requests.get('https://df-dev.bk.rw/interview01/customers')
transactions = requests.get('https://df-dev.bk.rw/interview01/transactions')

csv.writer(customers, 'excel')

# print(xmltodict.parse(customers))
print(transactions.json())
