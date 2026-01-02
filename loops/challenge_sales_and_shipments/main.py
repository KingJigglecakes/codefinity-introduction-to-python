# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Update product stock levels based on sales and shipments using loops.

#     Use a for loop with index iteration to go through the products list.
#         For each product, subtract the number of units sold (units_sold) from the products stock.

for index in range(len(products)):
    print(products[index])
    products[index][1] -= units_sold[index][1]
    print(products[index])
    
#     Use a second for loop (also with index iteration) to go through products again.
#         Add the corresponding value from shipment_received to update the stock.

for index in range(len(products)):
    print(products[index])
    products[index][1] += shipment_received[index][1]
    print(products[index])

# At the end, print: Final stock levels for all products: <products>

print("Final stock levels for all products:", products)