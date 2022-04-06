import json
from fulfillment import *

data_file = open('data.json')
data = json.load(data_file)

inventory = products_to_dict(data['products'])
orders = data['orders']
unfulfillable = process_orders(orders, inventory)

print('\nUnfillable orders:')
for order in unfulfillable:
    print(f'\t{order}')

reorder(inventory)
