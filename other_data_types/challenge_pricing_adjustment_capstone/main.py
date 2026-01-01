 # Create the Dictionary
    # Define grocery_inventory with the following items and details:
    #     "Milk": ("Dairy", 3.50, 8)
    #     "Eggs": ("Dairy", 5.50, 30)
    #     "Bread": ("Bakery", 2.99, 15)
    #     "Apples": ("Produce", 1.50, 50)

grocery_inventory = {
        "Milk": ("Dairy", 3.50, 8),
        "Eggs": ("Dairy", 5.50, 30),
        "Bread": ("Bakery", 2.99, 15),
        "Apples": ("Produce", 1.50, 50),
}
print(grocery_inventory)
# Check and Update Price
    #     Get the price of "Eggs".

eggs_price = grocery_inventory["Eggs"][1]
    #     If the price is greater than 5, print
    #     "Eggs are too expensive, reducing the price by $1."
    #     and reduce the price by 1.

if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    eggs_price = eggs_price - 1
    grocery_inventory.update({"Eggs": ("Dairy", eggs_price, 30)})
    
    #     Otherwise, print
    #     The price of Eggs is reasonable.

else:
    print("The price of Eggs is reasonable.")

print(grocery_inventory)

    # Add a New Item
    #     Add "Tomatoes" with details: category "Produce", price 1.20, stock 30.
grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})
    #     Then print
    #     Inventory after adding Tomatoes: <grocery_inventory>
print("Inventory after adding Tomatoes: ", grocery_inventory)

    # Manage Stock
    #     Check the stock of "Milk".
milk_stock = grocery_inventory["Milk"][2]
    #     If it is less than 10, print
    #     Milk needs to be restocked. Increasing stock by 20 units.
    #     and increase the stock by 20.
if (milk_stock < 10):
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_stock = milk_stock + 20
    grocery_inventory.update({"Milk": ("Dairy", 3.5, milk_stock)})
    #     Otherwise, print
    #     Milk has sufficient stock.
else:
    print("Milk has sufficient stock.")

print(grocery_inventory)

    # Remove Item Based on Price
    #     If the price of "Apples" exceeds 2, remove "Apples" and print
    #     Apples removed from inventory due to high price.

apples_price = grocery_inventory["Apples"][1]

if(apples_price > 2):
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")


    # Final Print
    #     Print
    #     Updated inventory: <grocery_inventory>

print("Updated inventory:", grocery_inventory)