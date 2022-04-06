import json
import pdb


def products_to_dict(product_list):
    inventory = {}
    for product in product_list:
        inventory[product['productId']] = product

    return inventory


def process_orders():
    pass


#  Main process
data_file = open('data.json')
data = json.load(data_file)

inventory = products_to_dict(data['products'])
orders = data['orders']
unfulfillable = []

# Check that an order can be fulfilled completetly before fulfilling any
# individual items and adjust stock levels
for order in orders:
    print(order['orderId'])
    can_fulfill = True
    id = None
    quantity = None
    for item in order['items']:
        on_hand  = inventory[item['productId']]['quantityOnHand']
        id = item['productId']
        quantity = item['quantity']
        print(f'\t{id} x {quantity} - on hand: {on_hand}')

        if item['quantity'] > on_hand:
            can_fulfill = False

    print(f'can fulfull: {can_fulfill}')

    # adjust the stock levels, create a list of unfulfillable IDs
    if can_fulfill:
        for item in order['items']:
            id = item['productId']
            quantity = item['quantity']
            on_hand  = inventory[id]['quantityOnHand']
            inventory[id]['quantityOnHand'] = on_hand - quantity
    else:
        order['status'] = 'Unfulfillable'
        unfulfillable.append(order['orderId'])

print('unfillable')
for id in unfulfillable:
    print(f'{id}')
