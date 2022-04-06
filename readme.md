# New Order Management System Services Documentation
## Quick Start
```bash
python fulfill_orders.py
```

## Program execution

- lines 4 and 5: parse the example data.json file using the built in 'json' module, yielding a Python dictionary.
- lines 7 and 8: separate the 'products' and 'orders' values from the raw data dictionary, and additionally create an 'inventory' dictionary keyed by ID from the list of products. This is just to make it easy to reference inventory products from order items.
- line 9: process the orders. The process_orders function returns a list of order IDs that couldn't be fulfilled.
- line 15: check and reorder products that have been depleted below their reorder threshold

## Caveats
- 'Pending purchase orders' are not tracked in the products data, but it would probably be necessary to track this so that new purchase orders are not generated before existing purchase orders are received.
- It would probably be desirable to merge purchase orders for products that come from the same supplier.
- Data sanitizing, and 'shape checking', would be important in production, along with unit tests. 

## Reference

function: **products_to_dict**(product_list)
- argument - product_list: list of products, each product a dictionary
- return - dictionary of products, keyed by product ID

function: **process_orders**(orders, inventory)
- argument - orders: list of orders, each order a dictionary
- argument - inventory: a dictionary of products keyed by ID, each value a dictionary
- return - a list of order IDs that could not be fulfilled

function: **reorder**(inventory)
- argument - inventory: a dictionary of products, each product a dictionary
- return - a list of product IDs that have pending purchase orders

function: **generate_purchase_order**(product):
- argument - product: dictionary representing a product to be ordered
- return - none
