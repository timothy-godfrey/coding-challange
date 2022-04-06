import json
import pdb

def list_to_dict(product_list):
    inventory = {}
    for product in product_list:
        # pdb.set_trace()
        inventory[product['productId']] = product

    return inventory


def process_orders():
    pass

#  Main process
data_file = open('data.json')
data = json.load(data_file)

inventory = list_to_dict(data['products'])
print(inventory.keys())
print(inventory.values())

orders = data['orders']
