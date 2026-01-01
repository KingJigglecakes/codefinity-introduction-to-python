

#     Define a dictionary grocery_inventory to store information:
#         "Milk": (113, "Dairy")
#         "Eggs": (116, "Dairy")
#         "Bread": (117, "Bakery")
#         "Apples": (141, "Produce")

grocery_inventory = {
        "Milk": (113, "Dairy"),
        "Eggs": (116, "Dairy"),
        "Bread": (117, "Bakery"),
        "Apples": (141, "Produce")
    
}

#     Retrieve the details of the item "Bread" from the dictionary and store them in the bread_details variable.

bread_details = grocery_inventory.get("Bread")

#     Add a new item, "Cookies", with product ID 143 and category "Bakery".

grocery_inventory.update({"Cookies": (143, "Bakery")})

#     After adding "Cookies", print the updated inventory: Inventory after adding Cookies: <$grocery_inventory>.

print("Inventory after adding Cookies: ", grocery_inventory)

#     Remove the item "Eggs" from the dictionary.

grocery_inventory.pop("Eggs")

#     After removing "Eggs", print the updated inventory: Inventory after removing Eggs: <$grocery_inventory>.

print("Inventory after removing Eggs: ", grocery_inventory)

#     Print the details of "Bread": Details of Bread: <$bread_details>.

print("Details of Bread: ", bread_details)





